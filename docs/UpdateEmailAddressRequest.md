# UpdateEmailAddressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verified** | **bool** | The email address will be marked as verified. | [optional] 
**primary** | **bool** | Set this email address as the primary email address for the user. | [optional] 

## Example

```python
from clerk_backend_sdk.models.update_email_address_request import UpdateEmailAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEmailAddressRequest from a JSON string
update_email_address_request_instance = UpdateEmailAddressRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateEmailAddressRequest.to_json())

# convert the object into a dict
update_email_address_request_dict = update_email_address_request_instance.to_dict()
# create an instance of UpdateEmailAddressRequest from a dict
update_email_address_request_from_dict = UpdateEmailAddressRequest.from_dict(update_email_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


