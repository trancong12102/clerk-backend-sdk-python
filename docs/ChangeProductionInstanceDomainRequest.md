# ChangeProductionInstanceDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home_url** | **str** | The new home URL of the production instance e.g. https://www.example.com | [optional] 
**is_secondary** | **bool** | Whether this is a domain for a secondary app, meaning that any subdomain provided is significant and will be stored as part of the domain. This is useful for supporting multiple apps (one primary and multiple secondaries) on the same root domain (eTLD+1). | [optional] 

## Example

```python
from clerk_backend_sdk.models.change_production_instance_domain_request import ChangeProductionInstanceDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeProductionInstanceDomainRequest from a JSON string
change_production_instance_domain_request_instance = ChangeProductionInstanceDomainRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeProductionInstanceDomainRequest.to_json())

# convert the object into a dict
change_production_instance_domain_request_dict = change_production_instance_domain_request_instance.to_dict()
# create an instance of ChangeProductionInstanceDomainRequest from a dict
change_production_instance_domain_request_from_dict = ChangeProductionInstanceDomainRequest.from_dict(change_production_instance_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


