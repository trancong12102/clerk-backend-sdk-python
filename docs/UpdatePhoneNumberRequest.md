# UpdatePhoneNumberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verified** | **bool** | The phone number will be marked as verified. | [optional] 
**primary** | **bool** | Set this phone number as the primary phone number for the user. | [optional] 
**reserved_for_second_factor** | **bool** | Set this phone number as reserved for multi-factor authentication. The phone number must also be verified. If there are no other reserved second factors, the phone number will be set as the default second factor. | [optional] 

## Example

```python
from clerk_backend_sdk.models.update_phone_number_request import UpdatePhoneNumberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePhoneNumberRequest from a JSON string
update_phone_number_request_instance = UpdatePhoneNumberRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePhoneNumberRequest.to_json())

# convert the object into a dict
update_phone_number_request_dict = update_phone_number_request_instance.to_dict()
# create an instance of UpdatePhoneNumberRequest from a dict
update_phone_number_request_from_dict = UpdatePhoneNumberRequest.from_dict(update_phone_number_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


