# PhoneNumberVerification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**strategy** | **str** |  | 
**attempts** | **int** |  | 
**expire_at** | **int** |  | 

## Example

```python
from clerk_backend_sdk.models.phone_number_verification import PhoneNumberVerification

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneNumberVerification from a JSON string
phone_number_verification_instance = PhoneNumberVerification.from_json(json)
# print the JSON string representation of the object
print(PhoneNumberVerification.to_json())

# convert the object into a dict
phone_number_verification_dict = phone_number_verification_instance.to_dict()
# create an instance of PhoneNumberVerification from a dict
phone_number_verification_from_dict = PhoneNumberVerification.from_dict(phone_number_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


