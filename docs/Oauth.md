# Oauth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**strategy** | **str** |  | 
**external_verification_redirect_url** | **str** |  | [optional] 
**error** | [**OauthError**](OauthError.md) |  | [optional] 
**expire_at** | **int** |  | 
**attempts** | **int** |  | [optional] 

## Example

```python
from clerk_backend_sdk.models.oauth import Oauth

# TODO update the JSON string below
json = "{}"
# create an instance of Oauth from a JSON string
oauth_instance = Oauth.from_json(json)
# print the JSON string representation of the object
print(Oauth.to_json())

# convert the object into a dict
oauth_dict = oauth_instance.to_dict()
# create an instance of Oauth from a dict
oauth_from_dict = Oauth.from_dict(oauth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


