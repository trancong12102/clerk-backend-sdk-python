# clerk_backend_sdk.InvitationsApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_invitation**](InvitationsApi.md#create_invitation) | **POST** /invitations | Create an invitation
[**list_invitations**](InvitationsApi.md#list_invitations) | **GET** /invitations | List all invitations
[**revoke_invitation**](InvitationsApi.md#revoke_invitation) | **POST** /invitations/{invitation_id}/revoke | Revokes an invitation


# **create_invitation**
> Invitation create_invitation(create_invitation_request=create_invitation_request)

Create an invitation

Creates a new invitation for the given email address and sends the invitation email. Keep in mind that you cannot create an invitation if there is already one for the given email address. Also, trying to create an invitation for an email address that already exists in your application will result to an error.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.create_invitation_request import CreateInvitationRequest
from clerk_backend_sdk.models.invitation import Invitation
from clerk_backend_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.clerk.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = clerk_backend_sdk.Configuration(
    host = "https://api.clerk.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (sk_<environment>_<secret value>): bearerAuth
configuration = clerk_backend_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with clerk_backend_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clerk_backend_sdk.InvitationsApi(api_client)
    create_invitation_request = clerk_backend_sdk.CreateInvitationRequest() # CreateInvitationRequest | Required parameters (optional)

    try:
        # Create an invitation
        api_response = await api_instance.create_invitation(create_invitation_request=create_invitation_request)
        print("The response of InvitationsApi->create_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->create_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_invitation_request** | [**CreateInvitationRequest**](CreateInvitationRequest.md)| Required parameters | [optional] 

### Return type

[**Invitation**](Invitation.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Request was not successful |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_invitations**
> List[Invitation] list_invitations(limit=limit, offset=offset, status=status)

List all invitations

Returns all non-revoked invitations for your application, sorted by creation date

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.invitation import Invitation
from clerk_backend_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.clerk.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = clerk_backend_sdk.Configuration(
    host = "https://api.clerk.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (sk_<environment>_<secret value>): bearerAuth
configuration = clerk_backend_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with clerk_backend_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clerk_backend_sdk.InvitationsApi(api_client)
    limit = 10 # float | Applies a limit to the number of results returned. Can be used for paginating the results together with `offset`. (optional) (default to 10)
    offset = 0 # float | Skip the first `offset` results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with `limit`. (optional) (default to 0)
    status = 'status_example' # str | Filter invitations based on their status (optional)

    try:
        # List all invitations
        api_response = await api_instance.list_invitations(limit=limit, offset=offset, status=status)
        print("The response of InvitationsApi->list_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->list_invitations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Applies a limit to the number of results returned. Can be used for paginating the results together with &#x60;offset&#x60;. | [optional] [default to 10]
 **offset** | **float**| Skip the first &#x60;offset&#x60; results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with &#x60;limit&#x60;. | [optional] [default to 0]
 **status** | **str**| Filter invitations based on their status | [optional] 

### Return type

[**List[Invitation]**](Invitation.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of invitations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_invitation**
> RevokeInvitation200Response revoke_invitation(invitation_id)

Revokes an invitation

Revokes the given invitation. Revoking an invitation will prevent the user from using the invitation link that was sent to them. However, it doesn't prevent the user from signing up if they follow the sign up flow. Only active (i.e. non-revoked) invitations can be revoked.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.revoke_invitation200_response import RevokeInvitation200Response
from clerk_backend_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.clerk.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = clerk_backend_sdk.Configuration(
    host = "https://api.clerk.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (sk_<environment>_<secret value>): bearerAuth
configuration = clerk_backend_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with clerk_backend_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clerk_backend_sdk.InvitationsApi(api_client)
    invitation_id = 'invitation_id_example' # str | The ID of the invitation to be revoked

    try:
        # Revokes an invitation
        api_response = await api_instance.revoke_invitation(invitation_id)
        print("The response of InvitationsApi->revoke_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->revoke_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_id** | **str**| The ID of the invitation to be revoked | 

### Return type

[**RevokeInvitation200Response**](RevokeInvitation200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Request was not successful |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

