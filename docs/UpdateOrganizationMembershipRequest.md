# UpdateOrganizationMembershipRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | The new role of the given membership. | 

## Example

```python
from clerk_backend_sdk.models.update_organization_membership_request import UpdateOrganizationMembershipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrganizationMembershipRequest from a JSON string
update_organization_membership_request_instance = UpdateOrganizationMembershipRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateOrganizationMembershipRequest.to_json())

# convert the object into a dict
update_organization_membership_request_dict = update_organization_membership_request_instance.to_dict()
# create an instance of UpdateOrganizationMembershipRequest from a dict
update_organization_membership_request_from_dict = UpdateOrganizationMembershipRequest.from_dict(update_organization_membership_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


