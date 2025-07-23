# UpgradeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ctm** | **str** | Control-M name. REQUIRED | [optional] 
**agent** | **str** | Agent name. REQUIRED | [optional] 
**type** | **str** | Product type (Agent, MFT, AppPack). REQUIRED | [optional] 
**version** | **str** | Target version to be installed or version that should be rollback REQUIRED | [optional] 
**activity_name** | **str** | Name of activity | [optional] 
**install_user** | **str** | User that will install, upgrade or uninstall HIDDEN | [optional] 
**notify_address** | **str** | List of email addresses separated by semicolon HIDDEN | [optional] 
**description** | **str** | Description of activity HIDDEN | [optional] 
**use_network_deployment** | **bool** | Whether to deploy from a network location HIDDEN | [optional] 
**transfer_only** | **bool** | True means perform only transfer. Install as well as transfer otherwise HIDDEN | [optional] 
**java_home** | **str** | The JRE location. If specified - will be used by the upgrade process and the upgraded Agent/Managed File Transfer/AppPack HIDDEN | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

