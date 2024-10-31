# DeploymentFileResults

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_file** | **str** | The name of a specific deployment file. | [optional] 
**poll_id** | **str** | Poll id in case of a long deploy process | [optional] 
**deployment_state** | **str** | Current deployment step and state. CALENDARS_DEPLOYED, CONNECTION_PROFILES_DEPLOYED, DEPLOYING_FOLDERS, folders deployed, etc. | [optional] 
**deployment_status** | **str** | Currently deployment status. ENDED_OK, ENDED_NOT_OK, PARTIAL_RESULTS, UNKNOWN | [optional] 
**successful_folders_count** | **int** | Determines the number of successfully deployed simple folders. | [optional] 
**successful_smart_folders_count** | **int** | Determines the number of successfully deployed smart folders. | [optional] 
**successful_sub_folders_count** | **int** | Determines the number of successfully deployed sub folders. | [optional] 
**successful_jobs_count** | **int** | Determines the number of successfully deployed sub folders. | [optional] 
**successful_connection_profiles_count** | **int** | Determines the number of successfully deployed sub folders. | [optional] 
**successful_drivers_count** | **int** | Determines the number of successfully deployed sub folders. | [optional] 
**successful_calendars_count** | **int** | Determines the number of successfully deployed sub folders. | [optional] 
**successful_site_standards_count** | **int** | Determines the number of successfully deployed sub folders. | [optional] 
**is_deploy_descriptor_valid** | **bool** | Determines if the deployment file is a valid deploy descriptor file. | [optional] 
**deployed_folders** | **list[str]** |  | [optional] 
**deployed_jobs** | **list[str]** |  | [optional] 
**deployed_sub_folders** | **list[str]** |  | [optional] 
**deployed_drivers** | **list[str]** |  | [optional] 
**deployed_connection_profiles** | **list[str]** |  | [optional] 
**deployed_calendars** | **list[str]** |  | [optional] 
**deployed_site_standardss** | **list[str]** |  | [optional] 
**errors** | [**list[DeploymentFileError]**](DeploymentFileError.md) |  | [optional] 
**warnings** | [**list[WarningData]**](WarningData.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

