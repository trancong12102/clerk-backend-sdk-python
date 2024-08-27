# Domain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**is_satellite** | **bool** |  | 
**frontend_api_url** | **str** |  | 
**accounts_portal_url** | **str** | Null for satellite domains.  | [optional] 
**proxy_url** | **str** |  | [optional] 
**development_origin** | **str** |  | 
**cname_targets** | [**List[CNameTarget]**](CNameTarget.md) |  | [optional] 

## Example

```python
from clerk_backend_sdk.models.domain import Domain

# TODO update the JSON string below
json = "{}"
# create an instance of Domain from a JSON string
domain_instance = Domain.from_json(json)
# print the JSON string representation of the object
print(Domain.to_json())

# convert the object into a dict
domain_dict = domain_instance.to_dict()
# create an instance of Domain from a dict
domain_from_dict = Domain.from_dict(domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


