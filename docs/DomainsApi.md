# clerk_backend_sdk.DomainsApi

All URIs are relative to *https://api.clerk.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_domain**](DomainsApi.md#add_domain) | **POST** /domains | Add a domain
[**delete_domain**](DomainsApi.md#delete_domain) | **DELETE** /domains/{domain_id} | Delete a satellite domain
[**list_domains**](DomainsApi.md#list_domains) | **GET** /domains | List all instance domains
[**update_domain**](DomainsApi.md#update_domain) | **PATCH** /domains/{domain_id} | Update a domain


# **add_domain**
> Domain add_domain(add_domain_request=add_domain_request)

Add a domain

Add a new domain for your instance. Useful in the case of multi-domain instances, allows adding satellite domains to an instance. The new domain must have a `name`. The domain name can contain the port for development instances, like `localhost:3000`. At the moment, instances can have only one primary domain, so the `is_satellite` parameter must be set to `true`. If you're planning to configure the new satellite domain to run behind a proxy, pass the `proxy_url` parameter accordingly.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.add_domain_request import AddDomainRequest
from clerk_backend_sdk.models.domain import Domain
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
    api_instance = clerk_backend_sdk.DomainsApi(api_client)
    add_domain_request = clerk_backend_sdk.AddDomainRequest() # AddDomainRequest |  (optional)

    try:
        # Add a domain
        api_response = await api_instance.add_domain(add_domain_request=add_domain_request)
        print("The response of DomainsApi->add_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->add_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_domain_request** | [**AddDomainRequest**](AddDomainRequest.md)|  | [optional] 

### Return type

[**Domain**](Domain.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A domain |  -  |
**400** | Request was not successful |  -  |
**402** | Request was not successful |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_domain**
> DeletedObject delete_domain(domain_id)

Delete a satellite domain

Deletes a satellite domain for the instance. It is currently not possible to delete the instance's primary domain.

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
    api_instance = clerk_backend_sdk.DomainsApi(api_client)
    domain_id = 'domain_id_example' # str | The ID of the domain that will be deleted. Must be a satellite domain.

    try:
        # Delete a satellite domain
        api_response = await api_instance.delete_domain(domain_id)
        print("The response of DomainsApi->delete_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->delete_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| The ID of the domain that will be deleted. Must be a satellite domain. | 

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
**403** | Request was not successful |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_domains**
> Domains list_domains()

List all instance domains

Use this endpoint to get a list of all domains for an instance. The response will contain the primary domain for the instance and any satellite domains. Each domain in the response contains information about the URLs where Clerk operates and the required CNAME targets.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.domains import Domains
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
    api_instance = clerk_backend_sdk.DomainsApi(api_client)

    try:
        # List all instance domains
        api_response = await api_instance.list_domains()
        print("The response of DomainsApi->list_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->list_domains: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Domains**](Domains.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of domains |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_domain**
> Domain update_domain(domain_id, update_domain_request)

Update a domain

The `proxy_url` can be updated only for production instances. Update one of the instance's domains. Both primary and satellite domains can be updated. If you choose to use Clerk via proxy, use this endpoint to specify the `proxy_url`. Whenever you decide you'd rather switch to DNS setup for Clerk, simply set `proxy_url` to `null` for the domain. When you update a production instance's primary domain name, you have to make sure that you've completed all the necessary setup steps for DNS and emails to work. Expect downtime otherwise. Updating a primary domain's name will also update the instance's home origin, affecting the default application paths.

### Example

* Bearer (sk_<environment>_<secret value>) Authentication (bearerAuth):

```python
import clerk_backend_sdk
from clerk_backend_sdk.models.domain import Domain
from clerk_backend_sdk.models.update_domain_request import UpdateDomainRequest
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
    api_instance = clerk_backend_sdk.DomainsApi(api_client)
    domain_id = 'domain_id_example' # str | The ID of the domain that will be updated.
    update_domain_request = clerk_backend_sdk.UpdateDomainRequest() # UpdateDomainRequest | 

    try:
        # Update a domain
        api_response = await api_instance.update_domain(domain_id, update_domain_request)
        print("The response of DomainsApi->update_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->update_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| The ID of the domain that will be updated. | 
 **update_domain_request** | [**UpdateDomainRequest**](UpdateDomainRequest.md)|  | 

### Return type

[**Domain**](Domain.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A domain |  -  |
**400** | Request was not successful |  -  |
**404** | Resource not found |  -  |
**422** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

