# BlocklistIdentifiers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BlocklistIdentifier]**](BlocklistIdentifier.md) |  | 
**total_count** | **int** | Total number of blocklist identifiers  | 

## Example

```python
from clerk_backend_sdk.models.blocklist_identifiers import BlocklistIdentifiers

# TODO update the JSON string below
json = "{}"
# create an instance of BlocklistIdentifiers from a JSON string
blocklist_identifiers_instance = BlocklistIdentifiers.from_json(json)
# print the JSON string representation of the object
print(BlocklistIdentifiers.to_json())

# convert the object into a dict
blocklist_identifiers_dict = blocklist_identifiers_instance.to_dict()
# create an instance of BlocklistIdentifiers from a dict
blocklist_identifiers_from_dict = BlocklistIdentifiers.from_dict(blocklist_identifiers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


