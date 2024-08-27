# MergeOrganizationMetadataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_metadata** | **object** | Metadata saved on the organization, that is visible to both your frontend and backend. The new object will be merged with the existing value. | [optional] 
**private_metadata** | **object** | Metadata saved on the organization that is only visible to your backend. The new object will be merged with the existing value. | [optional] 

## Example

```python
from clerk_backend_sdk.models.merge_organization_metadata_request import MergeOrganizationMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MergeOrganizationMetadataRequest from a JSON string
merge_organization_metadata_request_instance = MergeOrganizationMetadataRequest.from_json(json)
# print the JSON string representation of the object
print(MergeOrganizationMetadataRequest.to_json())

# convert the object into a dict
merge_organization_metadata_request_dict = merge_organization_metadata_request_instance.to_dict()
# create an instance of MergeOrganizationMetadataRequest from a dict
merge_organization_metadata_request_from_dict = MergeOrganizationMetadataRequest.from_dict(merge_organization_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


