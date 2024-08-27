# clerk_backend_sdk.InstanceSettingsApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_instance**](InstanceSettingsApi.md#update_instance) | **PATCH** /instance | Update instance settings
[**update_instance_organization_settings**](InstanceSettingsApi.md#update_instance_organization_settings) | **PATCH** /instance/organization_settings | Update instance organization settings
[**update_instance_restrictions**](InstanceSettingsApi.md#update_instance_restrictions) | **PATCH** /instance/restrictions | Update instance restrictions


# **update_instance**
> update_instance(update_instance_request=update_instance_request)

Update instance settings

Updates the settings of an instance

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.update_instance_request import UpdateInstanceRequest
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
    api_instance = clerk_backend_sdk.InstanceSettingsApi(api_client)
    update_instance_request = clerk_backend_sdk.UpdateInstanceRequest() # UpdateInstanceRequest |  (optional)

    try:
        # Update instance settings
        await api_instance.update_instance(update_instance_request=update_instance_request)
    except Exception as e:
        print("Exception when calling InstanceSettingsApi->update_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_instance_request** | [**UpdateInstanceRequest**](UpdateInstanceRequest.md)|  | [optional] 

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
**204** | Accepted |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_instance_organization_settings**
> OrganizationSettings update_instance_organization_settings(update_instance_organization_settings_request=update_instance_organization_settings_request)

Update instance organization settings

Updates the organization settings of the instance

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.organization_settings import OrganizationSettings
from clerk_backend_sdk.models.update_instance_organization_settings_request import UpdateInstanceOrganizationSettingsRequest
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
    api_instance = clerk_backend_sdk.InstanceSettingsApi(api_client)
    update_instance_organization_settings_request = clerk_backend_sdk.UpdateInstanceOrganizationSettingsRequest() # UpdateInstanceOrganizationSettingsRequest |  (optional)

    try:
        # Update instance organization settings
        api_response = await api_instance.update_instance_organization_settings(update_instance_organization_settings_request=update_instance_organization_settings_request)
        print("The response of InstanceSettingsApi->update_instance_organization_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstanceSettingsApi->update_instance_organization_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_instance_organization_settings_request** | [**UpdateInstanceOrganizationSettingsRequest**](UpdateInstanceOrganizationSettingsRequest.md)|  | [optional] 

### Return type

[**OrganizationSettings**](OrganizationSettings.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**402** | Payment required |  -  |
**404** | Resource not found |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_instance_restrictions**
> InstanceRestrictions update_instance_restrictions(update_instance_restrictions_request=update_instance_restrictions_request)

Update instance restrictions

Updates the restriction settings of an instance

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.instance_restrictions import InstanceRestrictions
from clerk_backend_sdk.models.update_instance_restrictions_request import UpdateInstanceRestrictionsRequest
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
    api_instance = clerk_backend_sdk.InstanceSettingsApi(api_client)
    update_instance_restrictions_request = clerk_backend_sdk.UpdateInstanceRestrictionsRequest() # UpdateInstanceRestrictionsRequest |  (optional)

    try:
        # Update instance restrictions
        api_response = await api_instance.update_instance_restrictions(update_instance_restrictions_request=update_instance_restrictions_request)
        print("The response of InstanceSettingsApi->update_instance_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstanceSettingsApi->update_instance_restrictions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_instance_restrictions_request** | [**UpdateInstanceRestrictionsRequest**](UpdateInstanceRestrictionsRequest.md)|  | [optional] 

### Return type

[**InstanceRestrictions**](InstanceRestrictions.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**402** | Payment required |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

