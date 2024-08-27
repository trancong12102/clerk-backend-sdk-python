# BlocklistIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | String representing the object&#39;s type. Objects of the same type share the same value.  | [optional] 
**id** | **str** |  | [optional] 
**identifier** | **str** | An email address, email domain, phone number or web3 wallet.  | [optional] 
**identifier_type** | **str** |  | [optional] 
**instance_id** | **str** |  | [optional] 
**created_at** | **int** | Unix timestamp of creation  | [optional] 
**updated_at** | **int** | Unix timestamp of last update.  | [optional] 

## Example

```python
from clerk_backend_sdk.models.blocklist_identifier import BlocklistIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of BlocklistIdentifier from a JSON string
blocklist_identifier_instance = BlocklistIdentifier.from_json(json)
# print the JSON string representation of the object
print(BlocklistIdentifier.to_json())

# convert the object into a dict
blocklist_identifier_dict = blocklist_identifier_instance.to_dict()
# create an instance of BlocklistIdentifier from a dict
blocklist_identifier_from_dict = BlocklistIdentifier.from_dict(blocklist_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


