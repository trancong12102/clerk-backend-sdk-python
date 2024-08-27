# CreateEmailAddressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The ID representing the user | [optional] 
**email_address** | **str** | The new email address. Must adhere to the RFC 5322 specification for email address format. | [optional] 
**verified** | **bool** | When created, the email address will be marked as verified. | [optional] 
**primary** | **bool** | Create this email address as the primary email address for the user. Default: false, unless it is the first email address. | [optional] 

## Example

```python
from clerk_backend_sdk.models.create_email_address_request import CreateEmailAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEmailAddressRequest from a JSON string
create_email_address_request_instance = CreateEmailAddressRequest.from_json(json)
# print the JSON string representation of the object
print(CreateEmailAddressRequest.to_json())

# convert the object into a dict
create_email_address_request_dict = create_email_address_request_instance.to_dict()
# create an instance of CreateEmailAddressRequest from a dict
create_email_address_request_from_dict = CreateEmailAddressRequest.from_dict(create_email_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


