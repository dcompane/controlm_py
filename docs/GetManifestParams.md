# GetManifestParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topology_identifier** | **str** | Holds the topology identifier | [optional] 
**environment** | **str** | Determines, whether the Agent or Plugin works in saas, selfhosted, or both | [optional] 
**category** | **str** | Holds the category of the entry | [optional] 
**order** | **int** | Order of appearance | [optional] 
**product_code** | **str** | Three letters that are the product unique identifier | [optional] 
**name** | **str** | The full official name of the product | [optional] 
**install_uri** | **str** | Specifies the path to the installation file | [optional] 
**visible** | **bool** | Determines whether or not the product should be visible in the web page | [optional] 
**icon_base64** | **str** | Base64 representaion of image file | [optional] 
**error** | **str** | Description of the specific error | [optional] 
**error_code** | **str** | Http response status code | [optional] 
**full_name** | **str** | The full name | [optional] 
**short_name** | **str** | The short name | [optional] 
**sub_category** | **str** | The sub-category | [optional] 
**keywords** | **list[str]** | List of words that user can use when searching for a plugin | [optional] 
**versions** | **list[str]** | Includes all the versions numbers of the product that exist in the repository | [optional] 
**versions_self_hosted** | **list[str]** | Includes all the version numbers of the product present in the repository and is compatible with a SelfHosted environment | [optional] 
**group** | [**ManifestGroupObject**](ManifestGroupObject.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

