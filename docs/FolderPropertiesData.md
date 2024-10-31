# FolderPropertiesData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the folder. REQUIRED:addMFTFolder,addMFTFolderForSite | HIDDEN | [optional] 
**authorized_internal_users** | **list[str]** | Authorized Internal Users. HIDDEN | [optional] 
**authorized_external_users_and_groups** | **list[str]** | Authorized External Users And User Groups. HIDDEN | [optional] 
**delete_files_after_download** | **bool** | Delete file after downloaded from incoming folder. HIDDEN | [optional] 
**notify_by_email_when_file_arrive** | **bool** | Send email notification to external users when a new file arrives. HIDDEN | [optional] 
**retention_policy** | **int** | Retention policy. HIDDEN | [optional] 
**retention_policy_units** | **str** | Retention policy units(Hours/Days). HIDDEN | [optional] [default to 'Hours']
**size_limit** | **int** | Size limit for folder (in Gigabyte). HIDDEN | [optional] 
**allowed_file_pattern** | **str** | allowed file pattern wildcard. HIDDEN | [optional] 
**blocked_file_pattern** | **str** | blocked file pattern wildcard. HIDDEN | [optional] 
**access_type** | **str** | Folder&#x27;s access type (Limited, Unlimited). HIDDEN | [optional] 
**access_level** | **str** | Access level of virtual folder - Read only, Write only, Full control | [optional] 
**delete_files_after_download_by_external_users** | **bool** | Delete file after downloaded by external users. HIDDEN | [optional] 
**fixed_sub_folders** | [**list[FixedSubFolder]**](FixedSubFolder.md) |  | [optional] 
**authorized_external_users_and_groups_extended** | [**list[UserOrGroupExtended]**](UserOrGroupExtended.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

