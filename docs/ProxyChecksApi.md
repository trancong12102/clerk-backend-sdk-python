# clerk_backend_sdk.ProxyChecksApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verify_domain_proxy**](ProxyChecksApi.md#verify_domain_proxy) | **POST** /proxy_checks | Verify the proxy configuration for your domain


# **verify_domain_proxy**
> ProxyCheck verify_domain_proxy(verify_domain_proxy_request=verify_domain_proxy_request)

Verify the proxy configuration for your domain

This endpoint can be used to validate that a proxy-enabled domain is operational. It tries to verify that the proxy URL provided in the parameters maps to a functional proxy that can reach the Clerk Frontend API.  You can use this endpoint before you set a proxy URL for a domain. This way you can ensure that switching to proxy-based configuration will not lead to downtime for your instance.  The `proxy_url` parameter allows for testing proxy configurations for domains that don't have a proxy URL yet, or operate on a different proxy URL than the one provided. It can also be used to re-validate a domain that is already configured to work with a proxy.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.proxy_check import ProxyCheck
from clerk_backend_sdk.models.verify_domain_proxy_request import VerifyDomainProxyRequest
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
    api_instance = clerk_backend_sdk.ProxyChecksApi(api_client)
    verify_domain_proxy_request = clerk_backend_sdk.VerifyDomainProxyRequest() # VerifyDomainProxyRequest |  (optional)

    try:
        # Verify the proxy configuration for your domain
        api_response = await api_instance.verify_domain_proxy(verify_domain_proxy_request=verify_domain_proxy_request)
        print("The response of ProxyChecksApi->verify_domain_proxy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProxyChecksApi->verify_domain_proxy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_domain_proxy_request** | [**VerifyDomainProxyRequest**](VerifyDomainProxyRequest.md)|  | [optional] 

### Return type

[**ProxyCheck**](ProxyCheck.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Health check information about a domain&#39;s proxy configuration validation attempt. |  -  |
**400** | Request was not successful |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

