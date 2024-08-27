# clerk_backend_sdk.OrganizationMembershipsApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization_membership**](OrganizationMembershipsApi.md#create_organization_membership) | **POST** /organizations/{organization_id}/memberships | Create a new organization membership
[**delete_organization_membership**](OrganizationMembershipsApi.md#delete_organization_membership) | **DELETE** /organizations/{organization_id}/memberships/{user_id} | Remove a member from an organization
[**list_organization_memberships**](OrganizationMembershipsApi.md#list_organization_memberships) | **GET** /organizations/{organization_id}/memberships | Get a list of all members of an organization
[**update_organization_membership**](OrganizationMembershipsApi.md#update_organization_membership) | **PATCH** /organizations/{organization_id}/memberships/{user_id} | Update an organization membership
[**update_organization_membership_metadata**](OrganizationMembershipsApi.md#update_organization_membership_metadata) | **PATCH** /organizations/{organization_id}/memberships/{user_id}/metadata | Merge and update organization membership metadata


# **create_organization_membership**
> OrganizationMembership create_organization_membership(organization_id, create_organization_membership_request)

Create a new organization membership

Adds a user as a member to the given organization. Only users in the same instance as the organization can be added as members. This organization will be the user's [active organization] (https://clerk.com/docs/organizations/overview#active-organization) the next time they create a session, presuming they don't explicitly set a different organization as active before then.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.create_organization_membership_request import CreateOrganizationMembershipRequest
from clerk_backend_sdk.models.organization_membership import OrganizationMembership
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
    api_instance = clerk_backend_sdk.OrganizationMembershipsApi(api_client)
    organization_id = 'organization_id_example' # str | The ID of the organization where the new membership will be created
    create_organization_membership_request = clerk_backend_sdk.CreateOrganizationMembershipRequest() # CreateOrganizationMembershipRequest | 

    try:
        # Create a new organization membership
        api_response = await api_instance.create_organization_membership(organization_id, create_organization_membership_request)
        print("The response of OrganizationMembershipsApi->create_organization_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationMembershipsApi->create_organization_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The ID of the organization where the new membership will be created | 
 **create_organization_membership_request** | [**CreateOrganizationMembershipRequest**](CreateOrganizationMembershipRequest.md)|  | 

### Return type

[**OrganizationMembership**](OrganizationMembership.md)

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
**403** | Authorization invalid |  -  |
**404** | Resource not found |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization_membership**
> OrganizationMembership delete_organization_membership(organization_id, user_id)

Remove a member from an organization

Removes the given membership from the organization

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.organization_membership import OrganizationMembership
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
    api_instance = clerk_backend_sdk.OrganizationMembershipsApi(api_client)
    organization_id = 'organization_id_example' # str | The ID of the organization the membership belongs to
    user_id = 'user_id_example' # str | The ID of the user that this membership belongs to

    try:
        # Remove a member from an organization
        api_response = await api_instance.delete_organization_membership(organization_id, user_id)
        print("The response of OrganizationMembershipsApi->delete_organization_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationMembershipsApi->delete_organization_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The ID of the organization the membership belongs to | 
 **user_id** | **str**| The ID of the user that this membership belongs to | 

### Return type

[**OrganizationMembership**](OrganizationMembership.md)

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
**401** | Authentication invalid |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization_memberships**
> OrganizationMemberships list_organization_memberships(organization_id, limit=limit, offset=offset, order_by=order_by)

Get a list of all members of an organization

Retrieves all user memberships for the given organization

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.organization_memberships import OrganizationMemberships
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
    api_instance = clerk_backend_sdk.OrganizationMembershipsApi(api_client)
    organization_id = 'organization_id_example' # str | The organization ID.
    limit = 10 # float | Applies a limit to the number of results returned. Can be used for paginating the results together with `offset`. (optional) (default to 10)
    offset = 0 # float | Skip the first `offset` results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with `limit`. (optional) (default to 0)
    order_by = 'order_by_example' # str | Sorts organizations memberships by phone_number, email_address, created_at, first_name, last_name or username. By prepending one of those values with + or -, we can choose to sort in ascending (ASC) or descending (DESC) order.\" (optional)

    try:
        # Get a list of all members of an organization
        api_response = await api_instance.list_organization_memberships(organization_id, limit=limit, offset=offset, order_by=order_by)
        print("The response of OrganizationMembershipsApi->list_organization_memberships:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationMembershipsApi->list_organization_memberships: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The organization ID. | 
 **limit** | **float**| Applies a limit to the number of results returned. Can be used for paginating the results together with &#x60;offset&#x60;. | [optional] [default to 10]
 **offset** | **float**| Skip the first &#x60;offset&#x60; results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with &#x60;limit&#x60;. | [optional] [default to 0]
 **order_by** | **str**| Sorts organizations memberships by phone_number, email_address, created_at, first_name, last_name or username. By prepending one of those values with + or -, we can choose to sort in ascending (ASC) or descending (DESC) order.\&quot; | [optional] 

### Return type

[**OrganizationMemberships**](OrganizationMemberships.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of organization memberships |  -  |
**401** | Authentication invalid |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization_membership**
> OrganizationMembership update_organization_membership(organization_id, user_id, update_organization_membership_request)

Update an organization membership

Updates the properties of an existing organization membership

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.organization_membership import OrganizationMembership
from clerk_backend_sdk.models.update_organization_membership_request import UpdateOrganizationMembershipRequest
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
    api_instance = clerk_backend_sdk.OrganizationMembershipsApi(api_client)
    organization_id = 'organization_id_example' # str | The ID of the organization the membership belongs to
    user_id = 'user_id_example' # str | The ID of the user that this membership belongs to
    update_organization_membership_request = clerk_backend_sdk.UpdateOrganizationMembershipRequest() # UpdateOrganizationMembershipRequest | 

    try:
        # Update an organization membership
        api_response = await api_instance.update_organization_membership(organization_id, user_id, update_organization_membership_request)
        print("The response of OrganizationMembershipsApi->update_organization_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationMembershipsApi->update_organization_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The ID of the organization the membership belongs to | 
 **user_id** | **str**| The ID of the user that this membership belongs to | 
 **update_organization_membership_request** | [**UpdateOrganizationMembershipRequest**](UpdateOrganizationMembershipRequest.md)|  | 

### Return type

[**OrganizationMembership**](OrganizationMembership.md)

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
**404** | Resource not found |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_organization_membership_metadata**
> OrganizationMembership update_organization_membership_metadata(organization_id, user_id, update_organization_membership_metadata_request)

Merge and update organization membership metadata

Update an organization membership's metadata attributes by merging existing values with the provided parameters. Metadata values will be updated via a deep merge. Deep means that any nested JSON objects will be merged as well. You can remove metadata keys at any level by setting their value to `null`.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.organization_membership import OrganizationMembership
from clerk_backend_sdk.models.update_organization_membership_metadata_request import UpdateOrganizationMembershipMetadataRequest
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
    api_instance = clerk_backend_sdk.OrganizationMembershipsApi(api_client)
    organization_id = 'organization_id_example' # str | The ID of the organization the membership belongs to
    user_id = 'user_id_example' # str | The ID of the user that this membership belongs to
    update_organization_membership_metadata_request = clerk_backend_sdk.UpdateOrganizationMembershipMetadataRequest() # UpdateOrganizationMembershipMetadataRequest | 

    try:
        # Merge and update organization membership metadata
        api_response = await api_instance.update_organization_membership_metadata(organization_id, user_id, update_organization_membership_metadata_request)
        print("The response of OrganizationMembershipsApi->update_organization_membership_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationMembershipsApi->update_organization_membership_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| The ID of the organization the membership belongs to | 
 **user_id** | **str**| The ID of the user that this membership belongs to | 
 **update_organization_membership_metadata_request** | [**UpdateOrganizationMembershipMetadataRequest**](UpdateOrganizationMembershipMetadataRequest.md)|  | 

### Return type

[**OrganizationMembership**](OrganizationMembership.md)

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
**404** | Resource not found |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

