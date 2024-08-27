# AddDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new domain name. Can contain the port for development instances. | 
**is_satellite** | **bool** | Marks the new domain as satellite. Only &#x60;true&#x60; is accepted at the moment. | 
**proxy_url** | **str** | The full URL of the proxy which will forward requests to the Clerk Frontend API for this domain. Applicable only to production instances. | [optional] 

## Example

```python
from clerk_backend_sdk.models.add_domain_request import AddDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDomainRequest from a JSON string
add_domain_request_instance = AddDomainRequest.from_json(json)
# print the JSON string representation of the object
print(AddDomainRequest.to_json())

# convert the object into a dict
add_domain_request_dict = add_domain_request_instance.to_dict()
# create an instance of AddDomainRequest from a dict
add_domain_request_from_dict = AddDomainRequest.from_dict(add_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


