# clerk_backend_sdk.WebhooksApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_svix_app**](WebhooksApi.md#create_svix_app) | **POST** /webhooks/svix | Create a Svix app
[**delete_svix_app**](WebhooksApi.md#delete_svix_app) | **DELETE** /webhooks/svix | Delete a Svix app
[**generate_svix_auth_url**](WebhooksApi.md#generate_svix_auth_url) | **POST** /webhooks/svix_url | Create a Svix Dashboard URL


# **create_svix_app**
> SvixURL create_svix_app()

Create a Svix app

Create a Svix app and associate it with the current instance

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.svix_url import SvixURL
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
    api_instance = clerk_backend_sdk.WebhooksApi(api_client)

    try:
        # Create a Svix app
        api_response = await api_instance.create_svix_app()
        print("The response of WebhooksApi->create_svix_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->create_svix_app: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SvixURL**](SvixURL.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response that contains a temporary Svix URL to access management dashboard |  -  |
**400** | Request was not successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_svix_app**
> delete_svix_app()

Delete a Svix app

Delete a Svix app and disassociate it from the current instance

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
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
    api_instance = clerk_backend_sdk.WebhooksApi(api_client)

    try:
        # Delete a Svix app
        await api_instance.delete_svix_app()
    except Exception as e:
        print("Exception when calling WebhooksApi->delete_svix_app: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Svix app was successfully deleted |  -  |
**400** | Request was not successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_svix_auth_url**
> SvixURL generate_svix_auth_url()

Create a Svix Dashboard URL

Generate a new url for accessing the Svix's management dashboard for that particular instance

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.svix_url import SvixURL
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
    api_instance = clerk_backend_sdk.WebhooksApi(api_client)

    try:
        # Create a Svix Dashboard URL
        api_response = await api_instance.generate_svix_auth_url()
        print("The response of WebhooksApi->generate_svix_auth_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->generate_svix_auth_url: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SvixURL**](SvixURL.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response that contains a temporary Svix URL to access management dashboard |  -  |
**400** | Request was not successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

