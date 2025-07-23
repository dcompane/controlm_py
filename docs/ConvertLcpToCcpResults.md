# ConvertLcpToCcpResults

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poll_id** | **str** | Poll id | [optional] 
**convert_status** | **str** | Currently convert status. ENDED_OK, ENDED_NOT_OK, PARTIAL_RESULTS, UNKNOWN | [optional] 
**convert_state** | **str** | Current convert local cps state. number of converted connection profiles from total connection profile. | [optional] 
**is_dry_run** | **bool** | Determines whether this is a simulation of conversion. | [optional] 
**successful_converted_cps** | **int** | Determines the number of successfully converted connections profiles. | [optional] 
**skipped_converted_cps** | **int** | Determines the number of skipped to connections profiles. | [optional] 
**failed_converted_cps** | **int** | Determines the number of failed to connections profiles. | [optional] 
**converted_connection_profiles** | **list[str]** |  | [optional] 
**skipped_to_convert_connection_profiles** | **list[str]** |  | [optional] 
**failed_to_convert_connection_profiles** | **list[str]** |  | [optional] 
**errors** | [**list[DeploymentFileError]**](DeploymentFileError.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

