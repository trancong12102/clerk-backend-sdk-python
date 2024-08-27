# UpdateDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new domain name. For development instances, can contain the port, i.e &#x60;myhostname:3000&#x60;. For production instances, must be a valid FQDN, i.e &#x60;mysite.com&#x60;. Cannot contain protocol scheme. | [optional] 
**proxy_url** | **str** | The full URL of the proxy that will forward requests to Clerk&#39;s Frontend API. Can only be updated for production instances. | [optional] 
**is_secondary** | **bool** | Whether this is a domain for a secondary app, meaning that any subdomain provided is significant and will be stored as part of the domain. This is useful for supporting multiple apps (one primary and multiple secondaries) on the same root domain (eTLD+1). | [optional] 

## Example

```python
from clerk_backend_sdk.models.update_domain_request import UpdateDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDomainRequest from a JSON string
update_domain_request_instance = UpdateDomainRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDomainRequest.to_json())

# convert the object into a dict
update_domain_request_dict = update_domain_request_instance.to_dict()
# create an instance of UpdateDomainRequest from a dict
update_domain_request_from_dict = UpdateDomainRequest.from_dict(update_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


