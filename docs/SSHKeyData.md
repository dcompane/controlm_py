# SSHKeyData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_name** | **str** | The name for the key . REQUIRED. | [optional] 
**pass_phrase** | **str** | The password for the key file . REQUIRED. | [optional] 
**format** | **str** | the format of the SSH key to generate. [OpenSSH/SSH2] | [optional] [default to 'OpenSSH']
**type** | **str** | The type of the SSH key to generate.  - For ctm versions under v22: [RSA (Default), DSA] - For ctm versions v22 and above: [RSA, ECDSA (Default)]  | [optional] 
**bits** | **int** | Generated keys defined with larger bits provides enhanced security.  For ctm versions under v22:   [512/768/1024 (Default)/2048/3072]  For ctm versions v22 and above:   - For RSA: 3072, 4096 (Default)   - For ECDSA: 256 (Default), 384, 521  | [optional] 
**_async** | **bool** | True to add SSH key asynchronously wit0h pollingId. HIDDEN | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

