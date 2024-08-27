# GetOAuthAccessToken200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] 
**external_account_id** | **str** | External account ID | [optional] 
**provider_user_id** | **str** | The unique ID of the user in the external provider&#39;s system | [optional] 
**token** | **str** | The access token | [optional] 
**provider** | **str** | The ID of the provider | [optional] 
**public_metadata** | **object** |  | [optional] 
**label** | **str** |  | [optional] 
**scopes** | **List[str]** | The list of scopes that the token is valid for. Only present for OAuth 2.0 tokens. | [optional] 
**token_secret** | **str** | The token secret. Only present for OAuth 1.0 tokens. | [optional] 

## Example

```python
from clerk_backend_sdk.models.get_o_auth_access_token200_response_inner import GetOAuthAccessToken200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetOAuthAccessToken200ResponseInner from a JSON string
get_o_auth_access_token200_response_inner_instance = GetOAuthAccessToken200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetOAuthAccessToken200ResponseInner.to_json())

# convert the object into a dict
get_o_auth_access_token200_response_inner_dict = get_o_auth_access_token200_response_inner_instance.to_dict()
# create an instance of GetOAuthAccessToken200ResponseInner from a dict
get_o_auth_access_token200_response_inner_from_dict = GetOAuthAccessToken200ResponseInner.from_dict(get_o_auth_access_token200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


