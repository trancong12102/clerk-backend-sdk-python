# UpdateOAuthApplicationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new name of the OAuth application | [optional] 
**callback_url** | **str** | The new callback URL of the OAuth application | [optional] 
**scopes** | **str** | Define the allowed scopes for the new OAuth applications that dictate the user payload of the OAuth user info endpoint. Available scopes are &#x60;profile&#x60;, &#x60;email&#x60;, &#x60;public_metadata&#x60;, &#x60;private_metadata&#x60;. Provide the requested scopes as a string, separated by spaces. | [optional] [default to 'profile email']

## Example

```python
from clerk_backend_sdk.models.update_o_auth_application_request import UpdateOAuthApplicationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOAuthApplicationRequest from a JSON string
update_o_auth_application_request_instance = UpdateOAuthApplicationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateOAuthApplicationRequest.to_json())

# convert the object into a dict
update_o_auth_application_request_dict = update_o_auth_application_request_instance.to_dict()
# create an instance of UpdateOAuthApplicationRequest from a dict
update_o_auth_application_request_from_dict = UpdateOAuthApplicationRequest.from_dict(update_o_auth_application_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


