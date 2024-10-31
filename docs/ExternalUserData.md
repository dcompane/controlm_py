# ExternalUserData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | external user name REQUIRED:addExternalUser,addExternalUserForSite | HIDDEN | [optional] 
**email** | **str** | user email REQUIRED:addExternalUser,addExternalUserForSite | HIDDEN | [optional] 
**company** | **str** | user&#x27;s company REQUIRED:addExternalUser,addExternalUserForSite | HIDDEN | [optional] 
**password** | **str** | user password HIDDEN:updateExternalUser,updateExternalUserForSite | [optional] 
**description** | **str** | user description HIDDEN | [optional] 
**phone_number** | **str** | external user phone number HIDDEN | [optional] 
**ssh_key** | **str** | SSH key string HIDDEN | [optional] 
**as2_key** | [**As2KeyData**](As2KeyData.md) |  | [optional] 
**is_locked** | **bool** | indicates whether the user account is locked HIDDEN | [optional] 
**lock_reason** | **str** | provides the reason for locking the user account HIDDEN | [optional] 
**change_password_at_next_login** | **bool** | indicates whether a password change is required at next login HIDDEN | [optional] 
**password_never_expires** | **bool** | indicates whether the user&#x27;s password is set to never expire HIDDEN | [optional] 
**home_folder** | **str** | default user&#x27;s home directory HIDDEN | [optional] 
**password_update_time** | **str** | indicate when the user&#x27;s password changed HIDDEN | [optional] 
**public_key_update_time** | **str** | indicate when the user&#x27;s ssh public key changed HIDDEN | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

