# CreatePhoneNumberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The ID representing the user | [optional] 
**phone_number** | **str** | The new phone number. Must adhere to the E.164 standard for phone number format. | [optional] 
**verified** | **bool** | When created, the phone number will be marked as verified. | [optional] 
**primary** | **bool** | Create this phone number as the primary phone number for the user. Default: false, unless it is the first phone number. | [optional] 
**reserved_for_second_factor** | **bool** | Create this phone number as reserved for multi-factor authentication. The phone number must also be verified. If there are no other reserved second factors, the phone number will be set as the default second factor. | [optional] 

## Example

```python
from clerk_backend_sdk.models.create_phone_number_request import CreatePhoneNumberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePhoneNumberRequest from a JSON string
create_phone_number_request_instance = CreatePhoneNumberRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePhoneNumberRequest.to_json())

# convert the object into a dict
create_phone_number_request_dict = create_phone_number_request_instance.to_dict()
# create an instance of CreatePhoneNumberRequest from a dict
create_phone_number_request_from_dict = CreatePhoneNumberRequest.from_dict(create_phone_number_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


