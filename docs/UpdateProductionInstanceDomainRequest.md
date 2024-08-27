# UpdateProductionInstanceDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home_url** | **str** | The new home URL of the production instance e.g. https://www.example.com | [optional] 

## Example

```python
from clerk_backend_sdk.models.update_production_instance_domain_request import UpdateProductionInstanceDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProductionInstanceDomainRequest from a JSON string
update_production_instance_domain_request_instance = UpdateProductionInstanceDomainRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateProductionInstanceDomainRequest.to_json())

# convert the object into a dict
update_production_instance_domain_request_dict = update_production_instance_domain_request_instance.to_dict()
# create an instance of UpdateProductionInstanceDomainRequest from a dict
update_production_instance_domain_request_from_dict = UpdateProductionInstanceDomainRequest.from_dict(update_production_instance_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


