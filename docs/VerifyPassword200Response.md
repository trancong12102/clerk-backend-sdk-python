# VerifyPassword200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verified** | **bool** |  | [optional] 

## Example

```python
from clerk_backend_sdk.models.verify_password200_response import VerifyPassword200Response

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyPassword200Response from a JSON string
verify_password200_response_instance = VerifyPassword200Response.from_json(json)
# print the JSON string representation of the object
print(VerifyPassword200Response.to_json())

# convert the object into a dict
verify_password200_response_dict = verify_password200_response_instance.to_dict()
# create an instance of VerifyPassword200Response from a dict
verify_password200_response_from_dict = VerifyPassword200Response.from_dict(verify_password200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


