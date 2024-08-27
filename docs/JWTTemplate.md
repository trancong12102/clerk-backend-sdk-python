# JWTTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**claims** | **object** |  | 
**lifetime** | **int** |  | 
**allowed_clock_skew** | **int** |  | 
**custom_signing_key** | **bool** |  | [optional] 
**signing_algorithm** | **str** |  | [optional] 
**created_at** | **int** | Unix timestamp of creation.  | 
**updated_at** | **int** | Unix timestamp of last update.  | 

## Example

```python
from clerk_backend_sdk.models.jwt_template import JWTTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of JWTTemplate from a JSON string
jwt_template_instance = JWTTemplate.from_json(json)
# print the JSON string representation of the object
print(JWTTemplate.to_json())

# convert the object into a dict
jwt_template_dict = jwt_template_instance.to_dict()
# create an instance of JWTTemplate from a dict
jwt_template_from_dict = JWTTemplate.from_dict(jwt_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


