# clerk_backend_sdk.SAMLConnectionsApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_saml_connection**](SAMLConnectionsApi.md#create_saml_connection) | **POST** /saml_connections | Create a SAML Connection
[**delete_saml_connection**](SAMLConnectionsApi.md#delete_saml_connection) | **DELETE** /saml_connections/{saml_connection_id} | Delete a SAML Connection
[**get_saml_connection**](SAMLConnectionsApi.md#get_saml_connection) | **GET** /saml_connections/{saml_connection_id} | Retrieve a SAML Connection by ID
[**list_saml_connections**](SAMLConnectionsApi.md#list_saml_connections) | **GET** /saml_connections | Get a list of SAML Connections for an instance
[**update_saml_connection**](SAMLConnectionsApi.md#update_saml_connection) | **PATCH** /saml_connections/{saml_connection_id} | Update a SAML Connection


# **create_saml_connection**
> SAMLConnection create_saml_connection(create_saml_connection_request=create_saml_connection_request)

Create a SAML Connection

Create a new SAML Connection.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.create_saml_connection_request import CreateSAMLConnectionRequest
from clerk_backend_sdk.models.saml_connection import SAMLConnection
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
    api_instance = clerk_backend_sdk.SAMLConnectionsApi(api_client)
    create_saml_connection_request = clerk_backend_sdk.CreateSAMLConnectionRequest() # CreateSAMLConnectionRequest |  (optional)

    try:
        # Create a SAML Connection
        api_response = await api_instance.create_saml_connection(create_saml_connection_request=create_saml_connection_request)
        print("The response of SAMLConnectionsApi->create_saml_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SAMLConnectionsApi->create_saml_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_saml_connection_request** | [**CreateSAMLConnectionRequest**](CreateSAMLConnectionRequest.md)|  | [optional] 

### Return type

[**SAMLConnection**](SAMLConnection.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A SAML Connection |  -  |
**402** | Payment required |  -  |
**403** | Authorization invalid |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_saml_connection**
> DeletedObject delete_saml_connection(saml_connection_id)

Delete a SAML Connection

Deletes the SAML Connection whose ID matches the provided `id` in the path.

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
    api_instance = clerk_backend_sdk.SAMLConnectionsApi(api_client)
    saml_connection_id = 'saml_connection_id_example' # str | The ID of the SAML Connection to delete

    try:
        # Delete a SAML Connection
        api_response = await api_instance.delete_saml_connection(saml_connection_id)
        print("The response of SAMLConnectionsApi->delete_saml_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SAMLConnectionsApi->delete_saml_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saml_connection_id** | **str**| The ID of the SAML Connection to delete | 

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
**403** | Authorization invalid |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saml_connection**
> SAMLConnection get_saml_connection(saml_connection_id)

Retrieve a SAML Connection by ID

Fetches the SAML Connection whose ID matches the provided `saml_connection_id` in the path.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.saml_connection import SAMLConnection
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
    api_instance = clerk_backend_sdk.SAMLConnectionsApi(api_client)
    saml_connection_id = 'saml_connection_id_example' # str | The ID of the SAML Connection

    try:
        # Retrieve a SAML Connection by ID
        api_response = await api_instance.get_saml_connection(saml_connection_id)
        print("The response of SAMLConnectionsApi->get_saml_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SAMLConnectionsApi->get_saml_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saml_connection_id** | **str**| The ID of the SAML Connection | 

### Return type

[**SAMLConnection**](SAMLConnection.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A SAML Connection |  -  |
**402** | Payment required |  -  |
**403** | Authorization invalid |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_saml_connections**
> SAMLConnections list_saml_connections(limit=limit, offset=offset)

Get a list of SAML Connections for an instance

Returns the list of SAML Connections for an instance. Results can be paginated using the optional `limit` and `offset` query parameters. The SAML Connections are ordered by descending creation date and the most recent will be returned first.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.saml_connections import SAMLConnections
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
    api_instance = clerk_backend_sdk.SAMLConnectionsApi(api_client)
    limit = 10 # float | Applies a limit to the number of results returned. Can be used for paginating the results together with `offset`. (optional) (default to 10)
    offset = 0 # float | Skip the first `offset` results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with `limit`. (optional) (default to 0)

    try:
        # Get a list of SAML Connections for an instance
        api_response = await api_instance.list_saml_connections(limit=limit, offset=offset)
        print("The response of SAMLConnectionsApi->list_saml_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SAMLConnectionsApi->list_saml_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Applies a limit to the number of results returned. Can be used for paginating the results together with &#x60;offset&#x60;. | [optional] [default to 10]
 **offset** | **float**| Skip the first &#x60;offset&#x60; results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with &#x60;limit&#x60;. | [optional] [default to 0]

### Return type

[**SAMLConnections**](SAMLConnections.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of SAML Connections |  -  |
**402** | Payment required |  -  |
**403** | Authorization invalid |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_saml_connection**
> SAMLConnection update_saml_connection(saml_connection_id, update_saml_connection_request)

Update a SAML Connection

Updates the SAML Connection whose ID matches the provided `id` in the path.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.saml_connection import SAMLConnection
from clerk_backend_sdk.models.update_saml_connection_request import UpdateSAMLConnectionRequest
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
    api_instance = clerk_backend_sdk.SAMLConnectionsApi(api_client)
    saml_connection_id = 'saml_connection_id_example' # str | The ID of the SAML Connection to update
    update_saml_connection_request = clerk_backend_sdk.UpdateSAMLConnectionRequest() # UpdateSAMLConnectionRequest | 

    try:
        # Update a SAML Connection
        api_response = await api_instance.update_saml_connection(saml_connection_id, update_saml_connection_request)
        print("The response of SAMLConnectionsApi->update_saml_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SAMLConnectionsApi->update_saml_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saml_connection_id** | **str**| The ID of the SAML Connection to update | 
 **update_saml_connection_request** | [**UpdateSAMLConnectionRequest**](UpdateSAMLConnectionRequest.md)|  | 

### Return type

[**SAMLConnection**](SAMLConnection.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A SAML Connection |  -  |
**402** | Payment required |  -  |
**403** | Authorization invalid |  -  |
**404** | Resource not found |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

