# DatabaseDef

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Database Name | [optional] 
**type** | **str** | Database Type (MSSQL, PostgreSQL) | [optional] 
**version** | **str** | Database Version | [optional] 
**host** | **str** | Database Host | [optional] 
**port** | **str** | Database Port | [optional] 
**message** | **str** | Database Message | [optional] 
**status** | **str** | Database Status | [optional] 
**service_name** | **str** | Database Service Name | [optional] 
**schema_name** | **str** | Database schema name | [optional] 
**additional_attributes** | [**list[AdditionalAttribute]**](AdditionalAttribute.md) | Additional Attributes | [optional] 
**pgattributes** | [**PgAttributes**](PgAttributes.md) |  | [optional] 
**shared_access** | [**list[SharedAccess]**](SharedAccess.md) | List of components that can access this database | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

