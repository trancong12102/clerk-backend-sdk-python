# OrganizationMembership

Hello world

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**object** | **str** | String representing the object&#39;s type. Objects of the same type share the same value.  | [optional] 
**role** | **str** |  | [optional] 
**permissions** | **List[str]** |  | [optional] 
**public_metadata** | **object** | Metadata saved on the organization membership, accessible from both Frontend and Backend APIs | [optional] 
**private_metadata** | **object** | Metadata saved on the organization membership, accessible only from the Backend API | [optional] 
**organization** | [**Organization**](Organization.md) |  | [optional] 
**public_user_data** | [**OrganizationMembershipPublicUserData**](OrganizationMembershipPublicUserData.md) |  | [optional] 
**created_at** | **int** | Unix timestamp of creation. | [optional] 
**updated_at** | **int** | Unix timestamp of last update. | [optional] 

## Example

```python
from clerk_backend_sdk.models.organization_membership import OrganizationMembership

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationMembership from a JSON string
organization_membership_instance = OrganizationMembership.from_json(json)
# print the JSON string representation of the object
print(OrganizationMembership.to_json())

# convert the object into a dict
organization_membership_dict = organization_membership_instance.to_dict()
# create an instance of OrganizationMembership from a dict
organization_membership_from_dict = OrganizationMembership.from_dict(organization_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


