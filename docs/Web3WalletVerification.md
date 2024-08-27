# Web3WalletVerification


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
from clerk_backend_sdk.models.web3_wallet_verification import Web3WalletVerification

# TODO update the JSON string below
json = "{}"
# create an instance of Web3WalletVerification from a JSON string
web3_wallet_verification_instance = Web3WalletVerification.from_json(json)
# print the JSON string representation of the object
print(Web3WalletVerification.to_json())

# convert the object into a dict
web3_wallet_verification_dict = web3_wallet_verification_instance.to_dict()
# create an instance of Web3WalletVerification from a dict
web3_wallet_verification_from_dict = Web3WalletVerification.from_dict(web3_wallet_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


