# RoleData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | role name | [optional] 
**description** | **str** | role description | [optional] 
**allowed_jobs** | [**AllowedJobs**](AllowedJobs.md) |  | [optional] 
**allowed_job_actions** | [**AllowedJobActions**](AllowedJobActions.md) |  | [optional] 
**privileges** | [**Privileges**](Privileges.md) |  | [optional] 
**folders** | [**list[FolderAuth]**](FolderAuth.md) |  | [optional] 
**calendars** | [**list[PrivilegeNameControlm]**](PrivilegeNameControlm.md) |  | [optional] 
**runas_users** | [**list[RunasUserAuth]**](RunasUserAuth.md) |  | [optional] 
**workload_policies** | [**list[PrivilegeName]**](PrivilegeName.md) |  | [optional] 
**site_standard** | [**list[PrivilegeName]**](PrivilegeName.md) |  | [optional] 
**site_customization** | [**list[PrivilegeName]**](PrivilegeName.md) |  | [optional] 
**services** | [**list[ServiceAuth]**](ServiceAuth.md) |  | [optional] 
**events** | [**list[PrivilegeNameControlm]**](PrivilegeNameControlm.md) |  | [optional] 
**mutexes** | [**list[PrivilegeNameControlm]**](PrivilegeNameControlm.md) |  | [optional] 
**locks** | [**list[PrivilegeNameControlm]**](PrivilegeNameControlm.md) |  | [optional] 
**semaphores** | [**list[PrivilegeNameControlm]**](PrivilegeNameControlm.md) |  | [optional] 
**pools** | [**list[PrivilegeNameControlm]**](PrivilegeNameControlm.md) |  | [optional] 
**variables** | [**list[PrivilegeNameControlm]**](PrivilegeNameControlm.md) |  | [optional] 
**global_events** | [**list[PrivilegeName]**](PrivilegeName.md) |  | [optional] 
**agent_management** | [**list[AgentMngAuth]**](AgentMngAuth.md) |  | [optional] 
**plugin_management** | [**list[PluginMngAuth]**](PluginMngAuth.md) |  | [optional] 
**connection_profile_management** | [**list[CPMngAuth]**](CPMngAuth.md) |  | [optional] 
**runas_definition_management** | [**list[RunasDefinitionAuth]**](RunasDefinitionAuth.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

