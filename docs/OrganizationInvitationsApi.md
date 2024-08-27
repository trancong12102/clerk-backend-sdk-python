# clerk_backend_sdk.OrganizationInvitationsApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization_invitation**](OrganizationInvitationsApi.md#create_organization_invitation) | **POST** /organizations/{organization_id}/invitations | Create and send an organization invitation
[**create_organization_invitation_bulk**](OrganizationInvitationsApi.md#create_organization_invitation_bulk) | **POST** /organizations/{organization_id}/invitations/bulk | Bulk create and send organization invitations
[**get_organization_invitation**](OrganizationInvitationsApi.md#get_organization_invitation) | **GET** /organizations/{organization_id}/invitations/{invitation_id} | Retrieve an organization invitation by ID
[**list_organization_invitations**](OrganizationInvitationsApi.md#list_organization_invitations) | **GET** /organizations/{organization_id}/invitations | Get a list of organization invitations
[**list_pending_organization_invitations**](OrganizationInvitationsApi.md#list_pending_organization_invitations) | **GET** /organizations/{organization_id}/invitations/pending | Get a list of pending organization invitations
[**revoke_organization_invitation**](OrganizationInvitationsApi.md#revoke_organization_invitation) | **POST** /organizations/{organization_id}/invitations/{invitation_id}/revoke | Revoke a pending organization invitation


# **create_organization_invitation**
> OrganizationInvitation create_organization_invitation(organization_id, create_organization_invitation_request)

Create and send an organization invitation

Creates a new organization invitation and sends an email to the provided `email_address` with a link to accept the invitation and join the organization. You can specify the `role` for the invited organization member.  New organization invitations get a \"pending\" status until they are revoked by an organization administrator or accepted by the invitee.  The request body supports passing an optional `redirect_url` parameter. When the invited user clicks the link to accept the invitation, they will be redirected to the URL provided. Use this parameter to implement a custom invitation acceptance flow.  You must specify the ID of the user that will send the invitation with the `inviter_user_id` parameter. That user must be a member with administrator privileges in the organization. Only \"admin\" members can create organization invitations.  You can optionally provide public and private metadata for the organization invitation. The public metadata are visible by both the Frontend and the Backend whereas the private ones only by the Backend. When the organization invitation is accepted, the metadata will be transferred to the newly created organization membership.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.create_organization_invitation_request import CreateOrganizationInvitationRequest
from clerk_backend_sdk.models.organization_invitation import OrganizationInvitation
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
    api_instance = clerk_backend_sdk.OrganizationInvitationsApi(api_client)
    organization_id = 'organization_id_example' # str | The ID of the organization for which to send the invitation
    create_organization_invitation_request = clerk_backend_sdk.CreateOrganizationInvitationRequest() # CreateOrganizationInvitationRequest | 

    try:
        # Create and send an organization invitation
        api_response = await api_instance.create_organization_invitation(organization_id, create_organization_invitation_request)
        print("The response of OrganizationInvitationsApi->create_organization_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationInvitationsApi->create_organization_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The ID of the organization for which to send the invitation | 
 **create_organization_invitation_request** | [**CreateOrganizationInvitationRequest**](CreateOrganizationInvitationRequest.md)|  | 

### Return type

[**OrganizationInvitation**](OrganizationInvitation.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An organization invitation |  -  |
**400** | Request was not successful |  -  |
**403** | Authorization invalid |  -  |
**404** | Resource not found |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_organization_invitation_bulk**
> OrganizationInvitations create_organization_invitation_bulk(organization_id, create_organization_invitation_bulk_request_inner)

Bulk create and send organization invitations

Creates new organization invitations in bulk and sends out emails to the provided email addresses with a link to accept the invitation and join the organization. You can specify a different `role` for each invited organization member. New organization invitations get a \"pending\" status until they are revoked by an organization administrator or accepted by the invitee. The request body supports passing an optional `redirect_url` parameter for each invitation. When the invited user clicks the link to accept the invitation, they will be redirected to the provided URL. Use this parameter to implement a custom invitation acceptance flow. You must specify the ID of the user that will send the invitation with the `inviter_user_id` parameter. Each invitation can have a different inviter user. Inviter users must be members with administrator privileges in the organization. Only \"admin\" members can create organization invitations. You can optionally provide public and private metadata for each organization invitation. The public metadata are visible by both the Frontend and the Backend, whereas the private metadata are only visible by the Backend. When the organization invitation is accepted, the metadata will be transferred to the newly created organization membership.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.create_organization_invitation_bulk_request_inner import CreateOrganizationInvitationBulkRequestInner
from clerk_backend_sdk.models.organization_invitations import OrganizationInvitations
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
    api_instance = clerk_backend_sdk.OrganizationInvitationsApi(api_client)
    organization_id = 'organization_id_example' # str | The organization ID.
    create_organization_invitation_bulk_request_inner = [clerk_backend_sdk.CreateOrganizationInvitationBulkRequestInner()] # List[CreateOrganizationInvitationBulkRequestInner] | 

    try:
        # Bulk create and send organization invitations
        api_response = await api_instance.create_organization_invitation_bulk(organization_id, create_organization_invitation_bulk_request_inner)
        print("The response of OrganizationInvitationsApi->create_organization_invitation_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationInvitationsApi->create_organization_invitation_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The organization ID. | 
 **create_organization_invitation_bulk_request_inner** | [**List[CreateOrganizationInvitationBulkRequestInner]**](CreateOrganizationInvitationBulkRequestInner.md)|  | 

### Return type

[**OrganizationInvitations**](OrganizationInvitations.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of organization invitations |  -  |
**400** | Request was not successful |  -  |
**403** | Authorization invalid |  -  |
**404** | Resource not found |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_invitation**
> OrganizationInvitation get_organization_invitation(organization_id, invitation_id)

Retrieve an organization invitation by ID

Use this request to get an existing organization invitation by ID.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.organization_invitation import OrganizationInvitation
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
    api_instance = clerk_backend_sdk.OrganizationInvitationsApi(api_client)
    organization_id = 'organization_id_example' # str | The organization ID.
    invitation_id = 'invitation_id_example' # str | The organization invitation ID.

    try:
        # Retrieve an organization invitation by ID
        api_response = await api_instance.get_organization_invitation(organization_id, invitation_id)
        print("The response of OrganizationInvitationsApi->get_organization_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationInvitationsApi->get_organization_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The organization ID. | 
 **invitation_id** | **str**| The organization invitation ID. | 

### Return type

[**OrganizationInvitation**](OrganizationInvitation.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An organization invitation |  -  |
**400** | Request was not successful |  -  |
**403** | Authorization invalid |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization_invitations**
> OrganizationInvitations list_organization_invitations(organization_id, limit=limit, offset=offset, status=status)

Get a list of organization invitations

This request returns the list of organization invitations. Results can be paginated using the optional `limit` and `offset` query parameters. You can filter them by providing the 'status' query parameter, that accepts multiple values. The organization invitations are ordered by descending creation date. Most recent invitations will be returned first. Any invitations created as a result of an Organization Domain are not included in the results.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.organization_invitations import OrganizationInvitations
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
    api_instance = clerk_backend_sdk.OrganizationInvitationsApi(api_client)
    organization_id = 'organization_id_example' # str | The organization ID.
    limit = 10 # float | Applies a limit to the number of results returned. Can be used for paginating the results together with `offset`. (optional) (default to 10)
    offset = 0 # float | Skip the first `offset` results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with `limit`. (optional) (default to 0)
    status = 'status_example' # str | Filter organization invitations based on their status (optional)

    try:
        # Get a list of organization invitations
        api_response = await api_instance.list_organization_invitations(organization_id, limit=limit, offset=offset, status=status)
        print("The response of OrganizationInvitationsApi->list_organization_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationInvitationsApi->list_organization_invitations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The organization ID. | 
 **limit** | **float**| Applies a limit to the number of results returned. Can be used for paginating the results together with &#x60;offset&#x60;. | [optional] [default to 10]
 **offset** | **float**| Skip the first &#x60;offset&#x60; results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with &#x60;limit&#x60;. | [optional] [default to 0]
 **status** | **str**| Filter organization invitations based on their status | [optional] 

### Return type

[**OrganizationInvitations**](OrganizationInvitations.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of organization invitations |  -  |
**400** | Request was not successful |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pending_organization_invitations**
> OrganizationInvitations list_pending_organization_invitations(organization_id, limit=limit, offset=offset)

Get a list of pending organization invitations

This request returns the list of organization invitations with \"pending\" status. These are the organization invitations that can still be used to join the organization, but have not been accepted by the invited user yet. Results can be paginated using the optional `limit` and `offset` query parameters. The organization invitations are ordered by descending creation date. Most recent invitations will be returned first. Any invitations created as a result of an Organization Domain are not included in the results.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.organization_invitations import OrganizationInvitations
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
    api_instance = clerk_backend_sdk.OrganizationInvitationsApi(api_client)
    organization_id = 'organization_id_example' # str | The organization ID.
    limit = 10 # float | Applies a limit to the number of results returned. Can be used for paginating the results together with `offset`. (optional) (default to 10)
    offset = 0 # float | Skip the first `offset` results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with `limit`. (optional) (default to 0)

    try:
        # Get a list of pending organization invitations
        api_response = await api_instance.list_pending_organization_invitations(organization_id, limit=limit, offset=offset)
        print("The response of OrganizationInvitationsApi->list_pending_organization_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationInvitationsApi->list_pending_organization_invitations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The organization ID. | 
 **limit** | **float**| Applies a limit to the number of results returned. Can be used for paginating the results together with &#x60;offset&#x60;. | [optional] [default to 10]
 **offset** | **float**| Skip the first &#x60;offset&#x60; results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with &#x60;limit&#x60;. | [optional] [default to 0]

### Return type

[**OrganizationInvitations**](OrganizationInvitations.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of organization invitations |  -  |
**400** | Request was not successful |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_organization_invitation**
> OrganizationInvitation revoke_organization_invitation(organization_id, invitation_id, revoke_organization_invitation_request)

Revoke a pending organization invitation

Use this request to revoke a previously issued organization invitation. Revoking an organization invitation makes it invalid; the invited user will no longer be able to join the organization with the revoked invitation. Only organization invitations with \"pending\" status can be revoked. The request needs the `requesting_user_id` parameter to specify the user which revokes the invitation. Only users with \"admin\" role can revoke invitations.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.organization_invitation import OrganizationInvitation
from clerk_backend_sdk.models.revoke_organization_invitation_request import RevokeOrganizationInvitationRequest
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
    api_instance = clerk_backend_sdk.OrganizationInvitationsApi(api_client)
    organization_id = 'organization_id_example' # str | The organization ID.
    invitation_id = 'invitation_id_example' # str | The organization invitation ID.
    revoke_organization_invitation_request = clerk_backend_sdk.RevokeOrganizationInvitationRequest() # RevokeOrganizationInvitationRequest | 

    try:
        # Revoke a pending organization invitation
        api_response = await api_instance.revoke_organization_invitation(organization_id, invitation_id, revoke_organization_invitation_request)
        print("The response of OrganizationInvitationsApi->revoke_organization_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationInvitationsApi->revoke_organization_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The organization ID. | 
 **invitation_id** | **str**| The organization invitation ID. | 
 **revoke_organization_invitation_request** | [**RevokeOrganizationInvitationRequest**](RevokeOrganizationInvitationRequest.md)|  | 

### Return type

[**OrganizationInvitation**](OrganizationInvitation.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An organization invitation |  -  |
**400** | Request was not successful |  -  |
**403** | Authorization invalid |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

