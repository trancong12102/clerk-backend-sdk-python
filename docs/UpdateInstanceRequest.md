# UpdateInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_mode** | **bool** | Toggles test mode for this instance, allowing the use of test email addresses and phone numbers. Defaults to true for development instances. | [optional] 
**hibp** | **bool** | Whether the instance should be using the HIBP service to check passwords for breaches | [optional] 
**enhanced_email_deliverability** | **bool** | The \&quot;enhanced_email_deliverability\&quot; feature will send emails from \&quot;verifications@clerk.dev\&quot; instead of your domain. This can be helpful if you do not have a high domain reputation. | [optional] 
**support_email** | **str** |  | [optional] 
**clerk_js_version** | **str** |  | [optional] 
**development_origin** | **str** |  | [optional] 
**allowed_origins** | **List[str]** | For browser-like stacks such as browser extensions, Electron, or Capacitor.js the instance allowed origins need to be updated with the request origin value. For Chrome extensions popup, background, or service worker pages the origin is chrome-extension://extension_uiid. For Electron apps the default origin is http://localhost:3000. For Capacitor, the origin is capacitor://localhost. | [optional] 
**cookieless_dev** | **bool** | Whether the instance should operate in cookieless development mode (i.e. without third-party cookies). Deprecated: Please use &#x60;url_based_session_syncing&#x60; instead. | [optional] 
**url_based_session_syncing** | **bool** | Whether the instance should use URL-based session syncing in development mode (i.e. without third-party cookies). | [optional] 

## Example

```python
from clerk_backend_sdk.models.update_instance_request import UpdateInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInstanceRequest from a JSON string
update_instance_request_instance = UpdateInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateInstanceRequest.to_json())

# convert the object into a dict
update_instance_request_dict = update_instance_request_instance.to_dict()
# create an instance of UpdateInstanceRequest from a dict
update_instance_request_from_dict = UpdateInstanceRequest.from_dict(update_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


