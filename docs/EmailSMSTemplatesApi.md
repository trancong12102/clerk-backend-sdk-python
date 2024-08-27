# clerk_backend_sdk.EmailSMSTemplatesApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_template**](EmailSMSTemplatesApi.md#get_template) | **GET** /templates/{template_type}/{slug} | Retrieve a template
[**get_template_list**](EmailSMSTemplatesApi.md#get_template_list) | **GET** /templates/{template_type} | List all templates
[**preview_template**](EmailSMSTemplatesApi.md#preview_template) | **POST** /templates/{template_type}/{slug}/preview | Preview changes to a template
[**revert_template**](EmailSMSTemplatesApi.md#revert_template) | **POST** /templates/{template_type}/{slug}/revert | Revert a template
[**toggle_template_delivery**](EmailSMSTemplatesApi.md#toggle_template_delivery) | **POST** /templates/{template_type}/{slug}/toggle_delivery | Toggle the delivery by Clerk for a template of a given type and slug
[**upsert_template**](EmailSMSTemplatesApi.md#upsert_template) | **PUT** /templates/{template_type}/{slug} | Update a template for a given type and slug


# **get_template**
> Template get_template(template_type, slug)

Retrieve a template

Returns the details of a template

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.template import Template
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
    api_instance = clerk_backend_sdk.EmailSMSTemplatesApi(api_client)
    template_type = 'template_type_example' # str | The type of templates to retrieve (email or SMS)
    slug = 'slug_example' # str | The slug (i.e. machine-friendly name) of the template to retrieve

    try:
        # Retrieve a template
        api_response = await api_instance.get_template(template_type, slug)
        print("The response of EmailSMSTemplatesApi->get_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSMSTemplatesApi->get_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_type** | **str**| The type of templates to retrieve (email or SMS) | 
 **slug** | **str**| The slug (i.e. machine-friendly name) of the template to retrieve | 

### Return type

[**Template**](Template.md)

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
**401** | Authentication invalid |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_list**
> List[Template] get_template_list(template_type)

List all templates

Returns a list of all templates. The templates are returned sorted by position.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.template import Template
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
    api_instance = clerk_backend_sdk.EmailSMSTemplatesApi(api_client)
    template_type = 'template_type_example' # str | The type of templates to list (email or SMS)

    try:
        # List all templates
        api_response = await api_instance.get_template_list(template_type)
        print("The response of EmailSMSTemplatesApi->get_template_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSMSTemplatesApi->get_template_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_type** | **str**| The type of templates to list (email or SMS) | 

### Return type

[**List[Template]**](Template.md)

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
**401** | Authentication invalid |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_template**
> object preview_template(template_type, slug, preview_template_request=preview_template_request)

Preview changes to a template

Returns a preview of a template for a given template_type, slug and body

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.preview_template_request import PreviewTemplateRequest
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
    api_instance = clerk_backend_sdk.EmailSMSTemplatesApi(api_client)
    template_type = 'template_type_example' # str | The type of template to preview
    slug = 'slug_example' # str | The slug of the template to preview
    preview_template_request = clerk_backend_sdk.PreviewTemplateRequest() # PreviewTemplateRequest | Required parameters (optional)

    try:
        # Preview changes to a template
        api_response = await api_instance.preview_template(template_type, slug, preview_template_request=preview_template_request)
        print("The response of EmailSMSTemplatesApi->preview_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSMSTemplatesApi->preview_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_type** | **str**| The type of template to preview | 
 **slug** | **str**| The slug of the template to preview | 
 **preview_template_request** | [**PreviewTemplateRequest**](PreviewTemplateRequest.md)| Required parameters | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Request was not successful |  -  |
**401** | Authentication invalid |  -  |
**404** | Resource not found |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revert_template**
> Template revert_template(template_type, slug)

Revert a template

Reverts an updated template to its default state

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.template import Template
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
    api_instance = clerk_backend_sdk.EmailSMSTemplatesApi(api_client)
    template_type = 'template_type_example' # str | The type of template to revert
    slug = 'slug_example' # str | The slug of the template to revert

    try:
        # Revert a template
        api_response = await api_instance.revert_template(template_type, slug)
        print("The response of EmailSMSTemplatesApi->revert_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSMSTemplatesApi->revert_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_type** | **str**| The type of template to revert | 
 **slug** | **str**| The slug of the template to revert | 

### Return type

[**Template**](Template.md)

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
**401** | Authentication invalid |  -  |
**402** | Payment required |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_template_delivery**
> Template toggle_template_delivery(template_type, slug, toggle_template_delivery_request=toggle_template_delivery_request)

Toggle the delivery by Clerk for a template of a given type and slug

Toggles the delivery by Clerk for a template of a given type and slug. If disabled, Clerk will not deliver the resulting email or SMS. The app developer will need to listen to the `email.created` or `sms.created` webhooks in order to handle delivery themselves.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.template import Template
from clerk_backend_sdk.models.toggle_template_delivery_request import ToggleTemplateDeliveryRequest
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
    api_instance = clerk_backend_sdk.EmailSMSTemplatesApi(api_client)
    template_type = 'template_type_example' # str | The type of template to toggle delivery for
    slug = 'slug_example' # str | The slug of the template for which to toggle delivery
    toggle_template_delivery_request = clerk_backend_sdk.ToggleTemplateDeliveryRequest() # ToggleTemplateDeliveryRequest |  (optional)

    try:
        # Toggle the delivery by Clerk for a template of a given type and slug
        api_response = await api_instance.toggle_template_delivery(template_type, slug, toggle_template_delivery_request=toggle_template_delivery_request)
        print("The response of EmailSMSTemplatesApi->toggle_template_delivery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSMSTemplatesApi->toggle_template_delivery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_type** | **str**| The type of template to toggle delivery for | 
 **slug** | **str**| The slug of the template for which to toggle delivery | 
 **toggle_template_delivery_request** | [**ToggleTemplateDeliveryRequest**](ToggleTemplateDeliveryRequest.md)|  | [optional] 

### Return type

[**Template**](Template.md)

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
**401** | Authentication invalid |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_template**
> Template upsert_template(template_type, slug, upsert_template_request=upsert_template_request)

Update a template for a given type and slug

Updates the existing template of the given type and slug

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.template import Template
from clerk_backend_sdk.models.upsert_template_request import UpsertTemplateRequest
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
    api_instance = clerk_backend_sdk.EmailSMSTemplatesApi(api_client)
    template_type = 'template_type_example' # str | The type of template to update
    slug = 'slug_example' # str | The slug of the template to update
    upsert_template_request = clerk_backend_sdk.UpsertTemplateRequest() # UpsertTemplateRequest |  (optional)

    try:
        # Update a template for a given type and slug
        api_response = await api_instance.upsert_template(template_type, slug, upsert_template_request=upsert_template_request)
        print("The response of EmailSMSTemplatesApi->upsert_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSMSTemplatesApi->upsert_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_type** | **str**| The type of template to update | 
 **slug** | **str**| The slug of the template to update | 
 **upsert_template_request** | [**UpsertTemplateRequest**](UpsertTemplateRequest.md)|  | [optional] 

### Return type

[**Template**](Template.md)

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
**401** | Authentication invalid |  -  |
**402** | Payment required |  -  |
**403** | Request was not successful |  -  |
**404** | Resource not found |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

