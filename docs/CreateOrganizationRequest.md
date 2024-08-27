# CreateOrganizationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the new organization | 
**created_by** | **str** | The ID of the User who will become the administrator for the new organization | 
**private_metadata** | **object** | Metadata saved on the organization, accessible only from the Backend API | [optional] 
**public_metadata** | **object** | Metadata saved on the organization, read-only from the Frontend API and fully accessible (read/write) from the Backend API | [optional] 
**slug** | **str** | A slug for the new organization. Can contain only lowercase alphanumeric characters and the dash \&quot;-\&quot;. Must be unique for the instance. | [optional] 
**max_allowed_memberships** | **int** | The maximum number of memberships allowed for this organization | [optional] 
**created_at** | **str** | A custom date/time denoting _when_ the organization was created, specified in RFC3339 format (e.g. &#x60;2012-10-20T07:15:20.902Z&#x60;). | [optional] 

## Example

```python
from clerk_backend_sdk.models.create_organization_request import CreateOrganizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationRequest from a JSON string
create_organization_request_instance = CreateOrganizationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrganizationRequest.to_json())

# convert the object into a dict
create_organization_request_dict = create_organization_request_instance.to_dict()
# create an instance of CreateOrganizationRequest from a dict
create_organization_request_from_dict = CreateOrganizationRequest.from_dict(create_organization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


