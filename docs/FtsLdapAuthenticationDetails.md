# FtsLdapAuthenticationDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_user_name** | **str** | Name of the user that runs the search action for users that log on | [optional] 
**search_user_password** | **str** | Password of the user that runs the search action for users that log on | [optional] 
**server_url** | **str** | URL of the LDAP Directory server | [optional] 
**base_dn** | **str** | Base DN (the point from where the server will search for users) | [optional] 
**username_attribute_name** | **str** | Name of the LDAP attribute containing the username | [optional] 
**dn_attribute_name** | **str** | Name of the LDAP attribute containing the distinguished name | [optional] 
**connection_timeout** | **int** | LDAP server connection timeout in milliseconds | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

