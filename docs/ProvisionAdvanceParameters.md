# ProvisionAdvanceParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**java_home** | **str** | The JRE that will be used to install and run the agent | [optional] 
**connection_initiator** | **str** | Which component is allowed to initiate the connection [ServerToAgent | AgentToServer | BothAllowed]. Parameters start with capital letter.  HIDDEN. | [optional] 
**tag** | **str** | Logical name that is used to label specific Control-M/Agents into a group with a specific authorization level.  HIDDEN. | [optional] 
**server_host_name** | **str** | Control-M/Server name (in case it has an alias or multiple network interfaces).  HIDDEN. | [optional] 
**server_port** | **int** | Control-M/Server port to communicate with the agent.  HIDDEN. | [optional] 
**secondary_server_host_name** | **str** | The secondary Control-M/Server host used in High Availability (HA) configurations.  HIDDEN. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

