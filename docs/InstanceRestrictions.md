# InstanceRestrictions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | String representing the object&#39;s type. Objects of the same type share the same value. | [optional] 
**allowlist** | **bool** |  | [optional] 
**blocklist** | **bool** |  | [optional] 
**block_email_subaddresses** | **bool** |  | [optional] 
**ignore_dots_for_gmail_addresses** | **bool** |  | [optional] 

## Example

```python
from clerk_backend_sdk.models.instance_restrictions import InstanceRestrictions

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceRestrictions from a JSON string
instance_restrictions_instance = InstanceRestrictions.from_json(json)
# print the JSON string representation of the object
print(InstanceRestrictions.to_json())

# convert the object into a dict
instance_restrictions_dict = instance_restrictions_instance.to_dict()
# create an instance of InstanceRestrictions from a dict
instance_restrictions_from_dict = InstanceRestrictions.from_dict(instance_restrictions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


