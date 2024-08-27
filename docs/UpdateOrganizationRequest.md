# UpdateOrganizationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_metadata** | **object** | Metadata saved on the organization, that is visible to both your frontend and backend. | [optional] 
**private_metadata** | **object** | Metadata saved on the organization that is only visible to your backend. | [optional] 
**name** | **str** | The new name of the organization | [optional] 
**slug** | **str** | The new slug of the organization, which needs to be unique in the instance | [optional] 
**max_allowed_memberships** | **int** | The maximum number of memberships allowed for this organization | [optional] 
**admin_delete_enabled** | **bool** | If true, an admin can delete this organization with the Frontend API. | [optional] 
**created_at** | **str** | A custom date/time denoting _when_ the organization was created, specified in RFC3339 format (e.g. &#x60;2012-10-20T07:15:20.902Z&#x60;). | [optional] 

## Example

```python
from clerk_backend_sdk.models.update_organization_request import UpdateOrganizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrganizationRequest from a JSON string
update_organization_request_instance = UpdateOrganizationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateOrganizationRequest.to_json())

# convert the object into a dict
update_organization_request_dict = update_organization_request_instance.to_dict()
# create an instance of UpdateOrganizationRequest from a dict
update_organization_request_from_dict = UpdateOrganizationRequest.from_dict(update_organization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


