# clerk_backend_sdk.OAuthApplicationsApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_o_auth_application**](OAuthApplicationsApi.md#create_o_auth_application) | **POST** /oauth_applications | Create an OAuth application
[**delete_o_auth_application**](OAuthApplicationsApi.md#delete_o_auth_application) | **DELETE** /oauth_applications/{oauth_application_id} | Delete an OAuth application
[**get_o_auth_application**](OAuthApplicationsApi.md#get_o_auth_application) | **GET** /oauth_applications/{oauth_application_id} | Retrieve an OAuth application by ID
[**list_o_auth_applications**](OAuthApplicationsApi.md#list_o_auth_applications) | **GET** /oauth_applications | Get a list of OAuth applications for an instance
[**rotate_o_auth_application_secret**](OAuthApplicationsApi.md#rotate_o_auth_application_secret) | **POST** /oauth_applications/{oauth_application_id}/rotate_secret | Rotate the client secret of the given OAuth application
[**update_o_auth_application**](OAuthApplicationsApi.md#update_o_auth_application) | **PATCH** /oauth_applications/{oauth_application_id} | Update an OAuth application


# **create_o_auth_application**
> OAuthApplicationWithSecret create_o_auth_application(create_o_auth_application_request=create_o_auth_application_request)

Create an OAuth application

Creates a new OAuth application with the given name and callback URL for an instance. The callback URL must be a valid url. All URL schemes are allowed such as `http://`, `https://`, `myapp://`, etc...

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.create_o_auth_application_request import CreateOAuthApplicationRequest
from clerk_backend_sdk.models.o_auth_application_with_secret import OAuthApplicationWithSecret
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
    api_instance = clerk_backend_sdk.OAuthApplicationsApi(api_client)
    create_o_auth_application_request = clerk_backend_sdk.CreateOAuthApplicationRequest() # CreateOAuthApplicationRequest |  (optional)

    try:
        # Create an OAuth application
        api_response = await api_instance.create_o_auth_application(create_o_auth_application_request=create_o_auth_application_request)
        print("The response of OAuthApplicationsApi->create_o_auth_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApplicationsApi->create_o_auth_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_o_auth_application_request** | [**CreateOAuthApplicationRequest**](CreateOAuthApplicationRequest.md)|  | [optional] 

### Return type

[**OAuthApplicationWithSecret**](OAuthApplicationWithSecret.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An OAuth application with client secret |  -  |
**400** | Request was not successful |  -  |
**403** | Authorization invalid |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_o_auth_application**
> DeletedObject delete_o_auth_application(oauth_application_id)

Delete an OAuth application

Deletes the given OAuth application. This is not reversible.

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
    api_instance = clerk_backend_sdk.OAuthApplicationsApi(api_client)
    oauth_application_id = 'oauth_application_id_example' # str | The ID of the OAuth application to delete

    try:
        # Delete an OAuth application
        api_response = await api_instance.delete_o_auth_application(oauth_application_id)
        print("The response of OAuthApplicationsApi->delete_o_auth_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApplicationsApi->delete_o_auth_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oauth_application_id** | **str**| The ID of the OAuth application to delete | 

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
**403** | Authorization invalid |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_o_auth_application**
> OAuthApplication get_o_auth_application(oauth_application_id)

Retrieve an OAuth application by ID

Fetches the OAuth application whose ID matches the provided `id` in the path.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.o_auth_application import OAuthApplication
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
    api_instance = clerk_backend_sdk.OAuthApplicationsApi(api_client)
    oauth_application_id = 'oauth_application_id_example' # str | The ID of the OAuth application

    try:
        # Retrieve an OAuth application by ID
        api_response = await api_instance.get_o_auth_application(oauth_application_id)
        print("The response of OAuthApplicationsApi->get_o_auth_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApplicationsApi->get_o_auth_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oauth_application_id** | **str**| The ID of the OAuth application | 

### Return type

[**OAuthApplication**](OAuthApplication.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An OAuth application |  -  |
**403** | Authorization invalid |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_o_auth_applications**
> OAuthApplications list_o_auth_applications(limit=limit, offset=offset)

Get a list of OAuth applications for an instance

This request returns the list of OAuth applications for an instance. Results can be paginated using the optional `limit` and `offset` query parameters. The OAuth applications are ordered by descending creation date. Most recent OAuth applications will be returned first.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.o_auth_applications import OAuthApplications
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
    api_instance = clerk_backend_sdk.OAuthApplicationsApi(api_client)
    limit = 10 # float | Applies a limit to the number of results returned. Can be used for paginating the results together with `offset`. (optional) (default to 10)
    offset = 0 # float | Skip the first `offset` results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with `limit`. (optional) (default to 0)

    try:
        # Get a list of OAuth applications for an instance
        api_response = await api_instance.list_o_auth_applications(limit=limit, offset=offset)
        print("The response of OAuthApplicationsApi->list_o_auth_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApplicationsApi->list_o_auth_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Applies a limit to the number of results returned. Can be used for paginating the results together with &#x60;offset&#x60;. | [optional] [default to 10]
 **offset** | **float**| Skip the first &#x60;offset&#x60; results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with &#x60;limit&#x60;. | [optional] [default to 0]

### Return type

[**OAuthApplications**](OAuthApplications.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of OAuth applications |  -  |
**400** | Request was not successful |  -  |
**403** | Authorization invalid |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_o_auth_application_secret**
> OAuthApplicationWithSecret rotate_o_auth_application_secret(oauth_application_id)

Rotate the client secret of the given OAuth application

Rotates the OAuth application's client secret. When the client secret is rotated, make sure to update it in authorized OAuth clients.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.o_auth_application_with_secret import OAuthApplicationWithSecret
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
    api_instance = clerk_backend_sdk.OAuthApplicationsApi(api_client)
    oauth_application_id = 'oauth_application_id_example' # str | The ID of the OAuth application for which to rotate the client secret

    try:
        # Rotate the client secret of the given OAuth application
        api_response = await api_instance.rotate_o_auth_application_secret(oauth_application_id)
        print("The response of OAuthApplicationsApi->rotate_o_auth_application_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApplicationsApi->rotate_o_auth_application_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oauth_application_id** | **str**| The ID of the OAuth application for which to rotate the client secret | 

### Return type

[**OAuthApplicationWithSecret**](OAuthApplicationWithSecret.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An OAuth application with client secret |  -  |
**403** | Authorization invalid |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_o_auth_application**
> OAuthApplication update_o_auth_application(oauth_application_id, update_o_auth_application_request)

Update an OAuth application

Updates an existing OAuth application

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.o_auth_application import OAuthApplication
from clerk_backend_sdk.models.update_o_auth_application_request import UpdateOAuthApplicationRequest
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
    api_instance = clerk_backend_sdk.OAuthApplicationsApi(api_client)
    oauth_application_id = 'oauth_application_id_example' # str | The ID of the OAuth application to update
    update_o_auth_application_request = clerk_backend_sdk.UpdateOAuthApplicationRequest() # UpdateOAuthApplicationRequest | 

    try:
        # Update an OAuth application
        api_response = await api_instance.update_o_auth_application(oauth_application_id, update_o_auth_application_request)
        print("The response of OAuthApplicationsApi->update_o_auth_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthApplicationsApi->update_o_auth_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oauth_application_id** | **str**| The ID of the OAuth application to update | 
 **update_o_auth_application_request** | [**UpdateOAuthApplicationRequest**](UpdateOAuthApplicationRequest.md)|  | 

### Return type

[**OAuthApplication**](OAuthApplication.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An OAuth application |  -  |
**403** | Authorization invalid |  -  |
**404** | Resource not found |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

