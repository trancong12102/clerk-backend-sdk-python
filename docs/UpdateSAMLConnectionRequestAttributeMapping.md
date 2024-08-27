# UpdateSAMLConnectionRequestAttributeMapping

Define the atrtibute name mapping between Identity Provider and Clerk's user properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 

## Example

```python
from clerk_backend_sdk.models.update_saml_connection_request_attribute_mapping import UpdateSAMLConnectionRequestAttributeMapping

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSAMLConnectionRequestAttributeMapping from a JSON string
update_saml_connection_request_attribute_mapping_instance = UpdateSAMLConnectionRequestAttributeMapping.from_json(json)
# print the JSON string representation of the object
print(UpdateSAMLConnectionRequestAttributeMapping.to_json())

# convert the object into a dict
update_saml_connection_request_attribute_mapping_dict = update_saml_connection_request_attribute_mapping_instance.to_dict()
# create an instance of UpdateSAMLConnectionRequestAttributeMapping from a dict
update_saml_connection_request_attribute_mapping_from_dict = UpdateSAMLConnectionRequestAttributeMapping.from_dict(update_saml_connection_request_attribute_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


