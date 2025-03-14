# VaultParam

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The UI Control type, could be &#x27;textbox&#x27; or &#x27;textarea&#x27; | 
**label** | **str** | The displayed name of the field parameter | 
**label_api** | **str** | The display name of the parameter in Automation API | 
**name** | **str** | The name of the field parameter | [optional] 
**is_mandatory** | **bool** | UI validation (optional) - indicates whether user must fill this parameter | [optional] 
**min_length** | **int** | UI validation (optional) - the minimum allowed value field length | [optional] 
**max_length** | **int** | UI validation (optional) - the maximum allowed value field length | [optional] 
**excluded_chars** | **str** | UI validation (optional) - indicates to excludes specific chars seperated by ; | [optional] 
**is_in_excluded_chars** | **bool** | UI validation (optional) - indicates whether excludedChars is enabled | [optional] 
**valid_values** | **str** | UI validation (optional) - indicates the allowed input types, &#x27;alphanumeric&#x27;, &#x27;numbers&#x27;, &#x27;chars&#x27; or &#x27;all&#x27; | [optional] 
**default_visibility** | **str** | UI appearance (optional) - indicates the UI Control visibility,  &#x27;visible&#x27;, &#x27;hidden&#x27; or &#x27;readonly&#x27; | [optional] 
**default_value** | **str** | UI appearance (optional)- this value automatically sets on the UI Control in-case no other value specified | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

