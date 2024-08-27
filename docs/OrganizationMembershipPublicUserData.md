# OrganizationMembershipPublicUserData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**profile_image_url** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**has_image** | **bool** |  | [optional] 
**identifier** | **str** |  | [optional] 

## Example

```python
from clerk_backend_sdk.models.organization_membership_public_user_data import OrganizationMembershipPublicUserData

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationMembershipPublicUserData from a JSON string
organization_membership_public_user_data_instance = OrganizationMembershipPublicUserData.from_json(json)
# print the JSON string representation of the object
print(OrganizationMembershipPublicUserData.to_json())

# convert the object into a dict
organization_membership_public_user_data_dict = organization_membership_public_user_data_instance.to_dict()
# create an instance of OrganizationMembershipPublicUserData from a dict
organization_membership_public_user_data_from_dict = OrganizationMembershipPublicUserData.from_dict(organization_membership_public_user_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


