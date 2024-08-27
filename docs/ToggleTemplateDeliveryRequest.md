# ToggleTemplateDeliveryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivered_by_clerk** | **bool** | Whether Clerk should deliver emails or SMS messages based on the current template | [optional] 

## Example

```python
from clerk_backend_sdk.models.toggle_template_delivery_request import ToggleTemplateDeliveryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ToggleTemplateDeliveryRequest from a JSON string
toggle_template_delivery_request_instance = ToggleTemplateDeliveryRequest.from_json(json)
# print the JSON string representation of the object
print(ToggleTemplateDeliveryRequest.to_json())

# convert the object into a dict
toggle_template_delivery_request_dict = toggle_template_delivery_request_instance.to_dict()
# create an instance of ToggleTemplateDeliveryRequest from a dict
toggle_template_delivery_request_from_dict = ToggleTemplateDeliveryRequest.from_dict(toggle_template_delivery_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


