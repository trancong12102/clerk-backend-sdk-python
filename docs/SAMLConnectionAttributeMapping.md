# SAMLConnectionAttributeMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 

## Example

```python
from clerk_backend_sdk.models.saml_connection_attribute_mapping import SAMLConnectionAttributeMapping

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLConnectionAttributeMapping from a JSON string
saml_connection_attribute_mapping_instance = SAMLConnectionAttributeMapping.from_json(json)
# print the JSON string representation of the object
print(SAMLConnectionAttributeMapping.to_json())

# convert the object into a dict
saml_connection_attribute_mapping_dict = saml_connection_attribute_mapping_instance.to_dict()
# create an instance of SAMLConnectionAttributeMapping from a dict
saml_connection_attribute_mapping_from_dict = SAMLConnectionAttributeMapping.from_dict(saml_connection_attribute_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


