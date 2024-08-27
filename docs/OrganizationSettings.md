# OrganizationSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | String representing the object&#39;s type. Objects of the same type share the same value. | 
**enabled** | **bool** |  | 
**max_allowed_memberships** | **int** |  | 
**max_allowed_roles** | **int** |  | [optional] 
**max_allowed_permissions** | **int** |  | [optional] 
**creator_role** | **str** | The role key that a user will be assigned after creating an organization. | 
**admin_delete_enabled** | **bool** | The default for whether an admin can delete an organization with the Frontend API. | 
**domains_enabled** | **bool** |  | 
**domains_enrollment_modes** | **List[str]** |  | 
**domains_default_role** | **str** | The role key that it will be used in order to create an organization invitation or suggestion. | 

## Example

```python
from clerk_backend_sdk.models.organization_settings import OrganizationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationSettings from a JSON string
organization_settings_instance = OrganizationSettings.from_json(json)
# print the JSON string representation of the object
print(OrganizationSettings.to_json())

# convert the object into a dict
organization_settings_dict = organization_settings_instance.to_dict()
# create an instance of OrganizationSettings from a dict
organization_settings_from_dict = OrganizationSettings.from_dict(organization_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


