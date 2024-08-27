# UpdateUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | The ID of the user as used in your external systems or your previous authentication solution. Must be unique across your instance. | [optional] 
**first_name** | **str** | The first name to assign to the user | [optional] 
**last_name** | **str** | The last name to assign to the user | [optional] 
**primary_email_address_id** | **str** | The ID of the email address to set as primary. It must be verified, and present on the current user. | [optional] 
**notify_primary_email_address_changed** | **bool** | If set to &#x60;true&#x60;, the user will be notified that their primary email address has changed. By default, no notification is sent. | [optional] [default to False]
**primary_phone_number_id** | **str** | The ID of the phone number to set as primary. It must be verified, and present on the current user. | [optional] 
**primary_web3_wallet_id** | **str** | The ID of the web3 wallets to set as primary. It must be verified, and present on the current user. | [optional] 
**username** | **str** | The username to give to the user. It must be unique across your instance. | [optional] 
**profile_image_id** | **str** | The ID of the image to set as the user&#39;s profile image | [optional] 
**password** | **str** | The plaintext password to give the user. Must be at least 8 characters long, and can not be in any list of hacked passwords. | [optional] 
**password_digest** | **str** | In case you already have the password digests and not the passwords, you can use them for the newly created user via this property. The digests should be generated with one of the supported algorithms. The hashing algorithm can be specified using the &#x60;password_hasher&#x60; property. | [optional] 
**password_hasher** | [**PasswordHasher**](PasswordHasher.md) |  | [optional] 
**skip_password_checks** | **bool** | Set it to &#x60;true&#x60; if you&#39;re updating the user&#39;s password and want to skip any password policy settings check. This parameter can only be used when providing a &#x60;password&#x60;. | [optional] 
**sign_out_of_other_sessions** | **bool** | Set to &#x60;true&#x60; to sign out the user from all their active sessions once their password is updated. This parameter can only be used when providing a &#x60;password&#x60;. | [optional] 
**totp_secret** | **str** | In case TOTP is configured on the instance, you can provide the secret to enable it on the specific user without the need to reset it. Please note that currently the supported options are: * Period: 30 seconds * Code length: 6 digits * Algorithm: SHA1 | [optional] 
**backup_codes** | **List[str]** | If Backup Codes are configured on the instance, you can provide them to enable it on the specific user without the need to reset them. You must provide the backup codes in plain format or the corresponding bcrypt digest. | [optional] 
**public_metadata** | **object** | Metadata saved on the user, that is visible to both your Frontend and Backend APIs | [optional] 
**private_metadata** | **object** | Metadata saved on the user, that is only visible to your Backend API | [optional] 
**unsafe_metadata** | **object** | Metadata saved on the user, that can be updated from both the Frontend and Backend APIs. Note: Since this data can be modified from the frontend, it is not guaranteed to be safe. | [optional] 
**delete_self_enabled** | **bool** | If true, the user can delete themselves with the Frontend API. | [optional] 
**create_organization_enabled** | **bool** | If true, the user can create organizations with the Frontend API. | [optional] 
**create_organizations_limit** | **int** | The maximum number of organizations the user can create. 0 means unlimited. | [optional] 
**created_at** | **str** | A custom date/time denoting _when_ the user signed up to the application, specified in RFC3339 format (e.g. &#x60;2012-10-20T07:15:20.902Z&#x60;). | [optional] 

## Example

```python
from clerk_backend_sdk.models.update_user_request import UpdateUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserRequest from a JSON string
update_user_request_instance = UpdateUserRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateUserRequest.to_json())

# convert the object into a dict
update_user_request_dict = update_user_request_instance.to_dict()
# create an instance of UpdateUserRequest from a dict
update_user_request_from_dict = UpdateUserRequest.from_dict(update_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


