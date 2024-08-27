# clerk_backend_sdk.ClientsApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_client**](ClientsApi.md#get_client) | **GET** /clients/{client_id} | Get a client
[**get_client_list**](ClientsApi.md#get_client_list) | **GET** /clients | List all clients
[**verify_client**](ClientsApi.md#verify_client) | **POST** /clients/verify | Verify a client


# **get_client**
> Client get_client(client_id)

Get a client

Returns the details of a client.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.client import Client
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
    api_instance = clerk_backend_sdk.ClientsApi(api_client)
    client_id = 'client_id_example' # str | Client ID.

    try:
        # Get a client
        api_response = await api_instance.get_client(client_id)
        print("The response of ClientsApi->get_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientsApi->get_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| Client ID. | 

### Return type

[**Client**](Client.md)

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

# **get_client_list**
> List[Client] get_client_list(limit=limit, offset=offset)

List all clients

Returns a list of all clients. The clients are returned sorted by creation date, with the newest clients appearing first. Warning: the endpoint is being deprecated and will be removed in future versions.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.client import Client
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
    api_instance = clerk_backend_sdk.ClientsApi(api_client)
    limit = 10 # float | Applies a limit to the number of results returned. Can be used for paginating the results together with `offset`. (optional) (default to 10)
    offset = 0 # float | Skip the first `offset` results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with `limit`. (optional) (default to 0)

    try:
        # List all clients
        api_response = await api_instance.get_client_list(limit=limit, offset=offset)
        print("The response of ClientsApi->get_client_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientsApi->get_client_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Applies a limit to the number of results returned. Can be used for paginating the results together with &#x60;offset&#x60;. | [optional] [default to 10]
 **offset** | **float**| Skip the first &#x60;offset&#x60; results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with &#x60;limit&#x60;. | [optional] [default to 0]

### Return type

[**List[Client]**](Client.md)

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
**410** | The endpoint is considered deprecated and is pending removal. |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_client**
> Client verify_client(verify_client_request=verify_client_request)

Verify a client

Verifies the client in the provided token

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.client import Client
from clerk_backend_sdk.models.verify_client_request import VerifyClientRequest
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
    api_instance = clerk_backend_sdk.ClientsApi(api_client)
    verify_client_request = clerk_backend_sdk.VerifyClientRequest() # VerifyClientRequest | Parameters. (optional)

    try:
        # Verify a client
        api_response = await api_instance.verify_client(verify_client_request=verify_client_request)
        print("The response of ClientsApi->verify_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientsApi->verify_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_client_request** | [**VerifyClientRequest**](VerifyClientRequest.md)| Parameters. | [optional] 

### Return type

[**Client**](Client.md)

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
**401** | Authentication invalid |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

