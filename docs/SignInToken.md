# SignInToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**id** | **str** |  | 
**status** | **str** |  | 
**user_id** | **str** |  | 
**token** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**created_at** | **int** | Unix timestamp of creation.  | 
**updated_at** | **int** | Unix timestamp of last update.  | 

## Example

```python
from clerk_backend_sdk.models.sign_in_token import SignInToken

# TODO update the JSON string below
json = "{}"
# create an instance of SignInToken from a JSON string
sign_in_token_instance = SignInToken.from_json(json)
# print the JSON string representation of the object
print(SignInToken.to_json())

# convert the object into a dict
sign_in_token_dict = sign_in_token_instance.to_dict()
# create an instance of SignInToken from a dict
sign_in_token_from_dict = SignInToken.from_dict(sign_in_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


