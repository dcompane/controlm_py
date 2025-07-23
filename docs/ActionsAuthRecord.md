# ActionsAuthRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | component in which the action sent - Possible Values - EM, CTM_Server, CTM_Agent, CTM_CM | [optional] 
**action** | **str** | action name unique list of actions&#x27; names as appear in the actions_auth em db table, along with the destination makes a unique action auth entry | [optional] 
**category** | **str** | Privilege (Can be empty) Possible Values for categories fields  - OPER, DATABASE, CONFIG, CTMSEC, CPMAN, RAMAN, AGMAN, CMMAN, CCP, UNKNOWN | [optional] 
**auth_level** | **str** | required minimum authorization level - BROWSE, UPDATE, FULL | [optional] 
**action_type** | **str** | R - request always pass, authorization is done on the response; C - Connection Profile name will remain empty and will be ignored; E - Not related to authorization | [optional] 
**additional_info** | **str** | currently not in use regarding authorization | [optional] 
**category2** | **str** |  | [optional] 
**policy** | **str** | relation between Category and category2 - 1. Only category, 2. Only Category2, 3. Category AND Category2, 4. Category OR Category2 | [optional] 
**auth_attr** | **str** | In case that not all information for authorization exist in the header request, it contain path in the body for the missing field\\fields. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

