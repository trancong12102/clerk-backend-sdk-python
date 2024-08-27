# clerk_backend_sdk.TestingTokensApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_testing_token**](TestingTokensApi.md#create_testing_token) | **POST** /testing_tokens | Retrieve a new testing token


# **create_testing_token**
> TestingToken create_testing_token()

Retrieve a new testing token

Retrieve a new testing token. Only available for development instances.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.testing_token import TestingToken
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
    api_instance = clerk_backend_sdk.TestingTokensApi(api_client)

    try:
        # Retrieve a new testing token
        api_response = await api_instance.create_testing_token()
        print("The response of TestingTokensApi->create_testing_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestingTokensApi->create_testing_token: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TestingToken**](TestingToken.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Testing Token |  -  |
**400** | The instance is a production instance, but this endpoint is only available in development instances. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

