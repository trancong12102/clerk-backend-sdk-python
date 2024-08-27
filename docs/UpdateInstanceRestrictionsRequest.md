# UpdateInstanceRestrictionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowlist** | **bool** |  | [optional] 
**blocklist** | **bool** |  | [optional] 
**block_email_subaddresses** | **bool** |  | [optional] 
**block_disposable_email_domains** | **bool** |  | [optional] 
**ignore_dots_for_gmail_addresses** | **bool** |  | [optional] 

## Example

```python
from clerk_backend_sdk.models.update_instance_restrictions_request import UpdateInstanceRestrictionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInstanceRestrictionsRequest from a JSON string
update_instance_restrictions_request_instance = UpdateInstanceRestrictionsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateInstanceRestrictionsRequest.to_json())

# convert the object into a dict
update_instance_restrictions_request_dict = update_instance_restrictions_request_instance.to_dict()
# create an instance of UpdateInstanceRestrictionsRequest from a dict
update_instance_restrictions_request_from_dict = UpdateInstanceRestrictionsRequest.from_dict(update_instance_restrictions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


