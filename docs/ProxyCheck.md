# ProxyCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**id** | **str** |  | 
**domain_id** | **str** |  | 
**last_run_at** | **int** |  | 
**proxy_url** | **str** |  | 
**successful** | **bool** |  | 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 

## Example

```python
from clerk_backend_sdk.models.proxy_check import ProxyCheck

# TODO update the JSON string below
json = "{}"
# create an instance of ProxyCheck from a JSON string
proxy_check_instance = ProxyCheck.from_json(json)
# print the JSON string representation of the object
print(ProxyCheck.to_json())

# convert the object into a dict
proxy_check_dict = proxy_check_instance.to_dict()
# create an instance of ProxyCheck from a dict
proxy_check_from_dict = ProxyCheck.from_dict(proxy_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


