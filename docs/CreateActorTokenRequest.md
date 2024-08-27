# CreateActorTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The ID of the user being impersonated. | 
**actor** | **object** | The actor payload. It needs to include a sub property which should contain the ID of the actor. This whole payload will be also included in the JWT session token. | 
**expires_in_seconds** | **int** | Optional parameter to specify the life duration of the actor token in seconds. By default, the duration is 1 hour. | [optional] [default to 3600]
**session_max_duration_in_seconds** | **int** | The maximum duration that the session which will be created by the generated actor token should last. By default, the duration of a session created via an actor token, lasts 30 minutes. | [optional] [default to 1800]

## Example

```python
from clerk_backend_sdk.models.create_actor_token_request import CreateActorTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateActorTokenRequest from a JSON string
create_actor_token_request_instance = CreateActorTokenRequest.from_json(json)
# print the JSON string representation of the object
print(CreateActorTokenRequest.to_json())

# convert the object into a dict
create_actor_token_request_dict = create_actor_token_request_instance.to_dict()
# create an instance of CreateActorTokenRequest from a dict
create_actor_token_request_from_dict = CreateActorTokenRequest.from_dict(create_actor_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


