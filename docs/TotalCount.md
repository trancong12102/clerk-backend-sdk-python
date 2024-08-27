# TotalCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | String representing the object&#39;s type. Objects of the same type share the same value.  | 
**total_count** | **int** |  | 

## Example

```python
from clerk_backend_sdk.models.total_count import TotalCount

# TODO update the JSON string below
json = "{}"
# create an instance of TotalCount from a JSON string
total_count_instance = TotalCount.from_json(json)
# print the JSON string representation of the object
print(TotalCount.to_json())

# convert the object into a dict
total_count_dict = total_count_instance.to_dict()
# create an instance of TotalCount from a dict
total_count_from_dict = TotalCount.from_dict(total_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


