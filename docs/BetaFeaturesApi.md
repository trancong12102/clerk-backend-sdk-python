# clerk_backend_sdk.BetaFeaturesApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_production_instance_domain**](BetaFeaturesApi.md#change_production_instance_domain) | **POST** /instance/change_domain | Update production instance domain
[**update_instance_auth_config**](BetaFeaturesApi.md#update_instance_auth_config) | **PATCH** /beta_features/instance_settings | Update instance settings
[**update_production_instance_domain**](BetaFeaturesApi.md#update_production_instance_domain) | **PUT** /beta_features/domain | Update production instance domain


# **change_production_instance_domain**
> change_production_instance_domain(change_production_instance_domain_request=change_production_instance_domain_request)

Update production instance domain

Change the domain of a production instance.  Changing the domain requires updating the [DNS records](https://clerk.com/docs/deployments/overview#dns-records) accordingly, deploying new [SSL certificates](https://clerk.com/docs/deployments/overview#deploy), updating your Social Connection's redirect URLs and setting the new keys in your code.  WARNING: Changing your domain will invalidate all current user sessions (i.e. users will be logged out). Also, while your application is being deployed, a small downtime is expected to occur.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.change_production_instance_domain_request import ChangeProductionInstanceDomainRequest
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
    api_instance = clerk_backend_sdk.BetaFeaturesApi(api_client)
    change_production_instance_domain_request = clerk_backend_sdk.ChangeProductionInstanceDomainRequest() # ChangeProductionInstanceDomainRequest |  (optional)

    try:
        # Update production instance domain
        await api_instance.change_production_instance_domain(change_production_instance_domain_request=change_production_instance_domain_request)
    except Exception as e:
        print("Exception when calling BetaFeaturesApi->change_production_instance_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_production_instance_domain_request** | [**ChangeProductionInstanceDomainRequest**](ChangeProductionInstanceDomainRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Request was not successful |  -  |
**422** | Request was not successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_instance_auth_config**
> UpdateInstanceAuthConfig200Response update_instance_auth_config(update_instance_auth_config_request=update_instance_auth_config_request)

Update instance settings

Updates the settings of an instance

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.update_instance_auth_config200_response import UpdateInstanceAuthConfig200Response
from clerk_backend_sdk.models.update_instance_auth_config_request import UpdateInstanceAuthConfigRequest
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
    api_instance = clerk_backend_sdk.BetaFeaturesApi(api_client)
    update_instance_auth_config_request = clerk_backend_sdk.UpdateInstanceAuthConfigRequest() # UpdateInstanceAuthConfigRequest |  (optional)

    try:
        # Update instance settings
        api_response = await api_instance.update_instance_auth_config(update_instance_auth_config_request=update_instance_auth_config_request)
        print("The response of BetaFeaturesApi->update_instance_auth_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BetaFeaturesApi->update_instance_auth_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_instance_auth_config_request** | [**UpdateInstanceAuthConfigRequest**](UpdateInstanceAuthConfigRequest.md)|  | [optional] 

### Return type

[**UpdateInstanceAuthConfig200Response**](UpdateInstanceAuthConfig200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | InstanceSettings Server API |  -  |
**402** | Payment required |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_production_instance_domain**
> update_production_instance_domain(update_production_instance_domain_request=update_production_instance_domain_request)

Update production instance domain

Change the domain of a production instance.  Changing the domain requires updating the [DNS records](https://clerk.com/docs/deployments/overview#dns-records) accordingly, deploying new [SSL certificates](https://clerk.com/docs/deployments/overview#deploy), updating your Social Connection's redirect URLs and setting the new keys in your code.  WARNING: Changing your domain will invalidate all current user sessions (i.e. users will be logged out). Also, while your application is being deployed, a small downtime is expected to occur.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.update_production_instance_domain_request import UpdateProductionInstanceDomainRequest
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
    api_instance = clerk_backend_sdk.BetaFeaturesApi(api_client)
    update_production_instance_domain_request = clerk_backend_sdk.UpdateProductionInstanceDomainRequest() # UpdateProductionInstanceDomainRequest |  (optional)

    try:
        # Update production instance domain
        await api_instance.update_production_instance_domain(update_production_instance_domain_request=update_production_instance_domain_request)
    except Exception as e:
        print("Exception when calling BetaFeaturesApi->update_production_instance_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_production_instance_domain_request** | [**UpdateProductionInstanceDomainRequest**](UpdateProductionInstanceDomainRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Request was not successful |  -  |
**422** | Request was not successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

