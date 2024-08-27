# clerk_backend_sdk.RedirectURLsApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_redirect_url**](RedirectURLsApi.md#create_redirect_url) | **POST** /redirect_urls | Create a redirect URL
[**delete_redirect_url**](RedirectURLsApi.md#delete_redirect_url) | **DELETE** /redirect_urls/{id} | Delete a redirect URL
[**get_redirect_url**](RedirectURLsApi.md#get_redirect_url) | **GET** /redirect_urls/{id} | Retrieve a redirect URL
[**list_redirect_urls**](RedirectURLsApi.md#list_redirect_urls) | **GET** /redirect_urls | List all redirect URLs


# **create_redirect_url**
> RedirectURL create_redirect_url(create_redirect_url_request=create_redirect_url_request)

Create a redirect URL

Create a redirect URL

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.create_redirect_url_request import CreateRedirectURLRequest
from clerk_backend_sdk.models.redirect_url import RedirectURL
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
    api_instance = clerk_backend_sdk.RedirectURLsApi(api_client)
    create_redirect_url_request = clerk_backend_sdk.CreateRedirectURLRequest() # CreateRedirectURLRequest |  (optional)

    try:
        # Create a redirect URL
        api_response = await api_instance.create_redirect_url(create_redirect_url_request=create_redirect_url_request)
        print("The response of RedirectURLsApi->create_redirect_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RedirectURLsApi->create_redirect_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_redirect_url_request** | [**CreateRedirectURLRequest**](CreateRedirectURLRequest.md)|  | [optional] 

### Return type

[**RedirectURL**](RedirectURL.md)

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

# **delete_redirect_url**
> DeletedObject delete_redirect_url(id)

Delete a redirect URL

Remove the selected redirect URL from the whitelist of the instance

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
    api_instance = clerk_backend_sdk.RedirectURLsApi(api_client)
    id = 'id_example' # str | The ID of the redirect URL

    try:
        # Delete a redirect URL
        api_response = await api_instance.delete_redirect_url(id)
        print("The response of RedirectURLsApi->delete_redirect_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RedirectURLsApi->delete_redirect_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the redirect URL | 

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
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_redirect_url**
> RedirectURL get_redirect_url(id)

Retrieve a redirect URL

Retrieve the details of the redirect URL with the given ID

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.redirect_url import RedirectURL
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
    api_instance = clerk_backend_sdk.RedirectURLsApi(api_client)
    id = 'id_example' # str | The ID of the redirect URL

    try:
        # Retrieve a redirect URL
        api_response = await api_instance.get_redirect_url(id)
        print("The response of RedirectURLsApi->get_redirect_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RedirectURLsApi->get_redirect_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the redirect URL | 

### Return type

[**RedirectURL**](RedirectURL.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_redirect_urls**
> List[RedirectURL] list_redirect_urls()

List all redirect URLs

Lists all whitelisted redirect_urls for the instance

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.redirect_url import RedirectURL
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
    api_instance = clerk_backend_sdk.RedirectURLsApi(api_client)

    try:
        # List all redirect URLs
        api_response = await api_instance.list_redirect_urls()
        print("The response of RedirectURLsApi->list_redirect_urls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RedirectURLsApi->list_redirect_urls: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[RedirectURL]**](RedirectURL.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Redirect URLs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

