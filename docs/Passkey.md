# Passkey


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
from clerk_backend_sdk.models.passkey import Passkey

# TODO update the JSON string below
json = "{}"
# create an instance of Passkey from a JSON string
passkey_instance = Passkey.from_json(json)
# print the JSON string representation of the object
print(Passkey.to_json())

# convert the object into a dict
passkey_dict = passkey_instance.to_dict()
# create an instance of Passkey from a dict
passkey_from_dict = Passkey.from_dict(passkey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


