# SAMLConnections


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SAMLConnection]**](SAMLConnection.md) |  | 
**total_count** | **int** | Total number of SAML Connections  | 

## Example

```python
from clerk_backend_sdk.models.saml_connections import SAMLConnections

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLConnections from a JSON string
saml_connections_instance = SAMLConnections.from_json(json)
# print the JSON string representation of the object
print(SAMLConnections.to_json())

# convert the object into a dict
saml_connections_dict = saml_connections_instance.to_dict()
# create an instance of SAMLConnections from a dict
saml_connections_from_dict = SAMLConnections.from_dict(saml_connections_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


