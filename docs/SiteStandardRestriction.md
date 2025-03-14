# SiteStandardRestriction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_required** | **bool** | Specifies if this field or business parameter must have a value. Relevant only for business parameters and simple fields with no sub-fields | [optional] 
**possible_options** | [**SiteStandardPossibleOptions**](SiteStandardPossibleOptions.md) |  | [optional] 
**possible_operator_value_options** | [**list[SiteStandardOperatorValueOptions]**](SiteStandardOperatorValueOptions.md) | List of possible operator-value pars | [optional] 
**min_length** | **int** |  | [optional] 
**max_length** | **int** |  | [optional] 
**numeric_limitation** | **str** | Limitation for numeric fields. Can include various ranges separated by comma, e.g. \&quot;1, 5-8\&quot; | [optional] 
**numeric_unit** | **str** | In case of Rerun Interval field, specifies the unit the numeric limitation is referring to. | [optional] 
**is_read_only** | **bool** | Specifies if this field can be set by the user. Relevant only for boolean fields. | [optional] 
**allow_uppercase_letters** | **bool** | Determines whether uppercase letters (A-Z) are allowed in the field value | [optional] 
**allow_lowercase_letters** | **bool** | Determines whether lowercase letters (a-z) are allowed in the field value | [optional] 
**allow_digits** | **bool** | Determines whether digits (0-9) are allowed in the field value | [optional] 
**allowed_characters** | **str** | A string contains all characters allowed in the field value (all digits or all letters shouldn&#x27;t be listed here) | [optional] 
**disallowed_characters** | **str** | A string contains all characters not allowed in the field value. This should specified only if the other \&quot;allowed...\&quot; properties are not set | [optional] 
**disallowed_options** | [**SiteStandardPossibleOptions**](SiteStandardPossibleOptions.md) |  | [optional] 
**disallowed_enum_values** | [**list[SiteStandardPossibleValue]**](SiteStandardPossibleValue.md) | List of enum values not allowed for the field | [optional] 
**allowed_enum_values** | [**list[SiteStandardPossibleValue]**](SiteStandardPossibleValue.md) | List of enum values that are allowed for the field. If this is empty, than any value is allowed if it is not in the disallowedEnumValues list and it matches the other restrictions. If it is not empty, only values listed in the list or values that matches the specified restrictions (if exists) are allowed. | [optional] 
**check_for_existence** | **bool** | Check if the field value need to be checked if it exists in the system. E.g. for node_id field - check that the specified host or host group exists in the system | [optional] 
**default_value** | **str** |  | [optional] 
**validation_error_message** | **str** | The validation error message to show the user when this rule is not met.&lt;br&gt; If not specified, the default error message will be used. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

