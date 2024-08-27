# CreateSignInTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The ID of the user that can use the newly created sign in token | [optional] 
**expires_in_seconds** | **int** | Optional parameter to specify the life duration of the sign in token in seconds. By default, the duration is 30 days. | [optional] [default to 2592000]

## Example

```python
from clerk_backend_sdk.models.create_sign_in_token_request import CreateSignInTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSignInTokenRequest from a JSON string
create_sign_in_token_request_instance = CreateSignInTokenRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSignInTokenRequest.to_json())

# convert the object into a dict
create_sign_in_token_request_dict = create_sign_in_token_request_instance.to_dict()
# create an instance of CreateSignInTokenRequest from a dict
create_sign_in_token_request_from_dict = CreateSignInTokenRequest.from_dict(create_sign_in_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


