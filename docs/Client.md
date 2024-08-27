# Client


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | String representing the object&#39;s type. Objects of the same type share the same value.  | 
**id** | **str** | String representing the identifier of the session.  | 
**session_ids** | **List[str]** |  | 
**sessions** | [**List[Session]**](Session.md) |  | 
**sign_in_id** | **str** |  | 
**sign_up_id** | **str** |  | 
**last_active_session_id** | **str** | Last active session_id.  | 
**updated_at** | **int** | Unix timestamp of last update.  | 
**created_at** | **int** | Unix timestamp of creation.  | 

## Example

```python
from clerk_backend_sdk.models.client import Client

# TODO update the JSON string below
json = "{}"
# create an instance of Client from a JSON string
client_instance = Client.from_json(json)
# print the JSON string representation of the object
print(Client.to_json())

# convert the object into a dict
client_dict = client_instance.to_dict()
# create an instance of Client from a dict
client_from_dict = Client.from_dict(client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


