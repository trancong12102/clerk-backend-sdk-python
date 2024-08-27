# CreateOrganizationMembershipRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The ID of the user that will be added as a member in the organization. The user needs to exist in the same instance as the organization and must not be a member of the given organization already. | 
**role** | **str** | The role that the new member will have in the organization. | 

## Example

```python
from clerk_backend_sdk.models.create_organization_membership_request import CreateOrganizationMembershipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationMembershipRequest from a JSON string
create_organization_membership_request_instance = CreateOrganizationMembershipRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrganizationMembershipRequest.to_json())

# convert the object into a dict
create_organization_membership_request_dict = create_organization_membership_request_instance.to_dict()
# create an instance of CreateOrganizationMembershipRequest from a dict
create_organization_membership_request_from_dict = CreateOrganizationMembershipRequest.from_dict(create_organization_membership_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


