# SAML


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**strategy** | **str** |  | 
**external_verification_redirect_url** | **str** |  | 
**error** | [**OauthError**](OauthError.md) |  | [optional] 
**expire_at** | **int** |  | 
**attempts** | **int** |  | [optional] 

## Example

```python
from clerk_backend_sdk.models.saml import SAML

# TODO update the JSON string below
json = "{}"
# create an instance of SAML from a JSON string
saml_instance = SAML.from_json(json)
# print the JSON string representation of the object
print(SAML.to_json())

# convert the object into a dict
saml_dict = saml_instance.to_dict()
# create an instance of SAML from a dict
saml_from_dict = SAML.from_dict(saml_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


