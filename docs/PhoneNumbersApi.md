# clerk_backend_sdk.PhoneNumbersApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_phone_number**](PhoneNumbersApi.md#create_phone_number) | **POST** /phone_numbers | Create a phone number
[**delete_phone_number**](PhoneNumbersApi.md#delete_phone_number) | **DELETE** /phone_numbers/{phone_number_id} | Delete a phone number
[**get_phone_number**](PhoneNumbersApi.md#get_phone_number) | **GET** /phone_numbers/{phone_number_id} | Retrieve a phone number
[**update_phone_number**](PhoneNumbersApi.md#update_phone_number) | **PATCH** /phone_numbers/{phone_number_id} | Update a phone number


# **create_phone_number**
> PhoneNumber create_phone_number(create_phone_number_request=create_phone_number_request)

Create a phone number

Create a new phone number

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.create_phone_number_request import CreatePhoneNumberRequest
from clerk_backend_sdk.models.phone_number import PhoneNumber
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
    api_instance = clerk_backend_sdk.PhoneNumbersApi(api_client)
    create_phone_number_request = clerk_backend_sdk.CreatePhoneNumberRequest() # CreatePhoneNumberRequest |  (optional)

    try:
        # Create a phone number
        api_response = await api_instance.create_phone_number(create_phone_number_request=create_phone_number_request)
        print("The response of PhoneNumbersApi->create_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->create_phone_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_phone_number_request** | [**CreatePhoneNumberRequest**](CreatePhoneNumberRequest.md)|  | [optional] 

### Return type

[**PhoneNumber**](PhoneNumber.md)

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

# **delete_phone_number**
> DeletedObject delete_phone_number(phone_number_id)

Delete a phone number

Delete the phone number with the given ID

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
    api_instance = clerk_backend_sdk.PhoneNumbersApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | The ID of the phone number to delete

    try:
        # Delete a phone number
        api_response = await api_instance.delete_phone_number(phone_number_id)
        print("The response of PhoneNumbersApi->delete_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->delete_phone_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**| The ID of the phone number to delete | 

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

# **get_phone_number**
> PhoneNumber get_phone_number(phone_number_id)

Retrieve a phone number

Returns the details of a phone number

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.phone_number import PhoneNumber
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
    api_instance = clerk_backend_sdk.PhoneNumbersApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | The ID of the phone number to retrieve

    try:
        # Retrieve a phone number
        api_response = await api_instance.get_phone_number(phone_number_id)
        print("The response of PhoneNumbersApi->get_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->get_phone_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**| The ID of the phone number to retrieve | 

### Return type

[**PhoneNumber**](PhoneNumber.md)

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

# **update_phone_number**
> PhoneNumber update_phone_number(phone_number_id, update_phone_number_request=update_phone_number_request)

Update a phone number

Updates a phone number

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.phone_number import PhoneNumber
from clerk_backend_sdk.models.update_phone_number_request import UpdatePhoneNumberRequest
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
    api_instance = clerk_backend_sdk.PhoneNumbersApi(api_client)
    phone_number_id = 'phone_number_id_example' # str | The ID of the phone number to update
    update_phone_number_request = clerk_backend_sdk.UpdatePhoneNumberRequest() # UpdatePhoneNumberRequest |  (optional)

    try:
        # Update a phone number
        api_response = await api_instance.update_phone_number(phone_number_id, update_phone_number_request=update_phone_number_request)
        print("The response of PhoneNumbersApi->update_phone_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhoneNumbersApi->update_phone_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number_id** | **str**| The ID of the phone number to update | 
 **update_phone_number_request** | [**UpdatePhoneNumberRequest**](UpdatePhoneNumberRequest.md)|  | [optional] 

### Return type

[**PhoneNumber**](PhoneNumber.md)

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

