# FolderProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the folder. REQUIRED:addMFTFolder | HIDDEN | [optional] 
**allowed_internal_user_names** | **list[str]** | Authorized Internal Users. HIDDEN | [optional] 
**allowed_user_names** | **list[str]** | Authorized External Users And User Groups. HIDDEN | [optional] 
**allowed_group_names** | **list[str]** | Array of allowed group names. HIDDEN | [optional] 
**delete_files_after_processing** | **bool** | Delete file after downloaded from incoming folder. HIDDEN | [optional] 
**notify_by_email_when_file_arrived** | **bool** | Send email notification to external users when a new file arrives. HIDDEN | [optional] 
**retention_hours** | **int** | Retention Time in hours. HIDDEN | [optional] 
**size_limit** | **int** | Size limit for folder (in Gigabyte). HIDDEN | [optional] 
**allowed_file_pattern** | **str** | allowed file pattern wildcard. HIDDEN | [optional] 
**exclude_file_pattern** | **str** | blocked file pattern wildcard. HIDDEN | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

