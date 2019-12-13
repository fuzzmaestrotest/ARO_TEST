import ipaddress
import uuid

from azure.cli.core.commands.client_factory import get_mgmt_service_client
from azure.cli.core.commands.client_factory import get_subscription_id
from azure.cli.core.profiles import ResourceType
from knack.util import CLIError
from msrestazure.azure_exceptions import CloudError
from msrestazure.tools import is_valid_resource_id
from msrestazure.tools import parse_resource_id
from msrestazure.tools import resource_id


def validate_cidr(key):
    def _validate_cidr(namespace):
        cidr = getattr(namespace, key)
        if cidr is not None:
            try:
                ipaddress.IPv4Network(cidr)
            except ValueError:
                raise CLIError("Invalid --%s '%s'." %
                               (key.replace('_', '-'), cidr))

    return _validate_cidr


def validate_client_id(namespace):
    if namespace.client_id is not None:
        try:
            uuid.UUID(namespace.client_id)
        except ValueError:
            raise CLIError("Invalid --client-id '%s'." % namespace.client_id)

        if namespace.client_secret is None or not str(namespace.client_secret):
            raise CLIError("Must specify --client-secret with --client-id.")


def validate_client_secret(namespace):
    if namespace.client_secret is not None:
        if namespace.client_id is not None or not str(namespace.client_id):
            raise CLIError("Must specify --client-id with --client-secret.")


def _validate_int(key, i):
    try:
        i = int(i)
    except ValueError:
        raise CLIError("Invalid --%s '%s'." % (key.replace('_', '-'), i))

    return i


def validate_subnet(key):
    def _validate_subnet(cmd, namespace):
        subnet = getattr(namespace, key)

        if not is_valid_resource_id(subnet):
            if not namespace.vnet:
                raise CLIError(
                    "Must specify --vnet if --%s is not an id." % key.replace('_', '-'))

            validate_vnet(cmd, namespace)

            subnet = namespace.vnet + "/subnets/" + subnet
            setattr(namespace, key, subnet)

        parts = parse_resource_id(subnet)

        if parts["subscription"] != get_subscription_id(cmd.cli_ctx):
            raise CLIError("--%s subscription '%s' must equal cluster subscription." %
                           (key.replace('_', '-'), parts["subscription"]))

        if parts["namespace"].lower() != "microsoft.network":
            raise CLIError("--%s namespace '%s' must equal Microsoft.Network." %
                           (key.replace('_', '-'), parts["namespace"]))

        if parts["type"].lower() != "virtualnetworks":
            raise CLIError("--%s type '%s' must equal virtualNetworks." %
                           (key.replace('_', '-'), parts["type"]))

        if parts["last_child_num"] != 1:
            raise CLIError("--%s '%s' must have one child." %
                           (key.replace('_', '-'), subnet))

        if "child_namespace_1" in parts:
            raise CLIError("--%s '%s' must not have child namespace." %
                           (key.replace('_', '-'), subnet))

        if parts["child_type_1"].lower() != "subnets":
            raise CLIError("--%s child type '%s' must equal subnets." %
                           (key.replace('_', '-'), subnet))

        client = get_mgmt_service_client(
            cmd.cli_ctx, ResourceType.MGMT_NETWORK)
        try:
            client.subnets.get(parts["resource_group"],
                               parts["name"], parts["child_name_1"])
        except CloudError as err:
            raise CLIError(err.message)

    return _validate_subnet


def validate_subnets(master_subnet, worker_subnet):
    master_parts = parse_resource_id(master_subnet)
    worker_parts = parse_resource_id(worker_subnet)

    if master_parts["resource_group"].lower() != worker_parts["resource_group"].lower():
        raise CLIError("--master-subnet resource group '%s' must equal --worker-subnet resource group '%s'." %
                       (master_parts["resource_group"], worker_parts["resource_group"]))

    if master_parts["name"].lower() != worker_parts["name"].lower():
        raise CLIError("--master-subnet vnet name '%s' must equal --worker-subnet vnet name '%s'." %
                       (master_parts["name"], worker_parts["name"]))

    if master_parts["child_name_1"].lower() == worker_parts["child_name_1"].lower():
        raise CLIError("--master-subnet name '%s' must not equal --worker-subnet name '%s'." %
                       (master_parts["child_name_1"], worker_parts["child_name_1"]))

    return resource_id(
        subscription=master_parts["subscription"],
        resource_group=master_parts["resource_group"],
        namespace='Microsoft.Network',
        type='virtualNetworks',
        name=master_parts["name"],
    )


def validate_vnet(cmd, namespace):
    if namespace.vnet:
        if not is_valid_resource_id(namespace.vnet):
            if not namespace.vnet_resource_group_name:
                raise CLIError(
                    "Must specify --vnet-resource-group-name if --vnet is not an id.")

            namespace.vnet = resource_id(
                subscription=get_subscription_id(cmd.cli_ctx),
                resource_group=namespace.vnet_resource_group_name,
                namespace='Microsoft.Network',
                type='virtualNetworks',
                name=namespace.vnet,
            )


def validate_worker_count(namespace):
    if namespace.worker_count:
        namespace.worker_count = _validate_int(
            "worker_count", namespace.worker_count)

        if namespace.worker_count < 3:
            raise CLIError(
                "--worker-count must be greater than or equal to 3.")


def validate_worker_vm_disk_size_gb(namespace):
    if namespace.worker_vm_disk_size_gb:
        namespace.worker_vm_disk_size_gb = _validate_int(
            "worker_vm_disk_size_gb", namespace.worker_vm_disk_size_gb)

        if namespace.worker_vm_disk_size_gb < 128:
            raise CLIError(
                "--worker_vm_disk_size_gb must be greater than or equal to 128.")
