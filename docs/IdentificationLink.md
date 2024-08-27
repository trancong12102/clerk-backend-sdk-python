# IdentificationLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from clerk_backend_sdk.models.identification_link import IdentificationLink

# TODO update the JSON string below
json = "{}"
# create an instance of IdentificationLink from a JSON string
identification_link_instance = IdentificationLink.from_json(json)
# print the JSON string representation of the object
print(IdentificationLink.to_json())

# convert the object into a dict
identification_link_dict = identification_link_instance.to_dict()
# create an instance of IdentificationLink from a dict
identification_link_from_dict = IdentificationLink.from_dict(identification_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


