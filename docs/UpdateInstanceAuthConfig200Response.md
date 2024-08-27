# UpdateInstanceAuthConfig200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | String representing the object&#39;s type. Objects of the same type share the same value. | [optional] 
**id** | **str** |  | [optional] 
**restricted_to_allowlist** | **bool** |  | [optional] 
**from_email_address** | **str** |  | [optional] 
**progressive_sign_up** | **bool** |  | [optional] 
**enhanced_email_deliverability** | **bool** |  | [optional] 

## Example

```python
from clerk_backend_sdk.models.update_instance_auth_config200_response import UpdateInstanceAuthConfig200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInstanceAuthConfig200Response from a JSON string
update_instance_auth_config200_response_instance = UpdateInstanceAuthConfig200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateInstanceAuthConfig200Response.to_json())

# convert the object into a dict
update_instance_auth_config200_response_dict = update_instance_auth_config200_response_instance.to_dict()
# create an instance of UpdateInstanceAuthConfig200Response from a dict
update_instance_auth_config200_response_from_dict = UpdateInstanceAuthConfig200Response.from_dict(update_instance_auth_config200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


