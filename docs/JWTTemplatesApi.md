# clerk_backend_sdk.JWTTemplatesApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_jwt_template**](JWTTemplatesApi.md#create_jwt_template) | **POST** /jwt_templates | Create a JWT template
[**delete_jwt_template**](JWTTemplatesApi.md#delete_jwt_template) | **DELETE** /jwt_templates/{template_id} | Delete a Template
[**get_jwt_template**](JWTTemplatesApi.md#get_jwt_template) | **GET** /jwt_templates/{template_id} | Retrieve a template
[**list_jwt_templates**](JWTTemplatesApi.md#list_jwt_templates) | **GET** /jwt_templates | List all templates
[**update_jwt_template**](JWTTemplatesApi.md#update_jwt_template) | **PATCH** /jwt_templates/{template_id} | Update a JWT template


# **create_jwt_template**
> JWTTemplate create_jwt_template(create_jwt_template_request=create_jwt_template_request)

Create a JWT template

Create a new JWT template

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.create_jwt_template_request import CreateJWTTemplateRequest
from clerk_backend_sdk.models.jwt_template import JWTTemplate
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
    api_instance = clerk_backend_sdk.JWTTemplatesApi(api_client)
    create_jwt_template_request = clerk_backend_sdk.CreateJWTTemplateRequest() # CreateJWTTemplateRequest |  (optional)

    try:
        # Create a JWT template
        api_response = await api_instance.create_jwt_template(create_jwt_template_request=create_jwt_template_request)
        print("The response of JWTTemplatesApi->create_jwt_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JWTTemplatesApi->create_jwt_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_jwt_template_request** | [**CreateJWTTemplateRequest**](CreateJWTTemplateRequest.md)|  | [optional] 

### Return type

[**JWTTemplate**](JWTTemplate.md)

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

# **delete_jwt_template**
> DeletedObject delete_jwt_template(template_id)

Delete a Template



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
    api_instance = clerk_backend_sdk.JWTTemplatesApi(api_client)
    template_id = 'template_id_example' # str | JWT Template ID

    try:
        # Delete a Template
        api_response = await api_instance.delete_jwt_template(template_id)
        print("The response of JWTTemplatesApi->delete_jwt_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JWTTemplatesApi->delete_jwt_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| JWT Template ID | 

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
**403** | Authorization invalid |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jwt_template**
> JWTTemplate get_jwt_template(template_id)

Retrieve a template

Retrieve the details of a given JWT template

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.jwt_template import JWTTemplate
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
    api_instance = clerk_backend_sdk.JWTTemplatesApi(api_client)
    template_id = 'template_id_example' # str | JWT Template ID

    try:
        # Retrieve a template
        api_response = await api_instance.get_jwt_template(template_id)
        print("The response of JWTTemplatesApi->get_jwt_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JWTTemplatesApi->get_jwt_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| JWT Template ID | 

### Return type

[**JWTTemplate**](JWTTemplate.md)

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

# **list_jwt_templates**
> List[JWTTemplate] list_jwt_templates()

List all templates

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.jwt_template import JWTTemplate
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
    api_instance = clerk_backend_sdk.JWTTemplatesApi(api_client)

    try:
        # List all templates
        api_response = await api_instance.list_jwt_templates()
        print("The response of JWTTemplatesApi->list_jwt_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JWTTemplatesApi->list_jwt_templates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[JWTTemplate]**](JWTTemplate.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of JWT templates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_jwt_template**
> JWTTemplate update_jwt_template(template_id, create_jwt_template_request=create_jwt_template_request)

Update a JWT template

Updates an existing JWT template

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.create_jwt_template_request import CreateJWTTemplateRequest
from clerk_backend_sdk.models.jwt_template import JWTTemplate
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
    api_instance = clerk_backend_sdk.JWTTemplatesApi(api_client)
    template_id = 'template_id_example' # str | The ID of the JWT template to update
    create_jwt_template_request = clerk_backend_sdk.CreateJWTTemplateRequest() # CreateJWTTemplateRequest |  (optional)

    try:
        # Update a JWT template
        api_response = await api_instance.update_jwt_template(template_id, create_jwt_template_request=create_jwt_template_request)
        print("The response of JWTTemplatesApi->update_jwt_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JWTTemplatesApi->update_jwt_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The ID of the JWT template to update | 
 **create_jwt_template_request** | [**CreateJWTTemplateRequest**](CreateJWTTemplateRequest.md)|  | [optional] 

### Return type

[**JWTTemplate**](JWTTemplate.md)

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

