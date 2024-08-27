# EmailAddressVerification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**strategy** | **str** |  | 
**attempts** | **int** |  | 
**expire_at** | **int** |  | 
**external_verification_redirect_url** | **str** |  | [optional] 
**error** | [**OauthError**](OauthError.md) |  | [optional] 

## Example

```python
from clerk_backend_sdk.models.email_address_verification import EmailAddressVerification

# TODO update the JSON string below
json = "{}"
# create an instance of EmailAddressVerification from a JSON string
email_address_verification_instance = EmailAddressVerification.from_json(json)
# print the JSON string representation of the object
print(EmailAddressVerification.to_json())

# convert the object into a dict
email_address_verification_dict = email_address_verification_instance.to_dict()
# create an instance of EmailAddressVerification from a dict
email_address_verification_from_dict = EmailAddressVerification.from_dict(email_address_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


