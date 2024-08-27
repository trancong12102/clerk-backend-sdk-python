# OAuthApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**id** | **str** |  | 
**instance_id** | **str** |  | 
**name** | **str** |  | 
**client_id** | **str** |  | 
**public** | **bool** |  | 
**scopes** | **str** |  | 
**callback_url** | **str** |  | 
**authorize_url** | **str** |  | 
**token_fetch_url** | **str** |  | 
**user_info_url** | **str** |  | 
**created_at** | **int** | Unix timestamp of creation.  | 
**updated_at** | **int** | Unix timestamp of last update.  | 

## Example

```python
from clerk_backend_sdk.models.o_auth_application import OAuthApplication

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthApplication from a JSON string
o_auth_application_instance = OAuthApplication.from_json(json)
# print the JSON string representation of the object
print(OAuthApplication.to_json())

# convert the object into a dict
o_auth_application_dict = o_auth_application_instance.to_dict()
# create an instance of OAuthApplication from a dict
o_auth_application_from_dict = OAuthApplication.from_dict(o_auth_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


