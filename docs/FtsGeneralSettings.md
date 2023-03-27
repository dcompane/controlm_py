# FtsGeneralSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home_directory** | **str** | Root path where transferred files are stored. If you want to use a different directory for each logged in user, you must add /${userName} to the path. | [optional] 
**multiple_login_allowed** | **bool** | Allow multiple open sessions | [optional] 
**max_open_sessions** | **int** | Maximum concurrent open sessions | [optional] 
**max_login_failures** | **int** | Number of retries before the server closes the connection | [optional] 
**delay_after_login_failure** | **int** | Time of waiting before letting the user to do another login in seconds | [optional] 
**throttling_activated** | **bool** | Allow bandwidth throttling | [optional] 
**max_simultaneous_uploads** | **int** | Maximum simultaneos uploads | [optional] 
**max_simultaneous_downloads** | **int** | Maximum simultaneos downloads | [optional] 
**server_enabled** | **bool** | Enable/Disable the File Transfer Server | [optional] 
**access_log_enabled** | **bool** | Is FTS Access Log enabled - true/false | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

