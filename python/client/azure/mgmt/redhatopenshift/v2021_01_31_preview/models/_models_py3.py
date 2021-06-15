# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class APIServerProfile(Model):
    """APIServerProfile represents an API server profile.

    :param visibility: API server visibility. Possible values include:
     'Private', 'Public'
    :type visibility: str or
     ~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.enum
    :param url: The URL to access the cluster API server.
    :type url: str
    :param ip: The IP of the cluster API server.
    :type ip: str
    """

    _attribute_map = {
        'visibility': {'key': 'visibility', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'ip': {'key': 'ip', 'type': 'str'},
    }

    def __init__(self, *, visibility=None, url: str=None, ip: str=None, **kwargs) -> None:
        super(APIServerProfile, self).__init__(**kwargs)
        self.visibility = visibility
        self.url = url
        self.ip = ip


class Resource(Model):
    """Common fields that are returned in the response for all Azure Resource
    Manager resources.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. E.g.
     "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class AzureEntityResource(Resource):
    """The resource model definition for an Azure Resource Manager resource with
    an etag.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. E.g.
     "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
    :vartype type: str
    :ivar etag: Resource Etag.
    :vartype etag: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(AzureEntityResource, self).__init__(**kwargs)
        self.etag = None


class CloudError(Model):
    """CloudError represents a cloud error.

    :param error: An error response from the service.
    :type error:
     ~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.CloudErrorBody
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'CloudErrorBody'},
    }

    def __init__(self, *, error=None, **kwargs) -> None:
        super(CloudError, self).__init__(**kwargs)
        self.error = error


class CloudErrorException(HttpOperationError):
    """Server responsed with exception of type: 'CloudError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(CloudErrorException, self).__init__(deserialize, response, 'CloudError', *args)


class CloudErrorBody(Model):
    """CloudErrorBody represents the body of a cloud error.

    :param code: An identifier for the error. Codes are invariant and are
     intended to be consumed programmatically.
    :type code: str
    :param message: A message describing the error, intended to be suitable
     for display in a user interface.
    :type message: str
    :param target: The target of the particular error. For example, the name
     of the property in error.
    :type target: str
    :param details: A list of additional details about the error.
    :type details:
     list[~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.CloudErrorBody]
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[CloudErrorBody]'},
    }

    def __init__(self, *, code: str=None, message: str=None, target: str=None, details=None, **kwargs) -> None:
        super(CloudErrorBody, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target
        self.details = details


class ClusterProfile(Model):
    """ClusterProfile represents a cluster profile.

    :param pull_secret: The pull secret for the cluster.
    :type pull_secret: str
    :param domain: The domain for the cluster.
    :type domain: str
    :param version: The version of the cluster.
    :type version: str
    :param resource_group_id: The ID of the cluster resource group.
    :type resource_group_id: str
    """

    _attribute_map = {
        'pull_secret': {'key': 'pullSecret', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'resource_group_id': {'key': 'resourceGroupId', 'type': 'str'},
    }

    def __init__(self, *, pull_secret: str=None, domain: str=None, version: str=None, resource_group_id: str=None, **kwargs) -> None:
        super(ClusterProfile, self).__init__(**kwargs)
        self.pull_secret = pull_secret
        self.domain = domain
        self.version = version
        self.resource_group_id = resource_group_id


class ConsoleProfile(Model):
    """ConsoleProfile represents a console profile.

    :param url: The URL to access the cluster console.
    :type url: str
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
    }

    def __init__(self, *, url: str=None, **kwargs) -> None:
        super(ConsoleProfile, self).__init__(**kwargs)
        self.url = url


class Display(Model):
    """Display represents the display details of an operation.

    :param provider: Friendly name of the resource provider.
    :type provider: str
    :param resource: Resource type on which the operation is performed.
    :type resource: str
    :param operation: Operation type: read, write, delete, listKeys/action,
     etc.
    :type operation: str
    :param description: Friendly name of the operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, *, provider: str=None, resource: str=None, operation: str=None, description: str=None, **kwargs) -> None:
        super(Display, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class IngressProfile(Model):
    """IngressProfile represents an ingress profile.

    :param name: The ingress profile name.
    :type name: str
    :param visibility: Ingress visibility. Possible values include: 'Private',
     'Public'
    :type visibility: str or
     ~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.enum
    :param ip: The IP of the ingress.
    :type ip: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'visibility': {'key': 'visibility', 'type': 'str'},
        'ip': {'key': 'ip', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, visibility=None, ip: str=None, **kwargs) -> None:
        super(IngressProfile, self).__init__(**kwargs)
        self.name = name
        self.visibility = visibility
        self.ip = ip


class MasterProfile(Model):
    """MasterProfile represents a master profile.

    :param vm_size: The size of the master VMs. Possible values include:
     'Standard_D16as_v4', 'Standard_D16s_v3', 'Standard_D2s_v3',
     'Standard_D32as_v4', 'Standard_D32s_v3', 'Standard_D4as_v4',
     'Standard_D4s_v3', 'Standard_D8as_v4', 'Standard_D8s_v3',
     'Standard_E16s_v3', 'Standard_E32s_v3', 'Standard_E4s_v3',
     'Standard_E8s_v3', 'Standard_F16s_v2', 'Standard_F32s_v2',
     'Standard_F4s_v2', 'Standard_F8s_v2'
    :type vm_size: str or
     ~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.VMSize
    :param subnet_id: The Azure resource ID of the master subnet.
    :type subnet_id: str
    """

    _attribute_map = {
        'vm_size': {'key': 'vmSize', 'type': 'str'},
        'subnet_id': {'key': 'subnetId', 'type': 'str'},
    }

    def __init__(self, *, vm_size=None, subnet_id: str=None, **kwargs) -> None:
        super(MasterProfile, self).__init__(**kwargs)
        self.vm_size = vm_size
        self.subnet_id = subnet_id


class NetworkProfile(Model):
    """NetworkProfile represents a network profile.

    :param pod_cidr: The CIDR used for OpenShift/Kubernetes Pods.
    :type pod_cidr: str
    :param service_cidr: The CIDR used for OpenShift/Kubernetes Services.
    :type service_cidr: str
    """

    _attribute_map = {
        'pod_cidr': {'key': 'podCidr', 'type': 'str'},
        'service_cidr': {'key': 'serviceCidr', 'type': 'str'},
    }

    def __init__(self, *, pod_cidr: str=None, service_cidr: str=None, **kwargs) -> None:
        super(NetworkProfile, self).__init__(**kwargs)
        self.pod_cidr = pod_cidr
        self.service_cidr = service_cidr


class TrackedResource(Resource):
    """The resource model definition for an Azure Resource Manager tracked top
    level resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. E.g.
     "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(self, *, location: str, tags=None, **kwargs) -> None:
        super(TrackedResource, self).__init__(**kwargs)
        self.tags = tags
        self.location = location


class OpenShiftCluster(TrackedResource):
    """OpenShiftCluster represents an Azure Red Hat OpenShift cluster.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. E.g.
     "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    :param provisioning_state: The cluster provisioning state. Possible values
     include: 'AdminUpdating', 'Creating', 'Deleting', 'Failed', 'Succeeded',
     'Updating'
    :type provisioning_state: str or
     ~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.enum
    :param cluster_profile: The cluster profile.
    :type cluster_profile:
     ~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.ClusterProfile
    :param console_profile: The console profile.
    :type console_profile:
     ~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.ConsoleProfile
    :param service_principal_profile: The cluster service principal profile.
    :type service_principal_profile:
     ~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.ServicePrincipalProfile
    :param network_profile: The cluster network profile.
    :type network_profile:
     ~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.NetworkProfile
    :param master_profile: The cluster master profile.
    :type master_profile:
     ~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.MasterProfile
    :param worker_profiles: The cluster worker profiles.
    :type worker_profiles:
     list[~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.WorkerProfile]
    :param apiserver_profile: The cluster API server profile.
    :type apiserver_profile:
     ~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.APIServerProfile
    :param ingress_profiles: The cluster ingress profiles.
    :type ingress_profiles:
     list[~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.IngressProfile]
    :ivar system_data: The system meta data relating to this resource.
    :vartype system_data:
     ~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.SystemData
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'cluster_profile': {'key': 'properties.clusterProfile', 'type': 'ClusterProfile'},
        'console_profile': {'key': 'properties.consoleProfile', 'type': 'ConsoleProfile'},
        'service_principal_profile': {'key': 'properties.servicePrincipalProfile', 'type': 'ServicePrincipalProfile'},
        'network_profile': {'key': 'properties.networkProfile', 'type': 'NetworkProfile'},
        'master_profile': {'key': 'properties.masterProfile', 'type': 'MasterProfile'},
        'worker_profiles': {'key': 'properties.workerProfiles', 'type': '[WorkerProfile]'},
        'apiserver_profile': {'key': 'properties.apiserverProfile', 'type': 'APIServerProfile'},
        'ingress_profiles': {'key': 'properties.ingressProfiles', 'type': '[IngressProfile]'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
    }

    def __init__(self, *, location: str, tags=None, provisioning_state=None, cluster_profile=None, console_profile=None, service_principal_profile=None, network_profile=None, master_profile=None, worker_profiles=None, apiserver_profile=None, ingress_profiles=None, **kwargs) -> None:
        super(OpenShiftCluster, self).__init__(tags=tags, location=location, **kwargs)
        self.provisioning_state = provisioning_state
        self.cluster_profile = cluster_profile
        self.console_profile = console_profile
        self.service_principal_profile = service_principal_profile
        self.network_profile = network_profile
        self.master_profile = master_profile
        self.worker_profiles = worker_profiles
        self.apiserver_profile = apiserver_profile
        self.ingress_profiles = ingress_profiles
        self.system_data = None


class OpenShiftClusterAdminKubeconfig(Model):
    """OpenShiftClusterAdminKubeconfig represents an OpenShift cluster's admin
    kubeconfig.

    :param kubeconfig: The base64-encoded kubeconfig file.
    :type kubeconfig: str
    """

    _attribute_map = {
        'kubeconfig': {'key': 'kubeconfig', 'type': 'str'},
    }

    def __init__(self, *, kubeconfig: str=None, **kwargs) -> None:
        super(OpenShiftClusterAdminKubeconfig, self).__init__(**kwargs)
        self.kubeconfig = kubeconfig


class OpenShiftClusterCredentials(Model):
    """OpenShiftClusterCredentials represents an OpenShift cluster's credentials.

    :param kubeadmin_username: The username for the kubeadmin user.
    :type kubeadmin_username: str
    :param kubeadmin_password: The password for the kubeadmin user.
    :type kubeadmin_password: str
    """

    _attribute_map = {
        'kubeadmin_username': {'key': 'kubeadminUsername', 'type': 'str'},
        'kubeadmin_password': {'key': 'kubeadminPassword', 'type': 'str'},
    }

    def __init__(self, *, kubeadmin_username: str=None, kubeadmin_password: str=None, **kwargs) -> None:
        super(OpenShiftClusterCredentials, self).__init__(**kwargs)
        self.kubeadmin_username = kubeadmin_username
        self.kubeadmin_password = kubeadmin_password


class OpenShiftClusterUpdate(Model):
    """OpenShiftCluster represents an Azure Red Hat OpenShift cluster.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param tags: The resource tags.
    :type tags: dict[str, str]
    :param provisioning_state: The cluster provisioning state. Possible values
     include: 'AdminUpdating', 'Creating', 'Deleting', 'Failed', 'Succeeded',
     'Updating'
    :type provisioning_state: str or
     ~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.enum
    :param cluster_profile: The cluster profile.
    :type cluster_profile:
     ~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.ClusterProfile
    :param console_profile: The console profile.
    :type console_profile:
     ~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.ConsoleProfile
    :param service_principal_profile: The cluster service principal profile.
    :type service_principal_profile:
     ~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.ServicePrincipalProfile
    :param network_profile: The cluster network profile.
    :type network_profile:
     ~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.NetworkProfile
    :param master_profile: The cluster master profile.
    :type master_profile:
     ~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.MasterProfile
    :param worker_profiles: The cluster worker profiles.
    :type worker_profiles:
     list[~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.WorkerProfile]
    :param apiserver_profile: The cluster API server profile.
    :type apiserver_profile:
     ~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.APIServerProfile
    :param ingress_profiles: The cluster ingress profiles.
    :type ingress_profiles:
     list[~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.IngressProfile]
    :ivar system_data: The system meta data relating to this resource.
    :vartype system_data:
     ~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.SystemData
    """

    _validation = {
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'cluster_profile': {'key': 'properties.clusterProfile', 'type': 'ClusterProfile'},
        'console_profile': {'key': 'properties.consoleProfile', 'type': 'ConsoleProfile'},
        'service_principal_profile': {'key': 'properties.servicePrincipalProfile', 'type': 'ServicePrincipalProfile'},
        'network_profile': {'key': 'properties.networkProfile', 'type': 'NetworkProfile'},
        'master_profile': {'key': 'properties.masterProfile', 'type': 'MasterProfile'},
        'worker_profiles': {'key': 'properties.workerProfiles', 'type': '[WorkerProfile]'},
        'apiserver_profile': {'key': 'properties.apiserverProfile', 'type': 'APIServerProfile'},
        'ingress_profiles': {'key': 'properties.ingressProfiles', 'type': '[IngressProfile]'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
    }

    def __init__(self, *, tags=None, provisioning_state=None, cluster_profile=None, console_profile=None, service_principal_profile=None, network_profile=None, master_profile=None, worker_profiles=None, apiserver_profile=None, ingress_profiles=None, **kwargs) -> None:
        super(OpenShiftClusterUpdate, self).__init__(**kwargs)
        self.tags = tags
        self.provisioning_state = provisioning_state
        self.cluster_profile = cluster_profile
        self.console_profile = console_profile
        self.service_principal_profile = service_principal_profile
        self.network_profile = network_profile
        self.master_profile = master_profile
        self.worker_profiles = worker_profiles
        self.apiserver_profile = apiserver_profile
        self.ingress_profiles = ingress_profiles
        self.system_data = None


class Operation(Model):
    """Operation represents an RP operation.

    :param name: Operation name: {provider}/{resource}/{operation}.
    :type name: str
    :param display: The object that describes the operation.
    :type display:
     ~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.Display
    :param origin: Sources of requests to this operation.  Comma separated
     list with valid values user or system, e.g. "user,system".
    :type origin: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'Display'},
        'origin': {'key': 'origin', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, display=None, origin: str=None, **kwargs) -> None:
        super(Operation, self).__init__(**kwargs)
        self.name = name
        self.display = display
        self.origin = origin


class ProxyResource(Resource):
    """The resource model definition for an Azure Resource Manager proxy resource.
    It will have everything other than required location and tags.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. E.g.
     "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(ProxyResource, self).__init__(**kwargs)


class ServicePrincipalProfile(Model):
    """ServicePrincipalProfile represents a service principal profile.

    :param client_id: The client ID used for the cluster.
    :type client_id: str
    :param client_secret: The client secret used for the cluster.
    :type client_secret: str
    """

    _attribute_map = {
        'client_id': {'key': 'clientId', 'type': 'str'},
        'client_secret': {'key': 'clientSecret', 'type': 'str'},
    }

    def __init__(self, *, client_id: str=None, client_secret: str=None, **kwargs) -> None:
        super(ServicePrincipalProfile, self).__init__(**kwargs)
        self.client_id = client_id
        self.client_secret = client_secret


class SystemData(Model):
    """Metadata pertaining to creation and last modification of the resource.

    :param created_by: The identity that created the resource.
    :type created_by: str
    :param created_by_type: The type of identity that created the resource.
     Possible values include: 'User', 'Application', 'ManagedIdentity', 'Key'
    :type created_by_type: str or
     ~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.CreatedByType
    :param created_at: The timestamp of resource creation (UTC).
    :type created_at: datetime
    :param last_modified_by: The identity that last modified the resource.
    :type last_modified_by: str
    :param last_modified_by_type: The type of identity that last modified the
     resource. Possible values include: 'User', 'Application',
     'ManagedIdentity', 'Key'
    :type last_modified_by_type: str or
     ~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.CreatedByType
    :param last_modified_at: The type of identity that last modified the
     resource.
    :type last_modified_at: datetime
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'created_by_type': {'key': 'createdByType', 'type': 'str'},
        'created_at': {'key': 'createdAt', 'type': 'iso-8601'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'str'},
        'last_modified_by_type': {'key': 'lastModifiedByType', 'type': 'str'},
        'last_modified_at': {'key': 'lastModifiedAt', 'type': 'iso-8601'},
    }

    def __init__(self, *, created_by: str=None, created_by_type=None, created_at=None, last_modified_by: str=None, last_modified_by_type=None, last_modified_at=None, **kwargs) -> None:
        super(SystemData, self).__init__(**kwargs)
        self.created_by = created_by
        self.created_by_type = created_by_type
        self.created_at = created_at
        self.last_modified_by = last_modified_by
        self.last_modified_by_type = last_modified_by_type
        self.last_modified_at = last_modified_at


class WorkerProfile(Model):
    """WorkerProfile represents a worker profile.

    :param name: The worker profile name.
    :type name: str
    :param vm_size: The size of the worker VMs. Possible values include:
     'Standard_D16as_v4', 'Standard_D16s_v3', 'Standard_D2s_v3',
     'Standard_D32as_v4', 'Standard_D32s_v3', 'Standard_D4as_v4',
     'Standard_D4s_v3', 'Standard_D8as_v4', 'Standard_D8s_v3',
     'Standard_E16s_v3', 'Standard_E32s_v3', 'Standard_E4s_v3',
     'Standard_E8s_v3', 'Standard_F16s_v2', 'Standard_F32s_v2',
     'Standard_F4s_v2', 'Standard_F8s_v2'
    :type vm_size: str or
     ~azure.mgmt.redhatopenshift.v2021_01_31_preview.models.VMSize
    :param disk_size_gb: The disk size of the worker VMs.
    :type disk_size_gb: int
    :param subnet_id: The Azure resource ID of the worker subnet.
    :type subnet_id: str
    :param count: The number of worker VMs.
    :type count: int
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'vm_size': {'key': 'vmSize', 'type': 'str'},
        'disk_size_gb': {'key': 'diskSizeGB', 'type': 'int'},
        'subnet_id': {'key': 'subnetId', 'type': 'str'},
        'count': {'key': 'count', 'type': 'int'},
    }

    def __init__(self, *, name: str=None, vm_size=None, disk_size_gb: int=None, subnet_id: str=None, count: int=None, **kwargs) -> None:
        super(WorkerProfile, self).__init__(**kwargs)
        self.name = name
        self.vm_size = vm_size
        self.disk_size_gb = disk_size_gb
        self.subnet_id = subnet_id
        self.count = count
