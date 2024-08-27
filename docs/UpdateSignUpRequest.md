# UpdateSignUpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_action** | **bool** | Specifies whether a custom action has run for this sign-up attempt. This is important when your instance has been configured to require a custom action to run before converting a sign-up into a user. After executing any external business logic you deem necessary, you can mark the sign-up as ready-to-convert by setting &#x60;custom_action&#x60; to &#x60;true&#x60;. | [optional] 
**external_id** | **str** | The ID of the guest attempting to sign up as used in your external systems or your previous authentication solution. This will be copied to the resulting user when the sign-up is completed. | [optional] 

## Example

```python
from clerk_backend_sdk.models.update_sign_up_request import UpdateSignUpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSignUpRequest from a JSON string
update_sign_up_request_instance = UpdateSignUpRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSignUpRequest.to_json())

# convert the object into a dict
update_sign_up_request_dict = update_sign_up_request_instance.to_dict()
# create an instance of UpdateSignUpRequest from a dict
update_sign_up_request_from_dict = UpdateSignUpRequest.from_dict(update_sign_up_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


