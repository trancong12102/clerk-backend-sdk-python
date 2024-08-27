# UpsertTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The user-friendly name of the template | [optional] 
**subject** | **str** | The email subject. Applicable only to email templates. | [optional] 
**markup** | **str** | The editor markup used to generate the body of the template | [optional] 
**body** | **str** | The template body before variable interpolation | [optional] 
**delivered_by_clerk** | **bool** | Whether Clerk should deliver emails or SMS messages based on the current template | [optional] 
**from_email_name** | **str** | The local part of the From email address that will be used for emails. For example, in the address &#39;hello@example.com&#39;, the local part is &#39;hello&#39;. Applicable only to email templates. | [optional] 
**reply_to_email_name** | **str** | The local part of the Reply To email address that will be used for emails. For example, in the address &#39;hello@example.com&#39;, the local part is &#39;hello&#39;. Applicable only to email templates. | [optional] 

## Example

```python
from clerk_backend_sdk.models.upsert_template_request import UpsertTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertTemplateRequest from a JSON string
upsert_template_request_instance = UpsertTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(UpsertTemplateRequest.to_json())

# convert the object into a dict
upsert_template_request_dict = upsert_template_request_instance.to_dict()
# create an instance of UpsertTemplateRequest from a dict
upsert_template_request_from_dict = UpsertTemplateRequest.from_dict(upsert_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


