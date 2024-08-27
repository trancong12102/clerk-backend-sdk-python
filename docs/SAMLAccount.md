# SAMLAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**object** | **str** | String representing the object&#39;s type. Objects of the same type share the same value.  | 
**provider** | **str** |  | 
**active** | **bool** |  | 
**email_address** | **str** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**provider_user_id** | **str** |  | [optional] 
**public_metadata** | **object** |  | [optional] 
**verification** | [**SAMLAccountVerification**](SAMLAccountVerification.md) |  | 

## Example

```python
from clerk_backend_sdk.models.saml_account import SAMLAccount

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLAccount from a JSON string
saml_account_instance = SAMLAccount.from_json(json)
# print the JSON string representation of the object
print(SAMLAccount.to_json())

# convert the object into a dict
saml_account_dict = saml_account_instance.to_dict()
# create an instance of SAMLAccount from a dict
saml_account_from_dict = SAMLAccount.from_dict(saml_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


