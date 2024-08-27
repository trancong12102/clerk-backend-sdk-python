# CreateAllowlistIdentifierRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | The identifier to be added in the allow-list. This can be an email address, a phone number or a web3 wallet. | 
**notify** | **bool** | This flag denotes whether the given identifier will receive an invitation to join the application. Note that this only works for email address and phone number identifiers. | [optional] [default to False]

## Example

```python
from clerk_backend_sdk.models.create_allowlist_identifier_request import CreateAllowlistIdentifierRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAllowlistIdentifierRequest from a JSON string
create_allowlist_identifier_request_instance = CreateAllowlistIdentifierRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAllowlistIdentifierRequest.to_json())

# convert the object into a dict
create_allowlist_identifier_request_dict = create_allowlist_identifier_request_instance.to_dict()
# create an instance of CreateAllowlistIdentifierRequest from a dict
create_allowlist_identifier_request_from_dict = CreateAllowlistIdentifierRequest.from_dict(create_allowlist_identifier_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


