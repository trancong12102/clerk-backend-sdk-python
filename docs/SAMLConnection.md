# SAMLConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**domain** | **str** |  | 
**idp_entity_id** | **str** |  | 
**idp_sso_url** | **str** |  | 
**idp_certificate** | **str** |  | 
**idp_metadata_url** | **str** |  | [optional] 
**idp_metadata** | **str** |  | [optional] 
**acs_url** | **str** |  | 
**sp_entity_id** | **str** |  | 
**sp_metadata_url** | **str** |  | 
**attribute_mapping** | [**SAMLConnectionAttributeMapping**](SAMLConnectionAttributeMapping.md) |  | [optional] 
**active** | **bool** |  | 
**provider** | **str** |  | 
**user_count** | **int** |  | 
**sync_user_attributes** | **bool** |  | 
**allow_subdomains** | **bool** |  | [optional] 
**allow_idp_initiated** | **bool** |  | [optional] 
**created_at** | **int** | Unix timestamp of creation.  | 
**updated_at** | **int** | Unix timestamp of last update.  | 

## Example

```python
from clerk_backend_sdk.models.saml_connection import SAMLConnection

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLConnection from a JSON string
saml_connection_instance = SAMLConnection.from_json(json)
# print the JSON string representation of the object
print(SAMLConnection.to_json())

# convert the object into a dict
saml_connection_dict = saml_connection_instance.to_dict()
# create an instance of SAMLConnection from a dict
saml_connection_from_dict = SAMLConnection.from_dict(saml_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


