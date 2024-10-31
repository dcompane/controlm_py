# CtmServerDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**saving_mode** | **str** | Saving Mode property determines what is the current status for the connection with Configuration Agent | [optional] 
**message** | **str** | Control-M/Server message describing the communication status | [optional] 
**services_message** | **str** | Control-M/Server services message | [optional] 
**state** | **str** | Control-M/Server state [up|down]. (Actual State) | [optional] 
**status** | **str** | Calculated Control-M/Server status | [optional] 
**os_type** | **str** | Control-M/Server operating system | [optional] 
**is_paused** | **bool** | Indicates if Control-M/Server is paused | [optional] 
**last_update** | **str** | The Control-M/Server last updated date | [optional] 
**is_high_availability_enabled** | **bool** | Indicates if High Availability is installed | [optional] 
**admin_agent_status** | **str** | Status of configuration agent on active host | [optional] 
**non_active_ca_status** | **str** | Status of configuration agent on non-active host | [optional] 
**primary_host** | **str** | Primary host | [optional] 
**secondary_host** | **str** | Secondary Host | [optional] 
**fail_over_mode** | **str** | High Availability fail over mode [Manual, Automatic] | [optional] 
**high_availability_process_name** | **str** | High Availability process name | [optional] 
**high_availability_status** | **str** | The server high availability status | [optional] 
**is_db_manager** | **str** | The server high availability status | [optional] 
**last_high_availability_process_date** | **str** | Last high availability Manual/Automatic Failover/Fallback date | [optional] 
**additional_attributes** | [**list[AdditionalAttribute]**](AdditionalAttribute.md) | Additional Attributes | [optional] 
**services** | [**list[CtmService]**](CtmService.md) |  | [optional] 
**database_def** | [**DatabaseDef**](DatabaseDef.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

