# SiteStandardFieldRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | The name of the field this rule applies to | 
**job_type** | **str** | The job type this rule applies for. Empty job type means it applies to all job types | [optional] 
**conditions** | [**list[SiteStandardCondition]**](SiteStandardCondition.md) | Job fields conditions to limit when this rule applies | [optional] 
**attribute_conditions** | [**list[SiteStandardCondition]**](SiteStandardCondition.md) | Multi-instance fields conditions to limit on what items this multi-instance rule applies. Should not be used in Must Have rules | [optional] 
**on_statement** | **str** | For on-do steps, specify the type of on statement this rule applies to. Omit this field for \&quot;any on\&quot; | [optional] 
**do_action** | **str** | For on-do steps, specify the type of do action this rule applies to. Omit this field for \&quot;any do\&quot; | [optional] 
**restriction** | [**SiteStandardRestriction**](SiteStandardRestriction.md) |  | [optional] 
**sub_fields** | [**list[SiteStandardFieldRule]**](SiteStandardFieldRule.md) | Used for list fields to indicate restrictions for items in the list. When mustHave is true, it means the list must contain at least one item with sub-fields that match these restrictions. | [optional] 
**must_have** | **bool** | Specifies if this is a must-have rule. Relevant only for list fields. true indicates that the field must contain at least one item that matches this rule&#x27;s restriction false (or missing) indicates that when the field has items, all of them must match the rule&#x27;s restriction | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

