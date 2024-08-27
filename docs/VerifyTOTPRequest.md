# VerifyTOTPRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The TOTP or backup code to verify | 

## Example

```python
from clerk_backend_sdk.models.verify_totp_request import VerifyTOTPRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyTOTPRequest from a JSON string
verify_totp_request_instance = VerifyTOTPRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyTOTPRequest.to_json())

# convert the object into a dict
verify_totp_request_dict = verify_totp_request_instance.to_dict()
# create an instance of VerifyTOTPRequest from a dict
verify_totp_request_from_dict = VerifyTOTPRequest.from_dict(verify_totp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


