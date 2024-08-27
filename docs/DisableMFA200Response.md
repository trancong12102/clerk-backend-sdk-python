# DisableMFA200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 

## Example

```python
from clerk_backend_sdk.models.disable_mfa200_response import DisableMFA200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DisableMFA200Response from a JSON string
disable_mfa200_response_instance = DisableMFA200Response.from_json(json)
# print the JSON string representation of the object
print(DisableMFA200Response.to_json())

# convert the object into a dict
disable_mfa200_response_dict = disable_mfa200_response_instance.to_dict()
# create an instance of DisableMFA200Response from a dict
disable_mfa200_response_from_dict = DisableMFA200Response.from_dict(disable_mfa200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


