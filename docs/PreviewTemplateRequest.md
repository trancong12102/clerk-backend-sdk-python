# PreviewTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | The email subject. Applicable only to email templates. | [optional] 
**body** | **str** | The template body before variable interpolation | [optional] 
**from_email_name** | **str** | The local part of the From email address that will be used for emails. For example, in the address &#39;hello@example.com&#39;, the local part is &#39;hello&#39;. Applicable only to email templates. | [optional] 
**reply_to_email_name** | **str** | The local part of the Reply To email address that will be used for emails. For example, in the address &#39;hello@example.com&#39;, the local part is &#39;hello&#39;. Applicable only to email templates. | [optional] 

## Example

```python
from clerk_backend_sdk.models.preview_template_request import PreviewTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewTemplateRequest from a JSON string
preview_template_request_instance = PreviewTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(PreviewTemplateRequest.to_json())

# convert the object into a dict
preview_template_request_dict = preview_template_request_instance.to_dict()
# create an instance of PreviewTemplateRequest from a dict
preview_template_request_from_dict = PreviewTemplateRequest.from_dict(preview_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


