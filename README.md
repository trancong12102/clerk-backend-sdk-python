# clerk-backend-sdk
The Clerk REST Backend API, meant to be accessed by backend
servers.

### Versions

When the API changes in a way that isn't compatible with older versions, a new version is released.
Each version is identified by its release date, e.g. `2021-02-05`. For more information, please see [Clerk API Versions](https://clerk.com/docs/backend-requests/versioning/overview).


Please see https://clerk.com/docs for more information.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.0.0
- Generator version: 7.8.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://clerk.com/support](https://clerk.com/support)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import clerk_backend_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import clerk_backend_sdk
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import clerk_backend_sdk
from clerk_backend_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.clerk.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = clerk_backend_sdk.Configuration(
    host = "https://api.clerk.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (sk_<environment>_<secret value>): bearerAuth
configuration = clerk_backend_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
async with clerk_backend_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clerk_backend_sdk.ActorTokensApi(api_client)
    create_actor_token_request = clerk_backend_sdk.CreateActorTokenRequest() # CreateActorTokenRequest |  (optional)

    try:
        # Create actor token
        api_response = await api_instance.create_actor_token(create_actor_token_request=create_actor_token_request)
        print("The response of ActorTokensApi->create_actor_token:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ActorTokensApi->create_actor_token: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.clerk.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ActorTokensApi* | [**create_actor_token**](docs/ActorTokensApi.md#create_actor_token) | **POST** /actor_tokens | Create actor token
*ActorTokensApi* | [**revoke_actor_token**](docs/ActorTokensApi.md#revoke_actor_token) | **POST** /actor_tokens/{actor_token_id}/revoke | Revoke actor token
*AllowListBlockListApi* | [**create_allowlist_identifier**](docs/AllowListBlockListApi.md#create_allowlist_identifier) | **POST** /allowlist_identifiers | Add identifier to the allow-list
*AllowListBlockListApi* | [**create_blocklist_identifier**](docs/AllowListBlockListApi.md#create_blocklist_identifier) | **POST** /blocklist_identifiers | Add identifier to the block-list
*AllowListBlockListApi* | [**delete_allowlist_identifier**](docs/AllowListBlockListApi.md#delete_allowlist_identifier) | **DELETE** /allowlist_identifiers/{identifier_id} | Delete identifier from allow-list
*AllowListBlockListApi* | [**delete_blocklist_identifier**](docs/AllowListBlockListApi.md#delete_blocklist_identifier) | **DELETE** /blocklist_identifiers/{identifier_id} | Delete identifier from block-list
*AllowListBlockListApi* | [**list_allowlist_identifiers**](docs/AllowListBlockListApi.md#list_allowlist_identifiers) | **GET** /allowlist_identifiers | List all identifiers on the allow-list
*AllowListBlockListApi* | [**list_blocklist_identifiers**](docs/AllowListBlockListApi.md#list_blocklist_identifiers) | **GET** /blocklist_identifiers | List all identifiers on the block-list
*BetaFeaturesApi* | [**change_production_instance_domain**](docs/BetaFeaturesApi.md#change_production_instance_domain) | **POST** /instance/change_domain | Update production instance domain
*BetaFeaturesApi* | [**update_instance_auth_config**](docs/BetaFeaturesApi.md#update_instance_auth_config) | **PATCH** /beta_features/instance_settings | Update instance settings
*BetaFeaturesApi* | [**update_production_instance_domain**](docs/BetaFeaturesApi.md#update_production_instance_domain) | **PUT** /beta_features/domain | Update production instance domain
*ClientsApi* | [**get_client**](docs/ClientsApi.md#get_client) | **GET** /clients/{client_id} | Get a client
*ClientsApi* | [**get_client_list**](docs/ClientsApi.md#get_client_list) | **GET** /clients | List all clients
*ClientsApi* | [**verify_client**](docs/ClientsApi.md#verify_client) | **POST** /clients/verify | Verify a client
*DomainsApi* | [**add_domain**](docs/DomainsApi.md#add_domain) | **POST** /domains | Add a domain
*DomainsApi* | [**delete_domain**](docs/DomainsApi.md#delete_domain) | **DELETE** /domains/{domain_id} | Delete a satellite domain
*DomainsApi* | [**list_domains**](docs/DomainsApi.md#list_domains) | **GET** /domains | List all instance domains
*DomainsApi* | [**update_domain**](docs/DomainsApi.md#update_domain) | **PATCH** /domains/{domain_id} | Update a domain
*EmailAddressesApi* | [**create_email_address**](docs/EmailAddressesApi.md#create_email_address) | **POST** /email_addresses | Create an email address
*EmailAddressesApi* | [**delete_email_address**](docs/EmailAddressesApi.md#delete_email_address) | **DELETE** /email_addresses/{email_address_id} | Delete an email address
*EmailAddressesApi* | [**get_email_address**](docs/EmailAddressesApi.md#get_email_address) | **GET** /email_addresses/{email_address_id} | Retrieve an email address
*EmailAddressesApi* | [**update_email_address**](docs/EmailAddressesApi.md#update_email_address) | **PATCH** /email_addresses/{email_address_id} | Update an email address
*EmailSMSTemplatesApi* | [**get_template**](docs/EmailSMSTemplatesApi.md#get_template) | **GET** /templates/{template_type}/{slug} | Retrieve a template
*EmailSMSTemplatesApi* | [**get_template_list**](docs/EmailSMSTemplatesApi.md#get_template_list) | **GET** /templates/{template_type} | List all templates
*EmailSMSTemplatesApi* | [**preview_template**](docs/EmailSMSTemplatesApi.md#preview_template) | **POST** /templates/{template_type}/{slug}/preview | Preview changes to a template
*EmailSMSTemplatesApi* | [**revert_template**](docs/EmailSMSTemplatesApi.md#revert_template) | **POST** /templates/{template_type}/{slug}/revert | Revert a template
*EmailSMSTemplatesApi* | [**toggle_template_delivery**](docs/EmailSMSTemplatesApi.md#toggle_template_delivery) | **POST** /templates/{template_type}/{slug}/toggle_delivery | Toggle the delivery by Clerk for a template of a given type and slug
*EmailSMSTemplatesApi* | [**upsert_template**](docs/EmailSMSTemplatesApi.md#upsert_template) | **PUT** /templates/{template_type}/{slug} | Update a template for a given type and slug
*InstanceSettingsApi* | [**update_instance**](docs/InstanceSettingsApi.md#update_instance) | **PATCH** /instance | Update instance settings
*InstanceSettingsApi* | [**update_instance_organization_settings**](docs/InstanceSettingsApi.md#update_instance_organization_settings) | **PATCH** /instance/organization_settings | Update instance organization settings
*InstanceSettingsApi* | [**update_instance_restrictions**](docs/InstanceSettingsApi.md#update_instance_restrictions) | **PATCH** /instance/restrictions | Update instance restrictions
*InvitationsApi* | [**create_invitation**](docs/InvitationsApi.md#create_invitation) | **POST** /invitations | Create an invitation
*InvitationsApi* | [**list_invitations**](docs/InvitationsApi.md#list_invitations) | **GET** /invitations | List all invitations
*InvitationsApi* | [**revoke_invitation**](docs/InvitationsApi.md#revoke_invitation) | **POST** /invitations/{invitation_id}/revoke | Revokes an invitation
*JWKSApi* | [**get_jwks**](docs/JWKSApi.md#get_jwks) | **GET** /jwks | Retrieve the JSON Web Key Set of the instance
*JWTTemplatesApi* | [**create_jwt_template**](docs/JWTTemplatesApi.md#create_jwt_template) | **POST** /jwt_templates | Create a JWT template
*JWTTemplatesApi* | [**delete_jwt_template**](docs/JWTTemplatesApi.md#delete_jwt_template) | **DELETE** /jwt_templates/{template_id} | Delete a Template
*JWTTemplatesApi* | [**get_jwt_template**](docs/JWTTemplatesApi.md#get_jwt_template) | **GET** /jwt_templates/{template_id} | Retrieve a template
*JWTTemplatesApi* | [**list_jwt_templates**](docs/JWTTemplatesApi.md#list_jwt_templates) | **GET** /jwt_templates | List all templates
*JWTTemplatesApi* | [**update_jwt_template**](docs/JWTTemplatesApi.md#update_jwt_template) | **PATCH** /jwt_templates/{template_id} | Update a JWT template
*MiscellaneousApi* | [**get_public_interstitial**](docs/MiscellaneousApi.md#get_public_interstitial) | **GET** /public/interstitial | Returns the markup for the interstitial page
*OAuthApplicationsApi* | [**create_o_auth_application**](docs/OAuthApplicationsApi.md#create_o_auth_application) | **POST** /oauth_applications | Create an OAuth application
*OAuthApplicationsApi* | [**delete_o_auth_application**](docs/OAuthApplicationsApi.md#delete_o_auth_application) | **DELETE** /oauth_applications/{oauth_application_id} | Delete an OAuth application
*OAuthApplicationsApi* | [**get_o_auth_application**](docs/OAuthApplicationsApi.md#get_o_auth_application) | **GET** /oauth_applications/{oauth_application_id} | Retrieve an OAuth application by ID
*OAuthApplicationsApi* | [**list_o_auth_applications**](docs/OAuthApplicationsApi.md#list_o_auth_applications) | **GET** /oauth_applications | Get a list of OAuth applications for an instance
*OAuthApplicationsApi* | [**rotate_o_auth_application_secret**](docs/OAuthApplicationsApi.md#rotate_o_auth_application_secret) | **POST** /oauth_applications/{oauth_application_id}/rotate_secret | Rotate the client secret of the given OAuth application
*OAuthApplicationsApi* | [**update_o_auth_application**](docs/OAuthApplicationsApi.md#update_o_auth_application) | **PATCH** /oauth_applications/{oauth_application_id} | Update an OAuth application
*OrganizationInvitationsApi* | [**create_organization_invitation**](docs/OrganizationInvitationsApi.md#create_organization_invitation) | **POST** /organizations/{organization_id}/invitations | Create and send an organization invitation
*OrganizationInvitationsApi* | [**create_organization_invitation_bulk**](docs/OrganizationInvitationsApi.md#create_organization_invitation_bulk) | **POST** /organizations/{organization_id}/invitations/bulk | Bulk create and send organization invitations
*OrganizationInvitationsApi* | [**get_organization_invitation**](docs/OrganizationInvitationsApi.md#get_organization_invitation) | **GET** /organizations/{organization_id}/invitations/{invitation_id} | Retrieve an organization invitation by ID
*OrganizationInvitationsApi* | [**list_organization_invitations**](docs/OrganizationInvitationsApi.md#list_organization_invitations) | **GET** /organizations/{organization_id}/invitations | Get a list of organization invitations
*OrganizationInvitationsApi* | [**list_pending_organization_invitations**](docs/OrganizationInvitationsApi.md#list_pending_organization_invitations) | **GET** /organizations/{organization_id}/invitations/pending | Get a list of pending organization invitations
*OrganizationInvitationsApi* | [**revoke_organization_invitation**](docs/OrganizationInvitationsApi.md#revoke_organization_invitation) | **POST** /organizations/{organization_id}/invitations/{invitation_id}/revoke | Revoke a pending organization invitation
*OrganizationMembershipsApi* | [**create_organization_membership**](docs/OrganizationMembershipsApi.md#create_organization_membership) | **POST** /organizations/{organization_id}/memberships | Create a new organization membership
*OrganizationMembershipsApi* | [**delete_organization_membership**](docs/OrganizationMembershipsApi.md#delete_organization_membership) | **DELETE** /organizations/{organization_id}/memberships/{user_id} | Remove a member from an organization
*OrganizationMembershipsApi* | [**list_organization_memberships**](docs/OrganizationMembershipsApi.md#list_organization_memberships) | **GET** /organizations/{organization_id}/memberships | Get a list of all members of an organization
*OrganizationMembershipsApi* | [**update_organization_membership**](docs/OrganizationMembershipsApi.md#update_organization_membership) | **PATCH** /organizations/{organization_id}/memberships/{user_id} | Update an organization membership
*OrganizationMembershipsApi* | [**update_organization_membership_metadata**](docs/OrganizationMembershipsApi.md#update_organization_membership_metadata) | **PATCH** /organizations/{organization_id}/memberships/{user_id}/metadata | Merge and update organization membership metadata
*OrganizationsApi* | [**create_organization**](docs/OrganizationsApi.md#create_organization) | **POST** /organizations | Create an organization
*OrganizationsApi* | [**delete_organization**](docs/OrganizationsApi.md#delete_organization) | **DELETE** /organizations/{organization_id} | Delete an organization
*OrganizationsApi* | [**delete_organization_logo**](docs/OrganizationsApi.md#delete_organization_logo) | **DELETE** /organizations/{organization_id}/logo | 
*OrganizationsApi* | [**get_organization**](docs/OrganizationsApi.md#get_organization) | **GET** /organizations/{organization_id} | Retrieve an organization by ID or slug
*OrganizationsApi* | [**list_organizations**](docs/OrganizationsApi.md#list_organizations) | **GET** /organizations | Get a list of organizations for an instance
*OrganizationsApi* | [**merge_organization_metadata**](docs/OrganizationsApi.md#merge_organization_metadata) | **PATCH** /organizations/{organization_id}/metadata | Merge and update metadata for an organization
*OrganizationsApi* | [**update_organization**](docs/OrganizationsApi.md#update_organization) | **PATCH** /organizations/{organization_id} | Update an organization
*OrganizationsApi* | [**upload_organization_logo**](docs/OrganizationsApi.md#upload_organization_logo) | **PUT** /organizations/{organization_id}/logo | Upload a logo for the organization
*PhoneNumbersApi* | [**create_phone_number**](docs/PhoneNumbersApi.md#create_phone_number) | **POST** /phone_numbers | Create a phone number
*PhoneNumbersApi* | [**delete_phone_number**](docs/PhoneNumbersApi.md#delete_phone_number) | **DELETE** /phone_numbers/{phone_number_id} | Delete a phone number
*PhoneNumbersApi* | [**get_phone_number**](docs/PhoneNumbersApi.md#get_phone_number) | **GET** /phone_numbers/{phone_number_id} | Retrieve a phone number
*PhoneNumbersApi* | [**update_phone_number**](docs/PhoneNumbersApi.md#update_phone_number) | **PATCH** /phone_numbers/{phone_number_id} | Update a phone number
*ProxyChecksApi* | [**verify_domain_proxy**](docs/ProxyChecksApi.md#verify_domain_proxy) | **POST** /proxy_checks | Verify the proxy configuration for your domain
*RedirectURLsApi* | [**create_redirect_url**](docs/RedirectURLsApi.md#create_redirect_url) | **POST** /redirect_urls | Create a redirect URL
*RedirectURLsApi* | [**delete_redirect_url**](docs/RedirectURLsApi.md#delete_redirect_url) | **DELETE** /redirect_urls/{id} | Delete a redirect URL
*RedirectURLsApi* | [**get_redirect_url**](docs/RedirectURLsApi.md#get_redirect_url) | **GET** /redirect_urls/{id} | Retrieve a redirect URL
*RedirectURLsApi* | [**list_redirect_urls**](docs/RedirectURLsApi.md#list_redirect_urls) | **GET** /redirect_urls | List all redirect URLs
*SAMLConnectionsApi* | [**create_saml_connection**](docs/SAMLConnectionsApi.md#create_saml_connection) | **POST** /saml_connections | Create a SAML Connection
*SAMLConnectionsApi* | [**delete_saml_connection**](docs/SAMLConnectionsApi.md#delete_saml_connection) | **DELETE** /saml_connections/{saml_connection_id} | Delete a SAML Connection
*SAMLConnectionsApi* | [**get_saml_connection**](docs/SAMLConnectionsApi.md#get_saml_connection) | **GET** /saml_connections/{saml_connection_id} | Retrieve a SAML Connection by ID
*SAMLConnectionsApi* | [**list_saml_connections**](docs/SAMLConnectionsApi.md#list_saml_connections) | **GET** /saml_connections | Get a list of SAML Connections for an instance
*SAMLConnectionsApi* | [**update_saml_connection**](docs/SAMLConnectionsApi.md#update_saml_connection) | **PATCH** /saml_connections/{saml_connection_id} | Update a SAML Connection
*SessionsApi* | [**create_session_token_from_template**](docs/SessionsApi.md#create_session_token_from_template) | **POST** /sessions/{session_id}/tokens/{template_name} | Create a session token from a jwt template
*SessionsApi* | [**get_session**](docs/SessionsApi.md#get_session) | **GET** /sessions/{session_id} | Retrieve a session
*SessionsApi* | [**get_session_list**](docs/SessionsApi.md#get_session_list) | **GET** /sessions | List all sessions
*SessionsApi* | [**revoke_session**](docs/SessionsApi.md#revoke_session) | **POST** /sessions/{session_id}/revoke | Revoke a session
*SessionsApi* | [**verify_session**](docs/SessionsApi.md#verify_session) | **POST** /sessions/{session_id}/verify | Verify a session
*SignInTokensApi* | [**create_sign_in_token**](docs/SignInTokensApi.md#create_sign_in_token) | **POST** /sign_in_tokens | Create sign-in token
*SignInTokensApi* | [**revoke_sign_in_token**](docs/SignInTokensApi.md#revoke_sign_in_token) | **POST** /sign_in_tokens/{sign_in_token_id}/revoke | Revoke the given sign-in token
*SignUpsApi* | [**update_sign_up**](docs/SignUpsApi.md#update_sign_up) | **PATCH** /sign_ups/{id} | Update a sign-up
*TestingTokensApi* | [**create_testing_token**](docs/TestingTokensApi.md#create_testing_token) | **POST** /testing_tokens | Retrieve a new testing token
*UsersApi* | [**ban_user**](docs/UsersApi.md#ban_user) | **POST** /users/{user_id}/ban | Ban a user
*UsersApi* | [**create_user**](docs/UsersApi.md#create_user) | **POST** /users | Create a new user
*UsersApi* | [**delete_user**](docs/UsersApi.md#delete_user) | **DELETE** /users/{user_id} | Delete a user
*UsersApi* | [**delete_user_profile_image**](docs/UsersApi.md#delete_user_profile_image) | **DELETE** /users/{user_id}/profile_image | Delete user profile image
*UsersApi* | [**disable_mfa**](docs/UsersApi.md#disable_mfa) | **DELETE** /users/{user_id}/mfa | Disable a user&#39;s MFA methods
*UsersApi* | [**get_o_auth_access_token**](docs/UsersApi.md#get_o_auth_access_token) | **GET** /users/{user_id}/oauth_access_tokens/{provider} | Retrieve the OAuth access token of a user
*UsersApi* | [**get_user**](docs/UsersApi.md#get_user) | **GET** /users/{user_id} | Retrieve a user
*UsersApi* | [**get_user_list**](docs/UsersApi.md#get_user_list) | **GET** /users | List all users
*UsersApi* | [**get_users_count**](docs/UsersApi.md#get_users_count) | **GET** /users/count | Count users
*UsersApi* | [**lock_user**](docs/UsersApi.md#lock_user) | **POST** /users/{user_id}/lock | Lock a user
*UsersApi* | [**set_user_profile_image**](docs/UsersApi.md#set_user_profile_image) | **POST** /users/{user_id}/profile_image | Set user profile image
*UsersApi* | [**unban_user**](docs/UsersApi.md#unban_user) | **POST** /users/{user_id}/unban | Unban a user
*UsersApi* | [**unlock_user**](docs/UsersApi.md#unlock_user) | **POST** /users/{user_id}/unlock | Unlock a user
*UsersApi* | [**update_user**](docs/UsersApi.md#update_user) | **PATCH** /users/{user_id} | Update a user
*UsersApi* | [**update_user_metadata**](docs/UsersApi.md#update_user_metadata) | **PATCH** /users/{user_id}/metadata | Merge and update a user&#39;s metadata
*UsersApi* | [**users_get_organization_memberships**](docs/UsersApi.md#users_get_organization_memberships) | **GET** /users/{user_id}/organization_memberships | Retrieve all memberships for a user
*UsersApi* | [**verify_password**](docs/UsersApi.md#verify_password) | **POST** /users/{user_id}/verify_password | Verify the password of a user
*UsersApi* | [**verify_totp**](docs/UsersApi.md#verify_totp) | **POST** /users/{user_id}/verify_totp | Verify a TOTP or backup code for a user
*WebhooksApi* | [**create_svix_app**](docs/WebhooksApi.md#create_svix_app) | **POST** /webhooks/svix | Create a Svix app
*WebhooksApi* | [**delete_svix_app**](docs/WebhooksApi.md#delete_svix_app) | **DELETE** /webhooks/svix | Delete a Svix app
*WebhooksApi* | [**generate_svix_auth_url**](docs/WebhooksApi.md#generate_svix_auth_url) | **POST** /webhooks/svix_url | Create a Svix Dashboard URL


## Documentation For Models

 - [ActorToken](docs/ActorToken.md)
 - [AddDomainRequest](docs/AddDomainRequest.md)
 - [Admin](docs/Admin.md)
 - [AllowlistIdentifier](docs/AllowlistIdentifier.md)
 - [BlocklistIdentifier](docs/BlocklistIdentifier.md)
 - [BlocklistIdentifiers](docs/BlocklistIdentifiers.md)
 - [CNameTarget](docs/CNameTarget.md)
 - [ChangeProductionInstanceDomainRequest](docs/ChangeProductionInstanceDomainRequest.md)
 - [ClerkError](docs/ClerkError.md)
 - [ClerkErrors](docs/ClerkErrors.md)
 - [Client](docs/Client.md)
 - [CreateActorTokenRequest](docs/CreateActorTokenRequest.md)
 - [CreateAllowlistIdentifierRequest](docs/CreateAllowlistIdentifierRequest.md)
 - [CreateBlocklistIdentifierRequest](docs/CreateBlocklistIdentifierRequest.md)
 - [CreateEmailAddressRequest](docs/CreateEmailAddressRequest.md)
 - [CreateInvitationRequest](docs/CreateInvitationRequest.md)
 - [CreateJWTTemplateRequest](docs/CreateJWTTemplateRequest.md)
 - [CreateOAuthApplicationRequest](docs/CreateOAuthApplicationRequest.md)
 - [CreateOrganizationInvitationBulkRequestInner](docs/CreateOrganizationInvitationBulkRequestInner.md)
 - [CreateOrganizationInvitationRequest](docs/CreateOrganizationInvitationRequest.md)
 - [CreateOrganizationMembershipRequest](docs/CreateOrganizationMembershipRequest.md)
 - [CreateOrganizationRequest](docs/CreateOrganizationRequest.md)
 - [CreatePhoneNumberRequest](docs/CreatePhoneNumberRequest.md)
 - [CreateRedirectURLRequest](docs/CreateRedirectURLRequest.md)
 - [CreateSAMLConnectionRequest](docs/CreateSAMLConnectionRequest.md)
 - [CreateSAMLConnectionRequestAttributeMapping](docs/CreateSAMLConnectionRequestAttributeMapping.md)
 - [CreateSessionTokenFromTemplate200Response](docs/CreateSessionTokenFromTemplate200Response.md)
 - [CreateSignInTokenRequest](docs/CreateSignInTokenRequest.md)
 - [CreateUserRequest](docs/CreateUserRequest.md)
 - [DeletedObject](docs/DeletedObject.md)
 - [DisableMFA200Response](docs/DisableMFA200Response.md)
 - [Domain](docs/Domain.md)
 - [Domains](docs/Domains.md)
 - [EmailAddress](docs/EmailAddress.md)
 - [EmailAddressVerification](docs/EmailAddressVerification.md)
 - [GetOAuthAccessToken200ResponseInner](docs/GetOAuthAccessToken200ResponseInner.md)
 - [IdentificationLink](docs/IdentificationLink.md)
 - [InstanceRestrictions](docs/InstanceRestrictions.md)
 - [Invitation](docs/Invitation.md)
 - [JWTTemplate](docs/JWTTemplate.md)
 - [MergeOrganizationMetadataRequest](docs/MergeOrganizationMetadataRequest.md)
 - [OAuthApplication](docs/OAuthApplication.md)
 - [OAuthApplicationWithSecret](docs/OAuthApplicationWithSecret.md)
 - [OAuthApplications](docs/OAuthApplications.md)
 - [OTP](docs/OTP.md)
 - [Oauth](docs/Oauth.md)
 - [OauthError](docs/OauthError.md)
 - [Organization](docs/Organization.md)
 - [OrganizationInvitation](docs/OrganizationInvitation.md)
 - [OrganizationInvitations](docs/OrganizationInvitations.md)
 - [OrganizationMembership](docs/OrganizationMembership.md)
 - [OrganizationMembershipPublicUserData](docs/OrganizationMembershipPublicUserData.md)
 - [OrganizationMemberships](docs/OrganizationMemberships.md)
 - [OrganizationSettings](docs/OrganizationSettings.md)
 - [OrganizationWithLogo](docs/OrganizationWithLogo.md)
 - [Organizations](docs/Organizations.md)
 - [Passkey](docs/Passkey.md)
 - [PasswordHasher](docs/PasswordHasher.md)
 - [PhoneNumber](docs/PhoneNumber.md)
 - [PhoneNumberVerification](docs/PhoneNumberVerification.md)
 - [PreviewTemplateRequest](docs/PreviewTemplateRequest.md)
 - [ProxyCheck](docs/ProxyCheck.md)
 - [RedirectURL](docs/RedirectURL.md)
 - [RevokeInvitation200Response](docs/RevokeInvitation200Response.md)
 - [RevokeOrganizationInvitationRequest](docs/RevokeOrganizationInvitationRequest.md)
 - [SAML](docs/SAML.md)
 - [SAMLAccount](docs/SAMLAccount.md)
 - [SAMLAccountVerification](docs/SAMLAccountVerification.md)
 - [SAMLConnection](docs/SAMLConnection.md)
 - [SAMLConnectionAttributeMapping](docs/SAMLConnectionAttributeMapping.md)
 - [SAMLConnections](docs/SAMLConnections.md)
 - [SchemasPasskey](docs/SchemasPasskey.md)
 - [SchemasPasskeyVerification](docs/SchemasPasskeyVerification.md)
 - [Session](docs/Session.md)
 - [SignInToken](docs/SignInToken.md)
 - [SignUp](docs/SignUp.md)
 - [SvixURL](docs/SvixURL.md)
 - [Template](docs/Template.md)
 - [TestingToken](docs/TestingToken.md)
 - [Ticket](docs/Ticket.md)
 - [ToggleTemplateDeliveryRequest](docs/ToggleTemplateDeliveryRequest.md)
 - [TotalCount](docs/TotalCount.md)
 - [UpdateDomainRequest](docs/UpdateDomainRequest.md)
 - [UpdateEmailAddressRequest](docs/UpdateEmailAddressRequest.md)
 - [UpdateInstanceAuthConfig200Response](docs/UpdateInstanceAuthConfig200Response.md)
 - [UpdateInstanceAuthConfigRequest](docs/UpdateInstanceAuthConfigRequest.md)
 - [UpdateInstanceOrganizationSettingsRequest](docs/UpdateInstanceOrganizationSettingsRequest.md)
 - [UpdateInstanceRequest](docs/UpdateInstanceRequest.md)
 - [UpdateInstanceRestrictionsRequest](docs/UpdateInstanceRestrictionsRequest.md)
 - [UpdateOAuthApplicationRequest](docs/UpdateOAuthApplicationRequest.md)
 - [UpdateOrganizationMembershipMetadataRequest](docs/UpdateOrganizationMembershipMetadataRequest.md)
 - [UpdateOrganizationMembershipRequest](docs/UpdateOrganizationMembershipRequest.md)
 - [UpdateOrganizationRequest](docs/UpdateOrganizationRequest.md)
 - [UpdatePhoneNumberRequest](docs/UpdatePhoneNumberRequest.md)
 - [UpdateProductionInstanceDomainRequest](docs/UpdateProductionInstanceDomainRequest.md)
 - [UpdateSAMLConnectionRequest](docs/UpdateSAMLConnectionRequest.md)
 - [UpdateSAMLConnectionRequestAttributeMapping](docs/UpdateSAMLConnectionRequestAttributeMapping.md)
 - [UpdateSignUpRequest](docs/UpdateSignUpRequest.md)
 - [UpdateUserMetadataRequest](docs/UpdateUserMetadataRequest.md)
 - [UpdateUserRequest](docs/UpdateUserRequest.md)
 - [UpsertTemplateRequest](docs/UpsertTemplateRequest.md)
 - [User](docs/User.md)
 - [VerifyClientRequest](docs/VerifyClientRequest.md)
 - [VerifyDomainProxyRequest](docs/VerifyDomainProxyRequest.md)
 - [VerifyPassword200Response](docs/VerifyPassword200Response.md)
 - [VerifyPasswordRequest](docs/VerifyPasswordRequest.md)
 - [VerifySessionRequest](docs/VerifySessionRequest.md)
 - [VerifyTOTP200Response](docs/VerifyTOTP200Response.md)
 - [VerifyTOTPRequest](docs/VerifyTOTPRequest.md)
 - [Web3Signature](docs/Web3Signature.md)
 - [Web3Wallet](docs/Web3Wallet.md)
 - [Web3WalletVerification](docs/Web3WalletVerification.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="bearerAuth"></a>
### bearerAuth

- **Type**: Bearer authentication (sk_<environment>_<secret value>)


## Author

support@clerk.com


