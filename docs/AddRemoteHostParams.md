# AddRemoteHostParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remotehost** | **str** | The remote host (name) which will execute the commands. REQUIRED. | [optional] 
**port** | **int** | The remote host SSH port. | [optional] 
**encrypt_algorithm** | **str** | The SSH encrypt algorithm to be used. HIDDEN. | [optional] 
**compression** | **bool** | Is compression used. HIDDEN. | [optional] 
**authorize** | **bool** | authorize SSL remote host while creating the remote host. HIDDEN. | [optional] 
**agents** | **list[str]** | Agents to execute the commands on. HIDDEN. | [optional] 
**tag** | **str** | tag of the remote host. | [optional] 
**w_mi_sysout_directory** | **str** | the WMI Sysout Directory. | [optional] 
**connection_type** | **str** | the connection type. | [optional] 
**convert_existing_agent** | **bool** | convert existing agent to Agentless host. HIDDEN. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

