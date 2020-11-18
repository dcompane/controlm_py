# swagger_client.ConfigApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_archive_rule**](ConfigApi.md#add_archive_rule) | **POST** /config/archive/rule | Add Workload Archiving rule
[**add_external_user**](ConfigApi.md#add_external_user) | **POST** /config/mft/externaluser | Add and external user
[**add_external_user_or_user_group_to_mft_folder**](ConfigApi.md#add_external_user_or_user_group_to_mft_folder) | **POST** /config/mft/virtualfolder/{folderName}/user/{userOrGroup} | Add external user or user groups to virtual folder external users list.
[**add_gateway**](ConfigApi.md#add_gateway) | **POST** /config/mft/gateway | add gateway.
[**add_host_to_hostgroup**](ConfigApi.md#add_host_to_hostgroup) | **POST** /config/server/{server}/hostgroup/{hostgroup}/agent | add agent to hostgroup
[**add_hub_to_cluster**](ConfigApi.md#add_hub_to_cluster) | **POST** /config/mft/cluster/hub/{agentname} | add hub to cluster.
[**add_mft_folder**](ConfigApi.md#add_mft_folder) | **POST** /config/mft/virtualfolder | Add virtual folder
[**add_mft_user_group**](ConfigApi.md#add_mft_user_group) | **POST** /config/mft/usergroup | Add user group.
[**add_pgp_template**](ConfigApi.md#add_pgp_template) | **POST** /config/server/{server}/agent/{agent}/mft/pgptemplate/{templateName} | Add PGP Template
[**add_remote_host**](ConfigApi.md#add_remote_host) | **POST** /config/server/{server}/remotehost | add remote host to Server
[**add_role**](ConfigApi.md#add_role) | **POST** /config/authorization/role | Add Authorization Role
[**add_role_to_ldap_group**](ConfigApi.md#add_role_to_ldap_group) | **POST** /config/authorization/ldap/{ldapgroup}/role/{role} | Add a role to LDAP group
[**add_role_to_user**](ConfigApi.md#add_role_to_user) | **POST** /config/authorization/user/{user}/role/{role} | Add a role to user
[**add_secret**](ConfigApi.md#add_secret) | **POST** /config/secret | Add a new secret
[**add_server**](ConfigApi.md#add_server) | **POST** /config/server | add server to the system
[**add_user**](ConfigApi.md#add_user) | **POST** /config/authorization/user | Add user
[**add_zos_template**](ConfigApi.md#add_zos_template) | **POST** /config/server/{server}/agent/{agent}/mft/zostemplate/{templateName} | Add z/OS Template
[**authorize_mft_ssh_cluster**](ConfigApi.md#authorize_mft_ssh_cluster) | **POST** /config/server/{server}/agent/{agent}/mft/ssh/cluster/{clusterName} | Authorize SSH Cluster
[**authorize_mft_ssh_host**](ConfigApi.md#authorize_mft_ssh_host) | **POST** /config/server/{server}/agent/{agent}/mft/ssh/host/{hostname} | Authorize SSH Host
[**authorize_ssh_known_remotehost**](ConfigApi.md#authorize_ssh_known_remotehost) | **POST** /config/server/{server}/remotehost/{remotehost}/authorize | Authorize
[**change_user_password**](ConfigApi.md#change_user_password) | **POST** /config/user/{user}/password/adminUpdate | Change user password
[**create_agent_certificate_signing_request**](ConfigApi.md#create_agent_certificate_signing_request) | **POST** /config/server/{server}/agent/{agent}/csr | Create certificate signing request (CSR).
[**create_run_as_user**](ConfigApi.md#create_run_as_user) | **POST** /config/server/{server}/runasuser | Add a new Run-as user
[**delete_agent**](ConfigApi.md#delete_agent) | **DELETE** /config/server/{server}/agent/{agent} | delete an agent from Server
[**delete_archive_rule**](ConfigApi.md#delete_archive_rule) | **DELETE** /config/archive/rule/{ruleName} | Delete Workload Archiving rule
[**delete_authorization_role**](ConfigApi.md#delete_authorization_role) | **DELETE** /config/authorization/role/{role} | Delete Authorization Role
[**delete_external_user**](ConfigApi.md#delete_external_user) | **DELETE** /config/mft/externaluser/{username} | Delete an external user
[**delete_external_user_or_user_group_from_mft_folder**](ConfigApi.md#delete_external_user_or_user_group_from_mft_folder) | **DELETE** /config/mft/virtualfolder/{folderName}/user/{userOrGroup} | Remove an external user or user group from an existing virtual folder in MFT.
[**delete_host_from_group**](ConfigApi.md#delete_host_from_group) | **DELETE** /config/server/{server}/hostgroup/{hostgroup}/agent/{host} | delete an agent from a hostgroup
[**delete_host_group**](ConfigApi.md#delete_host_group) | **DELETE** /config/server/{server}/hostgroup/{hostgroup} | delete host group
[**delete_mft_folder**](ConfigApi.md#delete_mft_folder) | **DELETE** /config/mft/virtualfolder/{folderName} | Delete a virtual folder.
[**delete_mft_user_group**](ConfigApi.md#delete_mft_user_group) | **DELETE** /config/mft/usergroup/{name} | Delete user group.
[**delete_pgp_template**](ConfigApi.md#delete_pgp_template) | **DELETE** /config/server/{server}/agent/{agent}/mft/pgptemplate/{templateName} | Delete PGP Template
[**delete_remote_host**](ConfigApi.md#delete_remote_host) | **DELETE** /config/server/{server}/remotehost/{remotehost} | delete a remote host from Server
[**delete_role_from_ldap_group**](ConfigApi.md#delete_role_from_ldap_group) | **DELETE** /config/authorization/ldap/{ldapgroup}/role/{role} | Delete a role from LDAP group
[**delete_run_as_user**](ConfigApi.md#delete_run_as_user) | **DELETE** /config/server/{server}/runasuser/{agent}/{user} | delete Run-as user
[**delete_secret**](ConfigApi.md#delete_secret) | **DELETE** /config/secret/{name} | Delete an existing secret
[**delete_user**](ConfigApi.md#delete_user) | **DELETE** /config/authorization/user/{user} | Delete user
[**delete_zos_template**](ConfigApi.md#delete_zos_template) | **DELETE** /config/server/{server}/agent/{agent}/mft/zostemplate/{templateName} | Delete z/OS Template
[**deploy_agent_certificate**](ConfigApi.md#deploy_agent_certificate) | **POST** /config/server/{server}/agent/{agent}/crt | Deploy certificate (CRT).
[**disable_agent**](ConfigApi.md#disable_agent) | **POST** /config/server/{server}/agent/{agent}/disable | disable agent from the Server
[**enable_agent**](ConfigApi.md#enable_agent) | **POST** /config/server/{server}/agent/{agent}/enable | enable agent from the Server
[**failover**](ConfigApi.md#failover) | **PUT** /config/server/{server}/failover | Perform Manual Failover on a specified Server
[**generate_mft_rsa_ssh_key**](ConfigApi.md#generate_mft_rsa_ssh_key) | **POST** /config/server/{server}/agent/{agent}/mft/ssh/key | Generate RSA SSH Key
[**get_agent_certificate_expiration_date**](ConfigApi.md#get_agent_certificate_expiration_date) | **GET** /config/server/{server}/agent/{agent}/crt/expiration | Get certificate expiration date.
[**get_agent_parameters**](ConfigApi.md#get_agent_parameters) | **GET** /config/server/{server}/agent/{agent}/params | get agent parameters
[**get_agents**](ConfigApi.md#get_agents) | **GET** /config/server/{server}/agents | get Server agents
[**get_all_archive_rules**](ConfigApi.md#get_all_archive_rules) | **GET** /config/archive/rules | Get all Workload Archiving rules
[**get_all_authorization_roles**](ConfigApi.md#get_all_authorization_roles) | **GET** /config/authorization/roles | Get Authorization Roles
[**get_all_ldap_groups**](ConfigApi.md#get_all_ldap_groups) | **GET** /config/authorization/ldaps | Get All LDAP groups
[**get_all_roles_associated_with_ldap**](ConfigApi.md#get_all_roles_associated_with_ldap) | **GET** /config/authorization/ldap/{ldapgroup}/roles | Get Authorization Roles associated with an LDAP group
[**get_all_users**](ConfigApi.md#get_all_users) | **GET** /config/authorization/users | Get users
[**get_archive_statistics**](ConfigApi.md#get_archive_statistics) | **GET** /config/archive/statistics | Get Workload Archiving statistics
[**get_external_user_authorized_folders**](ConfigApi.md#get_external_user_authorized_folders) | **GET** /config/mft/externaluser/{name}/virtualfolders | Get MFT external user authorized folders
[**get_external_users**](ConfigApi.md#get_external_users) | **GET** /config/mft/externalusers | Get MFT external users that match the search criteria.
[**get_fts_settings**](ConfigApi.md#get_fts_settings) | **GET** /config/server/{server}/agent/{agent}/mft/fts/settings | Get File Transfer Server (FTS) configuration data.
[**get_hostgroups**](ConfigApi.md#get_hostgroups) | **GET** /config/server/{server}/hostgroups | get Server hostgroups
[**get_hosts_in_group**](ConfigApi.md#get_hosts_in_group) | **GET** /config/server/{server}/hostgroup/{hostgroup}/agents | get hostgroup agents
[**get_hub_status_details**](ConfigApi.md#get_hub_status_details) | **GET** /config/mft/hub/{nodeId}/status | Get hub status.
[**get_mft_configuration**](ConfigApi.md#get_mft_configuration) | **GET** /config/server/{server}/agent/{agent}/mft/configuration | Get MFT Configuration
[**get_mft_folders**](ConfigApi.md#get_mft_folders) | **GET** /config/mft/virtualfolders | Get MFT virtual folders that match the search criteria.
[**get_mft_gateways**](ConfigApi.md#get_mft_gateways) | **GET** /config/mft/gateways | Get MFT gateways
[**get_mft_user_groups**](ConfigApi.md#get_mft_user_groups) | **GET** /config/mft/usergroups | Get all user groups that match the search criteria.
[**get_pgp_templates**](ConfigApi.md#get_pgp_templates) | **GET** /config/server/{server}/agent/{agent}/mft/pgptemplates | Get PGP Templates
[**get_remote_host_properties**](ConfigApi.md#get_remote_host_properties) | **GET** /config/server/{server}/remotehost/{remotehost} | get a remote host configuration from Server
[**get_remote_hosts**](ConfigApi.md#get_remote_hosts) | **GET** /config/server/{server}/remotehosts | get Server remote hosts
[**get_role**](ConfigApi.md#get_role) | **GET** /config/authorization/role/{role} | Get Authorization Role
[**get_role_associates**](ConfigApi.md#get_role_associates) | **GET** /config/authorization/role/{role}/associates | Get all authorization entities associated with role
[**get_run_as_user**](ConfigApi.md#get_run_as_user) | **GET** /config/server/{server}/runasuser/{agent}/{user} | Get Run-as user
[**get_run_as_users_list**](ConfigApi.md#get_run_as_users_list) | **GET** /config/server/{server}/runasusers | Get Run-as user list that match the requested search criteria.
[**get_server_parameters**](ConfigApi.md#get_server_parameters) | **GET** /config/server/{server}/params | get Server parameters
[**get_servers**](ConfigApi.md#get_servers) | **GET** /config/servers | get all the Servers name and hostname in the system
[**get_user**](ConfigApi.md#get_user) | **GET** /config/authorization/user/{user} | Get user
[**get_user_effective_rights**](ConfigApi.md#get_user_effective_rights) | **GET** /config/authorization/user/effectiveRights | Get user real effective authorizations
[**get_zos_templates**](ConfigApi.md#get_zos_templates) | **GET** /config/server/{server}/agent/{agent}/mft/zostemplates | Get z/OS Templates
[**list_secrets**](ConfigApi.md#list_secrets) | **GET** /config/secrets | Get list of secret names
[**ping_agent**](ConfigApi.md#ping_agent) | **POST** /config/server/{server}/agent/{agent}/ping | ping to the agent in the Server
[**recycle_item**](ConfigApi.md#recycle_item) | **POST** /config/item/{id}/recycle | recycle item
[**remove_controlm_server**](ConfigApi.md#remove_controlm_server) | **DELETE** /config/server/{server} | Delete Server
[**remove_gateway**](ConfigApi.md#remove_gateway) | **DELETE** /config/mft/gateway/{gatewayName} | remove gateway.
[**remove_hub_from_cluster**](ConfigApi.md#remove_hub_from_cluster) | **DELETE** /config/mft/cluster/hub/{agentname} | remove hub from cluster.
[**remove_role_from_user**](ConfigApi.md#remove_role_from_user) | **DELETE** /config/authorization/user/{user}/role/{role} | Remove a role from a user
[**send_archive_cleanup_request**](ConfigApi.md#send_archive_cleanup_request) | **DELETE** /config/archive/cleanup | Deletes data (jobs including outputs and logs) from the Workload Archiving database.
[**set_agent_parameter**](ConfigApi.md#set_agent_parameter) | **POST** /config/server/{server}/agent/{agent}/param/{name} | set agent parameter
[**set_system_param**](ConfigApi.md#set_system_param) | **POST** /config/em/param/{name} | set value of a an em system parameter
[**setasprimary**](ConfigApi.md#setasprimary) | **PUT** /config/server/{server}/setasprimary | Set secondary server as Primary on a specified Server
[**test_run_as_user**](ConfigApi.md#test_run_as_user) | **POST** /config/server/{server}/runasuser/{agent}/{user}/test | Test existed Run-as user
[**update_archive_rule**](ConfigApi.md#update_archive_rule) | **POST** /config/archive/rule/{ruleName} | Edit Workload Archiving rule
[**update_external_user**](ConfigApi.md#update_external_user) | **POST** /config/mft/externaluser/{username} | Update an external user
[**update_fts_settings**](ConfigApi.md#update_fts_settings) | **POST** /config/server/{server}/agent/{agent}/mft/fts/settings | Update File Transfer Server (FTS) configuration data.
[**update_hosts_in_hostgroup**](ConfigApi.md#update_hosts_in_hostgroup) | **POST** /config/server/{server}/hostgroup/{hostgroup} | update agents in hostgroup.
[**update_mft_configuration**](ConfigApi.md#update_mft_configuration) | **POST** /config/server/{server}/agent/{agent}/mft/configuration | Update MFT Configuration
[**update_mft_folder**](ConfigApi.md#update_mft_folder) | **POST** /config/mft/virtualfolder/{folderName} | Update an existing virtual folder in MFT.
[**update_mft_user_group**](ConfigApi.md#update_mft_user_group) | **POST** /config/mft/usergroup/{name} | Update user group.
[**update_pgp_template**](ConfigApi.md#update_pgp_template) | **PUT** /config/server/{server}/agent/{agent}/mft/pgptemplate/{templateName} | Update PGP Template
[**update_role**](ConfigApi.md#update_role) | **POST** /config/authorization/role/{role} | Update Authorization Role
[**update_run_as_user**](ConfigApi.md#update_run_as_user) | **POST** /config/server/{server}/runasuser/{agent}/{user} | Update Run-as user
[**update_secret**](ConfigApi.md#update_secret) | **POST** /config/secret/{name} | Update an existing secret
[**update_user**](ConfigApi.md#update_user) | **POST** /config/authorization/user/{user} | Update user
[**update_zos_template**](ConfigApi.md#update_zos_template) | **PUT** /config/server/{server}/agent/{agent}/mft/zostemplate/{templateName} | Update z/OS Template

# **add_archive_rule**
> SuccessData add_archive_rule(body)

Add Workload Archiving rule

Add a new Workload Archiving rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArchiveRule() # ArchiveRule | archive rule details to add

try:
    # Add Workload Archiving rule
    api_response = api_instance.add_archive_rule(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_archive_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArchiveRule**](ArchiveRule.md)| archive rule details to add | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_external_user**
> SuccessData add_external_user(body)

Add and external user

Add and external user for b2b

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.ExternalUserData() # ExternalUserData | External user data

try:
    # Add and external user
    api_response = api_instance.add_external_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_external_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExternalUserData**](ExternalUserData.md)| External user data | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_external_user_or_user_group_to_mft_folder**
> SuccessData add_external_user_or_user_group_to_mft_folder(folder_name, user_or_group)

Add external user or user groups to virtual folder external users list.

Add external user user groups to virtual folder external users list.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
folder_name = 'folder_name_example' # str | Name of folder
user_or_group = 'user_or_group_example' # str | The user name or group name

try:
    # Add external user or user groups to virtual folder external users list.
    api_response = api_instance.add_external_user_or_user_group_to_mft_folder(folder_name, user_or_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_external_user_or_user_group_to_mft_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_name** | **str**| Name of folder | 
 **user_or_group** | **str**| The user name or group name | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_gateway**
> SuccessData add_gateway(body)

add gateway.

add gateway.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.GatewayData() # GatewayData | gateway data

try:
    # add gateway.
    api_response = api_instance.add_gateway(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_gateway: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GatewayData**](GatewayData.md)| gateway data | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_host_to_hostgroup**
> AgentsInGroupSuccessData add_host_to_hostgroup(body, server, hostgroup)

add agent to hostgroup

Add an agent to hostgroup. Create the the hostgroup if it does not exist.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.AgentInGroupParams() # AgentInGroupParams | The hostname of the new agent
server = 'server_example' # str | The Server the hostgroup belongs to.
hostgroup = 'hostgroup_example' # str | The hostgroup name

try:
    # add agent to hostgroup
    api_response = api_instance.add_host_to_hostgroup(body, server, hostgroup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_host_to_hostgroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AgentInGroupParams**](AgentInGroupParams.md)| The hostname of the new agent | 
 **server** | **str**| The Server the hostgroup belongs to. | 
 **hostgroup** | **str**| The hostgroup name | 

### Return type

[**AgentsInGroupSuccessData**](AgentsInGroupSuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_hub_to_cluster**
> SuccessData add_hub_to_cluster(agentname)

add hub to cluster.

add hub to cluster.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
agentname = 'agentname_example' # str | Agent name

try:
    # add hub to cluster.
    api_response = api_instance.add_hub_to_cluster(agentname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_hub_to_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agentname** | **str**| Agent name | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_mft_folder**
> SuccessData add_mft_folder(body)

Add virtual folder

Add virtual folder

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.FolderPropertiesData() # FolderPropertiesData | virtual folder data

try:
    # Add virtual folder
    api_response = api_instance.add_mft_folder(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_mft_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FolderPropertiesData**](FolderPropertiesData.md)| virtual folder data | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_mft_user_group**
> SuccessData add_mft_user_group(body)

Add user group.

Add user group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserGroupPropertiesData() # UserGroupPropertiesData | User group object properites

try:
    # Add user group.
    api_response = api_instance.add_mft_user_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_mft_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserGroupPropertiesData**](UserGroupPropertiesData.md)| User group object properites | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_pgp_template**
> SuccessData add_pgp_template(body, server, agent, template_name)

Add PGP Template

Add PGP Template

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.PgpTemplateData() # PgpTemplateData | PGP Template Data
server = 'server_example' # str | The Server
agent = 'agent_example' # str | The Agent
template_name = 'template_name_example' # str | The PGP Template Name

try:
    # Add PGP Template
    api_response = api_instance.add_pgp_template(body, server, agent, template_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_pgp_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PgpTemplateData**](PgpTemplateData.md)| PGP Template Data | 
 **server** | **str**| The Server | 
 **agent** | **str**| The Agent | 
 **template_name** | **str**| The PGP Template Name | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_remote_host**
> SuccessData add_remote_host(server, body=body)

add remote host to Server

Add a remote host to Server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server the remote host is going to be added to.
body = swagger_client.AddRemoteHostParams() # AddRemoteHostParams | The non default, advanced configuration data (optional)

try:
    # add remote host to Server
    api_response = api_instance.add_remote_host(server, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_remote_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server the remote host is going to be added to. | 
 **body** | [**AddRemoteHostParams**](AddRemoteHostParams.md)| The non default, advanced configuration data | [optional] 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_role**
> SuccessData add_role(role_file)

Add Authorization Role

Add Authorization Role

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
role_file = 'role_file_example' # str | 

try:
    # Add Authorization Role
    api_response = api_instance.add_role(role_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_file** | **str**|  | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_role_to_ldap_group**
> SuccessData add_role_to_ldap_group(ldapgroup, role)

Add a role to LDAP group

Add a role to LDAP group so any user belong to the LDAP group will get all permissions defined in the role

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
ldapgroup = 'ldapgroup_example' # str | Name of LDAP group
role = 'role_example' # str | Name of role

try:
    # Add a role to LDAP group
    api_response = api_instance.add_role_to_ldap_group(ldapgroup, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_role_to_ldap_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldapgroup** | **str**| Name of LDAP group | 
 **role** | **str**| Name of role | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_role_to_user**
> SuccessData add_role_to_user(user, role)

Add a role to user

Add a role to user so that user will inherit role authorization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str | Name of user
role = 'role_example' # str | Name of role

try:
    # Add a role to user
    api_response = api_instance.add_role_to_user(user, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_role_to_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Name of user | 
 **role** | **str**| Name of role | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_secret**
> SuccessData add_secret(body)

Add a new secret

Add a new secret to the secrets vault.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.SecretKeyValue() # SecretKeyValue | The new secret value

try:
    # Add a new secret
    api_response = api_instance.add_secret(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SecretKeyValue**](SecretKeyValue.md)| The new secret value | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_server**
> SuccessData add_server(body)

add server to the system

Add a Server. This command setting up new server in the system

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.AddServerParams() # AddServerParams | 

try:
    # add server to the system
    api_response = api_instance.add_server(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddServerParams**](AddServerParams.md)|  | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_user**
> SuccessData add_user(user_file)

Add user

Add user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
user_file = 'user_file_example' # str | 

try:
    # Add user
    api_response = api_instance.add_user(user_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_file** | **str**|  | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_zos_template**
> SuccessData add_zos_template(body, server, agent, template_name)

Add z/OS Template

Add z/OS Template

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.ZosTemplateData() # ZosTemplateData | z/OS Template Data
server = 'server_example' # str | The Server
agent = 'agent_example' # str | The Agent
template_name = 'template_name_example' # str | The z/OS Template Name

try:
    # Add z/OS Template
    api_response = api_instance.add_zos_template(body, server, agent, template_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->add_zos_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ZosTemplateData**](ZosTemplateData.md)| z/OS Template Data | 
 **server** | **str**| The Server | 
 **agent** | **str**| The Agent | 
 **template_name** | **str**| The z/OS Template Name | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorize_mft_ssh_cluster**
> SuccessData authorize_mft_ssh_cluster(body, server, agent, cluster_name)

Authorize SSH Cluster

Authorize SSH Cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.ClusterAuthorizationData() # ClusterAuthorizationData | File with content of hostnames and ports
server = 'server_example' # str | The Server
agent = 'agent_example' # str | The Agent
cluster_name = 'cluster_name_example' # str | Ssh Cluster Name

try:
    # Authorize SSH Cluster
    api_response = api_instance.authorize_mft_ssh_cluster(body, server, agent, cluster_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->authorize_mft_ssh_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClusterAuthorizationData**](ClusterAuthorizationData.md)| File with content of hostnames and ports | 
 **server** | **str**| The Server | 
 **agent** | **str**| The Agent | 
 **cluster_name** | **str**| Ssh Cluster Name | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorize_mft_ssh_host**
> SuccessData authorize_mft_ssh_host(server, agent, hostname, port=port)

Authorize SSH Host

Authorize SSH Host for SFTP account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server
agent = 'agent_example' # str | The Agent
hostname = 'hostname_example' # str | Ssh Hostname
port = 'port_example' # str | Ssh port for the relevant host (optional)

try:
    # Authorize SSH Host
    api_response = api_instance.authorize_mft_ssh_host(server, agent, hostname, port=port)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->authorize_mft_ssh_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server | 
 **agent** | **str**| The Agent | 
 **hostname** | **str**| Ssh Hostname | 
 **port** | **str**| Ssh port for the relevant host | [optional] 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authorize_ssh_known_remotehost**
> SuccessData authorize_ssh_known_remotehost(server, remotehost)

Authorize

Authorized known ssh remote host.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server the remote host is connected to.
remotehost = 'remotehost_example' # str | The name of the remote host.

try:
    # Authorize
    api_response = api_instance.authorize_ssh_known_remotehost(server, remotehost)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->authorize_ssh_known_remotehost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server the remote host is connected to. | 
 **remotehost** | **str**| The name of the remote host. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user_password**
> SuccessData change_user_password(user, body=body)

Change user password

Change user password

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str | user name
body = swagger_client.UserPassword() # UserPassword | The new password. (optional)

try:
    # Change user password
    api_response = api_instance.change_user_password(user, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->change_user_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| user name | 
 **body** | [**UserPassword**](UserPassword.md)| The new password. | [optional] 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_agent_certificate_signing_request**
> str create_agent_certificate_signing_request(body, server, agent)

Create certificate signing request (CSR).

Create certificate signing request (CSR) on SSL configured Agent.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.CertificateSigningRequestData() # CertificateSigningRequestData | Certificate Signing Request (CSR) data
server = 'server_example' # str | The Server.
agent = 'agent_example' # str | The Agent.

try:
    # Create certificate signing request (CSR).
    api_response = api_instance.create_agent_certificate_signing_request(body, server, agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->create_agent_certificate_signing_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CertificateSigningRequestData**](CertificateSigningRequestData.md)| Certificate Signing Request (CSR) data | 
 **server** | **str**| The Server. | 
 **agent** | **str**| The Agent. | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_run_as_user**
> SuccessData create_run_as_user(body, server)

Add a new Run-as user

Add a new Run-as user to server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.RunAsUserData() # RunAsUserData | Run as user data
server = 'server_example' # str | The Server.

try:
    # Add a new Run-as user
    api_response = api_instance.create_run_as_user(body, server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->create_run_as_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RunAsUserData**](RunAsUserData.md)| Run as user data | 
 **server** | **str**| The Server. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent**
> SuccessData delete_agent(server, agent)

delete an agent from Server

Delete an agent from a Server. This will not shut the agent down. It only disconnects and removes it from the list.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server the agent is connected to.
agent = 'agent_example' # str | The name of the agent to delete.

try:
    # delete an agent from Server
    api_response = api_instance.delete_agent(server, agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->delete_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server the agent is connected to. | 
 **agent** | **str**| The name of the agent to delete. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_archive_rule**
> SuccessData delete_archive_rule(rule_name, delete_rule_data_flag)

Delete Workload Archiving rule

Deletes Workload Archiving rule by name. It is required to send deleteRuleData flag to specify if rule need to be deleted with all the collected data or deleteRuleWithoutData otherwise.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
rule_name = 'rule_name_example' # str | Rule name to delete
delete_rule_data_flag = 'delete_rule_data_flag_example' # str | Remove rule with collected data or without. REQUIRED.

try:
    # Delete Workload Archiving rule
    api_response = api_instance.delete_archive_rule(rule_name, delete_rule_data_flag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->delete_archive_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_name** | **str**| Rule name to delete | 
 **delete_rule_data_flag** | **str**| Remove rule with collected data or without. REQUIRED. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_authorization_role**
> SuccessData delete_authorization_role(role)

Delete Authorization Role

Delete Authorization Role

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
role = 'role_example' # str | The Role name.

try:
    # Delete Authorization Role
    api_response = api_instance.delete_authorization_role(role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->delete_authorization_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The Role name. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_external_user**
> SuccessData delete_external_user(username)

Delete an external user

Delete an existing external user in MFT

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
username = 'username_example' # str | The name of the external user to delete

try:
    # Delete an external user
    api_response = api_instance.delete_external_user(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->delete_external_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The name of the external user to delete | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_external_user_or_user_group_from_mft_folder**
> SuccessData delete_external_user_or_user_group_from_mft_folder(folder_name, user_or_group)

Remove an external user or user group from an existing virtual folder in MFT.

Remove an external user or user group from an existing virtual folder in MFT.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
folder_name = 'folder_name_example' # str | Name of folder
user_or_group = 'user_or_group_example' # str | The user name

try:
    # Remove an external user or user group from an existing virtual folder in MFT.
    api_response = api_instance.delete_external_user_or_user_group_from_mft_folder(folder_name, user_or_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->delete_external_user_or_user_group_from_mft_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_name** | **str**| Name of folder | 
 **user_or_group** | **str**| The user name | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_host_from_group**
> AgentsInGroupSuccessData delete_host_from_group(server, hostgroup, host)

delete an agent from a hostgroup

Delete an agent from the specified hostgroup. If the group is empty it will also be deleted.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server the hostgroup belongs to.
hostgroup = 'hostgroup_example' # str | The hostgroup name
host = 'host_example' # str | The agent to be deleted

try:
    # delete an agent from a hostgroup
    api_response = api_instance.delete_host_from_group(server, hostgroup, host)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->delete_host_from_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server the hostgroup belongs to. | 
 **hostgroup** | **str**| The hostgroup name | 
 **host** | **str**| The agent to be deleted | 

### Return type

[**AgentsInGroupSuccessData**](AgentsInGroupSuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_host_group**
> SuccessData delete_host_group(server, hostgroup)

delete host group

delete host group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server the agent is connected to.
hostgroup = 'hostgroup_example' # str | The hostgroup name

try:
    # delete host group
    api_response = api_instance.delete_host_group(server, hostgroup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->delete_host_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server the agent is connected to. | 
 **hostgroup** | **str**| The hostgroup name | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mft_folder**
> SuccessData delete_mft_folder(folder_name)

Delete a virtual folder.

Delete an existing virtual folder in MFT.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
folder_name = 'folder_name_example' # str | Name of folder

try:
    # Delete a virtual folder.
    api_response = api_instance.delete_mft_folder(folder_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->delete_mft_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_name** | **str**| Name of folder | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mft_user_group**
> SuccessData delete_mft_user_group(name)

Delete user group.

Delete user group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | User group name

try:
    # Delete user group.
    api_response = api_instance.delete_mft_user_group(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->delete_mft_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| User group name | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pgp_template**
> SuccessData delete_pgp_template(server, agent, template_name)

Delete PGP Template

Delete PGP Template

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server
agent = 'agent_example' # str | The Agent
template_name = 'template_name_example' # str | The PGP Template Name

try:
    # Delete PGP Template
    api_response = api_instance.delete_pgp_template(server, agent, template_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->delete_pgp_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server | 
 **agent** | **str**| The Agent | 
 **template_name** | **str**| The PGP Template Name | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_remote_host**
> SuccessData delete_remote_host(server, remotehost)

delete a remote host from Server

Delete a remote host from a Server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server the remote host is connected to.
remotehost = 'remotehost_example' # str | The name of the remote host to delete.

try:
    # delete a remote host from Server
    api_response = api_instance.delete_remote_host(server, remotehost)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->delete_remote_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server the remote host is connected to. | 
 **remotehost** | **str**| The name of the remote host to delete. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_from_ldap_group**
> SuccessData delete_role_from_ldap_group(ldapgroup, role)

Delete a role from LDAP group

Delete a role from LDAP group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
ldapgroup = 'ldapgroup_example' # str | Name of LDAP group
role = 'role_example' # str | Name of role

try:
    # Delete a role from LDAP group
    api_response = api_instance.delete_role_from_ldap_group(ldapgroup, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->delete_role_from_ldap_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldapgroup** | **str**| Name of LDAP group | 
 **role** | **str**| Name of role | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_run_as_user**
> SuccessData delete_run_as_user(server, agent, user)

delete Run-as user

Delete Run-as user from server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server.
agent = 'agent_example' # str | The Agent
user = 'user_example' # str | The user name

try:
    # delete Run-as user
    api_response = api_instance.delete_run_as_user(server, agent, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->delete_run_as_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server. | 
 **agent** | **str**| The Agent | 
 **user** | **str**| The user name | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_secret**
> SuccessData delete_secret(name)

Delete an existing secret

Delete an existing secret from the secrets vault.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | The name of the secret to update

try:
    # Delete an existing secret
    api_response = api_instance.delete_secret(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->delete_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the secret to update | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> SuccessData delete_user(user)

Delete user

Delete user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str | The user name.

try:
    # Delete user
    api_response = api_instance.delete_user(user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The user name. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_zos_template**
> SuccessData delete_zos_template(server, agent, template_name)

Delete z/OS Template

Delete z/OS Template

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server
agent = 'agent_example' # str | The Agent
template_name = 'template_name_example' # str | The z/OS Template Name

try:
    # Delete z/OS Template
    api_response = api_instance.delete_zos_template(server, agent, template_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->delete_zos_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server | 
 **agent** | **str**| The Agent | 
 **template_name** | **str**| The z/OS Template Name | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_agent_certificate**
> SuccessData deploy_agent_certificate(crt_file, ca_chain_file, server, agent)

Deploy certificate (CRT).

Deploy certificate (CRT) on SSL configured Agent.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
crt_file = 'crt_file_example' # str | 
ca_chain_file = 'ca_chain_file_example' # str | 
server = 'server_example' # str | The Server.
agent = 'agent_example' # str | The Agent.

try:
    # Deploy certificate (CRT).
    api_response = api_instance.deploy_agent_certificate(crt_file, ca_chain_file, server, agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->deploy_agent_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crt_file** | **str**|  | 
 **ca_chain_file** | **str**|  | 
 **server** | **str**| The Server. | 
 **agent** | **str**| The Agent. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_agent**
> SuccessData disable_agent(server, agent)

disable agent from the Server

Disable an Agent.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server the agent is connected too.
agent = 'agent_example' # str | The Agent to be disabled.

try:
    # disable agent from the Server
    api_response = api_instance.disable_agent(server, agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->disable_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server the agent is connected too. | 
 **agent** | **str**| The Agent to be disabled. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_agent**
> SuccessData enable_agent(server, agent)

enable agent from the Server

Enable an Agent. This command does not install or configure the agent. It only enable existing agent in the system.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server the agent is connected too.
agent = 'agent_example' # str | The Agent to be enabled.

try:
    # enable agent from the Server
    api_response = api_instance.enable_agent(server, agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->enable_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server the agent is connected too. | 
 **agent** | **str**| The Agent to be enabled. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **failover**
> SuccessData failover(server)

Perform Manual Failover on a specified Server

Perform Manual Failover on a specified Server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | 

try:
    # Perform Manual Failover on a specified Server
    api_response = api_instance.failover(server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->failover: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**|  | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_mft_rsa_ssh_key**
> SuccessData generate_mft_rsa_ssh_key(body, server, agent)

Generate RSA SSH Key

Generate RSA SSH Key pair for SFTP account authentication

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.SshKeyProperties() # SshKeyProperties | Ssh Key pair properites
server = 'server_example' # str | The Server
agent = 'agent_example' # str | The Agent

try:
    # Generate RSA SSH Key
    api_response = api_instance.generate_mft_rsa_ssh_key(body, server, agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->generate_mft_rsa_ssh_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SshKeyProperties**](SshKeyProperties.md)| Ssh Key pair properites | 
 **server** | **str**| The Server | 
 **agent** | **str**| The Agent | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_certificate_expiration_date**
> AgentCertificateExpirationData get_agent_certificate_expiration_date(server, agent)

Get certificate expiration date.

Get the certificate expiration date of SSL configured Agent.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server.
agent = 'agent_example' # str | The Agent.

try:
    # Get certificate expiration date.
    api_response = api_instance.get_agent_certificate_expiration_date(server, agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_agent_certificate_expiration_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server. | 
 **agent** | **str**| The Agent. | 

### Return type

[**AgentCertificateExpirationData**](AgentCertificateExpirationData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_parameters**
> KeyValueListResult get_agent_parameters(server, agent)

get agent parameters

Get all the parameters of the specified Agent.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server the agent is connected to.
agent = 'agent_example' # str | The name of the agent to query.

try:
    # get agent parameters
    api_response = api_instance.get_agent_parameters(server, agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_agent_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server the agent is connected to. | 
 **agent** | **str**| The name of the agent to query. | 

### Return type

[**KeyValueListResult**](KeyValueListResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agents**
> AgentDetailsList get_agents(server, agent=agent)

get Server agents

Get all the agents of the specified Server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server to query. Optionally you can filter agent name of host or alias of the Agent
agent = 'agent_example' # str | Optionally case insensitive agent name filter of host or alias of the Agent. `ctm server:agents::get Server AgentName` returns all agents which names start with `agentname` (optional)

try:
    # get Server agents
    api_response = api_instance.get_agents(server, agent=agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_agents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server to query. Optionally you can filter agent name of host or alias of the Agent | 
 **agent** | **str**| Optionally case insensitive agent name filter of host or alias of the Agent. &#x60;ctm server:agents::get Server AgentName&#x60; returns all agents which names start with &#x60;agentname&#x60; | [optional] 

### Return type

[**AgentDetailsList**](AgentDetailsList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_archive_rules**
> ArchiveRulesList get_all_archive_rules()

Get all Workload Archiving rules

Get all the Archiving rules

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))

try:
    # Get all Workload Archiving rules
    api_response = api_instance.get_all_archive_rules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_all_archive_rules: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ArchiveRulesList**](ArchiveRulesList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_authorization_roles**
> RoleHeaderList get_all_authorization_roles(role=role, description=description)

Get Authorization Roles

Get Authorization Roles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
role = 'role_example' # str | The Role name. (optional)
description = 'description_example' # str | The Role description. (optional)

try:
    # Get Authorization Roles
    api_response = api_instance.get_all_authorization_roles(role=role, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_all_authorization_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The Role name. | [optional] 
 **description** | **str**| The Role description. | [optional] 

### Return type

[**RoleHeaderList**](RoleHeaderList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ldap_groups**
> list[str] get_all_ldap_groups(ldap=ldap)

Get All LDAP groups

Get All LDAP groups

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
ldap = 'ldap_example' # str | The ldap name. (optional)

try:
    # Get All LDAP groups
    api_response = api_instance.get_all_ldap_groups(ldap=ldap)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_all_ldap_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldap** | **str**| The ldap name. | [optional] 

### Return type

**list[str]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_roles_associated_with_ldap**
> list[str] get_all_roles_associated_with_ldap(ldapgroup, role=role)

Get Authorization Roles associated with an LDAP group

Get Authorization Roles associated with an LDAP group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
ldapgroup = 'ldapgroup_example' # str | Name of Ldap group
role = 'role_example' # str | The Role name. (optional)

try:
    # Get Authorization Roles associated with an LDAP group
    api_response = api_instance.get_all_roles_associated_with_ldap(ldapgroup, role=role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_all_roles_associated_with_ldap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldapgroup** | **str**| Name of Ldap group | 
 **role** | **str**| The Role name. | [optional] 

### Return type

**list[str]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_users**
> list[UserHeader] get_all_users(name=name, full_name=full_name, description=description)

Get users

Get users

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | The user name. (optional)
full_name = 'full_name_example' # str | The user full name. (optional)
description = 'description_example' # str | The user description. (optional)

try:
    # Get users
    api_response = api_instance.get_all_users(name=name, full_name=full_name, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_all_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The user name. | [optional] 
 **full_name** | **str**| The user full name. | [optional] 
 **description** | **str**| The user description. | [optional] 

### Return type

[**list[UserHeader]**](UserHeader.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_archive_statistics**
> RulesStatisticListSummary get_archive_statistics()

Get Workload Archiving statistics

Get list of statistical information for each Archiving rule and total information about the number of jobs that have been archived, data size of all job logs and outputs that have been archived, size of the Workload Archiving database including all tables and indexes and percentage of disk space used on the Workload Archiving server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))

try:
    # Get Workload Archiving statistics
    api_response = api_instance.get_archive_statistics()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_archive_statistics: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RulesStatisticListSummary**](RulesStatisticListSummary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_user_authorized_folders**
> list[str] get_external_user_authorized_folders(name)

Get MFT external user authorized folders

Get MFT external user authorized folders

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | The external user name.

try:
    # Get MFT external user authorized folders
    api_response = api_instance.get_external_user_authorized_folders(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_external_user_authorized_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The external user name. | 

### Return type

**list[str]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_users**
> list[ExternalUserData] get_external_users(name=name, email=email, description=description, company=company, phone_number=phone_number)

Get MFT external users that match the search criteria.

Get MFT external users that match the search criteria.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | The user name. (optional)
email = 'email_example' # str | The user email. (optional)
description = 'description_example' # str | The user description. (optional)
company = 'company_example' # str | The user company. (optional)
phone_number = 'phone_number_example' # str | The user phoneNumber. (optional)

try:
    # Get MFT external users that match the search criteria.
    api_response = api_instance.get_external_users(name=name, email=email, description=description, company=company, phone_number=phone_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_external_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The user name. | [optional] 
 **email** | **str**| The user email. | [optional] 
 **description** | **str**| The user description. | [optional] 
 **company** | **str**| The user company. | [optional] 
 **phone_number** | **str**| The user phoneNumber. | [optional] 

### Return type

[**list[ExternalUserData]**](ExternalUserData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fts_settings**
> FtsSettingsData get_fts_settings(server, agent)

Get File Transfer Server (FTS) configuration data.

Get File Transfer Server (FTS) configuration data.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server
agent = 'agent_example' # str | The Agent

try:
    # Get File Transfer Server (FTS) configuration data.
    api_response = api_instance.get_fts_settings(server, agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_fts_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server | 
 **agent** | **str**| The Agent | 

### Return type

[**FtsSettingsData**](FtsSettingsData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hostgroups**
> StringListResult get_hostgroups(server)

get Server hostgroups

Get all the hostgroups of the specified Server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server the hostgroups belong to.

try:
    # get Server hostgroups
    api_response = api_instance.get_hostgroups(server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_hostgroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server the hostgroups belong to. | 

### Return type

[**StringListResult**](StringListResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hosts_in_group**
> AgentsInGroupListResult get_hosts_in_group(server, hostgroup)

get hostgroup agents

Get the agents that compose the specified hostgroup

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server the hostgroup belongs to.
hostgroup = 'hostgroup_example' # str | The hostgroup name

try:
    # get hostgroup agents
    api_response = api_instance.get_hosts_in_group(server, hostgroup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_hosts_in_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server the hostgroup belongs to. | 
 **hostgroup** | **str**| The hostgroup name | 

### Return type

[**AgentsInGroupListResult**](AgentsInGroupListResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hub_status_details**
> str get_hub_status_details(node_id)

Get hub status.

Get hub status.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
node_id = 'node_id_example' # str | Node ID of the hub

try:
    # Get hub status.
    api_response = api_instance.get_hub_status_details(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_hub_status_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Node ID of the hub | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mft_configuration**
> MftConfigurationData get_mft_configuration(server, agent)

Get MFT Configuration

Get MFT Configuration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server
agent = 'agent_example' # str | The Agent

try:
    # Get MFT Configuration
    api_response = api_instance.get_mft_configuration(server, agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_mft_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server | 
 **agent** | **str**| The Agent | 

### Return type

[**MftConfigurationData**](MftConfigurationData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mft_folders**
> list[FolderPropertiesData] get_mft_folders(name=name)

Get MFT virtual folders that match the search criteria.

Get MFT virtual folders that match the search criteria.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | The virtual folder name. (optional)

try:
    # Get MFT virtual folders that match the search criteria.
    api_response = api_instance.get_mft_folders(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_mft_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The virtual folder name. | [optional] 

### Return type

[**list[FolderPropertiesData]**](FolderPropertiesData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mft_gateways**
> list[GatewayData] get_mft_gateways()

Get MFT gateways

Get MFT gateways

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))

try:
    # Get MFT gateways
    api_response = api_instance.get_mft_gateways()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_mft_gateways: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GatewayData]**](GatewayData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mft_user_groups**
> list[UserGroupPropertiesData] get_mft_user_groups(name=name, external_users=external_users, ldap_groups=ldap_groups)

Get all user groups that match the search criteria.

Get all user groups that match the search criteria.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | The user group name. (optional)
external_users = 'external_users_example' # str | external users. (optional)
ldap_groups = 'ldap_groups_example' # str | ldap groups. (optional)

try:
    # Get all user groups that match the search criteria.
    api_response = api_instance.get_mft_user_groups(name=name, external_users=external_users, ldap_groups=ldap_groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_mft_user_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The user group name. | [optional] 
 **external_users** | **str**| external users. | [optional] 
 **ldap_groups** | **str**| ldap groups. | [optional] 

### Return type

[**list[UserGroupPropertiesData]**](UserGroupPropertiesData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pgp_templates**
> list[PgpTemplateData] get_pgp_templates(server, agent, name=name)

Get PGP Templates

Get PGP Templates

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server
agent = 'agent_example' # str | The Agent
name = 'name_example' # str | The PGP Template Name (optional)

try:
    # Get PGP Templates
    api_response = api_instance.get_pgp_templates(server, agent, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_pgp_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server | 
 **agent** | **str**| The Agent | 
 **name** | **str**| The PGP Template Name | [optional] 

### Return type

[**list[PgpTemplateData]**](PgpTemplateData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remote_host_properties**
> AddRemoteHostParams get_remote_host_properties(server, remotehost)

get a remote host configuration from Server

Get the remote host configuration properties from the Server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server the remote host  is connected to.
remotehost = 'remotehost_example' # str | The name of the remote host.

try:
    # get a remote host configuration from Server
    api_response = api_instance.get_remote_host_properties(server, remotehost)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_remote_host_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server the remote host  is connected to. | 
 **remotehost** | **str**| The name of the remote host. | 

### Return type

[**AddRemoteHostParams**](AddRemoteHostParams.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remote_hosts**
> StringListResult get_remote_hosts(server)

get Server remote hosts

Get all the remote hosts of the specified Server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server to query.

try:
    # get Server remote hosts
    api_response = api_instance.get_remote_hosts(server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_remote_hosts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server to query. | 

### Return type

[**StringListResult**](StringListResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> RoleData get_role(role)

Get Authorization Role

Get Authorization Role

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
role = 'role_example' # str | The Role name.

try:
    # Get Authorization Role
    api_response = api_instance.get_role(role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The Role name. | 

### Return type

[**RoleData**](RoleData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_associates**
> list[AssociateData] get_role_associates(role)

Get all authorization entities associated with role

Get all authorization entities associated with role

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
role = 'role_example' # str | role name.

try:
    # Get all authorization entities associated with role
    api_response = api_instance.get_role_associates(role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_role_associates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| role name. | 

### Return type

[**list[AssociateData]**](AssociateData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run_as_user**
> RunAsUserData get_run_as_user(server, agent, user)

Get Run-as user

Get Run-as user details from server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server.
agent = 'agent_example' # str | The Agent
user = 'user_example' # str | The user name

try:
    # Get Run-as user
    api_response = api_instance.get_run_as_user(server, agent, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_run_as_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server. | 
 **agent** | **str**| The Agent | 
 **user** | **str**| The user name | 

### Return type

[**RunAsUserData**](RunAsUserData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run_as_users_list**
> RunAsUsersList get_run_as_users_list(server, user=user, agent=agent)

Get Run-as user list that match the requested search criteria.

Get Run-as user list that match the requested search criteria from server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server.
user = 'user_example' # str | The Run-as user. (optional)
agent = 'agent_example' # str | The agent. (optional)

try:
    # Get Run-as user list that match the requested search criteria.
    api_response = api_instance.get_run_as_users_list(server, user=user, agent=agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_run_as_users_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server. | 
 **user** | **str**| The Run-as user. | [optional] 
 **agent** | **str**| The agent. | [optional] 

### Return type

[**RunAsUsersList**](RunAsUsersList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_parameters**
> KeyValueListResult get_server_parameters(server)

get Server parameters

Get all the parameters of the specified Server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server to query.

try:
    # get Server parameters
    api_response = api_instance.get_server_parameters(server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_server_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server to query. | 

### Return type

[**KeyValueListResult**](KeyValueListResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_servers**
> CtmDetailsList get_servers()

get all the Servers name and hostname in the system

Get the names and hostnames of all Servers in the system.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))

try:
    # get all the Servers name and hostname in the system
    api_response = api_instance.get_servers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_servers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CtmDetailsList**](CtmDetailsList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserData get_user(user)

Get user

Get user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str | The user name.

try:
    # Get user
    api_response = api_instance.get_user(user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| The user name. | 

### Return type

[**UserData**](UserData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_effective_rights**
> RoleData get_user_effective_rights()

Get user real effective authorizations

Get user real effective authorizations by all his roles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))

try:
    # Get user real effective authorizations
    api_response = api_instance.get_user_effective_rights()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_user_effective_rights: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RoleData**](RoleData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zos_templates**
> list[ZosTemplateData] get_zos_templates(server, agent, name=name)

Get z/OS Templates

Get z/OS Templates

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server
agent = 'agent_example' # str | The Agent
name = 'name_example' # str | The z/OS Template Name (optional)

try:
    # Get z/OS Templates
    api_response = api_instance.get_zos_templates(server, agent, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_zos_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server | 
 **agent** | **str**| The Agent | 
 **name** | **str**| The z/OS Template Name | [optional] 

### Return type

[**list[ZosTemplateData]**](ZosTemplateData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_secrets**
> StringListResult list_secrets()

Get list of secret names

Get the list of names of all the secrets in the vault

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))

try:
    # Get list of secret names
    api_response = api_instance.list_secrets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->list_secrets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StringListResult**](StringListResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_agent**
> SuccessData ping_agent(server, agent, body=body)

ping to the agent in the Server

Ping an Agent.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server.
agent = 'agent_example' # str | The Agent.
body = swagger_client.PingAgentParams() # PingAgentParams |  (optional)

try:
    # ping to the agent in the Server
    api_response = api_instance.ping_agent(server, agent, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->ping_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server. | 
 **agent** | **str**| The Agent. | 
 **body** | [**PingAgentParams**](PingAgentParams.md)|  | [optional] 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recycle_item**
> SuccessData recycle_item(id)

recycle item

Recycle an item

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | item data

try:
    # recycle item
    api_response = api_instance.recycle_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->recycle_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| item data | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_controlm_server**
> SuccessData remove_controlm_server(server)

Delete Server

Delete Server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | Server host name.

try:
    # Delete Server
    api_response = api_instance.remove_controlm_server(server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->remove_controlm_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| Server host name. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_gateway**
> SuccessData remove_gateway(gateway_name)

remove gateway.

remove gateway.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
gateway_name = 'gateway_name_example' # str | gateway name

try:
    # remove gateway.
    api_response = api_instance.remove_gateway(gateway_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->remove_gateway: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_name** | **str**| gateway name | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_hub_from_cluster**
> SuccessData remove_hub_from_cluster(agentname)

remove hub from cluster.

remove hub from cluster.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
agentname = 'agentname_example' # str | Agent name

try:
    # remove hub from cluster.
    api_response = api_instance.remove_hub_from_cluster(agentname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->remove_hub_from_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agentname** | **str**| Agent name | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_role_from_user**
> SuccessData remove_role_from_user(user, role)

Remove a role from a user

Remove a role from a user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
user = 'user_example' # str | Name of user
role = 'role_example' # str | Name of role

try:
    # Remove a role from a user
    api_response = api_instance.remove_role_from_user(user, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->remove_role_from_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Name of user | 
 **role** | **str**| Name of role | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_archive_cleanup_request**
> SuccessData send_archive_cleanup_request(application=application, application_exceptions=application_exceptions, sub_application=sub_application, sub_application_exceptions=sub_application_exceptions, ctm=ctm, server=server, ctm_exceptions=ctm_exceptions, server_exceptions=server_exceptions, folder=folder, folder_exceptions=folder_exceptions, jobname=jobname, jobname_exceptions=jobname_exceptions, library=library, library_exceptions=library_exceptions, rule_name=rule_name, job_status=job_status)

Deletes data (jobs including outputs and logs) from the Workload Archiving database.

Deletes data (jobs including outputs and logs) by search criteria from the Workload Archiving database.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
application = 'application_example' # str | Job's application. (optional)
application_exceptions = 'application_exceptions_example' # str | Cleanup should skip job's application that are mentioned in exceptions (optional)
sub_application = 'sub_application_example' # str | Job's sub application (optional)
sub_application_exceptions = 'sub_application_exceptions_example' # str | Job's sub application exception (optional)
ctm = 'ctm_example' # str | server name (optional)
server = 'server_example' # str | Server name (optional)
ctm_exceptions = 'ctm_exceptions_example' # str | server exceptions (optional)
server_exceptions = 'server_exceptions_example' # str | Server exceptions (optional)
folder = 'folder_example' # str | Job's folder. (optional)
folder_exceptions = 'folder_exceptions_example' # str | Job's folder exceptions (optional)
jobname = 'jobname_example' # str | Job's name (optional)
jobname_exceptions = 'jobname_exceptions_example' # str | Job's name exceptions (optional)
library = 'library_example' # str | Job's library (optional)
library_exceptions = 'library_exceptions_example' # str | Job's library exceptions (optional)
rule_name = 'rule_name_example' # str | Job's archive rule (optional)
job_status = 'job_status_example' # str | The job's end status. (optional)

try:
    # Deletes data (jobs including outputs and logs) from the Workload Archiving database.
    api_response = api_instance.send_archive_cleanup_request(application=application, application_exceptions=application_exceptions, sub_application=sub_application, sub_application_exceptions=sub_application_exceptions, ctm=ctm, server=server, ctm_exceptions=ctm_exceptions, server_exceptions=server_exceptions, folder=folder, folder_exceptions=folder_exceptions, jobname=jobname, jobname_exceptions=jobname_exceptions, library=library, library_exceptions=library_exceptions, rule_name=rule_name, job_status=job_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->send_archive_cleanup_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**| Job&#x27;s application. | [optional] 
 **application_exceptions** | **str**| Cleanup should skip job&#x27;s application that are mentioned in exceptions | [optional] 
 **sub_application** | **str**| Job&#x27;s sub application | [optional] 
 **sub_application_exceptions** | **str**| Job&#x27;s sub application exception | [optional] 
 **ctm** | **str**| server name | [optional] 
 **server** | **str**| Server name | [optional] 
 **ctm_exceptions** | **str**| server exceptions | [optional] 
 **server_exceptions** | **str**| Server exceptions | [optional] 
 **folder** | **str**| Job&#x27;s folder. | [optional] 
 **folder_exceptions** | **str**| Job&#x27;s folder exceptions | [optional] 
 **jobname** | **str**| Job&#x27;s name | [optional] 
 **jobname_exceptions** | **str**| Job&#x27;s name exceptions | [optional] 
 **library** | **str**| Job&#x27;s library | [optional] 
 **library_exceptions** | **str**| Job&#x27;s library exceptions | [optional] 
 **rule_name** | **str**| Job&#x27;s archive rule | [optional] 
 **job_status** | **str**| The job&#x27;s end status. | [optional] 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_agent_parameter**
> KeyValue set_agent_parameter(body, server, agent, name)

set agent parameter

Set the value of the specified parameter in the specified agent.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.Value() # Value | The new parameter value.
server = 'server_example' # str | The Server the agent is connected to.
agent = 'agent_example' # str | The name of the agent to update.
name = 'name_example' # str | The parameter name.

try:
    # set agent parameter
    api_response = api_instance.set_agent_parameter(body, server, agent, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->set_agent_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Value**](Value.md)| The new parameter value. | 
 **server** | **str**| The Server the agent is connected to. | 
 **agent** | **str**| The name of the agent to update. | 
 **name** | **str**| The parameter name. | 

### Return type

[**KeyValue**](KeyValue.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_system_param**
> SuccessData set_system_param(body, name)

set value of a an em system parameter

Set value of an enterprise management system parameter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.Value() # Value | Param new value
name = 'name_example' # str | Parameter name

try:
    # set value of a an em system parameter
    api_response = api_instance.set_system_param(body, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->set_system_param: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Value**](Value.md)| Param new value | 
 **name** | **str**| Parameter name | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setasprimary**
> SuccessData setasprimary(server)

Set secondary server as Primary on a specified Server

Set secondary server as Primary on a specified Server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | 

try:
    # Set secondary server as Primary on a specified Server
    api_response = api_instance.setasprimary(server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->setasprimary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**|  | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_run_as_user**
> SuccessData test_run_as_user(server, agent, user, body=body)

Test existed Run-as user

Test existing Run-as user in server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
server = 'server_example' # str | The Server.
agent = 'agent_example' # str | The Agent
user = 'user_example' # str | The user name
body = swagger_client.RunAsUserDetailsData() # RunAsUserDetailsData | Run as user details data (optional)

try:
    # Test existed Run-as user
    api_response = api_instance.test_run_as_user(server, agent, user, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->test_run_as_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Server. | 
 **agent** | **str**| The Agent | 
 **user** | **str**| The user name | 
 **body** | [**RunAsUserDetailsData**](RunAsUserDetailsData.md)| Run as user details data | [optional] 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_archive_rule**
> SuccessData update_archive_rule(body, rule_name)

Edit Workload Archiving rule

Edit Workload Archiving rule details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.ArchiveRule() # ArchiveRule | Edit Workload Archiving rule details
rule_name = 'rule_name_example' # str | Rule name to update

try:
    # Edit Workload Archiving rule
    api_response = api_instance.update_archive_rule(body, rule_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->update_archive_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArchiveRule**](ArchiveRule.md)| Edit Workload Archiving rule details | 
 **rule_name** | **str**| Rule name to update | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_external_user**
> SuccessData update_external_user(body, username)

Update an external user

Update an external user for b2b

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.ExternalUserData() # ExternalUserData | External user data
username = 'username_example' # str | The external user name

try:
    # Update an external user
    api_response = api_instance.update_external_user(body, username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->update_external_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExternalUserData**](ExternalUserData.md)| External user data | 
 **username** | **str**| The external user name | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fts_settings**
> SuccessData update_fts_settings(body, server, agent)

Update File Transfer Server (FTS) configuration data.

Update File Transfer Server (FTS) configuration data.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.FtsSettingsData() # FtsSettingsData | File Transfer Server (FTS) configuration data
server = 'server_example' # str | The Server
agent = 'agent_example' # str | The Agent

try:
    # Update File Transfer Server (FTS) configuration data.
    api_response = api_instance.update_fts_settings(body, server, agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->update_fts_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FtsSettingsData**](FtsSettingsData.md)| File Transfer Server (FTS) configuration data | 
 **server** | **str**| The Server | 
 **agent** | **str**| The Agent | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_hosts_in_hostgroup**
> SuccessData update_hosts_in_hostgroup(body, server, hostgroup)

update agents in hostgroup.

update agents in hostgroup.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.AgentInGroupParamsList() # AgentInGroupParamsList | Agent list to update in a hostgroup
server = 'server_example' # str | The Server the agent is connected to.
hostgroup = 'hostgroup_example' # str | The hostgroup name

try:
    # update agents in hostgroup.
    api_response = api_instance.update_hosts_in_hostgroup(body, server, hostgroup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->update_hosts_in_hostgroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AgentInGroupParamsList**](AgentInGroupParamsList.md)| Agent list to update in a hostgroup | 
 **server** | **str**| The Server the agent is connected to. | 
 **hostgroup** | **str**| The hostgroup name | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mft_configuration**
> SuccessData update_mft_configuration(body, server, agent)

Update MFT Configuration

Update MFT Configuration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.MftConfigurationData() # MftConfigurationData | MFT Configuration Data
server = 'server_example' # str | The Server
agent = 'agent_example' # str | The Agent

try:
    # Update MFT Configuration
    api_response = api_instance.update_mft_configuration(body, server, agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->update_mft_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MftConfigurationData**](MftConfigurationData.md)| MFT Configuration Data | 
 **server** | **str**| The Server | 
 **agent** | **str**| The Agent | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mft_folder**
> SuccessData update_mft_folder(body, folder_name)

Update an existing virtual folder in MFT.

Update an existing virtual folder in MFT.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.FolderPropertiesData() # FolderPropertiesData | virtual folder data
folder_name = 'folder_name_example' # str | Name of folder

try:
    # Update an existing virtual folder in MFT.
    api_response = api_instance.update_mft_folder(body, folder_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->update_mft_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FolderPropertiesData**](FolderPropertiesData.md)| virtual folder data | 
 **folder_name** | **str**| Name of folder | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mft_user_group**
> SuccessData update_mft_user_group(body, name)

Update user group.

Update user group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserGroupDetailsData() # UserGroupDetailsData | User group details
name = 'name_example' # str | User group name

try:
    # Update user group.
    api_response = api_instance.update_mft_user_group(body, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->update_mft_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserGroupDetailsData**](UserGroupDetailsData.md)| User group details | 
 **name** | **str**| User group name | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pgp_template**
> SuccessData update_pgp_template(body, server, agent, template_name)

Update PGP Template

Update PGP Template

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.PgpTemplateData() # PgpTemplateData | PGP Template Data
server = 'server_example' # str | The Server
agent = 'agent_example' # str | The Agent
template_name = 'template_name_example' # str | The PGP Template Name

try:
    # Update PGP Template
    api_response = api_instance.update_pgp_template(body, server, agent, template_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->update_pgp_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PgpTemplateData**](PgpTemplateData.md)| PGP Template Data | 
 **server** | **str**| The Server | 
 **agent** | **str**| The Agent | 
 **template_name** | **str**| The PGP Template Name | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> SuccessData update_role(role_file, role)

Update Authorization Role

Update Authorization Role

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
role_file = 'role_file_example' # str | 
role = 'role_example' # str | The Role name.

try:
    # Update Authorization Role
    api_response = api_instance.update_role(role_file, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->update_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_file** | **str**|  | 
 **role** | **str**| The Role name. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_run_as_user**
> SuccessData update_run_as_user(body, server, agent, user)

Update Run-as user

Update Run-as user details in server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.RunAsUserDetailsData() # RunAsUserDetailsData | Run as user details data
server = 'server_example' # str | The Server.
agent = 'agent_example' # str | The Agent
user = 'user_example' # str | The user name

try:
    # Update Run-as user
    api_response = api_instance.update_run_as_user(body, server, agent, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->update_run_as_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RunAsUserDetailsData**](RunAsUserDetailsData.md)| Run as user details data | 
 **server** | **str**| The Server. | 
 **agent** | **str**| The Agent | 
 **user** | **str**| The user name | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_secret**
> SuccessData update_secret(name, body=body)

Update an existing secret

Update an existing secret in the secrets vault.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | The name of the secret to update
body = swagger_client.SecretValue() # SecretValue | The new value for the secret (optional)

try:
    # Update an existing secret
    api_response = api_instance.update_secret(name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->update_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the secret to update | 
 **body** | [**SecretValue**](SecretValue.md)| The new value for the secret | [optional] 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> SuccessData update_user(user_file, user)

Update user

Update user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
user_file = 'user_file_example' # str | 
user = 'user_example' # str | The user name.

try:
    # Update user
    api_response = api_instance.update_user(user_file, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_file** | **str**|  | 
 **user** | **str**| The user name. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_zos_template**
> SuccessData update_zos_template(body, server, agent, template_name)

Update z/OS Template

Update z/OS Template

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
body = swagger_client.ZosTemplateData() # ZosTemplateData | z/OS Template Data
server = 'server_example' # str | The Server
agent = 'agent_example' # str | The Agent
template_name = 'template_name_example' # str | The z/OS Template Name

try:
    # Update z/OS Template
    api_response = api_instance.update_zos_template(body, server, agent, template_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->update_zos_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ZosTemplateData**](ZosTemplateData.md)| z/OS Template Data | 
 **server** | **str**| The Server | 
 **agent** | **str**| The Agent | 
 **template_name** | **str**| The z/OS Template Name | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

