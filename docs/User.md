# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**object** | **str** | String representing the object&#39;s type. Objects of the same type share the same value.  | [optional] 
**external_id** | **str** |  | [optional] 
**primary_email_address_id** | **str** |  | [optional] 
**primary_phone_number_id** | **str** |  | [optional] 
**primary_web3_wallet_id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**profile_image_url** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**has_image** | **bool** |  | [optional] 
**public_metadata** | **object** |  | [optional] 
**private_metadata** | **object** |  | [optional] 
**unsafe_metadata** | **object** |  | [optional] 
**email_addresses** | [**List[EmailAddress]**](EmailAddress.md) |  | [optional] 
**phone_numbers** | [**List[PhoneNumber]**](PhoneNumber.md) |  | [optional] 
**web3_wallets** | [**List[Web3Wallet]**](Web3Wallet.md) |  | [optional] 
**passkeys** | [**List[SchemasPasskey]**](SchemasPasskey.md) |  | [optional] 
**password_enabled** | **bool** |  | [optional] 
**two_factor_enabled** | **bool** |  | [optional] 
**totp_enabled** | **bool** |  | [optional] 
**backup_code_enabled** | **bool** |  | [optional] 
**mfa_enabled_at** | **int** | Unix timestamp of when MFA was last enabled for this user. It should be noted that this field is not nullified if MFA is disabled.  | [optional] 
**mfa_disabled_at** | **int** | Unix timestamp of when MFA was last disabled for this user. It should be noted that this field is not nullified if MFA is enabled again.  | [optional] 
**external_accounts** | **List[object]** |  | [optional] 
**saml_accounts** | [**List[SAMLAccount]**](SAMLAccount.md) |  | [optional] 
**last_sign_in_at** | **int** | Unix timestamp of last sign-in.  | [optional] 
**banned** | **bool** | Flag to denote whether user is banned or not.  | [optional] 
**locked** | **bool** | Flag to denote whether user is currently locked, i.e. restricted from signing in or not.  | [optional] 
**lockout_expires_in_seconds** | **int** | The number of seconds remaining until the lockout period expires for a locked user. A null value for a locked user indicates that lockout never expires.  | [optional] 
**verification_attempts_remaining** | **int** | The number of verification attempts remaining until the user is locked. Null if account lockout is not enabled. Note: if a user is locked explicitly via the Backend API, they may still have verification attempts remaining.  | [optional] 
**updated_at** | **int** | Unix timestamp of last update.  | [optional] 
**created_at** | **int** | Unix timestamp of creation.  | [optional] 
**delete_self_enabled** | **bool** | If enabled, user can delete themselves via FAPI.  | [optional] 
**create_organization_enabled** | **bool** | If enabled, user can create organizations via FAPI.  | [optional] 
**create_organizations_limit** | **int** | The maximum number of organizations the user can create. 0 means unlimited.  | [optional] 
**last_active_at** | **int** | Unix timestamp of the latest session activity, with day precision.  | [optional] 

## Example

```python
from clerk_backend_sdk.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


