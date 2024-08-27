# ActorToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | 
**id** | **str** |  | 
**status** | **str** |  | 
**user_id** | **str** |  | 
**actor** | **object** |  | 
**token** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**created_at** | **int** | Unix timestamp of creation.  | 
**updated_at** | **int** | Unix timestamp of last update.  | 

## Example

```python
from clerk_backend_sdk.models.actor_token import ActorToken

# TODO update the JSON string below
json = "{}"
# create an instance of ActorToken from a JSON string
actor_token_instance = ActorToken.from_json(json)
# print the JSON string representation of the object
print(ActorToken.to_json())

# convert the object into a dict
actor_token_dict = actor_token_instance.to_dict()
# create an instance of ActorToken from a dict
actor_token_from_dict = ActorToken.from_dict(actor_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


