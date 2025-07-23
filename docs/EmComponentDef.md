# EmComponentDef

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | The hostname of the server where the EM component is running. | [optional] 
**type** | **str** | The type of the EM component (e.g., Gateway, GUI_Server, ARCHIVE). | [optional] 
**name** | **str** | The logical name of the EM component. | [optional] 
**desired_state** | **str** | The desired state of the EM component (Up, Down, Ignored, Recycle). | [optional] 
**check_interval** | **int** | The interval, in seconds, at which to check the component&#x27;s status. | [optional] 
**additional_parameters** | **str** | Additional startup options for the component. | [optional] 
**gui_server_name** | **str** | The name of the GUI Server connected to this EM component. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

