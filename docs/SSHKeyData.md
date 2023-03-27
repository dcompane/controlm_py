# SSHKeyData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_name** | **str** | The name for the key . REQUIRED. | [optional] 
**pass_phrase** | **str** | The password for the key file . REQUIRED. | [optional] 
**format** | **str** | the format of the SSH key to generate. [OpenSSH/SSH2] | [optional] [default to 'OpenSSH']
**type** | **str** | the type of the SSH key to generate. [RSA/DSA] | [optional] [default to 'RSA']
**bits** | **int** | Generated keys defined with larger bits provides enhanced security . [512/768/1024/2048/3076] | [optional] [default to 1024]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

