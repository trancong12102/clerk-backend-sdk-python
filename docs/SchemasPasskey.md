# SchemasPasskey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**object** | **str** | String representing the object&#39;s type. Objects of the same type share the same value.  | 
**name** | **str** |  | 
**last_used_at** | **int** | Unix timestamp of when the passkey was last used.  | 
**verification** | [**SchemasPasskeyVerification**](SchemasPasskeyVerification.md) |  | 

## Example

```python
from clerk_backend_sdk.models.schemas_passkey import SchemasPasskey

# TODO update the JSON string below
json = "{}"
# create an instance of SchemasPasskey from a JSON string
schemas_passkey_instance = SchemasPasskey.from_json(json)
# print the JSON string representation of the object
print(SchemasPasskey.to_json())

# convert the object into a dict
schemas_passkey_dict = schemas_passkey_instance.to_dict()
# create an instance of SchemasPasskey from a dict
schemas_passkey_from_dict = SchemasPasskey.from_dict(schemas_passkey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


