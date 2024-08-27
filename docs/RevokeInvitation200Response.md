# RevokeInvitation200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**id** | **str** |  | 
**email_address** | **str** |  | 
**public_metadata** | **object** |  | [optional] 
**revoked** | **bool** |  | [optional] 
**status** | **str** |  | 
**url** | **str** |  | [optional] 
**created_at** | **int** | Unix timestamp of creation.  | 
**updated_at** | **int** | Unix timestamp of last update.  | 

## Example

```python
from clerk_backend_sdk.models.revoke_invitation200_response import RevokeInvitation200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeInvitation200Response from a JSON string
revoke_invitation200_response_instance = RevokeInvitation200Response.from_json(json)
# print the JSON string representation of the object
print(RevokeInvitation200Response.to_json())

# convert the object into a dict
revoke_invitation200_response_dict = revoke_invitation200_response_instance.to_dict()
# create an instance of RevokeInvitation200Response from a dict
revoke_invitation200_response_from_dict = RevokeInvitation200Response.from_dict(revoke_invitation200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


