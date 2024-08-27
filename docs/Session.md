# Session


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | String representing the object&#39;s type. Objects of the same type share the same value.  | 
**id** | **str** |  | 
**user_id** | **str** |  | 
**client_id** | **str** |  | 
**actor** | **object** |  | [optional] 
**status** | **str** |  | 
**last_active_organization_id** | **str** |  | [optional] 
**last_active_at** | **int** |  | 
**expire_at** | **int** |  | 
**abandon_at** | **int** |  | 
**updated_at** | **int** | Unix timestamp of last update.  | 
**created_at** | **int** | Unix timestamp of creation.  | 

## Example

```python
from clerk_backend_sdk.models.session import Session

# TODO update the JSON string below
json = "{}"
# create an instance of Session from a JSON string
session_instance = Session.from_json(json)
# print the JSON string representation of the object
print(Session.to_json())

# convert the object into a dict
session_dict = session_instance.to_dict()
# create an instance of Session from a dict
session_from_dict = Session.from_dict(session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


