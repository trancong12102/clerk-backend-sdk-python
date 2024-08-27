# CreateSAMLConnectionRequestAttributeMapping

Define the attribute name mapping between Identity Provider and Clerk's user properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 

## Example

```python
from clerk_backend_sdk.models.create_saml_connection_request_attribute_mapping import CreateSAMLConnectionRequestAttributeMapping

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSAMLConnectionRequestAttributeMapping from a JSON string
create_saml_connection_request_attribute_mapping_instance = CreateSAMLConnectionRequestAttributeMapping.from_json(json)
# print the JSON string representation of the object
print(CreateSAMLConnectionRequestAttributeMapping.to_json())

# convert the object into a dict
create_saml_connection_request_attribute_mapping_dict = create_saml_connection_request_attribute_mapping_instance.to_dict()
# create an instance of CreateSAMLConnectionRequestAttributeMapping from a dict
create_saml_connection_request_attribute_mapping_from_dict = CreateSAMLConnectionRequestAttributeMapping.from_dict(create_saml_connection_request_attribute_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


