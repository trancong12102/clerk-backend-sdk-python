# clerk_backend_sdk.SignInTokensApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sign_in_token**](SignInTokensApi.md#create_sign_in_token) | **POST** /sign_in_tokens | Create sign-in token
[**revoke_sign_in_token**](SignInTokensApi.md#revoke_sign_in_token) | **POST** /sign_in_tokens/{sign_in_token_id}/revoke | Revoke the given sign-in token


# **create_sign_in_token**
> SignInToken create_sign_in_token(create_sign_in_token_request=create_sign_in_token_request)

Create sign-in token

Creates a new sign-in token and associates it with the given user. By default, sign-in tokens expire in 30 days. You can optionally supply a different duration in seconds using the `expires_in_seconds` property.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.create_sign_in_token_request import CreateSignInTokenRequest
from clerk_backend_sdk.models.sign_in_token import SignInToken
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
    api_instance = clerk_backend_sdk.SignInTokensApi(api_client)
    create_sign_in_token_request = clerk_backend_sdk.CreateSignInTokenRequest() # CreateSignInTokenRequest |  (optional)

    try:
        # Create sign-in token
        api_response = await api_instance.create_sign_in_token(create_sign_in_token_request=create_sign_in_token_request)
        print("The response of SignInTokensApi->create_sign_in_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignInTokensApi->create_sign_in_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_sign_in_token_request** | [**CreateSignInTokenRequest**](CreateSignInTokenRequest.md)|  | [optional] 

### Return type

[**SignInToken**](SignInToken.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Resource not found |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_sign_in_token**
> SignInToken revoke_sign_in_token(sign_in_token_id)

Revoke the given sign-in token

Revokes a pending sign-in token

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.sign_in_token import SignInToken
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
    api_instance = clerk_backend_sdk.SignInTokensApi(api_client)
    sign_in_token_id = 'sign_in_token_id_example' # str | The ID of the sign-in token to be revoked

    try:
        # Revoke the given sign-in token
        api_response = await api_instance.revoke_sign_in_token(sign_in_token_id)
        print("The response of SignInTokensApi->revoke_sign_in_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignInTokensApi->revoke_sign_in_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sign_in_token_id** | **str**| The ID of the sign-in token to be revoked | 

### Return type

[**SignInToken**](SignInToken.md)

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

