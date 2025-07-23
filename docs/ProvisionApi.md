# controlm_py.ProvisionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_provision_repo**](ProvisionApi.md#add_provision_repo) | **POST** /provision/repository | Add a configuration of a local repository.
[**cancel_upgrade_activity**](ProvisionApi.md#cancel_upgrade_activity) | **POST** /provision/upgrade/{upgradeId}/cancel | Cancel upgrade activity
[**delete_provision_repo**](ProvisionApi.md#delete_provision_repo) | **DELETE** /provision/repository/{repoName} | Delete configuration of a local repository
[**delete_upgrade_activity**](ProvisionApi.md#delete_upgrade_activity) | **DELETE** /provision/upgrade/{upgradeId} | Delete upgrade activity status for specific upgrade id.
[**get_all_upgrade_activities_status**](ProvisionApi.md#get_all_upgrade_activities_status) | **GET** /provision/upgrades | Get all upgrade activities status.
[**get_deploy_versions**](ProvisionApi.md#get_deploy_versions) | **GET** /provision/upgrades/versions | Get available versions for upgrade.
[**get_eligible_agents_for_upgrade**](ProvisionApi.md#get_eligible_agents_for_upgrade) | **GET** /provision/upgrades/agents | Get eligible agents for upgrade that match the requested search criteria.
[**get_images**](ProvisionApi.md#get_images) | **GET** /provision/images/{os} | get list of available images for the requested OS
[**get_provision_repo**](ProvisionApi.md#get_provision_repo) | **GET** /provision/repository/{repoName} | Get the configuration of the local repo from EM
[**get_upgrade_activity_log**](ProvisionApi.md#get_upgrade_activity_log) | **GET** /provision/upgrade/{upgradeId}/output | Returns log of upgrade activity.
[**get_upgrade_activity_status_per_upgrade_id**](ProvisionApi.md#get_upgrade_activity_status_per_upgrade_id) | **GET** /provision/upgrade/{upgradeId} | Get upgrade activity status for specific upgrade id.
[**list_provision_repos**](ProvisionApi.md#list_provision_repos) | **GET** /provision/repositories | Get the configuration of all the local repos from EM
[**retry_upgrade_activity**](ProvisionApi.md#retry_upgrade_activity) | **POST** /provision/upgrade/{upgradeId}/retry | Retry upgrade activity
[**transfer_and_install_product**](ProvisionApi.md#transfer_and_install_product) | **POST** /provision/upgrade/install | Transfer and install a product on an agent
[**uninstall_product**](ProvisionApi.md#uninstall_product) | **POST** /provision/upgrade/uninstall | Uninstall a product from an agent

# **add_provision_repo**
> ProvisionRepo add_provision_repo(repo_name, location, description=description, helix_repo=helix_repo)

Add a configuration of a local repository.

Add a configuration of a local repository.

### Example
```python
from __future__ import print_function
import time
import controlm_py
from controlm_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = controlm_py.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure API key authorization: Bearer
configuration = controlm_py.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_py.ProvisionApi(controlm_py.ApiClient(configuration))
repo_name = 'repo_name_example' # str | 
location = 'location_example' # str | 
description = 'description_example' # str |  (optional)
helix_repo = false # bool | True means this is a Helix repository. Otherwise it is an on-prem repo. Default is on prem (optional) (default to false)

try:
    # Add a configuration of a local repository.
    api_response = api_instance.add_provision_repo(repo_name, location, description=description, helix_repo=helix_repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionApi->add_provision_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**|  | 
 **location** | **str**|  | 
 **description** | **str**|  | [optional] 
 **helix_repo** | **bool**| True means this is a Helix repository. Otherwise it is an on-prem repo. Default is on prem | [optional] [default to false]

### Return type

[**ProvisionRepo**](ProvisionRepo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_upgrade_activity**
> SuccessData cancel_upgrade_activity(upgrade_id)

Cancel upgrade activity

Cancel upgrade activity

### Example
```python
from __future__ import print_function
import time
import controlm_py
from controlm_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = controlm_py.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure API key authorization: Bearer
configuration = controlm_py.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_py.ProvisionApi(controlm_py.ApiClient(configuration))
upgrade_id = 'upgrade_id_example' # str | Id of upgrade to cancel

try:
    # Cancel upgrade activity
    api_response = api_instance.cancel_upgrade_activity(upgrade_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionApi->cancel_upgrade_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upgrade_id** | **str**| Id of upgrade to cancel | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_provision_repo**
> ProvisionReposResults delete_provision_repo(repo_name)

Delete configuration of a local repository

Delete configuration of a local repository which is identified with the ID specified.

### Example
```python
from __future__ import print_function
import time
import controlm_py
from controlm_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = controlm_py.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure API key authorization: Bearer
configuration = controlm_py.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_py.ProvisionApi(controlm_py.ApiClient(configuration))
repo_name = 'repo_name_example' # str | The name of the local repository configuratioin to be deleted.

try:
    # Delete configuration of a local repository
    api_response = api_instance.delete_provision_repo(repo_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionApi->delete_provision_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| The name of the local repository configuratioin to be deleted. | 

### Return type

[**ProvisionReposResults**](ProvisionReposResults.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_upgrade_activity**
> SuccessData delete_upgrade_activity(upgrade_id)

Delete upgrade activity status for specific upgrade id.

Delete upgrade activity status for specific upgrade id.

### Example
```python
from __future__ import print_function
import time
import controlm_py
from controlm_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = controlm_py.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure API key authorization: Bearer
configuration = controlm_py.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_py.ProvisionApi(controlm_py.ApiClient(configuration))
upgrade_id = 'upgrade_id_example' # str | The upgrade id.

try:
    # Delete upgrade activity status for specific upgrade id.
    api_response = api_instance.delete_upgrade_activity(upgrade_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionApi->delete_upgrade_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upgrade_id** | **str**| The upgrade id. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_upgrade_activities_status**
> UpgradeRecordList get_all_upgrade_activities_status(ctm=ctm, server=server, agent=agent, from_version=from_version, to_version=to_version, activity=activity, status=status, activity_name=activity_name)

Get all upgrade activities status.

Get all upgrade activities status.

### Example
```python
from __future__ import print_function
import time
import controlm_py
from controlm_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = controlm_py.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure API key authorization: Bearer
configuration = controlm_py.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_py.ProvisionApi(controlm_py.ApiClient(configuration))
ctm = 'ctm_example' # str | The Control-M server name (optional)
server = 'server_example' # str | The Control-M server name (optional)
agent = 'agent_example' # str | The Control-M Agent name (optional)
from_version = 'from_version_example' # str | Current product version (optional)
to_version = 'to_version_example' # str | Upgrade to version (optional)
activity = 'activity_example' # str | Activity type (Install, Uninstall) (optional)
status = 'status_example' # str | Upgrade activity status (Cancel, Running, Completed, TransferCompleted, Failed, Unavailable) (optional)
activity_name = 'activity_name_example' # str | Name of the upgrade activity (optional)

try:
    # Get all upgrade activities status.
    api_response = api_instance.get_all_upgrade_activities_status(ctm=ctm, server=server, agent=agent, from_version=from_version, to_version=to_version, activity=activity, status=status, activity_name=activity_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionApi->get_all_upgrade_activities_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| The Control-M server name | [optional] 
 **server** | **str**| The Control-M server name | [optional] 
 **agent** | **str**| The Control-M Agent name | [optional] 
 **from_version** | **str**| Current product version | [optional] 
 **to_version** | **str**| Upgrade to version | [optional] 
 **activity** | **str**| Activity type (Install, Uninstall) | [optional] 
 **status** | **str**| Upgrade activity status (Cancel, Running, Completed, TransferCompleted, Failed, Unavailable) | [optional] 
 **activity_name** | **str**| Name of the upgrade activity | [optional] 

### Return type

[**UpgradeRecordList**](UpgradeRecordList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deploy_versions**
> list[UpgradeInfo] get_deploy_versions()

Get available versions for upgrade.

Get available versions for upgrade

### Example
```python
from __future__ import print_function
import time
import controlm_py
from controlm_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = controlm_py.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure API key authorization: Bearer
configuration = controlm_py.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_py.ProvisionApi(controlm_py.ApiClient(configuration))

try:
    # Get available versions for upgrade.
    api_response = api_instance.get_deploy_versions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionApi->get_deploy_versions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UpgradeInfo]**](UpgradeInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_eligible_agents_for_upgrade**
> UpgradeAgentInfoList get_eligible_agents_for_upgrade(type=type, version=version)

Get eligible agents for upgrade that match the requested search criteria.

Get eligible agents for upgrade that match the requested search criteria from Control-M server.

### Example
```python
from __future__ import print_function
import time
import controlm_py
from controlm_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = controlm_py.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure API key authorization: Bearer
configuration = controlm_py.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_py.ProvisionApi(controlm_py.ApiClient(configuration))
type = 'type_example' # str | The type (Agent, MFT, AppPack). (optional)
version = 'version_example' # str | The version. (optional)

try:
    # Get eligible agents for upgrade that match the requested search criteria.
    api_response = api_instance.get_eligible_agents_for_upgrade(type=type, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionApi->get_eligible_agents_for_upgrade: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type (Agent, MFT, AppPack). | [optional] 
 **version** | **str**| The version. | [optional] 

### Return type

[**UpgradeAgentInfoList**](UpgradeAgentInfoList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_images**
> StringListResult get_images(os, version=version)

get list of available images for the requested OS

Get a list of the images in the system for the requested OS.

### Example
```python
from __future__ import print_function
import time
import controlm_py
from controlm_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = controlm_py.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure API key authorization: Bearer
configuration = controlm_py.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_py.ProvisionApi(controlm_py.ApiClient(configuration))
os = 'os_example' # str | The OS name of the requested images.
version = 'version_example' # str | filter according to specific version. (optional)

try:
    # get list of available images for the requested OS
    api_response = api_instance.get_images(os, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionApi->get_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **os** | **str**| The OS name of the requested images. | 
 **version** | **str**| filter according to specific version. | [optional] 

### Return type

[**StringListResult**](StringListResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_provision_repo**
> ProvisionRepo get_provision_repo(repo_name)

Get the configuration of the local repo from EM

Get the configuration of the local repo from EM

### Example
```python
from __future__ import print_function
import time
import controlm_py
from controlm_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = controlm_py.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure API key authorization: Bearer
configuration = controlm_py.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_py.ProvisionApi(controlm_py.ApiClient(configuration))
repo_name = 'repo_name_example' # str | Local repo configuration name

try:
    # Get the configuration of the local repo from EM
    api_response = api_instance.get_provision_repo(repo_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionApi->get_provision_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Local repo configuration name | 

### Return type

[**ProvisionRepo**](ProvisionRepo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_activity_log**
> str get_upgrade_activity_log(upgrade_id)

Returns log of upgrade activity.

Returns log of upgrade activity

### Example
```python
from __future__ import print_function
import time
import controlm_py
from controlm_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = controlm_py.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure API key authorization: Bearer
configuration = controlm_py.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_py.ProvisionApi(controlm_py.ApiClient(configuration))
upgrade_id = 'upgrade_id_example' # str | The upgrade id.

try:
    # Returns log of upgrade activity.
    api_response = api_instance.get_upgrade_activity_log(upgrade_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionApi->get_upgrade_activity_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upgrade_id** | **str**| The upgrade id. | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_activity_status_per_upgrade_id**
> UpgradeRecord get_upgrade_activity_status_per_upgrade_id(upgrade_id)

Get upgrade activity status for specific upgrade id.

Get upgrade activity status for specific upgrade id.

### Example
```python
from __future__ import print_function
import time
import controlm_py
from controlm_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = controlm_py.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure API key authorization: Bearer
configuration = controlm_py.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_py.ProvisionApi(controlm_py.ApiClient(configuration))
upgrade_id = 'upgrade_id_example' # str | The upgrade id.

try:
    # Get upgrade activity status for specific upgrade id.
    api_response = api_instance.get_upgrade_activity_status_per_upgrade_id(upgrade_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionApi->get_upgrade_activity_status_per_upgrade_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upgrade_id** | **str**| The upgrade id. | 

### Return type

[**UpgradeRecord**](UpgradeRecord.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_provision_repos**
> ProvisionReposResults list_provision_repos()

Get the configuration of all the local repos from EM

Get the configuration of all the local repos from EM

### Example
```python
from __future__ import print_function
import time
import controlm_py
from controlm_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = controlm_py.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure API key authorization: Bearer
configuration = controlm_py.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_py.ProvisionApi(controlm_py.ApiClient(configuration))

try:
    # Get the configuration of all the local repos from EM
    api_response = api_instance.list_provision_repos()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionApi->list_provision_repos: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProvisionReposResults**](ProvisionReposResults.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_upgrade_activity**
> SuccessData retry_upgrade_activity(upgrade_id)

Retry upgrade activity

Retry upgrade activity

### Example
```python
from __future__ import print_function
import time
import controlm_py
from controlm_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = controlm_py.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure API key authorization: Bearer
configuration = controlm_py.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_py.ProvisionApi(controlm_py.ApiClient(configuration))
upgrade_id = 'upgrade_id_example' # str | Id of upgrade to retry

try:
    # Retry upgrade activity
    api_response = api_instance.retry_upgrade_activity(upgrade_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionApi->retry_upgrade_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upgrade_id** | **str**| Id of upgrade to retry | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_and_install_product**
> UpgradeResponse transfer_and_install_product(body)

Transfer and install a product on an agent

Transfer and install a product on an agent

### Example
```python
from __future__ import print_function
import time
import controlm_py
from controlm_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = controlm_py.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure API key authorization: Bearer
configuration = controlm_py.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_py.ProvisionApi(controlm_py.ApiClient(configuration))
body = controlm_py.UpgradeRequest() # UpgradeRequest | Upgrade request details

try:
    # Transfer and install a product on an agent
    api_response = api_instance.transfer_and_install_product(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionApi->transfer_and_install_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpgradeRequest**](UpgradeRequest.md)| Upgrade request details | 

### Return type

[**UpgradeResponse**](UpgradeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uninstall_product**
> UpgradeResponse uninstall_product(body)

Uninstall a product from an agent

Uninstall a product from an agent

### Example
```python
from __future__ import print_function
import time
import controlm_py
from controlm_py.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = controlm_py.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'
# Configure API key authorization: Bearer
configuration = controlm_py.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = controlm_py.ProvisionApi(controlm_py.ApiClient(configuration))
body = controlm_py.UpgradeRequest() # UpgradeRequest | Rollback request details

try:
    # Uninstall a product from an agent
    api_response = api_instance.uninstall_product(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvisionApi->uninstall_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpgradeRequest**](UpgradeRequest.md)| Rollback request details | 

### Return type

[**UpgradeResponse**](UpgradeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

