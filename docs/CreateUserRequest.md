# CreateUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | The ID of the user as used in your external systems or your previous authentication solution. Must be unique across your instance. | [optional] 
**first_name** | **str** | The first name to assign to the user | [optional] 
**last_name** | **str** | The last name to assign to the user | [optional] 
**email_address** | **List[str]** | Email addresses to add to the user. Must be unique across your instance. The first email address will be set as the user&#39;s primary email address. | [optional] 
**phone_number** | **List[str]** | Phone numbers to add to the user. Must be unique across your instance. The first phone number will be set as the user&#39;s primary phone number. | [optional] 
**web3_wallet** | **List[str]** | Web3 wallets to add to the user. Must be unique across your instance. The first wallet will be set as the user&#39;s primary wallet. | [optional] 
**username** | **str** | The username to give to the user. It must be unique across your instance. | [optional] 
**password** | **str** | The plaintext password to give the user. Must be at least 8 characters long, and can not be in any list of hacked passwords. | [optional] 
**password_digest** | **str** | In case you already have the password digests and not the passwords, you can use them for the newly created user via this property. The digests should be generated with one of the supported algorithms. The hashing algorithm can be specified using the &#x60;password_hasher&#x60; property. | [optional] 
**password_hasher** | [**PasswordHasher**](PasswordHasher.md) |  | [optional] 
**skip_password_checks** | **bool** | When set to &#x60;true&#x60; all password checks are skipped. It is recommended to use this method only when migrating plaintext passwords to Clerk. Upon migration the user base should be prompted to pick stronger password. | [optional] 
**skip_password_requirement** | **bool** | When set to &#x60;true&#x60;, &#x60;password&#x60; is not required anymore when creating the user and can be omitted. This is useful when you are trying to create a user that doesn&#39;t have a password, in an instance that is using passwords. Please note that you cannot use this flag if password is the only way for a user to sign into your instance. | [optional] 
**totp_secret** | **str** | In case TOTP is configured on the instance, you can provide the secret to enable it on the newly created user without the need to reset it. Please note that currently the supported options are: * Period: 30 seconds * Code length: 6 digits * Algorithm: SHA1 | [optional] 
**backup_codes** | **List[str]** | If Backup Codes are configured on the instance, you can provide them to enable it on the newly created user without the need to reset them. You must provide the backup codes in plain format or the corresponding bcrypt digest. | [optional] 
**public_metadata** | **object** | Metadata saved on the user, that is visible to both your Frontend and Backend APIs | [optional] 
**private_metadata** | **object** | Metadata saved on the user, that is only visible to your Backend API | [optional] 
**unsafe_metadata** | **object** | Metadata saved on the user, that can be updated from both the Frontend and Backend APIs. Note: Since this data can be modified from the frontend, it is not guaranteed to be safe. | [optional] 
**delete_self_enabled** | **bool** | If enabled, user can delete themselves via FAPI.  | [optional] 
**create_organization_enabled** | **bool** | If enabled, user can create organizations via FAPI.  | [optional] 
**create_organizations_limit** | **int** | The maximum number of organizations the user can create. 0 means unlimited.  | [optional] 
**created_at** | **str** | A custom date/time denoting _when_ the user signed up to the application, specified in RFC3339 format (e.g. &#x60;2012-10-20T07:15:20.902Z&#x60;). | [optional] 

## Example

```python
from clerk_backend_sdk.models.create_user_request import CreateUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserRequest from a JSON string
create_user_request_instance = CreateUserRequest.from_json(json)
# print the JSON string representation of the object
print(CreateUserRequest.to_json())

# convert the object into a dict
create_user_request_dict = create_user_request_instance.to_dict()
# create an instance of CreateUserRequest from a dict
create_user_request_from_dict = CreateUserRequest.from_dict(create_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


