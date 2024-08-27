# CreateSAMLConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name to use as a label for this SAML Connection | 
**domain** | **str** | The domain of your organization. Sign in flows using an email with this domain, will use this SAML Connection. | 
**provider** | **str** | The IdP provider of the connection. | 
**idp_entity_id** | **str** | The Entity ID as provided by the IdP | [optional] 
**idp_sso_url** | **str** | The Single-Sign On URL as provided by the IdP | [optional] 
**idp_certificate** | **str** | The X.509 certificate as provided by the IdP | [optional] 
**idp_metadata_url** | **str** | The URL which serves the IdP metadata. If present, it takes priority over the corresponding individual properties | [optional] 
**idp_metadata** | **str** | The XML content of the IdP metadata file. If present, it takes priority over the corresponding individual properties | [optional] 
**attribute_mapping** | [**CreateSAMLConnectionRequestAttributeMapping**](CreateSAMLConnectionRequestAttributeMapping.md) |  | [optional] 

## Example

```python
from clerk_backend_sdk.models.create_saml_connection_request import CreateSAMLConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSAMLConnectionRequest from a JSON string
create_saml_connection_request_instance = CreateSAMLConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSAMLConnectionRequest.to_json())

# convert the object into a dict
create_saml_connection_request_dict = create_saml_connection_request_instance.to_dict()
# create an instance of CreateSAMLConnectionRequest from a dict
create_saml_connection_request_from_dict = CreateSAMLConnectionRequest.from_dict(create_saml_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


