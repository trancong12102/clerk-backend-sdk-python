# ClerkError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**long_message** | **str** |  | 
**code** | **str** |  | 
**meta** | **object** |  | [optional] 
**clerk_trace_id** | **str** |  | [optional] 

## Example

```python
from clerk_backend_sdk.models.clerk_error import ClerkError

# TODO update the JSON string below
json = "{}"
# create an instance of ClerkError from a JSON string
clerk_error_instance = ClerkError.from_json(json)
# print the JSON string representation of the object
print(ClerkError.to_json())

# convert the object into a dict
clerk_error_dict = clerk_error_instance.to_dict()
# create an instance of ClerkError from a dict
clerk_error_from_dict = ClerkError.from_dict(clerk_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


