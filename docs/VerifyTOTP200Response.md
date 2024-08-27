# VerifyTOTP200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verified** | **bool** |  | [optional] 
**code_type** | **str** |  | [optional] 

## Example

```python
from clerk_backend_sdk.models.verify_totp200_response import VerifyTOTP200Response

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyTOTP200Response from a JSON string
verify_totp200_response_instance = VerifyTOTP200Response.from_json(json)
# print the JSON string representation of the object
print(VerifyTOTP200Response.to_json())

# convert the object into a dict
verify_totp200_response_dict = verify_totp200_response_instance.to_dict()
# create an instance of VerifyTOTP200Response from a dict
verify_totp200_response_from_dict = VerifyTOTP200Response.from_dict(verify_totp200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


