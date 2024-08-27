# CreateSessionTokenFromTemplate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] 
**jwt** | **str** |  | [optional] 

## Example

```python
from clerk_backend_sdk.models.create_session_token_from_template200_response import CreateSessionTokenFromTemplate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSessionTokenFromTemplate200Response from a JSON string
create_session_token_from_template200_response_instance = CreateSessionTokenFromTemplate200Response.from_json(json)
# print the JSON string representation of the object
print(CreateSessionTokenFromTemplate200Response.to_json())

# convert the object into a dict
create_session_token_from_template200_response_dict = create_session_token_from_template200_response_instance.to_dict()
# create an instance of CreateSessionTokenFromTemplate200Response from a dict
create_session_token_from_template200_response_from_dict = CreateSessionTokenFromTemplate200Response.from_dict(create_session_token_from_template200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


