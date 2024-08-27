# clerk_backend_sdk.AllowListBlockListApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_allowlist_identifier**](AllowListBlockListApi.md#create_allowlist_identifier) | **POST** /allowlist_identifiers | Add identifier to the allow-list
[**create_blocklist_identifier**](AllowListBlockListApi.md#create_blocklist_identifier) | **POST** /blocklist_identifiers | Add identifier to the block-list
[**delete_allowlist_identifier**](AllowListBlockListApi.md#delete_allowlist_identifier) | **DELETE** /allowlist_identifiers/{identifier_id} | Delete identifier from allow-list
[**delete_blocklist_identifier**](AllowListBlockListApi.md#delete_blocklist_identifier) | **DELETE** /blocklist_identifiers/{identifier_id} | Delete identifier from block-list
[**list_allowlist_identifiers**](AllowListBlockListApi.md#list_allowlist_identifiers) | **GET** /allowlist_identifiers | List all identifiers on the allow-list
[**list_blocklist_identifiers**](AllowListBlockListApi.md#list_blocklist_identifiers) | **GET** /blocklist_identifiers | List all identifiers on the block-list


# **create_allowlist_identifier**
> AllowlistIdentifier create_allowlist_identifier(create_allowlist_identifier_request=create_allowlist_identifier_request)

Add identifier to the allow-list

Create an identifier allowed to sign up to an instance

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.allowlist_identifier import AllowlistIdentifier
from clerk_backend_sdk.models.create_allowlist_identifier_request import CreateAllowlistIdentifierRequest
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
    api_instance = clerk_backend_sdk.AllowListBlockListApi(api_client)
    create_allowlist_identifier_request = clerk_backend_sdk.CreateAllowlistIdentifierRequest() # CreateAllowlistIdentifierRequest |  (optional)

    try:
        # Add identifier to the allow-list
        api_response = await api_instance.create_allowlist_identifier(create_allowlist_identifier_request=create_allowlist_identifier_request)
        print("The response of AllowListBlockListApi->create_allowlist_identifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllowListBlockListApi->create_allowlist_identifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_allowlist_identifier_request** | [**CreateAllowlistIdentifierRequest**](CreateAllowlistIdentifierRequest.md)|  | [optional] 

### Return type

[**AllowlistIdentifier**](AllowlistIdentifier.md)

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
**402** | Payment required |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_blocklist_identifier**
> BlocklistIdentifier create_blocklist_identifier(create_blocklist_identifier_request=create_blocklist_identifier_request)

Add identifier to the block-list

Create an identifier that is blocked from accessing an instance

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.blocklist_identifier import BlocklistIdentifier
from clerk_backend_sdk.models.create_blocklist_identifier_request import CreateBlocklistIdentifierRequest
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
    api_instance = clerk_backend_sdk.AllowListBlockListApi(api_client)
    create_blocklist_identifier_request = clerk_backend_sdk.CreateBlocklistIdentifierRequest() # CreateBlocklistIdentifierRequest |  (optional)

    try:
        # Add identifier to the block-list
        api_response = await api_instance.create_blocklist_identifier(create_blocklist_identifier_request=create_blocklist_identifier_request)
        print("The response of AllowListBlockListApi->create_blocklist_identifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllowListBlockListApi->create_blocklist_identifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_blocklist_identifier_request** | [**CreateBlocklistIdentifierRequest**](CreateBlocklistIdentifierRequest.md)|  | [optional] 

### Return type

[**BlocklistIdentifier**](BlocklistIdentifier.md)

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
**402** | Payment required |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_allowlist_identifier**
> DeletedObject delete_allowlist_identifier(identifier_id)

Delete identifier from allow-list

Delete an identifier from the instance allow-list

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.deleted_object import DeletedObject
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
    api_instance = clerk_backend_sdk.AllowListBlockListApi(api_client)
    identifier_id = 'identifier_id_example' # str | The ID of the identifier to delete from the allow-list

    try:
        # Delete identifier from allow-list
        api_response = await api_instance.delete_allowlist_identifier(identifier_id)
        print("The response of AllowListBlockListApi->delete_allowlist_identifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllowListBlockListApi->delete_allowlist_identifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_id** | **str**| The ID of the identifier to delete from the allow-list | 

### Return type

[**DeletedObject**](DeletedObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted Object |  -  |
**402** | Payment required |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_blocklist_identifier**
> DeletedObject delete_blocklist_identifier(identifier_id)

Delete identifier from block-list

Delete an identifier from the instance block-list

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.deleted_object import DeletedObject
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
    api_instance = clerk_backend_sdk.AllowListBlockListApi(api_client)
    identifier_id = 'identifier_id_example' # str | The ID of the identifier to delete from the block-list

    try:
        # Delete identifier from block-list
        api_response = await api_instance.delete_blocklist_identifier(identifier_id)
        print("The response of AllowListBlockListApi->delete_blocklist_identifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllowListBlockListApi->delete_blocklist_identifier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier_id** | **str**| The ID of the identifier to delete from the block-list | 

### Return type

[**DeletedObject**](DeletedObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted Object |  -  |
**402** | Payment required |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_allowlist_identifiers**
> List[AllowlistIdentifier] list_allowlist_identifiers()

List all identifiers on the allow-list

Get a list of all identifiers allowed to sign up to an instance

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.allowlist_identifier import AllowlistIdentifier
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
    api_instance = clerk_backend_sdk.AllowListBlockListApi(api_client)

    try:
        # List all identifiers on the allow-list
        api_response = await api_instance.list_allowlist_identifiers()
        print("The response of AllowListBlockListApi->list_allowlist_identifiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllowListBlockListApi->list_allowlist_identifiers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AllowlistIdentifier]**](AllowlistIdentifier.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Authentication invalid |  -  |
**402** | Payment required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_blocklist_identifiers**
> BlocklistIdentifiers list_blocklist_identifiers()

List all identifiers on the block-list

Get a list of all identifiers which are not allowed to access an instance

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.blocklist_identifiers import BlocklistIdentifiers
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
    api_instance = clerk_backend_sdk.AllowListBlockListApi(api_client)

    try:
        # List all identifiers on the block-list
        api_response = await api_instance.list_blocklist_identifiers()
        print("The response of AllowListBlockListApi->list_blocklist_identifiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllowListBlockListApi->list_blocklist_identifiers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BlocklistIdentifiers**](BlocklistIdentifiers.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Authentication invalid |  -  |
**402** | Payment required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

