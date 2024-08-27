# UpdateUserMetadataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_metadata** | **Dict[str, object]** | Metadata saved on the user, that is visible to both your frontend and backend. The new object will be merged with the existing value. | [optional] 
**private_metadata** | **Dict[str, object]** | Metadata saved on the user that is only visible to your backend. The new object will be merged with the existing value. | [optional] 
**unsafe_metadata** | **Dict[str, object]** | Metadata saved on the user, that can be updated from both the Frontend and Backend APIs. The new object will be merged with the existing value.  Note: Since this data can be modified from the frontend, it is not guaranteed to be safe. | [optional] 

## Example

```python
from clerk_backend_sdk.models.update_user_metadata_request import UpdateUserMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserMetadataRequest from a JSON string
update_user_metadata_request_instance = UpdateUserMetadataRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateUserMetadataRequest.to_json())

# convert the object into a dict
update_user_metadata_request_dict = update_user_metadata_request_instance.to_dict()
# create an instance of UpdateUserMetadataRequest from a dict
update_user_metadata_request_from_dict = UpdateUserMetadataRequest.from_dict(update_user_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


