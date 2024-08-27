# clerk_backend_sdk.SignUpsApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_sign_up**](SignUpsApi.md#update_sign_up) | **PATCH** /sign_ups/{id} | Update a sign-up


# **update_sign_up**
> SignUp update_sign_up(id, update_sign_up_request=update_sign_up_request)

Update a sign-up

Update the sign-up with the given ID

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.sign_up import SignUp
from clerk_backend_sdk.models.update_sign_up_request import UpdateSignUpRequest
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
    api_instance = clerk_backend_sdk.SignUpsApi(api_client)
    id = 'id_example' # str | The ID of the sign-up to update
    update_sign_up_request = clerk_backend_sdk.UpdateSignUpRequest() # UpdateSignUpRequest |  (optional)

    try:
        # Update a sign-up
        api_response = await api_instance.update_sign_up(id, update_sign_up_request=update_sign_up_request)
        print("The response of SignUpsApi->update_sign_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignUpsApi->update_sign_up: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the sign-up to update | 
 **update_sign_up_request** | [**UpdateSignUpRequest**](UpdateSignUpRequest.md)|  | [optional] 

### Return type

[**SignUp**](SignUp.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Authorization invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

