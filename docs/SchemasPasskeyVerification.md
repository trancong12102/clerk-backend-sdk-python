# SchemasPasskeyVerification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**strategy** | **str** |  | 
**nonce** | **str** |  | [optional] 
**attempts** | **int** |  | [optional] 
**expire_at** | **int** |  | [optional] 

## Example

```python
from clerk_backend_sdk.models.schemas_passkey_verification import SchemasPasskeyVerification

# TODO update the JSON string below
json = "{}"
# create an instance of SchemasPasskeyVerification from a JSON string
schemas_passkey_verification_instance = SchemasPasskeyVerification.from_json(json)
# print the JSON string representation of the object
print(SchemasPasskeyVerification.to_json())

# convert the object into a dict
schemas_passkey_verification_dict = schemas_passkey_verification_instance.to_dict()
# create an instance of SchemasPasskeyVerification from a dict
schemas_passkey_verification_from_dict = SchemasPasskeyVerification.from_dict(schemas_passkey_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


