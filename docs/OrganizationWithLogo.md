# OrganizationWithLogo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 
**members_count** | **int** |  | [optional] 
**max_allowed_memberships** | **int** |  | 
**admin_delete_enabled** | **bool** |  | [optional] 
**public_metadata** | **object** |  | 
**private_metadata** | **object** |  | 
**created_by** | **str** |  | [optional] 
**created_at** | **int** | Unix timestamp of creation.  | 
**updated_at** | **int** | Unix timestamp of last update.  | 
**logo_url** | **str** |  | [optional] 
**image_url** | **str** |  | 
**has_image** | **bool** |  | [optional] 

## Example

```python
from clerk_backend_sdk.models.organization_with_logo import OrganizationWithLogo

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationWithLogo from a JSON string
organization_with_logo_instance = OrganizationWithLogo.from_json(json)
# print the JSON string representation of the object
print(OrganizationWithLogo.to_json())

# convert the object into a dict
organization_with_logo_dict = organization_with_logo_instance.to_dict()
# create an instance of OrganizationWithLogo from a dict
organization_with_logo_from_dict = OrganizationWithLogo.from_dict(organization_with_logo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


