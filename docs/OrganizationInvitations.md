# OrganizationInvitations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[OrganizationInvitation]**](OrganizationInvitation.md) |  | 
**total_count** | **int** | Total number of organization invitations  | 

## Example

```python
from clerk_backend_sdk.models.organization_invitations import OrganizationInvitations

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationInvitations from a JSON string
organization_invitations_instance = OrganizationInvitations.from_json(json)
# print the JSON string representation of the object
print(OrganizationInvitations.to_json())

# convert the object into a dict
organization_invitations_dict = organization_invitations_instance.to_dict()
# create an instance of OrganizationInvitations from a dict
organization_invitations_from_dict = OrganizationInvitations.from_dict(organization_invitations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


