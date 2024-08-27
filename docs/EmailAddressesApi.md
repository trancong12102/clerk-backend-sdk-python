# clerk_backend_sdk.EmailAddressesApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_email_address**](EmailAddressesApi.md#create_email_address) | **POST** /email_addresses | Create an email address
[**delete_email_address**](EmailAddressesApi.md#delete_email_address) | **DELETE** /email_addresses/{email_address_id} | Delete an email address
[**get_email_address**](EmailAddressesApi.md#get_email_address) | **GET** /email_addresses/{email_address_id} | Retrieve an email address
[**update_email_address**](EmailAddressesApi.md#update_email_address) | **PATCH** /email_addresses/{email_address_id} | Update an email address


# **create_email_address**
> EmailAddress create_email_address(create_email_address_request=create_email_address_request)

Create an email address

Create a new email address

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.create_email_address_request import CreateEmailAddressRequest
from clerk_backend_sdk.models.email_address import EmailAddress
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
    api_instance = clerk_backend_sdk.EmailAddressesApi(api_client)
    create_email_address_request = clerk_backend_sdk.CreateEmailAddressRequest() # CreateEmailAddressRequest |  (optional)

    try:
        # Create an email address
        api_response = await api_instance.create_email_address(create_email_address_request=create_email_address_request)
        print("The response of EmailAddressesApi->create_email_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAddressesApi->create_email_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_email_address_request** | [**CreateEmailAddressRequest**](CreateEmailAddressRequest.md)|  | [optional] 

### Return type

[**EmailAddress**](EmailAddress.md)

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
**403** | Authorization invalid |  -  |
**404** | Resource not found |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_address**
> DeletedObject delete_email_address(email_address_id)

Delete an email address

Delete the email address with the given ID

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
    api_instance = clerk_backend_sdk.EmailAddressesApi(api_client)
    email_address_id = 'email_address_id_example' # str | The ID of the email address to delete

    try:
        # Delete an email address
        api_response = await api_instance.delete_email_address(email_address_id)
        print("The response of EmailAddressesApi->delete_email_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAddressesApi->delete_email_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address_id** | **str**| The ID of the email address to delete | 

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
**400** | Request was not successful |  -  |
**401** | Authentication invalid |  -  |
**403** | Authorization invalid |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_address**
> EmailAddress get_email_address(email_address_id)

Retrieve an email address

Returns the details of an email address.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.email_address import EmailAddress
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
    api_instance = clerk_backend_sdk.EmailAddressesApi(api_client)
    email_address_id = 'email_address_id_example' # str | The ID of the email address to retrieve

    try:
        # Retrieve an email address
        api_response = await api_instance.get_email_address(email_address_id)
        print("The response of EmailAddressesApi->get_email_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAddressesApi->get_email_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address_id** | **str**| The ID of the email address to retrieve | 

### Return type

[**EmailAddress**](EmailAddress.md)

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
**403** | Authorization invalid |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_address**
> EmailAddress update_email_address(email_address_id, update_email_address_request=update_email_address_request)

Update an email address

Updates an email address.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.email_address import EmailAddress
from clerk_backend_sdk.models.update_email_address_request import UpdateEmailAddressRequest
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
    api_instance = clerk_backend_sdk.EmailAddressesApi(api_client)
    email_address_id = 'email_address_id_example' # str | The ID of the email address to update
    update_email_address_request = clerk_backend_sdk.UpdateEmailAddressRequest() # UpdateEmailAddressRequest |  (optional)

    try:
        # Update an email address
        api_response = await api_instance.update_email_address(email_address_id, update_email_address_request=update_email_address_request)
        print("The response of EmailAddressesApi->update_email_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailAddressesApi->update_email_address: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address_id** | **str**| The ID of the email address to update | 
 **update_email_address_request** | [**UpdateEmailAddressRequest**](UpdateEmailAddressRequest.md)|  | [optional] 

### Return type

[**EmailAddress**](EmailAddress.md)

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
**403** | Authorization invalid |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

