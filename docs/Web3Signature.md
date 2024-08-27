# Web3Signature


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
from clerk_backend_sdk.models.web3_signature import Web3Signature

# TODO update the JSON string below
json = "{}"
# create an instance of Web3Signature from a JSON string
web3_signature_instance = Web3Signature.from_json(json)
# print the JSON string representation of the object
print(Web3Signature.to_json())

# convert the object into a dict
web3_signature_dict = web3_signature_instance.to_dict()
# create an instance of Web3Signature from a dict
web3_signature_from_dict = Web3Signature.from_dict(web3_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


