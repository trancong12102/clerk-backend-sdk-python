# UpdateInstanceAuthConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**restricted_to_allowlist** | **bool** | Whether sign up is restricted to email addresses, phone numbers and usernames that are on the allowlist. | [optional] [default to False]
**from_email_address** | **str** | The local part of the email address from which authentication-related emails (e.g. OTP code, magic links) will be sent. Only alphanumeric values are allowed. Note that this value should contain only the local part of the address (e.g. &#x60;foo&#x60; for &#x60;foo@example.com&#x60;). | [optional] 
**progressive_sign_up** | **bool** | Enable the Progressive Sign Up algorithm. Refer to the [docs](https://clerk.com/docs/upgrade-guides/progressive-sign-up) for more info. | [optional] 
**session_token_template** | **str** | The name of the JWT Template used to augment your session tokens. To disable this, pass an empty string. | [optional] 
**enhanced_email_deliverability** | **bool** | The \&quot;enhanced_email_deliverability\&quot; feature will send emails from \&quot;verifications@clerk.dev\&quot; instead of your domain. This can be helpful if you do not have a high domain reputation. | [optional] 
**test_mode** | **bool** | Toggles test mode for this instance, allowing the use of test email addresses and phone numbers. Defaults to true for development instances. | [optional] 

## Example

```python
from clerk_backend_sdk.models.update_instance_auth_config_request import UpdateInstanceAuthConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInstanceAuthConfigRequest from a JSON string
update_instance_auth_config_request_instance = UpdateInstanceAuthConfigRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateInstanceAuthConfigRequest.to_json())

# convert the object into a dict
update_instance_auth_config_request_dict = update_instance_auth_config_request_instance.to_dict()
# create an instance of UpdateInstanceAuthConfigRequest from a dict
update_instance_auth_config_request_from_dict = UpdateInstanceAuthConfigRequest.from_dict(update_instance_auth_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


