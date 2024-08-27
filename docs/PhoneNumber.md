# PhoneNumber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**object** | **str** | String representing the object&#39;s type. Objects of the same type share the same value.  | 
**phone_number** | **str** |  | 
**reserved_for_second_factor** | **bool** |  | [optional] 
**default_second_factor** | **bool** |  | [optional] 
**reserved** | **bool** |  | 
**verification** | [**PhoneNumberVerification**](PhoneNumberVerification.md) |  | 
**linked_to** | [**List[IdentificationLink]**](IdentificationLink.md) |  | 
**backup_codes** | **List[str]** |  | [optional] 
**created_at** | **int** | Unix timestamp of creation  | 
**updated_at** | **int** | Unix timestamp of creation  | 

## Example

```python
from clerk_backend_sdk.models.phone_number import PhoneNumber

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneNumber from a JSON string
phone_number_instance = PhoneNumber.from_json(json)
# print the JSON string representation of the object
print(PhoneNumber.to_json())

# convert the object into a dict
phone_number_dict = phone_number_instance.to_dict()
# create an instance of PhoneNumber from a dict
phone_number_from_dict = PhoneNumber.from_dict(phone_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


