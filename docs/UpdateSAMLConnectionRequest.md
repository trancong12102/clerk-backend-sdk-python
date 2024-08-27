# UpdateSAMLConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the new SAML Connection | [optional] 
**domain** | **str** | The domain to use for the new SAML Connection | [optional] 
**idp_entity_id** | **str** | The entity id as provided by the IdP | [optional] 
**idp_sso_url** | **str** | The SSO url as provided by the IdP | [optional] 
**idp_certificate** | **str** | The x509 certificated as provided by the IdP | [optional] 
**idp_metadata_url** | **str** | The URL which serves the IdP metadata. If present, it takes priority over the corresponding individual properties and replaces them | [optional] 
**idp_metadata** | **str** | The XML content of the IdP metadata file. If present, it takes priority over the corresponding individual properties | [optional] 
**attribute_mapping** | [**UpdateSAMLConnectionRequestAttributeMapping**](UpdateSAMLConnectionRequestAttributeMapping.md) |  | [optional] 
**active** | **bool** | Activate or de-activate the SAML Connection | [optional] 
**sync_user_attributes** | **bool** | Controls whether to update the user&#39;s attributes in each sign-in | [optional] 
**allow_subdomains** | **bool** | Allow users with an email address subdomain to use this connection in order to authenticate | [optional] 
**allow_idp_initiated** | **bool** | Enable or deactivate IdP-initiated flows | [optional] 

## Example

```python
from clerk_backend_sdk.models.update_saml_connection_request import UpdateSAMLConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSAMLConnectionRequest from a JSON string
update_saml_connection_request_instance = UpdateSAMLConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSAMLConnectionRequest.to_json())

# convert the object into a dict
update_saml_connection_request_dict = update_saml_connection_request_instance.to_dict()
# create an instance of UpdateSAMLConnectionRequest from a dict
update_saml_connection_request_from_dict = UpdateSAMLConnectionRequest.from_dict(update_saml_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


