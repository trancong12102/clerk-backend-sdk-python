# DeletedObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**id** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**deleted** | **bool** |  | 

## Example

```python
from clerk_backend_sdk.models.deleted_object import DeletedObject

# TODO update the JSON string below
json = "{}"
# create an instance of DeletedObject from a JSON string
deleted_object_instance = DeletedObject.from_json(json)
# print the JSON string representation of the object
print(DeletedObject.to_json())

# convert the object into a dict
deleted_object_dict = deleted_object_instance.to_dict()
# create an instance of DeletedObject from a dict
deleted_object_from_dict = DeletedObject.from_dict(deleted_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


