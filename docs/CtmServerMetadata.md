# CtmServerMetadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owned_by** | **str** | Is the server belongs to a saas environment | [optional] 
**name** | **str** | The server name | [optional] 
**host** | **str** | The server host | [optional] 
**state** | **str** | The server state | [optional] 
**message** | **str** | The server message | [optional] 
**version** | **str** | The server version | [optional] 
**desired_state** | **str** | The server desired state | [optional] 
**status** | **str** | The server status | [optional] 
**os_type** | **str** | The server operating system | [optional] 
**platform** | **str** | The server platform | [optional] 
**last_updated** | **str** | The server last updated date | [optional] 
**db_host** | **str** | The server database host | [optional] 
**has_high_availability** | **str** | Is server in high availability | [optional] 
**primary_db_host** | **str** | The server primary database host | [optional] 
**secondary_db_host** | **str** | The server secondary database host | [optional] 
**primary_host** | **str** | The server primary host | [optional] 
**secondary_host** | **str** | The server secondary host | [optional] 
**fail_over_mode** | **str** | The server high availability fail over mode | [optional] 
**high_availability_process_name** | **str** | High Availability process name | [optional] 
**high_availability_status** | **str** | The server high availability status | [optional] 
**is_db_manager** | **str** | Indicates if this host is manager of DB | [optional] 
**replication_status** | **str** | Status of DB replication | [optional] 
**replication_mode** | **str** | Indicates which mode DB replication is in [Sync,  Async] | [optional] 
**admin_agent_status** | **str** | Status of the Configuration Agent of the active host | [optional] 
**non_active_ca_status** | **str** | Status of the Configuration Agent of the non-active host | [optional] 
**is_paused** | **str** | Is the server in pause | [optional] 
**is_managed** | **str** | Is the server in managed state | [optional] 
**is_enabled** | **str** | Is the server enabled | [optional] 
**ssl_state** | **str** | The server ssl state | [optional] 
**services** | [**list[CtmServerComponentStatusInfo]**](CtmServerComponentStatusInfo.md) | The server services | [optional] 
**gateways** | [**list[CtmServerComponentStatusInfo]**](CtmServerComponentStatusInfo.md) | The server gateway | [optional] 
**databases** | [**list[CtmServerComponentStatusInfo]**](CtmServerComponentStatusInfo.md) | The server databases | [optional] 
**agents** | [**list[CtmServerComponentStatusInfo]**](CtmServerComponentStatusInfo.md) | The server agents | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

