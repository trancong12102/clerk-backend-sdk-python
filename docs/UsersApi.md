# clerk_backend_sdk.UsersApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ban_user**](UsersApi.md#ban_user) | **POST** /users/{user_id}/ban | Ban a user
[**create_user**](UsersApi.md#create_user) | **POST** /users | Create a new user
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /users/{user_id} | Delete a user
[**delete_user_profile_image**](UsersApi.md#delete_user_profile_image) | **DELETE** /users/{user_id}/profile_image | Delete user profile image
[**disable_mfa**](UsersApi.md#disable_mfa) | **DELETE** /users/{user_id}/mfa | Disable a user&#39;s MFA methods
[**get_o_auth_access_token**](UsersApi.md#get_o_auth_access_token) | **GET** /users/{user_id}/oauth_access_tokens/{provider} | Retrieve the OAuth access token of a user
[**get_user**](UsersApi.md#get_user) | **GET** /users/{user_id} | Retrieve a user
[**get_user_list**](UsersApi.md#get_user_list) | **GET** /users | List all users
[**get_users_count**](UsersApi.md#get_users_count) | **GET** /users/count | Count users
[**lock_user**](UsersApi.md#lock_user) | **POST** /users/{user_id}/lock | Lock a user
[**set_user_profile_image**](UsersApi.md#set_user_profile_image) | **POST** /users/{user_id}/profile_image | Set user profile image
[**unban_user**](UsersApi.md#unban_user) | **POST** /users/{user_id}/unban | Unban a user
[**unlock_user**](UsersApi.md#unlock_user) | **POST** /users/{user_id}/unlock | Unlock a user
[**update_user**](UsersApi.md#update_user) | **PATCH** /users/{user_id} | Update a user
[**update_user_metadata**](UsersApi.md#update_user_metadata) | **PATCH** /users/{user_id}/metadata | Merge and update a user&#39;s metadata
[**users_get_organization_memberships**](UsersApi.md#users_get_organization_memberships) | **GET** /users/{user_id}/organization_memberships | Retrieve all memberships for a user
[**verify_password**](UsersApi.md#verify_password) | **POST** /users/{user_id}/verify_password | Verify the password of a user
[**verify_totp**](UsersApi.md#verify_totp) | **POST** /users/{user_id}/verify_totp | Verify a TOTP or backup code for a user


# **ban_user**
> User ban_user(user_id)

Ban a user

Marks the given user as banned, which means that all their sessions are revoked and they are not allowed to sign in again.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.user import User
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
    api_instance = clerk_backend_sdk.UsersApi(api_client)
    user_id = 'user_id_example' # str | The ID of the user to ban

    try:
        # Ban a user
        api_response = await api_instance.ban_user(user_id)
        print("The response of UsersApi->ban_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->ban_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user to ban | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**402** | Payment required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> User create_user(create_user_request)

Create a new user

Creates a new user. Your user management settings determine how you should setup your user model.  Any email address and phone number created using this method will be marked as verified.  Note: If you are performing a migration, check out our guide on [zero downtime migrations](https://clerk.com/docs/deployments/migrate-overview).  A rate limit rule of 20 requests per 10 seconds is applied to this endpoint.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.create_user_request import CreateUserRequest
from clerk_backend_sdk.models.user import User
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
    api_instance = clerk_backend_sdk.UsersApi(api_client)
    create_user_request = clerk_backend_sdk.CreateUserRequest() # CreateUserRequest | 

    try:
        # Create a new user
        api_response = await api_instance.create_user(create_user_request)
        print("The response of UsersApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_request** | [**CreateUserRequest**](CreateUserRequest.md)|  | 

### Return type

[**User**](User.md)

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
**403** | Authentication invalid |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> DeletedObject delete_user(user_id)

Delete a user

Delete the specified user

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
    api_instance = clerk_backend_sdk.UsersApi(api_client)
    user_id = 'user_id_example' # str | The ID of the user to delete

    try:
        # Delete a user
        api_response = await api_instance.delete_user(user_id)
        print("The response of UsersApi->delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user to delete | 

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
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_profile_image**
> User delete_user_profile_image(user_id)

Delete user profile image

Delete a user's profile image

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.user import User
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
    api_instance = clerk_backend_sdk.UsersApi(api_client)
    user_id = 'user_id_example' # str | The ID of the user to delete the profile image for

    try:
        # Delete user profile image
        api_response = await api_instance.delete_user_profile_image(user_id)
        print("The response of UsersApi->delete_user_profile_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->delete_user_profile_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user to delete the profile image for | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Request was not successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_mfa**
> DisableMFA200Response disable_mfa(user_id)

Disable a user's MFA methods

Disable all of a user's MFA methods (e.g. OTP sent via SMS, TOTP on their authenticator app) at once.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.disable_mfa200_response import DisableMFA200Response
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
    api_instance = clerk_backend_sdk.UsersApi(api_client)
    user_id = 'user_id_example' # str | The ID of the user whose MFA methods are to be disabled

    try:
        # Disable a user's MFA methods
        api_response = await api_instance.disable_mfa(user_id)
        print("The response of UsersApi->disable_mfa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->disable_mfa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user whose MFA methods are to be disabled | 

### Return type

[**DisableMFA200Response**](DisableMFA200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**404** | Resource not found |  -  |
**500** | Request was not successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_o_auth_access_token**
> List[GetOAuthAccessToken200ResponseInner] get_o_auth_access_token(user_id, provider)

Retrieve the OAuth access token of a user

Fetch the corresponding OAuth access token for a user that has previously authenticated with a particular OAuth provider. For OAuth 2.0, if the access token has expired and we have a corresponding refresh token, the access token will be refreshed transparently the new one will be returned.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.get_o_auth_access_token200_response_inner import GetOAuthAccessToken200ResponseInner
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
    api_instance = clerk_backend_sdk.UsersApi(api_client)
    user_id = 'user_id_example' # str | The ID of the user for which to retrieve the OAuth access token
    provider = 'provider_example' # str | The ID of the OAuth provider (e.g. `oauth_google`)

    try:
        # Retrieve the OAuth access token of a user
        api_response = await api_instance.get_o_auth_access_token(user_id, provider)
        print("The response of UsersApi->get_o_auth_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_o_auth_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user for which to retrieve the OAuth access token | 
 **provider** | **str**| The ID of the OAuth provider (e.g. &#x60;oauth_google&#x60;) | 

### Return type

[**List[GetOAuthAccessToken200ResponseInner]**](GetOAuthAccessToken200ResponseInner.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The OAuth access token of the user, if any. |  -  |
**400** | Request was not successful |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(user_id)

Retrieve a user

Retrieve the details of a user

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.user import User
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
    api_instance = clerk_backend_sdk.UsersApi(api_client)
    user_id = 'user_id_example' # str | The ID of the user to retrieve

    try:
        # Retrieve a user
        api_response = await api_instance.get_user(user_id)
        print("The response of UsersApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user to retrieve | 

### Return type

[**User**](User.md)

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

# **get_user_list**
> List[User] get_user_list(email_address=email_address, phone_number=phone_number, external_id=external_id, username=username, web3_wallet=web3_wallet, user_id=user_id, organization_id=organization_id, query=query, last_active_at_since=last_active_at_since, limit=limit, offset=offset, order_by=order_by)

List all users

Returns a list of all users. The users are returned sorted by creation date, with the newest users appearing first.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.user import User
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
    api_instance = clerk_backend_sdk.UsersApi(api_client)
    email_address = ['email_address_example'] # List[str] | Returns users with the specified email addresses. Accepts up to 100 email addresses. Any email addresses not found are ignored. (optional)
    phone_number = ['phone_number_example'] # List[str] | Returns users with the specified phone numbers. Accepts up to 100 phone numbers. Any phone numbers not found are ignored. (optional)
    external_id = ['external_id_example'] # List[str] | Returns users with the specified external ids. For each external id, the `+` and `-` can be prepended to the id, which denote whether the respective external id should be included or excluded from the result set. Accepts up to 100 external ids. Any external ids not found are ignored. (optional)
    username = ['username_example'] # List[str] | Returns users with the specified usernames. Accepts up to 100 usernames. Any usernames not found are ignored. (optional)
    web3_wallet = ['web3_wallet_example'] # List[str] | Returns users with the specified web3 wallet addresses. Accepts up to 100 web3 wallet addresses. Any web3 wallet addressed not found are ignored. (optional)
    user_id = ['user_id_example'] # List[str] | Returns users with the user ids specified. For each user id, the `+` and `-` can be prepended to the id, which denote whether the respective user id should be included or excluded from the result set. Accepts up to 100 user ids. Any user ids not found are ignored. (optional)
    organization_id = ['organization_id_example'] # List[str] | Returns users that have memberships to the given organizations. For each organization id, the `+` and `-` can be prepended to the id, which denote whether the respective organization should be included or excluded from the result set. Accepts up to 100 organization ids. (optional)
    query = 'query_example' # str | Returns users that match the given query. For possible matches, we check the email addresses, phone numbers, usernames, web3 wallets, user ids, first and last names. The query value doesn't need to match the exact value you are looking for, it is capable of partial matches as well. (optional)
    last_active_at_since = 1700690400000 # int | Returns users that had session activity since the given date, with day precision. Providing a value with higher precision than day will result in an error. Example: use 1700690400000 to retrieve users that had session activity from 2023-11-23 until the current day. (optional)
    limit = 10 # float | Applies a limit to the number of results returned. Can be used for paginating the results together with `offset`. (optional) (default to 10)
    offset = 0 # float | Skip the first `offset` results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with `limit`. (optional) (default to 0)
    order_by = '-created_at' # str | Allows to return users in a particular order. At the moment, you can order the returned users by their `created_at`,`updated_at`,`email_address`,`web3wallet`,`first_name`,`last_name`,`phone_number`,`username`,`last_active_at`,`last_sign_in_at`. In order to specify the direction, you can use the `+/-` symbols prepended in the property to order by. For example, if you want users to be returned in descending order according to their `created_at` property, you can use `-created_at`. If you don't use `+` or `-`, then `+` is implied. We only support one `order_by` parameter, and if multiple `order_by` parameters are provided, we will only keep the first one. For example, if you pass `order_by=username&order_by=created_at`, we will consider only the first `order_by` parameter, which is `username`. The `created_at` parameter will be ignored in this case. (optional) (default to '-created_at')

    try:
        # List all users
        api_response = await api_instance.get_user_list(email_address=email_address, phone_number=phone_number, external_id=external_id, username=username, web3_wallet=web3_wallet, user_id=user_id, organization_id=organization_id, query=query, last_active_at_since=last_active_at_since, limit=limit, offset=offset, order_by=order_by)
        print("The response of UsersApi->get_user_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address** | [**List[str]**](str.md)| Returns users with the specified email addresses. Accepts up to 100 email addresses. Any email addresses not found are ignored. | [optional] 
 **phone_number** | [**List[str]**](str.md)| Returns users with the specified phone numbers. Accepts up to 100 phone numbers. Any phone numbers not found are ignored. | [optional] 
 **external_id** | [**List[str]**](str.md)| Returns users with the specified external ids. For each external id, the &#x60;+&#x60; and &#x60;-&#x60; can be prepended to the id, which denote whether the respective external id should be included or excluded from the result set. Accepts up to 100 external ids. Any external ids not found are ignored. | [optional] 
 **username** | [**List[str]**](str.md)| Returns users with the specified usernames. Accepts up to 100 usernames. Any usernames not found are ignored. | [optional] 
 **web3_wallet** | [**List[str]**](str.md)| Returns users with the specified web3 wallet addresses. Accepts up to 100 web3 wallet addresses. Any web3 wallet addressed not found are ignored. | [optional] 
 **user_id** | [**List[str]**](str.md)| Returns users with the user ids specified. For each user id, the &#x60;+&#x60; and &#x60;-&#x60; can be prepended to the id, which denote whether the respective user id should be included or excluded from the result set. Accepts up to 100 user ids. Any user ids not found are ignored. | [optional] 
 **organization_id** | [**List[str]**](str.md)| Returns users that have memberships to the given organizations. For each organization id, the &#x60;+&#x60; and &#x60;-&#x60; can be prepended to the id, which denote whether the respective organization should be included or excluded from the result set. Accepts up to 100 organization ids. | [optional] 
 **query** | **str**| Returns users that match the given query. For possible matches, we check the email addresses, phone numbers, usernames, web3 wallets, user ids, first and last names. The query value doesn&#39;t need to match the exact value you are looking for, it is capable of partial matches as well. | [optional] 
 **last_active_at_since** | **int**| Returns users that had session activity since the given date, with day precision. Providing a value with higher precision than day will result in an error. Example: use 1700690400000 to retrieve users that had session activity from 2023-11-23 until the current day. | [optional] 
 **limit** | **float**| Applies a limit to the number of results returned. Can be used for paginating the results together with &#x60;offset&#x60;. | [optional] [default to 10]
 **offset** | **float**| Skip the first &#x60;offset&#x60; results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with &#x60;limit&#x60;. | [optional] [default to 0]
 **order_by** | **str**| Allows to return users in a particular order. At the moment, you can order the returned users by their &#x60;created_at&#x60;,&#x60;updated_at&#x60;,&#x60;email_address&#x60;,&#x60;web3wallet&#x60;,&#x60;first_name&#x60;,&#x60;last_name&#x60;,&#x60;phone_number&#x60;,&#x60;username&#x60;,&#x60;last_active_at&#x60;,&#x60;last_sign_in_at&#x60;. In order to specify the direction, you can use the &#x60;+/-&#x60; symbols prepended in the property to order by. For example, if you want users to be returned in descending order according to their &#x60;created_at&#x60; property, you can use &#x60;-created_at&#x60;. If you don&#39;t use &#x60;+&#x60; or &#x60;-&#x60;, then &#x60;+&#x60; is implied. We only support one &#x60;order_by&#x60; parameter, and if multiple &#x60;order_by&#x60; parameters are provided, we will only keep the first one. For example, if you pass &#x60;order_by&#x3D;username&amp;order_by&#x3D;created_at&#x60;, we will consider only the first &#x60;order_by&#x60; parameter, which is &#x60;username&#x60;. The &#x60;created_at&#x60; parameter will be ignored in this case. | [optional] [default to &#39;-created_at&#39;]

### Return type

[**List[User]**](User.md)

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

# **get_users_count**
> TotalCount get_users_count(email_address=email_address, phone_number=phone_number, external_id=external_id, username=username, web3_wallet=web3_wallet, user_id=user_id, query=query)

Count users

Returns a total count of all users that match the given filtering criteria.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.total_count import TotalCount
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
    api_instance = clerk_backend_sdk.UsersApi(api_client)
    email_address = ['email_address_example'] # List[str] | Counts users with the specified email addresses. Accepts up to 100 email addresses. Any email addresses not found are ignored. (optional)
    phone_number = ['phone_number_example'] # List[str] | Counts users with the specified phone numbers. Accepts up to 100 phone numbers. Any phone numbers not found are ignored. (optional)
    external_id = ['external_id_example'] # List[str] | Counts users with the specified external ids. Accepts up to 100 external ids. Any external ids not found are ignored. (optional)
    username = ['username_example'] # List[str] | Counts users with the specified usernames. Accepts up to 100 usernames. Any usernames not found are ignored. (optional)
    web3_wallet = ['web3_wallet_example'] # List[str] | Counts users with the specified web3 wallet addresses. Accepts up to 100 web3 wallet addresses. Any web3 wallet addressed not found are ignored. (optional)
    user_id = ['user_id_example'] # List[str] | Counts users with the user ids specified. Accepts up to 100 user ids. Any user ids not found are ignored. (optional)
    query = 'query_example' # str | Counts users that match the given query. For possible matches, we check the email addresses, phone numbers, usernames, web3 wallets, user ids, first and last names. The query value doesn't need to match the exact value you are looking for, it is capable of partial matches as well. (optional)

    try:
        # Count users
        api_response = await api_instance.get_users_count(email_address=email_address, phone_number=phone_number, external_id=external_id, username=username, web3_wallet=web3_wallet, user_id=user_id, query=query)
        print("The response of UsersApi->get_users_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_users_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address** | [**List[str]**](str.md)| Counts users with the specified email addresses. Accepts up to 100 email addresses. Any email addresses not found are ignored. | [optional] 
 **phone_number** | [**List[str]**](str.md)| Counts users with the specified phone numbers. Accepts up to 100 phone numbers. Any phone numbers not found are ignored. | [optional] 
 **external_id** | [**List[str]**](str.md)| Counts users with the specified external ids. Accepts up to 100 external ids. Any external ids not found are ignored. | [optional] 
 **username** | [**List[str]**](str.md)| Counts users with the specified usernames. Accepts up to 100 usernames. Any usernames not found are ignored. | [optional] 
 **web3_wallet** | [**List[str]**](str.md)| Counts users with the specified web3 wallet addresses. Accepts up to 100 web3 wallet addresses. Any web3 wallet addressed not found are ignored. | [optional] 
 **user_id** | [**List[str]**](str.md)| Counts users with the user ids specified. Accepts up to 100 user ids. Any user ids not found are ignored. | [optional] 
 **query** | **str**| Counts users that match the given query. For possible matches, we check the email addresses, phone numbers, usernames, web3 wallets, user ids, first and last names. The query value doesn&#39;t need to match the exact value you are looking for, it is capable of partial matches as well. | [optional] 

### Return type

[**TotalCount**](TotalCount.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lock_user**
> User lock_user(user_id)

Lock a user

Marks the given user as locked, which means they are not allowed to sign in again until the lock expires. Lock duration can be configured in the instance's restrictions settings.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.user import User
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
    api_instance = clerk_backend_sdk.UsersApi(api_client)
    user_id = 'user_id_example' # str | The ID of the user to lock

    try:
        # Lock a user
        api_response = await api_instance.lock_user(user_id)
        print("The response of UsersApi->lock_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->lock_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user to lock | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Authorization invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_profile_image**
> User set_user_profile_image(user_id, file=file)

Set user profile image

Update a user's profile image

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.user import User
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
    api_instance = clerk_backend_sdk.UsersApi(api_client)
    user_id = 'user_id_example' # str | The ID of the user to update the profile image for
    file = None # bytearray |  (optional)

    try:
        # Set user profile image
        api_response = await api_instance.set_user_profile_image(user_id, file=file)
        print("The response of UsersApi->set_user_profile_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->set_user_profile_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user to update the profile image for | 
 **file** | **bytearray**|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Request was not successful |  -  |
**401** | Request was not successful |  -  |
**404** | Request was not successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unban_user**
> User unban_user(user_id)

Unban a user

Removes the ban mark from the given user.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.user import User
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
    api_instance = clerk_backend_sdk.UsersApi(api_client)
    user_id = 'user_id_example' # str | The ID of the user to unban

    try:
        # Unban a user
        api_response = await api_instance.unban_user(user_id)
        print("The response of UsersApi->unban_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->unban_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user to unban | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**402** | Payment required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlock_user**
> User unlock_user(user_id)

Unlock a user

Removes the lock from the given user.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.user import User
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
    api_instance = clerk_backend_sdk.UsersApi(api_client)
    user_id = 'user_id_example' # str | The ID of the user to unlock

    try:
        # Unlock a user
        api_response = await api_instance.unlock_user(user_id)
        print("The response of UsersApi->unlock_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->unlock_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user to unlock | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Authorization invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> User update_user(user_id, update_user_request)

Update a user

Update a user's attributes.  You can set the user's primary contact identifiers (email address and phone numbers) by updating the `primary_email_address_id` and `primary_phone_number_id` attributes respectively. Both IDs should correspond to verified identifications that belong to the user.  You can remove a user's username by setting the username attribute to null or the blank string \"\". This is a destructive action; the identification will be deleted forever. Usernames can be removed only if they are optional in your instance settings and there's at least one other identifier which can be used for authentication.  This endpoint allows changing a user's password. When passing the `password` parameter directly you have two further options. You can ignore the password policy checks for your instance by setting the `skip_password_checks` parameter to `true`. You can also choose to sign the user out of all their active sessions on any device once the password is updated. Just set `sign_out_of_other_sessions` to `true`.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.update_user_request import UpdateUserRequest
from clerk_backend_sdk.models.user import User
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
    api_instance = clerk_backend_sdk.UsersApi(api_client)
    user_id = 'user_id_example' # str | The ID of the user to update
    update_user_request = clerk_backend_sdk.UpdateUserRequest() # UpdateUserRequest | 

    try:
        # Update a user
        api_response = await api_instance.update_user(user_id, update_user_request)
        print("The response of UsersApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user to update | 
 **update_user_request** | [**UpdateUserRequest**](UpdateUserRequest.md)|  | 

### Return type

[**User**](User.md)

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
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_metadata**
> User update_user_metadata(user_id, update_user_metadata_request=update_user_metadata_request)

Merge and update a user's metadata

Update a user's metadata attributes by merging existing values with the provided parameters.  This endpoint behaves differently than the *Update a user* endpoint. Metadata values will not be replaced entirely. Instead, a deep merge will be performed. Deep means that any nested JSON objects will be merged as well.  You can remove metadata keys at any level by setting their value to `null`.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.update_user_metadata_request import UpdateUserMetadataRequest
from clerk_backend_sdk.models.user import User
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
    api_instance = clerk_backend_sdk.UsersApi(api_client)
    user_id = 'user_id_example' # str | The ID of the user whose metadata will be updated and merged
    update_user_metadata_request = clerk_backend_sdk.UpdateUserMetadataRequest() # UpdateUserMetadataRequest |  (optional)

    try:
        # Merge and update a user's metadata
        api_response = await api_instance.update_user_metadata(user_id, update_user_metadata_request=update_user_metadata_request)
        print("The response of UsersApi->update_user_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user whose metadata will be updated and merged | 
 **update_user_metadata_request** | [**UpdateUserMetadataRequest**](UpdateUserMetadataRequest.md)|  | [optional] 

### Return type

[**User**](User.md)

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
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_organization_memberships**
> OrganizationMemberships users_get_organization_memberships(user_id, limit=limit, offset=offset)

Retrieve all memberships for a user

Retrieve a paginated list of the user's organization memberships

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.organization_memberships import OrganizationMemberships
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
    api_instance = clerk_backend_sdk.UsersApi(api_client)
    user_id = 'user_id_example' # str | The ID of the user whose organization memberships we want to retrieve
    limit = 10 # float | Applies a limit to the number of results returned. Can be used for paginating the results together with `offset`. (optional) (default to 10)
    offset = 0 # float | Skip the first `offset` results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with `limit`. (optional) (default to 0)

    try:
        # Retrieve all memberships for a user
        api_response = await api_instance.users_get_organization_memberships(user_id, limit=limit, offset=offset)
        print("The response of UsersApi->users_get_organization_memberships:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_get_organization_memberships: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user whose organization memberships we want to retrieve | 
 **limit** | **float**| Applies a limit to the number of results returned. Can be used for paginating the results together with &#x60;offset&#x60;. | [optional] [default to 10]
 **offset** | **float**| Skip the first &#x60;offset&#x60; results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with &#x60;limit&#x60;. | [optional] [default to 0]

### Return type

[**OrganizationMemberships**](OrganizationMemberships.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of organization memberships |  -  |
**403** | Request was not successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_password**
> VerifyPassword200Response verify_password(user_id, verify_password_request=verify_password_request)

Verify the password of a user

Check that the user's password matches the supplied input. Useful for custom auth flows and re-verification.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.verify_password200_response import VerifyPassword200Response
from clerk_backend_sdk.models.verify_password_request import VerifyPasswordRequest
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
    api_instance = clerk_backend_sdk.UsersApi(api_client)
    user_id = 'user_id_example' # str | The ID of the user for whom to verify the password
    verify_password_request = clerk_backend_sdk.VerifyPasswordRequest() # VerifyPasswordRequest |  (optional)

    try:
        # Verify the password of a user
        api_response = await api_instance.verify_password(user_id, verify_password_request=verify_password_request)
        print("The response of UsersApi->verify_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->verify_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user for whom to verify the password | 
 **verify_password_request** | [**VerifyPasswordRequest**](VerifyPasswordRequest.md)|  | [optional] 

### Return type

[**VerifyPassword200Response**](VerifyPassword200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The provided password was correct. |  -  |
**400** | The user does not have a password set. |  -  |
**404** | The user does not exist. |  -  |
**422** | The provided password was incorrect. |  -  |
**500** | Request was not successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_totp**
> VerifyTOTP200Response verify_totp(user_id, verify_totp_request=verify_totp_request)

Verify a TOTP or backup code for a user

Verify that the provided TOTP or backup code is valid for the user. Verifying a backup code will result it in being consumed (i.e. it will become invalid). Useful for custom auth flows and re-verification.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.verify_totp200_response import VerifyTOTP200Response
from clerk_backend_sdk.models.verify_totp_request import VerifyTOTPRequest
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
    api_instance = clerk_backend_sdk.UsersApi(api_client)
    user_id = 'user_id_example' # str | The ID of the user for whom to verify the TOTP
    verify_totp_request = clerk_backend_sdk.VerifyTOTPRequest() # VerifyTOTPRequest |  (optional)

    try:
        # Verify a TOTP or backup code for a user
        api_response = await api_instance.verify_totp(user_id, verify_totp_request=verify_totp_request)
        print("The response of UsersApi->verify_totp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->verify_totp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The ID of the user for whom to verify the TOTP | 
 **verify_totp_request** | [**VerifyTOTPRequest**](VerifyTOTPRequest.md)|  | [optional] 

### Return type

[**VerifyTOTP200Response**](VerifyTOTP200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The provided TOTP or backup code was correct. |  -  |
**400** | The user does not have TOTP configured for their account. |  -  |
**404** | The user does not exist. |  -  |
**422** | The provided TOTP or backup code was incorrect. |  -  |
**500** | Request was not successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

