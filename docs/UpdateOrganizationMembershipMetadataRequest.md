# UpdateOrganizationMembershipMetadataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_metadata** | **object** | Metadata saved on the organization membership, that is visible to both your frontend and backend. The new object will be merged with the existing value. | [optional] 
**private_metadata** | **object** | Metadata saved on the organization membership that is only visible to your backend. The new object will be merged with the existing value. | [optional] 

## Example

```python
from clerk_backend_sdk.models.update_organization_membership_metadata_request import UpdateOrganizationMembershipMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrganizationMembershipMetadataRequest from a JSON string
update_organization_membership_metadata_request_instance = UpdateOrganizationMembershipMetadataRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateOrganizationMembershipMetadataRequest.to_json())

# convert the object into a dict
update_organization_membership_metadata_request_dict = update_organization_membership_metadata_request_instance.to_dict()
# create an instance of UpdateOrganizationMembershipMetadataRequest from a dict
update_organization_membership_metadata_request_from_dict = UpdateOrganizationMembershipMetadataRequest.from_dict(update_organization_membership_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


