# ArchiveRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Control-M Workload Archiving rule name. REQUIRED. HIDDEN. | [optional] 
**description** | **str** | The description of Control-M Workload Archiving rule. HIDDEN. | [optional] 
**max_output_size** | **str** | The maximum job&#x27;s output size to collect. HIDDEN. | [optional] 
**max_output_size_type** | **str** | The maximum job&#x27;s output size type to collect - KB or MB. The default is MB. HIDDEN. | [optional] 
**trim_type** | **str** | Trim in case the output exceed the maximum job&#x27;s output - Omit , Beginning, End. The default is to Omit. HIDDEN. | [optional] 
**retention** | **str** | The retention period to keep archive job by rule. The default is 1. HIDDEN. | [optional] 
**retention_type** | **str** | The retention period type to keep archive job by rule- Years, Months and Days are available. The default is Years. HIDDEN. | [optional] 
**is_active** | **str** | Is Control-M Workload Archiving rule is active. HIDDEN. | [optional] 
**archived_type** | **str** | The rule archived data - logs, output or both. The default is both. HIDDEN. | [optional] 
**rule_parameters** | [**list[RuleCriteria]**](RuleCriteria.md) | Rule parameters - ctm, type, jobName, jobType, application, subApplication, jobStatus, folder and library. HIDDEN. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

