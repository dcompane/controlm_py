# FtsSftpSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_enabled** | **bool** | Enable/Disable listening for SFTP connection | [optional] 
**port** | **int** | SFTP server port | [optional] 
**authentication_method** | **str** | Authentication method being used to connect FTP server | [optional] 
**keystore_file_path** | **str** | SFTP keystore file location | [optional] 
**keystore_file_password** | **str** | Password being used to access the SFTP keystore | [optional] 
**ciphers** | **str** | Ftps server allowed cipher suites (comma-separated). Leave empty to allow all supported cipher suites. | [optional] 
**known_users_file_path** | **str** | Known users file location | [optional] 
**overridden_users_home_directories** | [**list[FtsUserHomeDirectoryData]**](FtsUserHomeDirectoryData.md) | Overridden home directories for specific internal users | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

