# OTP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**strategy** | **str** |  | 
**attempts** | **int** |  | 
**expire_at** | **int** |  | 

## Example

```python
from clerk_backend_sdk.models.otp import OTP

# TODO update the JSON string below
json = "{}"
# create an instance of OTP from a JSON string
otp_instance = OTP.from_json(json)
# print the JSON string representation of the object
print(OTP.to_json())

# convert the object into a dict
otp_dict = otp_instance.to_dict()
# create an instance of OTP from a dict
otp_from_dict = OTP.from_dict(otp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


