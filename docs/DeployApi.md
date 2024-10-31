# controlm_py.DeployApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_calendar**](DeployApi.md#delete_calendar) | **DELETE** /deploy/calendar/{calendarName} | delete a calendar
[**delete_connection_profile**](DeployApi.md#delete_connection_profile) | **DELETE** /deploy/connectionprofile/{server}/{agent}/{type}/{name} | Delete Local Connection Profile
[**delete_folder**](DeployApi.md#delete_folder) | **DELETE** /deploy/folder/{server}/{folderName} | delete a folder
[**delete_job_path**](DeployApi.md#delete_job_path) | **DELETE** /deploy/job/{jobPath} | delete a job
[**delete_local_connection_profile**](DeployApi.md#delete_local_connection_profile) | **DELETE** /deploy/connectionprofile/local/{server}/{agent}/{type}/{name} | Delete Local Connection Profile
[**delete_shared_connection_profile**](DeployApi.md#delete_shared_connection_profile) | **DELETE** /deploy/connectionprofile/centralized/{type}/{name} | Delete centralized Connection Profile
[**delete_site_standard**](DeployApi.md#delete_site_standard) | **DELETE** /deploy/sitestandard/{siteStandardName} | Delete a Site Standard.
[**delete_site_standard_policy**](DeployApi.md#delete_site_standard_policy) | **DELETE** /deploy/sitestandardpolicy/{siteStandardPolicyName} | Delete a Site Standard Policy.
[**delete_sub_folder**](DeployApi.md#delete_sub_folder) | **DELETE** /deploy/subfolder/{subFolderPath} | delete a sub folder
[**deploy_ai_jobtype**](DeployApi.md#deploy_ai_jobtype) | **POST** /deploy/ai/jobtype | Deploy of Application Integrator job type.
[**deploy_file**](DeployApi.md#deploy_file) | **POST** /deploy | Deploy definitions file
[**deploy_jobtype_file**](DeployApi.md#deploy_jobtype_file) | **POST** /deploy/jobtype | Deploy jobtype
[**deploy_site_standard_policies**](DeployApi.md#deploy_site_standard_policies) | **POST** /deploy/sitestandardpolicies | Deploy Site Standard Policies.
[**get_connection_profiles_deployment_status**](DeployApi.md#get_connection_profiles_deployment_status) | **GET** /deploy/connectionprofile/centralized/deploymentstatus/{type}/{name} | Get deployed connection profiles deployment status
[**get_ctm_ai_job_type_plugin**](DeployApi.md#get_ctm_ai_job_type_plugin) | **GET** /deploy/jobtype | Get AI based job type content
[**get_deployed_ai_jobtypes**](DeployApi.md#get_deployed_ai_jobtypes) | **GET** /deploy/ai/jobtypes | Get Application Integrator job types
[**get_deployed_calendars**](DeployApi.md#get_deployed_calendars) | **GET** /deploy/calendars | Get deployed calendars that match the search criteria.
[**get_deployed_connection_profiles**](DeployApi.md#get_deployed_connection_profiles) | **GET** /deploy/connectionprofiles | Get local deployed connection profiles
[**get_deployed_connection_profiles_status**](DeployApi.md#get_deployed_connection_profiles_status) | **GET** /deploy/connectionprofiles/centralized/status | Get deployed connection profiles status
[**get_deployed_folders**](DeployApi.md#get_deployed_folders) | **GET** /deploy/folders | Get deployed folders that match the search criteria.
[**get_deployed_folders_new**](DeployApi.md#get_deployed_folders_new) | **GET** /deploy/jobs | Get deployed jobs that match the search criteria.
[**get_local_connection_profiles**](DeployApi.md#get_local_connection_profiles) | **GET** /deploy/connectionprofiles/local | Get local deployed connection profiles
[**get_shared_connection_profiles**](DeployApi.md#get_shared_connection_profiles) | **GET** /deploy/connectionprofiles/centralized | Get centralized deployed connection profile
[**get_site_standard_field_restrictions**](DeployApi.md#get_site_standard_field_restrictions) | **GET** /deploy/sitestandard/{standardName}/fieldRestriction/{fieldName} | Get the allowed values for the specified field in the specified site standard.
[**get_site_standard_policies**](DeployApi.md#get_site_standard_policies) | **GET** /deploy/sitestandardpolicies | Get definitions of deployed Site Standard Policies that match the search criteria.
[**get_site_standard_policies_details**](DeployApi.md#get_site_standard_policies_details) | **GET** /deploy/sitestandardpolicies/details | Get details of deployed Site Standard Policies that match the search criteria.
[**get_site_standards**](DeployApi.md#get_site_standards) | **GET** /deploy/sitestandards | Get definitions of deployed Site Standards that match the search criteria.
[**get_site_standards_details**](DeployApi.md#get_site_standards_details) | **GET** /deploy/sitestandards/details | Get details of deployed Site Standards that match the search criteria.
[**poll_deploy_results**](DeployApi.md#poll_deploy_results) | **GET** /deploy/poll | Get the deploy result
[**rename_site_standard**](DeployApi.md#rename_site_standard) | **POST** /deploy/sitestandard/{siteStandardName} | Rename deployed Site Standard.
[**rename_site_standard_policy**](DeployApi.md#rename_site_standard_policy) | **POST** /deploy/sitestandardpolicy/{siteStandardPolicyName} | Rename deployed Site Standard Policy.
[**set_site_standard_field_restrictions**](DeployApi.md#set_site_standard_field_restrictions) | **POST** /deploy/sitestandard/{standardName}/fieldRestriction/{fieldName} | Replace the allowed values for the specified field in the specified site standard.
[**test_centralized_connection_profile**](DeployApi.md#test_centralized_connection_profile) | **POST** /deploy/connectionprofile/centralized/test/{type}/{name}/{server}/{agent} | Test connection profile centralized on agent
[**test_connection_profile**](DeployApi.md#test_connection_profile) | **POST** /deploy/connectionprofile/test | Test connection profile on agent
[**transform_file**](DeployApi.md#transform_file) | **POST** /deploy/transform | Transform a definitions file

# **delete_calendar**
> SuccessData delete_calendar(calendar_name, server=server)

delete a calendar

Delete a calendar

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
calendar_name = 'calendar_name_example' # str | The name of the calendar to be deleted.
server = 'Global' # str | The name of the server in which the calendar deploy. (optional) (default to Global)

try:
    # delete a calendar
    api_response = api_instance.delete_calendar(calendar_name, server=server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->delete_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calendar_name** | **str**| The name of the calendar to be deleted. | 
 **server** | **str**| The name of the server in which the calendar deploy. | [optional] [default to Global]

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connection_profile**
> SuccessData delete_connection_profile(server, agent, type, name)

Delete Local Connection Profile

Delete Local Connection Profile.

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
server = 'server_example' # str | The name of the Control-M in which the connection profile is deployed.
agent = 'agent_example' # str | The name of the agent the connection profile is deployed on.
type = 'type_example' # str | The type of connection profile to delete.
name = 'name_example' # str | Name of the Connection Profile

try:
    # Delete Local Connection Profile
    api_response = api_instance.delete_connection_profile(server, agent, type, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->delete_connection_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The name of the Control-M in which the connection profile is deployed. | 
 **agent** | **str**| The name of the agent the connection profile is deployed on. | 
 **type** | **str**| The type of connection profile to delete. | 
 **name** | **str**| Name of the Connection Profile | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> SuccessData delete_folder(server, folder_name, library=library)

delete a folder

Delete a folder

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
server = 'server_example' # str | The name of the Control-M in which the folder(s) are deployed.
folder_name = 'folder_name_example' # str | The name of the required folder(s).
library = 'library_example' # str | library be filled only for z/os. (optional)

try:
    # delete a folder
    api_response = api_instance.delete_folder(server, folder_name, library=library)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->delete_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The name of the Control-M in which the folder(s) are deployed. | 
 **folder_name** | **str**| The name of the required folder(s). | 
 **library** | **str**| library be filled only for z/os. | [optional] 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job_path**
> SuccessData delete_job_path(job_path, server=server, library=library)

delete a job

Delete a job

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
job_path = 'job_path_example' # str | The name of the required jobPath.
server = 'Global' # str | The name of the Control-M in which the job are deployed. (optional) (default to Global)
library = 'library_example' # str | library be filled only for z/os. (optional)

try:
    # delete a job
    api_response = api_instance.delete_job_path(job_path, server=server, library=library)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->delete_job_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_path** | **str**| The name of the required jobPath. | 
 **server** | **str**| The name of the Control-M in which the job are deployed. | [optional] [default to Global]
 **library** | **str**| library be filled only for z/os. | [optional] 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_local_connection_profile**
> SuccessData delete_local_connection_profile(server, agent, type, name)

Delete Local Connection Profile

Delete Local Connection Profile

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
server = 'server_example' # str | The name of the Control-M in which the connection profile is deployed.
agent = 'agent_example' # str | The name of the agent the connection profile is deployed on.
type = 'type_example' # str | The type of connection profile to delete.
name = 'name_example' # str | Name of the Connection Profile

try:
    # Delete Local Connection Profile
    api_response = api_instance.delete_local_connection_profile(server, agent, type, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->delete_local_connection_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The name of the Control-M in which the connection profile is deployed. | 
 **agent** | **str**| The name of the agent the connection profile is deployed on. | 
 **type** | **str**| The type of connection profile to delete. | 
 **name** | **str**| Name of the Connection Profile | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shared_connection_profile**
> SuccessData delete_shared_connection_profile(type, name)

Delete centralized Connection Profile

Delete centralized Connection Profile

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
type = 'type_example' # str | The type of connection profile to delete.
name = 'name_example' # str | Name of the Connection Profile

try:
    # Delete centralized Connection Profile
    api_response = api_instance.delete_shared_connection_profile(type, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->delete_shared_connection_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of connection profile to delete. | 
 **name** | **str**| Name of the Connection Profile | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_site_standard**
> SuccessData delete_site_standard(site_standard_name)

Delete a Site Standard.

Delete a Site Standard.

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
site_standard_name = 'site_standard_name_example' # str | The name of the Site Standard to be deleted.

try:
    # Delete a Site Standard.
    api_response = api_instance.delete_site_standard(site_standard_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->delete_site_standard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_standard_name** | **str**| The name of the Site Standard to be deleted. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_site_standard_policy**
> SuccessData delete_site_standard_policy(site_standard_policy_name)

Delete a Site Standard Policy.

Delete a Site Standard Policy.

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
site_standard_policy_name = 'site_standard_policy_name_example' # str | The name of the Site Standard Policy to be deleted.

try:
    # Delete a Site Standard Policy.
    api_response = api_instance.delete_site_standard_policy(site_standard_policy_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->delete_site_standard_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_standard_policy_name** | **str**| The name of the Site Standard Policy to be deleted. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sub_folder**
> SuccessData delete_sub_folder(sub_folder_path, server=server, library=library)

delete a sub folder

Delete a sub folder

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
sub_folder_path = 'sub_folder_path_example' # str | The name of the required subFolderPath.
server = 'Global' # str | The name of the Control-M in which the sub folder are deployed. (optional) (default to Global)
library = 'library_example' # str | library be filled only for z/os. (optional)

try:
    # delete a sub folder
    api_response = api_instance.delete_sub_folder(sub_folder_path, server=server, library=library)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->delete_sub_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_folder_path** | **str**| The name of the required subFolderPath. | 
 **server** | **str**| The name of the Control-M in which the sub folder are deployed. | [optional] [default to Global]
 **library** | **str**| library be filled only for z/os. | [optional] 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_ai_jobtype**
> AiDeployResponse deploy_ai_jobtype(ctm, agent, job_type_id)

Deploy of Application Integrator job type.

Deploy an existing Application Integrator job type to agent in order to allow it to run

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
ctm = 'ctm_example' # str | 
agent = 'agent_example' # str | 
job_type_id = 'job_type_id_example' # str | 

try:
    # Deploy of Application Integrator job type.
    api_response = api_instance.deploy_ai_jobtype(ctm, agent, job_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->deploy_ai_jobtype: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**|  | 
 **agent** | **str**|  | 
 **job_type_id** | **str**|  | 

### Return type

[**AiDeployResponse**](AiDeployResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_file**
> list[DeploymentFileResults] deploy_file(definitions_file, deploy_descriptor_file, additional_configuration)

Deploy definitions file

Deploy the provided definition file (JSON, XML or zip) to Control-M

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
definitions_file = 'definitions_file_example' # str | 
deploy_descriptor_file = 'deploy_descriptor_file_example' # str | 
additional_configuration = 'additional_configuration_example' # str | 

try:
    # Deploy definitions file
    api_response = api_instance.deploy_file(definitions_file, deploy_descriptor_file, additional_configuration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->deploy_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definitions_file** | **str**|  | 
 **deploy_descriptor_file** | **str**|  | 
 **additional_configuration** | **str**|  | 

### Return type

[**list[DeploymentFileResults]**](DeploymentFileResults.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_jobtype_file**
> DeployJobtypeResponse deploy_jobtype_file(definitions_file, payload_file, agent=agent, server=server)

Deploy jobtype

Deploy the provided jobtype to AI server, EM server, and Agent.

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
definitions_file = 'definitions_file_example' # str | 
payload_file = 'payload_file_example' # str | 
agent = 'agent_example' # str |  (optional)
server = 'server_example' # str |  (optional)

try:
    # Deploy jobtype
    api_response = api_instance.deploy_jobtype_file(definitions_file, payload_file, agent=agent, server=server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->deploy_jobtype_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definitions_file** | **str**|  | 
 **payload_file** | **str**|  | 
 **agent** | **str**|  | [optional] 
 **server** | **str**|  | [optional] 

### Return type

[**DeployJobtypeResponse**](DeployJobtypeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_site_standard_policies**
> SiteStandardPoliciesFileResults deploy_site_standard_policies(site_standard_policies_file)

Deploy Site Standard Policies.

Deploy Site Standard Policies.

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
site_standard_policies_file = 'site_standard_policies_file_example' # str | 

try:
    # Deploy Site Standard Policies.
    api_response = api_instance.deploy_site_standard_policies(site_standard_policies_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->deploy_site_standard_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_standard_policies_file** | **str**|  | 

### Return type

[**SiteStandardPoliciesFileResults**](SiteStandardPoliciesFileResults.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection_profiles_deployment_status**
> ConnectionProfilesDeploymentStatusResult get_connection_profiles_deployment_status(type, name)

Get deployed connection profiles deployment status

Get currently deployed connection profiles deployment status according to the search query as JSON.

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
type = 'type_example' # str | The type of connection profile such as Database, FileTransfer, Hadoop, Informatica, SAP.
name = 'name_example' # str | Name of the Connection Profile

try:
    # Get deployed connection profiles deployment status
    api_response = api_instance.get_connection_profiles_deployment_status(type, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_connection_profiles_deployment_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of connection profile such as Database, FileTransfer, Hadoop, Informatica, SAP. | 
 **name** | **str**| Name of the Connection Profile | 

### Return type

[**ConnectionProfilesDeploymentStatusResult**](ConnectionProfilesDeploymentStatusResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ctm_ai_job_type_plugin**
> str get_ctm_ai_job_type_plugin(job_type_name)

Get AI based job type content

Get AI based job type content. When used with CLI content is saved as a .ctmai file.

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
job_type_name = 'job_type_name_example' # str | The job type name

try:
    # Get AI based job type content
    api_response = api_instance.get_ctm_ai_job_type_plugin(job_type_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_ctm_ai_job_type_plugin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_type_name** | **str**| The job type name | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployed_ai_jobtypes**
> AiJobtypeList get_deployed_ai_jobtypes(job_type_name=job_type_name, job_type_id=job_type_id)

Get Application Integrator job types

Get deployed Application Integrator job types that match the requested search criteria.

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
job_type_name = 'job_type_name_example' # str | Job type display name ( or partial name ) for query. It accepts * as wildcard. (optional)
job_type_id = 'job_type_id_example' # str | Job type id ( or partial name ) for query. It accepts * as wildcard. (optional)

try:
    # Get Application Integrator job types
    api_response = api_instance.get_deployed_ai_jobtypes(job_type_name=job_type_name, job_type_id=job_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_deployed_ai_jobtypes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_type_name** | **str**| Job type display name ( or partial name ) for query. It accepts * as wildcard. | [optional] 
 **job_type_id** | **str**| Job type id ( or partial name ) for query. It accepts * as wildcard. | [optional] 

### Return type

[**AiJobtypeList**](AiJobtypeList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployed_calendars**
> str get_deployed_calendars(name=name, server=server, type=type, alias=alias)

Get deployed calendars that match the search criteria.

Get definition of calendars as json code that match the requested search criteria.

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
name = 'name_example' # str |  (optional)
server = 'server_example' # str |  (optional)
type = 'type_example' # str | Calendar type. (optional)
alias = 'alias_example' # str | Calendar alias name for z/OS servers. (optional)

try:
    # Get deployed calendars that match the search criteria.
    api_response = api_instance.get_deployed_calendars(name=name, server=server, type=type, alias=alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_deployed_calendars: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **server** | **str**|  | [optional] 
 **type** | **str**| Calendar type. | [optional] 
 **alias** | **str**| Calendar alias name for z/OS servers. | [optional] 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployed_connection_profiles**
> str get_deployed_connection_profiles(agent, type, ctm=ctm, server=server)

Get local deployed connection profiles

Get currently local deployed connection profiles according to the search query as JSON.

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
agent = 'agent_example' # str | The name of the agent the connection profile is deployed on
type = 'type_example' # str | The type of connection profile such as Database, FileTransfer, Hadoop, Informatica, SAP.
ctm = 'ctm_example' # str | The name of the Control-M in which the connection profile is deployed on (optional)
server = 'server_example' # str | The name of the Control-M in which the connection profile is deployed on (optional)

try:
    # Get local deployed connection profiles
    api_response = api_instance.get_deployed_connection_profiles(agent, type, ctm=ctm, server=server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_deployed_connection_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent** | **str**| The name of the agent the connection profile is deployed on | 
 **type** | **str**| The type of connection profile such as Database, FileTransfer, Hadoop, Informatica, SAP. | 
 **ctm** | **str**| The name of the Control-M in which the connection profile is deployed on | [optional] 
 **server** | **str**| The name of the Control-M in which the connection profile is deployed on | [optional] 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployed_connection_profiles_status**
> ConnectionProfilesStatusResult get_deployed_connection_profiles_status(limit=limit, name=name, type=type)

Get deployed connection profiles status

Get currently deployed connection profiles status according to the search query as JSON.

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
limit = 0 # int | number to limit the returned connection profiles. If missed - get all (optional) (default to 0)
name = '*' # str | conn profile name (support *, ?, and comma, default is * for all). (optional) (default to *)
type = '*' # str | conn profile type (default is * for accounts from all CMs). (optional) (default to *)

try:
    # Get deployed connection profiles status
    api_response = api_instance.get_deployed_connection_profiles_status(limit=limit, name=name, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_deployed_connection_profiles_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| number to limit the returned connection profiles. If missed - get all | [optional] [default to 0]
 **name** | **str**| conn profile name (support *, ?, and comma, default is * for all). | [optional] [default to *]
 **type** | **str**| conn profile type (default is * for accounts from all CMs). | [optional] [default to *]

### Return type

[**ConnectionProfilesStatusResult**](ConnectionProfilesStatusResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployed_folders**
> object get_deployed_folders(folder=folder, server=server, library=library, folder_type=folder_type, site_standard=site_standard, application=application, sub_application=sub_application)

Get deployed folders that match the search criteria.

Get definition of folders that match the requested search criteria.

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
folder = 'folder_example' # str |  (optional)
server = 'server_example' # str |  (optional)
library = 'library_example' # str | library be filled only for z/os. (optional)
folder_type = 'folder_type_example' # str | filter by simpleFolder (optional)
site_standard = 'site_standard_example' # str | filter by siteStandard (optional)
application = 'application_example' # str | filter by application (optional)
sub_application = 'sub_application_example' # str | filter by subApplication (optional)

try:
    # Get deployed folders that match the search criteria.
    api_response = api_instance.get_deployed_folders(folder=folder, server=server, library=library, folder_type=folder_type, site_standard=site_standard, application=application, sub_application=sub_application)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_deployed_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**|  | [optional] 
 **server** | **str**|  | [optional] 
 **library** | **str**| library be filled only for z/os. | [optional] 
 **folder_type** | **str**| filter by simpleFolder | [optional] 
 **site_standard** | **str**| filter by siteStandard | [optional] 
 **application** | **str**| filter by application | [optional] 
 **sub_application** | **str**| filter by subApplication | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployed_folders_new**
> object get_deployed_folders_new(format=format, folder=folder, job=job, ctm=ctm, server=server, use_array_format=use_array_format, library=library, flow_data=flow_data)

Get deployed jobs that match the search criteria.

Get definition of jobs and folders (in the desired format - JSON or XML) that match the requested search criteria.

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
format = 'json' # str | Output format (json or xml) (optional) (default to json)
folder = 'folder_example' # str |  (optional)
job = 'job_example' # str |  (optional)
ctm = 'ctm_example' # str |  (optional)
server = 'server_example' # str |  (optional)
use_array_format = true # bool | When set to true, the jobs in the json response will always be arranged in arrays (optional)
library = 'library_example' # str | library be filled only for z/os. (optional)
flow_data = true # bool | When set to true, only data cache will be return (optional)

try:
    # Get deployed jobs that match the search criteria.
    api_response = api_instance.get_deployed_folders_new(format=format, folder=folder, job=job, ctm=ctm, server=server, use_array_format=use_array_format, library=library, flow_data=flow_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_deployed_folders_new: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Output format (json or xml) | [optional] [default to json]
 **folder** | **str**|  | [optional] 
 **job** | **str**|  | [optional] 
 **ctm** | **str**|  | [optional] 
 **server** | **str**|  | [optional] 
 **use_array_format** | **bool**| When set to true, the jobs in the json response will always be arranged in arrays | [optional] 
 **library** | **str**| library be filled only for z/os. | [optional] 
 **flow_data** | **bool**| When set to true, only data cache will be return | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_local_connection_profiles**
> str get_local_connection_profiles(agent, type, ctm=ctm, server=server)

Get local deployed connection profiles

Get currently local deployed connection profiles according to the search query as JSON.

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
agent = 'agent_example' # str | The name of the agent the connection profile is deployed on
type = 'type_example' # str | The type of connection profile such as Database, FileTransfer, Hadoop, Informatica, SAP.
ctm = 'ctm_example' # str | The name of the Control-M in which the connection profile is deployed on (optional)
server = 'server_example' # str | The name of the Control-M in which the connection profile is deployed on (optional)

try:
    # Get local deployed connection profiles
    api_response = api_instance.get_local_connection_profiles(agent, type, ctm=ctm, server=server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_local_connection_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent** | **str**| The name of the agent the connection profile is deployed on | 
 **type** | **str**| The type of connection profile such as Database, FileTransfer, Hadoop, Informatica, SAP. | 
 **ctm** | **str**| The name of the Control-M in which the connection profile is deployed on | [optional] 
 **server** | **str**| The name of the Control-M in which the connection profile is deployed on | [optional] 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_connection_profiles**
> str get_shared_connection_profiles(type, name=name)

Get centralized deployed connection profile

Get currently centralized deployed connection profiles according to the search query as JSON.

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
type = '*' # str | The type of connection profile such as Database, FileTransfer, Hadoop, Informatica, SAP. Use * to get all types (default to *)
name = '*' # str | The name of centralized connection profile. Supports for *, ?, and comma. By default is * (optional) (default to *)

try:
    # Get centralized deployed connection profile
    api_response = api_instance.get_shared_connection_profiles(type, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_shared_connection_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of connection profile such as Database, FileTransfer, Hadoop, Informatica, SAP. Use * to get all types | [default to *]
 **name** | **str**| The name of centralized connection profile. Supports for *, ?, and comma. By default is * | [optional] [default to *]

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_standard_field_restrictions**
> str get_site_standard_field_restrictions(standard_name, field_name)

Get the allowed values for the specified field in the specified site standard.

Get the allowed values for the specified field in the specified site standard.

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
standard_name = 'standard_name_example' # str | 
field_name = 'field_name_example' # str | 

try:
    # Get the allowed values for the specified field in the specified site standard.
    api_response = api_instance.get_site_standard_field_restrictions(standard_name, field_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_site_standard_field_restrictions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **standard_name** | **str**|  | 
 **field_name** | **str**|  | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_standard_policies**
> str get_site_standard_policies(name=name)

Get definitions of deployed Site Standard Policies that match the search criteria.

Get definitions of deployed Site Standard Policies that match the search criteria.

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
name = 'name_example' # str |  (optional)

try:
    # Get definitions of deployed Site Standard Policies that match the search criteria.
    api_response = api_instance.get_site_standard_policies(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_site_standard_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_standard_policies_details**
> SiteStandardPolicyDetailsList get_site_standard_policies_details(name=name)

Get details of deployed Site Standard Policies that match the search criteria.

Get details of deployed Site Standard Policies that match the requested search criteria.

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
name = 'name_example' # str |  (optional)

try:
    # Get details of deployed Site Standard Policies that match the search criteria.
    api_response = api_instance.get_site_standard_policies_details(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_site_standard_policies_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

[**SiteStandardPolicyDetailsList**](SiteStandardPolicyDetailsList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_standards**
> str get_site_standards(name=name)

Get definitions of deployed Site Standards that match the search criteria.

Get definitions of deployed Site Standards that match the search criteria.

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
name = 'name_example' # str |  (optional)

try:
    # Get definitions of deployed Site Standards that match the search criteria.
    api_response = api_instance.get_site_standards(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_site_standards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_standards_details**
> SiteStandardDetailsList get_site_standards_details(name=name)

Get details of deployed Site Standards that match the search criteria.

Get details of deployed Site Standards that match the requested search criteria.

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
name = 'name_example' # str |  (optional)

try:
    # Get details of deployed Site Standards that match the search criteria.
    api_response = api_instance.get_site_standards_details(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->get_site_standards_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

[**SiteStandardDetailsList**](SiteStandardDetailsList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poll_deploy_results**
> DeploymentFileResults poll_deploy_results(poll_id)

Get the deploy result

Get the deploy result

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
poll_id = 'poll_id_example' # str | deploy request identification

try:
    # Get the deploy result
    api_response = api_instance.poll_deploy_results(poll_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->poll_deploy_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poll_id** | **str**| deploy request identification | 

### Return type

[**DeploymentFileResults**](DeploymentFileResults.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_site_standard**
> SuccessData rename_site_standard(site_standard_name, site_standard_new_name)

Rename deployed Site Standard.

Rename deployed Site Standard.

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
site_standard_name = 'site_standard_name_example' # str | 
site_standard_new_name = 'site_standard_new_name_example' # str | 

try:
    # Rename deployed Site Standard.
    api_response = api_instance.rename_site_standard(site_standard_name, site_standard_new_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->rename_site_standard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_standard_name** | **str**|  | 
 **site_standard_new_name** | **str**|  | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_site_standard_policy**
> SuccessData rename_site_standard_policy(site_standard_policy_name, site_standard_policy_new_name)

Rename deployed Site Standard Policy.

Rename deployed Site Standard Policy.

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
site_standard_policy_name = 'site_standard_policy_name_example' # str | 
site_standard_policy_new_name = 'site_standard_policy_new_name_example' # str | 

try:
    # Rename deployed Site Standard Policy.
    api_response = api_instance.rename_site_standard_policy(site_standard_policy_name, site_standard_policy_new_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->rename_site_standard_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_standard_policy_name** | **str**|  | 
 **site_standard_policy_new_name** | **str**|  | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_site_standard_field_restrictions**
> SuccessData set_site_standard_field_restrictions(body, standard_name, field_name)

Replace the allowed values for the specified field in the specified site standard.

Replace the allowed values for the specified field in the specified site standard.

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
body = controlm_py.FieldValues() # FieldValues | The JSON file with the allowed values
standard_name = 'standard_name_example' # str | 
field_name = 'field_name_example' # str | 

try:
    # Replace the allowed values for the specified field in the specified site standard.
    api_response = api_instance.set_site_standard_field_restrictions(body, standard_name, field_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->set_site_standard_field_restrictions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FieldValues**](FieldValues.md)| The JSON file with the allowed values | 
 **standard_name** | **str**|  | 
 **field_name** | **str**|  | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_centralized_connection_profile**
> SuccessData test_centralized_connection_profile(type, name, server, agent)

Test connection profile centralized on agent

Test connection profile centralized on agent

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
type = 'type_example' # str | The type of connection profile.
name = 'name_example' # str | Name of the Connection Profile
server = 'server_example' # str | The ctm of connection profile.
agent = 'agent_example' # str | 

try:
    # Test connection profile centralized on agent
    api_response = api_instance.test_centralized_connection_profile(type, name, server, agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->test_centralized_connection_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of connection profile. | 
 **name** | **str**| Name of the Connection Profile | 
 **server** | **str**| The ctm of connection profile. | 
 **agent** | **str**|  | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_connection_profile**
> SuccessData test_connection_profile(definitions_file, ctm=ctm, agent=agent)

Test connection profile on agent

Test connection profile on agent

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
definitions_file = 'definitions_file_example' # str | 
ctm = 'ctm_example' # str |  (optional)
agent = 'agent_example' # str |  (optional)

try:
    # Test connection profile on agent
    api_response = api_instance.test_connection_profile(definitions_file, ctm=ctm, agent=agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->test_connection_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definitions_file** | **str**|  | 
 **ctm** | **str**|  | [optional] 
 **agent** | **str**|  | [optional] 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transform_file**
> str transform_file(definitions_file, deploy_descriptor_file)

Transform a definitions file

Transform the provided definitions file (JSON) according to the provided Deploy Descriptor file (JSON).

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
api_instance = controlm_py.DeployApi(controlm_py.ApiClient(configuration))
definitions_file = 'definitions_file_example' # str | 
deploy_descriptor_file = 'deploy_descriptor_file_example' # str | 

try:
    # Transform a definitions file
    api_response = api_instance.transform_file(definitions_file, deploy_descriptor_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeployApi->transform_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **definitions_file** | **str**|  | 
 **deploy_descriptor_file** | **str**|  | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

