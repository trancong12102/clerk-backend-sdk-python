# OAuthApplicationWithSecret


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
**client_secret** | **str** | Empty if public client.  | [optional] 

## Example

```python
from clerk_backend_sdk.models.o_auth_application_with_secret import OAuthApplicationWithSecret

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthApplicationWithSecret from a JSON string
o_auth_application_with_secret_instance = OAuthApplicationWithSecret.from_json(json)
# print the JSON string representation of the object
print(OAuthApplicationWithSecret.to_json())

# convert the object into a dict
o_auth_application_with_secret_dict = o_auth_application_with_secret_instance.to_dict()
# create an instance of OAuthApplicationWithSecret from a dict
o_auth_application_with_secret_from_dict = OAuthApplicationWithSecret.from_dict(o_auth_application_with_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


