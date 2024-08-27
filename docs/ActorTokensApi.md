# clerk_backend_sdk.ActorTokensApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_actor_token**](ActorTokensApi.md#create_actor_token) | **POST** /actor_tokens | Create actor token
[**revoke_actor_token**](ActorTokensApi.md#revoke_actor_token) | **POST** /actor_tokens/{actor_token_id}/revoke | Revoke actor token


# **create_actor_token**
> ActorToken create_actor_token(create_actor_token_request=create_actor_token_request)

Create actor token

Create an actor token that can be used to impersonate the given user. The `actor` parameter needs to include at least a \"sub\" key whose value is the ID of the actor (impersonating) user.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.actor_token import ActorToken
from clerk_backend_sdk.models.create_actor_token_request import CreateActorTokenRequest
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
    api_instance = clerk_backend_sdk.ActorTokensApi(api_client)
    create_actor_token_request = clerk_backend_sdk.CreateActorTokenRequest() # CreateActorTokenRequest |  (optional)

    try:
        # Create actor token
        api_response = await api_instance.create_actor_token(create_actor_token_request=create_actor_token_request)
        print("The response of ActorTokensApi->create_actor_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActorTokensApi->create_actor_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_actor_token_request** | [**CreateActorTokenRequest**](CreateActorTokenRequest.md)|  | [optional] 

### Return type

[**ActorToken**](ActorToken.md)

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

# **revoke_actor_token**
> ActorToken revoke_actor_token(actor_token_id)

Revoke actor token

Revokes a pending actor token.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.actor_token import ActorToken
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
    api_instance = clerk_backend_sdk.ActorTokensApi(api_client)
    actor_token_id = 'actor_token_id_example' # str | The ID of the actor token to be revoked.

    try:
        # Revoke actor token
        api_response = await api_instance.revoke_actor_token(actor_token_id)
        print("The response of ActorTokensApi->revoke_actor_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActorTokensApi->revoke_actor_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_token_id** | **str**| The ID of the actor token to be revoked. | 

### Return type

[**ActorToken**](ActorToken.md)

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

