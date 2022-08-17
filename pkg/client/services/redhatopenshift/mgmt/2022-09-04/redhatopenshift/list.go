package redhatopenshift

// Copyright (c) Microsoft and contributors.  All rights reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//
// See the License for the specific language governing permissions and
// limitations under the License.
//
// Code generated by Microsoft (R) AutoRest Code Generator.
// Changes may cause incorrect behavior and will be lost if the code is regenerated.

import (
	"context"
	"net/http"

	"github.com/Azure/go-autorest/autorest"
	"github.com/Azure/go-autorest/autorest/azure"
	"github.com/Azure/go-autorest/autorest/validation"
	"github.com/Azure/go-autorest/tracing"
)

// ListClient is the rest API for Azure Red Hat OpenShift 4
type ListClient struct {
	BaseClient
}

// NewListClient creates an instance of the ListClient client.
func NewListClient(subscriptionID string) ListClient {
	return NewListClientWithBaseURI(DefaultBaseURI, subscriptionID)
}

// NewListClientWithBaseURI creates an instance of the ListClient client using a custom endpoint.  Use this when
// interacting with an Azure cloud that uses a non-standard base URI (sovereign clouds, Azure stack).
func NewListClientWithBaseURI(baseURI string, subscriptionID string) ListClient {
	return ListClient{NewWithBaseURI(baseURI, subscriptionID)}
}

// Versions the operation returns the installable OpenShift versions as strings.
// Parameters:
// location - the name of Azure region.
func (client ListClient) Versions(ctx context.Context, location string) (result SetObject, err error) {
	if tracing.IsEnabled() {
		ctx = tracing.StartSpan(ctx, fqdn+"/ListClient.Versions")
		defer func() {
			sc := -1
			if result.Response.Response != nil {
				sc = result.Response.Response.StatusCode
			}
			tracing.EndSpan(ctx, sc, err)
		}()
	}
	if err := validation.Validate([]validation.Validation{
		{TargetValue: client.SubscriptionID,
			Constraints: []validation.Constraint{{Target: "client.SubscriptionID", Name: validation.MinLength, Rule: 1, Chain: nil}}},
		{TargetValue: location,
			Constraints: []validation.Constraint{{Target: "location", Name: validation.MinLength, Rule: 1, Chain: nil}}}}); err != nil {
		return result, validation.NewError("redhatopenshift.ListClient", "Versions", err.Error())
	}

	req, err := client.VersionsPreparer(ctx, location)
	if err != nil {
		err = autorest.NewErrorWithError(err, "redhatopenshift.ListClient", "Versions", nil, "Failure preparing request")
		return
	}

	resp, err := client.VersionsSender(req)
	if err != nil {
		result.Response = autorest.Response{Response: resp}
		err = autorest.NewErrorWithError(err, "redhatopenshift.ListClient", "Versions", resp, "Failure sending request")
		return
	}

	result, err = client.VersionsResponder(resp)
	if err != nil {
		err = autorest.NewErrorWithError(err, "redhatopenshift.ListClient", "Versions", resp, "Failure responding to request")
		return
	}

	return
}

// VersionsPreparer prepares the Versions request.
func (client ListClient) VersionsPreparer(ctx context.Context, location string) (*http.Request, error) {
	pathParameters := map[string]interface{}{
		"location":       autorest.Encode("path", location),
		"subscriptionId": autorest.Encode("path", client.SubscriptionID),
	}

	const APIVersion = "2022-09-04"
	queryParameters := map[string]interface{}{
		"api-version": APIVersion,
	}

	preparer := autorest.CreatePreparer(
		autorest.AsGet(),
		autorest.WithBaseURL(client.BaseURI),
		autorest.WithPathParameters("/subscriptions/{subscriptionId}/providers/Microsoft.RedHatOpenShift/locations/{location}/listinstallversions", pathParameters),
		autorest.WithQueryParameters(queryParameters))
	return preparer.Prepare((&http.Request{}).WithContext(ctx))
}

// VersionsSender sends the Versions request. The method will close the
// http.Response Body if it receives an error.
func (client ListClient) VersionsSender(req *http.Request) (*http.Response, error) {
	return client.Send(req, azure.DoRetryWithRegistration(client.Client))
}

// VersionsResponder handles the response to the Versions request. The method always
// closes the http.Response Body.
func (client ListClient) VersionsResponder(resp *http.Response) (result SetObject, err error) {
	err = autorest.Respond(
		resp,
		azure.WithErrorUnlessStatusCode(http.StatusOK),
		autorest.ByUnmarshallingJSON(&result.Value),
		autorest.ByClosing())
	result.Response = autorest.Response{Response: resp}
	return
}
