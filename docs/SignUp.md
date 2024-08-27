# SignUp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**id** | **str** |  | 
**status** | **str** |  | 
**required_fields** | **List[str]** |  | [optional] 
**optional_fields** | **List[str]** |  | [optional] 
**missing_fields** | **List[str]** |  | [optional] 
**unverified_fields** | **List[str]** |  | [optional] 
**verifications** | **object** |  | [optional] 
**username** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**web3_wallet** | **str** |  | [optional] 
**password_enabled** | **bool** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**unsafe_metadata** | **object** |  | [optional] 
**public_metadata** | **object** |  | [optional] 
**custom_action** | **bool** |  | 
**external_id** | **str** |  | [optional] 
**created_session_id** | **str** |  | [optional] 
**created_user_id** | **str** |  | [optional] 
**abandon_at** | **int** |  | 
**external_account** | **object** |  | [optional] 

## Example

```python
from clerk_backend_sdk.models.sign_up import SignUp

# TODO update the JSON string below
json = "{}"
# create an instance of SignUp from a JSON string
sign_up_instance = SignUp.from_json(json)
# print the JSON string representation of the object
print(SignUp.to_json())

# convert the object into a dict
sign_up_dict = sign_up_instance.to_dict()
# create an instance of SignUp from a dict
sign_up_from_dict = SignUp.from_dict(sign_up_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


