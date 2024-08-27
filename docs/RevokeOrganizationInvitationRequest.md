# RevokeOrganizationInvitationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requesting_user_id** | **str** | The ID of the user that revokes the invitation. Must be an administrator in the organization. | 

## Example

```python
from clerk_backend_sdk.models.revoke_organization_invitation_request import RevokeOrganizationInvitationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeOrganizationInvitationRequest from a JSON string
revoke_organization_invitation_request_instance = RevokeOrganizationInvitationRequest.from_json(json)
# print the JSON string representation of the object
print(RevokeOrganizationInvitationRequest.to_json())

# convert the object into a dict
revoke_organization_invitation_request_dict = revoke_organization_invitation_request_instance.to_dict()
# create an instance of RevokeOrganizationInvitationRequest from a dict
revoke_organization_invitation_request_from_dict = RevokeOrganizationInvitationRequest.from_dict(revoke_organization_invitation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


