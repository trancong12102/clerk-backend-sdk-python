# OrganizationMemberships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[OrganizationMembership]**](OrganizationMembership.md) |  | 
**total_count** | **int** | Total number of organization memberships  | 

## Example

```python
from clerk_backend_sdk.models.organization_memberships import OrganizationMemberships

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationMemberships from a JSON string
organization_memberships_instance = OrganizationMemberships.from_json(json)
# print the JSON string representation of the object
print(OrganizationMemberships.to_json())

# convert the object into a dict
organization_memberships_dict = organization_memberships_instance.to_dict()
# create an instance of OrganizationMemberships from a dict
organization_memberships_from_dict = OrganizationMemberships.from_dict(organization_memberships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


