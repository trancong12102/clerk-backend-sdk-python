# AllowlistIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | String representing the object&#39;s type. Objects of the same type share the same value.  | [optional] 
**id** | **str** |  | [optional] 
**invitation_id** | **str** |  | [optional] 
**identifier** | **str** | An email address or a phone number.  | [optional] 
**identifier_type** | **str** |  | [optional] 
**instance_id** | **str** |  | [optional] 
**created_at** | **int** | Unix timestamp of creation  | [optional] 
**updated_at** | **int** | Unix timestamp of last update.  | [optional] 

## Example

```python
from clerk_backend_sdk.models.allowlist_identifier import AllowlistIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of AllowlistIdentifier from a JSON string
allowlist_identifier_instance = AllowlistIdentifier.from_json(json)
# print the JSON string representation of the object
print(AllowlistIdentifier.to_json())

# convert the object into a dict
allowlist_identifier_dict = allowlist_identifier_instance.to_dict()
# create an instance of AllowlistIdentifier from a dict
allowlist_identifier_from_dict = AllowlistIdentifier.from_dict(allowlist_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


