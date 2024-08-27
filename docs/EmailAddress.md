# EmailAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**object** | **str** | String representing the object&#39;s type. Objects of the same type share the same value.  | 
**email_address** | **str** |  | 
**reserved** | **bool** |  | 
**verification** | [**EmailAddressVerification**](EmailAddressVerification.md) |  | 
**linked_to** | [**List[IdentificationLink]**](IdentificationLink.md) |  | 
**created_at** | **int** | Unix timestamp of creation  | 
**updated_at** | **int** | Unix timestamp of creation  | 

## Example

```python
from clerk_backend_sdk.models.email_address import EmailAddress

# TODO update the JSON string below
json = "{}"
# create an instance of EmailAddress from a JSON string
email_address_instance = EmailAddress.from_json(json)
# print the JSON string representation of the object
print(EmailAddress.to_json())

# convert the object into a dict
email_address_dict = email_address_instance.to_dict()
# create an instance of EmailAddress from a dict
email_address_from_dict = EmailAddress.from_dict(email_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


