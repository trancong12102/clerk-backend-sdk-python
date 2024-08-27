# CreateJWTTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | JWT template name | [optional] 
**claims** | **object** | JWT template claims in JSON format | [optional] 
**lifetime** | **float** | JWT token lifetime | [optional] 
**allowed_clock_skew** | **float** | JWT token allowed clock skew | [optional] 
**custom_signing_key** | **bool** | Whether a custom signing key/algorithm is also provided for this template | [optional] 
**signing_algorithm** | **str** | The custom signing algorithm to use when minting JWTs | [optional] 
**signing_key** | **str** | The custom signing private key to use when minting JWTs | [optional] 

## Example

```python
from clerk_backend_sdk.models.create_jwt_template_request import CreateJWTTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateJWTTemplateRequest from a JSON string
create_jwt_template_request_instance = CreateJWTTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(CreateJWTTemplateRequest.to_json())

# convert the object into a dict
create_jwt_template_request_dict = create_jwt_template_request_instance.to_dict()
# create an instance of CreateJWTTemplateRequest from a dict
create_jwt_template_request_from_dict = CreateJWTTemplateRequest.from_dict(create_jwt_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


