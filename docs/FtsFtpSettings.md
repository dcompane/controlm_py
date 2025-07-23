# FtsFtpSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_enabled** | **bool** | Enable/Disable listening for FTP/S connection | [optional] 
**port** | **int** | FTP server port | [optional] 
**authentication_method** | **str** | Authentication method being used to connect FTP server | [optional] 
**secured** | **bool** | Use FTP secure connection (SSL/TLS) | [optional] 
**keystore_file_path** | **str** | FTPS keystore file location | [optional] 
**keystore_file_password** | **str** | Password being used to access the FTPS keystore | [optional] 
**ciphers** | **str** | Ftps server allowed cipher suites (comma-separated). Leave empty to allow all supported cipher suites. | [optional] 
**listen_for_implicit_connection** | **bool** | Implicit negotiation mode - requires that the entire FTP session must be encrypted | [optional] 
**passive_ports** | **str** | Passive FTP ports range - for PASV connections, the server will open a random port in this range for client to connect to | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

