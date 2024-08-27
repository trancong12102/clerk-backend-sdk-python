# Web3Wallet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**object** | **str** | String representing the object&#39;s type. Objects of the same type share the same value.  | 
**web3_wallet** | **str** |  | 
**verification** | [**Web3WalletVerification**](Web3WalletVerification.md) |  | 
**created_at** | **int** | Unix timestamp of creation  | 
**updated_at** | **int** | Unix timestamp of creation  | 

## Example

```python
from clerk_backend_sdk.models.web3_wallet import Web3Wallet

# TODO update the JSON string below
json = "{}"
# create an instance of Web3Wallet from a JSON string
web3_wallet_instance = Web3Wallet.from_json(json)
# print the JSON string representation of the object
print(Web3Wallet.to_json())

# convert the object into a dict
web3_wallet_dict = web3_wallet_instance.to_dict()
# create an instance of Web3Wallet from a dict
web3_wallet_from_dict = Web3Wallet.from_dict(web3_wallet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


