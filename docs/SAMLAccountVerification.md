# SAMLAccountVerification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**strategy** | **str** |  | 
**external_verification_redirect_url** | **str** |  | 
**error** | [**OauthError**](OauthError.md) |  | [optional] 
**expire_at** | **int** |  | 
**attempts** | **int** |  | [optional] 

## Example

```python
from clerk_backend_sdk.models.saml_account_verification import SAMLAccountVerification

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLAccountVerification from a JSON string
saml_account_verification_instance = SAMLAccountVerification.from_json(json)
# print the JSON string representation of the object
print(SAMLAccountVerification.to_json())

# convert the object into a dict
saml_account_verification_dict = saml_account_verification_instance.to_dict()
# create an instance of SAMLAccountVerification from a dict
saml_account_verification_from_dict = SAMLAccountVerification.from_dict(saml_account_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


