# CNameTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | 
**value** | **str** |  | 
**required** | **bool** | Denotes whether this CNAME target is required to be set in order for the domain to be considered deployed.  | 

## Example

```python
from clerk_backend_sdk.models.c_name_target import CNameTarget

# TODO update the JSON string below
json = "{}"
# create an instance of CNameTarget from a JSON string
c_name_target_instance = CNameTarget.from_json(json)
# print the JSON string representation of the object
print(CNameTarget.to_json())

# convert the object into a dict
c_name_target_dict = c_name_target_instance.to_dict()
# create an instance of CNameTarget from a dict
c_name_target_from_dict = CNameTarget.from_dict(c_name_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


