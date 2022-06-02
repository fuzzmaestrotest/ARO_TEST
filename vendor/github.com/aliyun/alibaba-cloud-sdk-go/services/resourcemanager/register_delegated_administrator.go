package resourcemanager

//Licensed under the Apache License, Version 2.0 (the "License");
//you may not use this file except in compliance with the License.
//You may obtain a copy of the License at
//
//http://www.apache.org/licenses/LICENSE-2.0
//
//Unless required by applicable law or agreed to in writing, software
//distributed under the License is distributed on an "AS IS" BASIS,
//WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//See the License for the specific language governing permissions and
//limitations under the License.
//
// Code generated by Alibaba Cloud SDK Code Generator.
// Changes may cause incorrect behavior and will be lost if the code is regenerated.

import (
	"github.com/aliyun/alibaba-cloud-sdk-go/sdk/requests"
	"github.com/aliyun/alibaba-cloud-sdk-go/sdk/responses"
)

// RegisterDelegatedAdministrator invokes the resourcemanager.RegisterDelegatedAdministrator API synchronously
func (client *Client) RegisterDelegatedAdministrator(request *RegisterDelegatedAdministratorRequest) (response *RegisterDelegatedAdministratorResponse, err error) {
	response = CreateRegisterDelegatedAdministratorResponse()
	err = client.DoAction(request, response)
	return
}

// RegisterDelegatedAdministratorWithChan invokes the resourcemanager.RegisterDelegatedAdministrator API asynchronously
func (client *Client) RegisterDelegatedAdministratorWithChan(request *RegisterDelegatedAdministratorRequest) (<-chan *RegisterDelegatedAdministratorResponse, <-chan error) {
	responseChan := make(chan *RegisterDelegatedAdministratorResponse, 1)
	errChan := make(chan error, 1)
	err := client.AddAsyncTask(func() {
		defer close(responseChan)
		defer close(errChan)
		response, err := client.RegisterDelegatedAdministrator(request)
		if err != nil {
			errChan <- err
		} else {
			responseChan <- response
		}
	})
	if err != nil {
		errChan <- err
		close(responseChan)
		close(errChan)
	}
	return responseChan, errChan
}

// RegisterDelegatedAdministratorWithCallback invokes the resourcemanager.RegisterDelegatedAdministrator API asynchronously
func (client *Client) RegisterDelegatedAdministratorWithCallback(request *RegisterDelegatedAdministratorRequest, callback func(response *RegisterDelegatedAdministratorResponse, err error)) <-chan int {
	result := make(chan int, 1)
	err := client.AddAsyncTask(func() {
		var response *RegisterDelegatedAdministratorResponse
		var err error
		defer close(result)
		response, err = client.RegisterDelegatedAdministrator(request)
		callback(response, err)
		result <- 1
	})
	if err != nil {
		defer close(result)
		callback(nil, err)
		result <- 0
	}
	return result
}

// RegisterDelegatedAdministratorRequest is the request struct for api RegisterDelegatedAdministrator
type RegisterDelegatedAdministratorRequest struct {
	*requests.RpcRequest
	AccountId        string `position:"Query" name:"AccountId"`
	ServicePrincipal string `position:"Query" name:"ServicePrincipal"`
}

// RegisterDelegatedAdministratorResponse is the response struct for api RegisterDelegatedAdministrator
type RegisterDelegatedAdministratorResponse struct {
	*responses.BaseResponse
	RequestId string `json:"RequestId" xml:"RequestId"`
}

// CreateRegisterDelegatedAdministratorRequest creates a request to invoke RegisterDelegatedAdministrator API
func CreateRegisterDelegatedAdministratorRequest() (request *RegisterDelegatedAdministratorRequest) {
	request = &RegisterDelegatedAdministratorRequest{
		RpcRequest: &requests.RpcRequest{},
	}
	request.InitWithApiInfo("ResourceManager", "2020-03-31", "RegisterDelegatedAdministrator", "", "")
	request.Method = requests.POST
	return
}

// CreateRegisterDelegatedAdministratorResponse creates a response to parse from RegisterDelegatedAdministrator response
func CreateRegisterDelegatedAdministratorResponse() (response *RegisterDelegatedAdministratorResponse) {
	response = &RegisterDelegatedAdministratorResponse{
		BaseResponse: &responses.BaseResponse{},
	}
	return
}
