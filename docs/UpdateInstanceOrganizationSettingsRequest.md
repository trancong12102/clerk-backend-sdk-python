# UpdateInstanceOrganizationSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**max_allowed_memberships** | **int** |  | [optional] 
**admin_delete_enabled** | **bool** |  | [optional] 
**domains_enabled** | **bool** |  | [optional] 
**domains_enrollment_modes** | **List[str]** | Specify which enrollment modes to enable for your Organization Domains. Supported modes are &#39;automatic_invitation&#39; &amp; &#39;automatic_suggestion&#39;. | [optional] 
**creator_role_id** | **str** | Specify what the default organization role is for an organization creator. | [optional] 
**domains_default_role_id** | **str** | Specify what the default organization role is for the organization domains. | [optional] 

## Example

```python
from clerk_backend_sdk.models.update_instance_organization_settings_request import UpdateInstanceOrganizationSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInstanceOrganizationSettingsRequest from a JSON string
update_instance_organization_settings_request_instance = UpdateInstanceOrganizationSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateInstanceOrganizationSettingsRequest.to_json())

# convert the object into a dict
update_instance_organization_settings_request_dict = update_instance_organization_settings_request_instance.to_dict()
# create an instance of UpdateInstanceOrganizationSettingsRequest from a dict
update_instance_organization_settings_request_from_dict = UpdateInstanceOrganizationSettingsRequest.from_dict(update_instance_organization_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


