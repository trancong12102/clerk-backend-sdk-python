# CreateBlocklistIdentifierRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | The identifier to be added in the block-list. This can be an email address, a phone number or a web3 wallet. | 

## Example

```python
from clerk_backend_sdk.models.create_blocklist_identifier_request import CreateBlocklistIdentifierRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBlocklistIdentifierRequest from a JSON string
create_blocklist_identifier_request_instance = CreateBlocklistIdentifierRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBlocklistIdentifierRequest.to_json())

# convert the object into a dict
create_blocklist_identifier_request_dict = create_blocklist_identifier_request_instance.to_dict()
# create an instance of CreateBlocklistIdentifierRequest from a dict
create_blocklist_identifier_request_from_dict = CreateBlocklistIdentifierRequest.from_dict(create_blocklist_identifier_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


