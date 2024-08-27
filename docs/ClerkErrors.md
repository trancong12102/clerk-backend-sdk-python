# ClerkErrors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[ClerkError]**](ClerkError.md) |  | 
**meta** | **object** |  | [optional] 

## Example

```python
from clerk_backend_sdk.models.clerk_errors import ClerkErrors

# TODO update the JSON string below
json = "{}"
# create an instance of ClerkErrors from a JSON string
clerk_errors_instance = ClerkErrors.from_json(json)
# print the JSON string representation of the object
print(ClerkErrors.to_json())

# convert the object into a dict
clerk_errors_dict = clerk_errors_instance.to_dict()
# create an instance of ClerkErrors from a dict
clerk_errors_from_dict = ClerkErrors.from_dict(clerk_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


