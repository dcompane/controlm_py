# controlm_py.RunApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_workload_policy**](RunApi.md#activate_workload_policy) | **POST** /run/workloadpolicy/{policy}/activate | activate workload policy
[**add_event**](RunApi.md#add_event) | **POST** /run/event/{server} | Add a new  event.
[**add_resource**](RunApi.md#add_resource) | **POST** /run/resource/{server} | Add a new pool resource.
[**add_workload_policies**](RunApi.md#add_workload_policies) | **POST** /run/workloadpolicies | Add workload policies from definitions file
[**confirm_job**](RunApi.md#confirm_job) | **POST** /run/job/{jobId}/confirm | confirm a job
[**deactivate_workload_policy**](RunApi.md#deactivate_workload_policy) | **POST** /run/workloadpolicy/{policy}/deactivate | deactivate a workload policy
[**delete_event**](RunApi.md#delete_event) | **DELETE** /run/event/{server}/{name}/{date} | Delete a  event.
[**delete_job**](RunApi.md#delete_job) | **POST** /run/job/{jobId}/delete | mark job as deleted
[**delete_resource**](RunApi.md#delete_resource) | **DELETE** /run/resource/{server}/{name} | Delete a pool resource.
[**delete_variables**](RunApi.md#delete_variables) | **DELETE** /run/variables/{server} | Delete variables from the server.
[**delete_workload_policy**](RunApi.md#delete_workload_policy) | **DELETE** /run/workloadpolicy/{workloadpolicyName} | delete workloadpolicy
[**free_job**](RunApi.md#free_job) | **POST** /run/job/{jobId}/free | free an already held the job
[**get_active_job**](RunApi.md#get_active_job) | **GET** /run/job/{jobId}/get | get active job
[**get_active_services**](RunApi.md#get_active_services) | **GET** /run/services/sla | Get SLA active services
[**get_detailed_workload_policies**](RunApi.md#get_detailed_workload_policies) | **GET** /run/workloadpolicies/detailed | get full workLoad policies data that match the search criteria.
[**get_events**](RunApi.md#get_events) | **GET** /run/events | Get all events records for specific search.
[**get_job_log**](RunApi.md#get_job_log) | **GET** /run/job/{jobId}/log | Get job&#x27;s log
[**get_job_output**](RunApi.md#get_job_output) | **GET** /run/job/{jobId}/output | Get job output
[**get_job_statistics**](RunApi.md#get_job_statistics) | **GET** /run/job/{jobId}/statistics | Get job statistics
[**get_job_status**](RunApi.md#get_job_status) | **GET** /run/job/{jobId}/status | Get status of a job
[**get_jobs_status**](RunApi.md#get_jobs_status) | **GET** /run/status/{runId} | Get status of running jobs
[**get_jobs_status_by_filter**](RunApi.md#get_jobs_status_by_filter) | **GET** /run/jobs/status | Get jobs that match the search criteria.
[**get_resources**](RunApi.md#get_resources) | **GET** /run/resources | Get all resources records matching search.
[**get_variables**](RunApi.md#get_variables) | **GET** /run/variables | Return variable values based on specified search criteria.
[**get_waiting_info**](RunApi.md#get_waiting_info) | **GET** /run/job/{jobId}/waitingInfo | get job&#x27;s waiting information
[**get_workload_policies**](RunApi.md#get_workload_policies) | **GET** /run/workloadpolicies | get workload policies
[**hold_job**](RunApi.md#hold_job) | **POST** /run/job/{jobId}/hold | hold the job so it will not start untill it is freed
[**kill_job**](RunApi.md#kill_job) | **POST** /run/job/{jobId}/kill | Cancel running job
[**modify_job**](RunApi.md#modify_job) | **POST** /run/job/{jobId}/modify | Modify active job
[**order_jobs_in_folder**](RunApi.md#order_jobs_in_folder) | **POST** /run/order | Execute requested jobs in certain folder
[**rerun_job**](RunApi.md#rerun_job) | **POST** /run/job/{jobId}/rerun | Run job again
[**run_jobs**](RunApi.md#run_jobs) | **POST** /run | Run jobs
[**run_now**](RunApi.md#run_now) | **POST** /run/job/{jobId}/runNow | Bypass scheduling cretirias and start the job
[**set_to_ok**](RunApi.md#set_to_ok) | **POST** /run/job/{jobId}/setToOk | set job end status to OK
[**set_variables**](RunApi.md#set_variables) | **POST** /run/variables/{server} | Set variable values as defined in json input. Use this API to create new variables or update existing variables.
[**undelete_job**](RunApi.md#undelete_job) | **POST** /run/job/{jobId}/undelete | recover a mark for deletion job
[**update_alert**](RunApi.md#update_alert) | **POST** /run/alerts | Update alert.
[**update_alert_status**](RunApi.md#update_alert_status) | **POST** /run/alerts/status | Update alert status.
[**update_resource**](RunApi.md#update_resource) | **POST** /run/resource/{server}/{name} | Update a pool resource.

# **activate_workload_policy**
> WorkloadPolicyStateList activate_workload_policy(policy, ctm=ctm, server=server)

activate workload policy

Activate a workload policy, supports wildcard in names

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
policy = 'policy_example' # str | The policy name to be activated. Case sensitive. Wildcards can be used.
ctm = 'ctm_example' # str | Optional Control-M Server filter. (optional)
server = 'server_example' # str | Optional Control-M Server filter. (optional)

try:
    # activate workload policy
    api_response = api_instance.activate_workload_policy(policy, ctm=ctm, server=server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->activate_workload_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy** | **str**| The policy name to be activated. Case sensitive. Wildcards can be used. | 
 **ctm** | **str**| Optional Control-M Server filter. | [optional] 
 **server** | **str**| Optional Control-M Server filter. | [optional] 

### Return type

[**WorkloadPolicyStateList**](WorkloadPolicyStateList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_event**
> SuccessData add_event(body, server)

Add a new  event.

Add a new  event. date may be of format MMDD, ODAT to set current controlm date, STAT to set no date. default value is ODAT.

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
body = controlm_py.EventParam() # EventParam | The defined event name.
server = 'server_example' # str | The Control-M Server hosting the event.

try:
    # Add a new  event.
    api_response = api_instance.add_event(body, server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->add_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EventParam**](EventParam.md)| The defined event name. | 
 **server** | **str**| The Control-M Server hosting the event. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_resource**
> SuccessData add_resource(body, server)

Add a new pool resource.

Add a new pool resource.

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
body = controlm_py.ResourceParam() # ResourceParam | The defined resource name.
server = 'server_example' # str | The Control-M Server hosting the resource.

try:
    # Add a new pool resource.
    api_response = api_instance.add_resource(body, server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->add_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResourceParam**](ResourceParam.md)| The defined resource name. | 
 **server** | **str**| The Control-M Server hosting the resource. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_workload_policies**
> WorkloadPoliciesFileResults add_workload_policies(workloadpoliciesfile)

Add workload policies from definitions file

Add workload policies from json definitions file to Control-M

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
workloadpoliciesfile = 'workloadpoliciesfile_example' # str | 

try:
    # Add workload policies from definitions file
    api_response = api_instance.add_workload_policies(workloadpoliciesfile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->add_workload_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workloadpoliciesfile** | **str**|  | 

### Return type

[**WorkloadPoliciesFileResults**](WorkloadPoliciesFileResults.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_job**
> SuccessData confirm_job(job_id)

confirm a job

confirm a job that waits for confirmation

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID

try:
    # confirm a job
    api_response = api_instance.confirm_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->confirm_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_workload_policy**
> WorkloadPolicyStateList deactivate_workload_policy(policy, ctm=ctm, server=server)

deactivate a workload policy

Deactivate a workload policy, supports wildcard in names

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
policy = 'policy_example' # str | The policy name to be deactivated. Case sensitive. Wildcards can be used.
ctm = 'ctm_example' # str | Optional Control-M Server filter. (optional)
server = 'server_example' # str | Optional Control-M Server filter. (optional)

try:
    # deactivate a workload policy
    api_response = api_instance.deactivate_workload_policy(policy, ctm=ctm, server=server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->deactivate_workload_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy** | **str**| The policy name to be deactivated. Case sensitive. Wildcards can be used. | 
 **ctm** | **str**| Optional Control-M Server filter. | [optional] 
 **server** | **str**| Optional Control-M Server filter. | [optional] 

### Return type

[**WorkloadPolicyStateList**](WorkloadPolicyStateList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event**
> SuccessData delete_event(server, name, _date)

Delete a  event.

Delete a  event.

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
server = 'server_example' # str | The Control-M Server hosting the event.
name = 'name_example' # str | event name
_date = '_date_example' # str | event date

try:
    # Delete a  event.
    api_response = api_instance.delete_event(server, name, _date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->delete_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Control-M Server hosting the event. | 
 **name** | **str**| event name | 
 **_date** | **str**| event date | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job**
> SuccessData delete_job(job_id)

mark job as deleted

mark delete as deleted

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID

try:
    # mark job as deleted
    api_response = api_instance.delete_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->delete_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource**
> SuccessData delete_resource(server, name)

Delete a pool resource.

Delete a pool resource.

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
server = 'server_example' # str | The Control-M Server hosting the resource.
name = 'name_example' # str | Resource name

try:
    # Delete a pool resource.
    api_response = api_instance.delete_resource(server, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->delete_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**| The Control-M Server hosting the resource. | 
 **name** | **str**| Resource name | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_variables**
> SuccessData delete_variables(body, server)

Delete variables from the server.

Delete variables from the server.

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
body = controlm_py.VariableNames() # VariableNames | Variables definition file.
server = 'server_example' # str | The server that hosts the variables.

try:
    # Delete variables from the server.
    api_response = api_instance.delete_variables(body, server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->delete_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VariableNames**](VariableNames.md)| Variables definition file. | 
 **server** | **str**| The server that hosts the variables. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workload_policy**
> SuccessData delete_workload_policy(workloadpolicy_name)

delete workloadpolicy

Delete workloadpolicy

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
workloadpolicy_name = 'workloadpolicy_name_example' # str | The name of the workloadPolicy to be deleted.

try:
    # delete workloadpolicy
    api_response = api_instance.delete_workload_policy(workloadpolicy_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->delete_workload_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workloadpolicy_name** | **str**| The name of the workloadPolicy to be deleted. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **free_job**
> SuccessData free_job(job_id)

free an already held the job

free the job

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID

try:
    # free an already held the job
    api_response = api_instance.free_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->free_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_job**
> str get_active_job(job_id)

get active job

get the active job's data by job's order ID

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID

try:
    # get active job
    api_response = api_instance.get_active_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->get_active_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_services**
> ActiveServices get_active_services()

Get SLA active services

Get all SLA active services

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))

try:
    # Get SLA active services
    api_response = api_instance.get_active_services()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->get_active_services: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ActiveServices**](ActiveServices.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_detailed_workload_policies**
> str get_detailed_workload_policies(name=name)

get full workLoad policies data that match the search criteria.

get full workLoad policies data as json code that match the requested search criteria.

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
name = 'name_example' # str |  (optional)

try:
    # get full workLoad policies data that match the search criteria.
    api_response = api_instance.get_detailed_workload_policies(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->get_detailed_workload_policies: %s\n" % e)
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

# **get_events**
> EventSet get_events(ctm=ctm, server=server, name=name, _date=_date, limit=limit)

Get all events records for specific search.

Get all events records for specific search.

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
ctm = 'ctm_example' # str | Control-M Server filter. (optional)
server = 'server_example' # str | Control-M Server filter. (optional)
name = 'name_example' # str | The event name filter. (optional)
_date = '_date_example' # str | The event date filter. (optional)
limit = 1000 # int | maximum events to fetch (default 1000). (optional) (default to 1000)

try:
    # Get all events records for specific search.
    api_response = api_instance.get_events(ctm=ctm, server=server, name=name, _date=_date, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->get_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| Control-M Server filter. | [optional] 
 **server** | **str**| Control-M Server filter. | [optional] 
 **name** | **str**| The event name filter. | [optional] 
 **_date** | **str**| The event date filter. | [optional] 
 **limit** | **int**| maximum events to fetch (default 1000). | [optional] [default to 1000]

### Return type

[**EventSet**](EventSet.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_log**
> str get_job_log(job_id)

Get job's log

Get the job execution log.

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID

try:
    # Get job's log
    api_response = api_instance.get_job_log(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->get_job_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_output**
> str get_job_output(job_id, run_no=run_no)

Get job output

Get the output returned from a job.

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID
run_no = 0 # int | The execution number in case of multiple executions (0 will get the last execution's output) (optional) (default to 0)

try:
    # Get job output
    api_response = api_instance.get_job_output(job_id, run_no=run_no)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->get_job_output: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 
 **run_no** | **int**| The execution number in case of multiple executions (0 will get the last execution&#x27;s output) | [optional] [default to 0]

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_statistics**
> Statistics get_job_statistics(job_id)

Get job statistics

Get the statistics from a job.

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID

try:
    # Get job statistics
    api_response = api_instance.get_job_statistics(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->get_job_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 

### Return type

[**Statistics**](Statistics.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_status**
> JobRunStatus get_job_status(job_id)

Get status of a job

Get the job status.

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
job_id = 'job_id_example' # str | Job ID returned from the run status action.

try:
    # Get status of a job
    api_response = api_instance.get_job_status(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->get_job_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID returned from the run status action. | 

### Return type

[**JobRunStatus**](JobRunStatus.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobs_status**
> JobStatusResult get_jobs_status(run_id, start_index=start_index)

Get status of running jobs

Run status of jobs started with the Run service.

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
run_id = 'run_id_example' # str | Run ID returned from the run action.
start_index = 0 # int | The index of the job status from which to start. returning results (optional) (default to 0)

try:
    # Get status of running jobs
    api_response = api_instance.get_jobs_status(run_id, start_index=start_index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->get_jobs_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| Run ID returned from the run action. | 
 **start_index** | **int**| The index of the job status from which to start. returning results | [optional] [default to 0]

### Return type

[**JobStatusResult**](JobStatusResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobs_status_by_filter**
> JobStatusResult get_jobs_status_by_filter(limit=limit, jobname=jobname, ctm=ctm, server=server, application=application, sub_application=sub_application, host=host, status=status, folder=folder, description=description, jobid=jobid, neighborhood=neighborhood, depth=depth, direction=direction, order_date_from=order_date_from, order_date_to=order_date_to, from_time=from_time, to_time=to_time, folder_library=folder_library, host_group=host_group, run_as=run_as, command=command, file_path=file_path, file_name=file_name, workload_policy=workload_policy, rule_based_calendar=rule_based_calendar, resource_mutex=resource_mutex, resource_semaphore=resource_semaphore, resource_lock=resource_lock, resource_pool=resource_pool, held=held, folder_held=folder_held, cyclic=cyclic, deleted=deleted)

Get jobs that match the search criteria.

Get status of jobs that match the requested search criteria.

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
limit = 1000 # int | maximum jobs status to fetch (default 1000). (optional) (default to 1000)
jobname = 'jobname_example' # str |  (optional)
ctm = 'ctm_example' # str |  (optional)
server = 'server_example' # str |  (optional)
application = 'application_example' # str |  (optional)
sub_application = 'sub_application_example' # str |  (optional)
host = 'host_example' # str |  (optional)
status = 'status_example' # str |  (optional)
folder = 'folder_example' # str |  (optional)
description = 'description_example' # str |  (optional)
jobid = 'jobid_example' # str |  (optional)
neighborhood = 'neighborhood_example' # str |  (optional)
depth = 56 # int |  (optional)
direction = 'direction_example' # str |  (optional)
order_date_from = 'order_date_from_example' # str |  (optional)
order_date_to = 'order_date_to_example' # str |  (optional)
from_time = 'from_time_example' # str |  (optional)
to_time = 'to_time_example' # str |  (optional)
folder_library = 'folder_library_example' # str |  (optional)
host_group = 'host_group_example' # str |  (optional)
run_as = 'run_as_example' # str |  (optional)
command = 'command_example' # str |  (optional)
file_path = 'file_path_example' # str |  (optional)
file_name = 'file_name_example' # str |  (optional)
workload_policy = 'workload_policy_example' # str |  (optional)
rule_based_calendar = 'rule_based_calendar_example' # str |  (optional)
resource_mutex = 'resource_mutex_example' # str |  (optional)
resource_semaphore = 'resource_semaphore_example' # str |  (optional)
resource_lock = 'resource_lock_example' # str |  (optional)
resource_pool = 'resource_pool_example' # str |  (optional)
held = true # bool |  (optional)
folder_held = true # bool |  (optional)
cyclic = true # bool |  (optional)
deleted = true # bool |  (optional)

try:
    # Get jobs that match the search criteria.
    api_response = api_instance.get_jobs_status_by_filter(limit=limit, jobname=jobname, ctm=ctm, server=server, application=application, sub_application=sub_application, host=host, status=status, folder=folder, description=description, jobid=jobid, neighborhood=neighborhood, depth=depth, direction=direction, order_date_from=order_date_from, order_date_to=order_date_to, from_time=from_time, to_time=to_time, folder_library=folder_library, host_group=host_group, run_as=run_as, command=command, file_path=file_path, file_name=file_name, workload_policy=workload_policy, rule_based_calendar=rule_based_calendar, resource_mutex=resource_mutex, resource_semaphore=resource_semaphore, resource_lock=resource_lock, resource_pool=resource_pool, held=held, folder_held=folder_held, cyclic=cyclic, deleted=deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->get_jobs_status_by_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| maximum jobs status to fetch (default 1000). | [optional] [default to 1000]
 **jobname** | **str**|  | [optional] 
 **ctm** | **str**|  | [optional] 
 **server** | **str**|  | [optional] 
 **application** | **str**|  | [optional] 
 **sub_application** | **str**|  | [optional] 
 **host** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **folder** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **jobid** | **str**|  | [optional] 
 **neighborhood** | **str**|  | [optional] 
 **depth** | **int**|  | [optional] 
 **direction** | **str**|  | [optional] 
 **order_date_from** | **str**|  | [optional] 
 **order_date_to** | **str**|  | [optional] 
 **from_time** | **str**|  | [optional] 
 **to_time** | **str**|  | [optional] 
 **folder_library** | **str**|  | [optional] 
 **host_group** | **str**|  | [optional] 
 **run_as** | **str**|  | [optional] 
 **command** | **str**|  | [optional] 
 **file_path** | **str**|  | [optional] 
 **file_name** | **str**|  | [optional] 
 **workload_policy** | **str**|  | [optional] 
 **rule_based_calendar** | **str**|  | [optional] 
 **resource_mutex** | **str**|  | [optional] 
 **resource_semaphore** | **str**|  | [optional] 
 **resource_lock** | **str**|  | [optional] 
 **resource_pool** | **str**|  | [optional] 
 **held** | **bool**|  | [optional] 
 **folder_held** | **bool**|  | [optional] 
 **cyclic** | **bool**|  | [optional] 
 **deleted** | **bool**|  | [optional] 

### Return type

[**JobStatusResult**](JobStatusResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resources**
> ResourceSet get_resources(ctm=ctm, server=server, name=name)

Get all resources records matching search.

Get all resources records matching search.

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
ctm = 'ctm_example' # str | Control-M Server filter. (optional)
server = 'server_example' # str | Control-M Server filter. (optional)
name = 'name_example' # str | The resource name filter. (optional)

try:
    # Get all resources records matching search.
    api_response = api_instance.get_resources(ctm=ctm, server=server, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->get_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctm** | **str**| Control-M Server filter. | [optional] 
 **server** | **str**| Control-M Server filter. | [optional] 
 **name** | **str**| The resource name filter. | [optional] 

### Return type

[**ResourceSet**](ResourceSet.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_variables**
> Variables get_variables(pool=pool, variable=variable, server=server)

Return variable values based on specified search criteria.

Return variable values based on specified search criteria.

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
pool = '*' # str | The pool name filter (optional) (default to *)
variable = '*' # str | The variable name filter (optional) (default to *)
server = '*' # str | The server name filter (optional) (default to *)

try:
    # Return variable values based on specified search criteria.
    api_response = api_instance.get_variables(pool=pool, variable=variable, server=server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->get_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool** | **str**| The pool name filter | [optional] [default to *]
 **variable** | **str**| The variable name filter | [optional] [default to *]
 **server** | **str**| The server name filter | [optional] [default to *]

### Return type

[**Variables**](Variables.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_waiting_info**
> StringListResult get_waiting_info(job_id)

get job's waiting information

get the reason why the job is in waiting status

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID

try:
    # get job's waiting information
    api_response = api_instance.get_waiting_info(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->get_waiting_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 

### Return type

[**StringListResult**](StringListResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workload_policies**
> WorkloadPolicyList get_workload_policies(state=state)

get workload policies

Get all the workload policies.

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
state = 'state_example' # str | Optionally state filter. Available values Active, Inactive (optional)

try:
    # get workload policies
    api_response = api_instance.get_workload_policies(state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->get_workload_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| Optionally state filter. Available values Active, Inactive | [optional] 

### Return type

[**WorkloadPolicyList**](WorkloadPolicyList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hold_job**
> SuccessData hold_job(job_id)

hold the job so it will not start untill it is freed

hold the job

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID

try:
    # hold the job so it will not start untill it is freed
    api_response = api_instance.hold_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->hold_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kill_job**
> SuccessData kill_job(job_id)

Cancel running job

Abort job execution.

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID

try:
    # Cancel running job
    api_response = api_instance.kill_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->kill_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_job**
> SuccessData modify_job(job_definitions_file, job_id)

Modify active job

Modify active job, specified by order id according to given definitions file (JSON).

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
job_definitions_file = 'job_definitions_file_example' # str | 
job_id = 'job_id_example' # str | The job ID

try:
    # Modify active job
    api_response = api_instance.modify_job(job_definitions_file, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->modify_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_definitions_file** | **str**|  | 
 **job_id** | **str**| The job ID | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_jobs_in_folder**
> RunResult order_jobs_in_folder(body=body)

Execute requested jobs in certain folder

Run jobs from selected folder according to given filter

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
body = controlm_py.OrderFolderParameters() # OrderFolderParameters | parameters to select the jobs to run (optional)

try:
    # Execute requested jobs in certain folder
    api_response = api_instance.order_jobs_in_folder(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->order_jobs_in_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderFolderParameters**](OrderFolderParameters.md)| parameters to select the jobs to run | [optional] 

### Return type

[**RunResult**](RunResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rerun_job**
> JobRunStatus rerun_job(job_id, body=body)

Run job again

Run an already executed job (again).

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID
body = controlm_py.RerunParameters() # RerunParameters | The JSON file with the restart configuration and parameters (optional)

try:
    # Run job again
    api_response = api_instance.rerun_job(job_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->rerun_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 
 **body** | [**RerunParameters**](RerunParameters.md)| The JSON file with the restart configuration and parameters | [optional] 

### Return type

[**JobRunStatus**](JobRunStatus.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_jobs**
> RunResult run_jobs(job_definitions_file, deploy_descriptor_file, additional_configuration)

Run jobs

Run jobs according to given definitions file (JSON or zip).

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
job_definitions_file = 'job_definitions_file_example' # str | 
deploy_descriptor_file = 'deploy_descriptor_file_example' # str | 
additional_configuration = 'additional_configuration_example' # str | 

try:
    # Run jobs
    api_response = api_instance.run_jobs(job_definitions_file, deploy_descriptor_file, additional_configuration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->run_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_definitions_file** | **str**|  | 
 **deploy_descriptor_file** | **str**|  | 
 **additional_configuration** | **str**|  | 

### Return type

[**RunResult**](RunResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_now**
> SuccessData run_now(job_id)

Bypass scheduling cretirias and start the job

start a job immediately

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID

try:
    # Bypass scheduling cretirias and start the job
    api_response = api_instance.run_now(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->run_now: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_to_ok**
> SuccessData set_to_ok(job_id)

set job end status to OK

set job status to OK, post processing action

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID

try:
    # set job end status to OK
    api_response = api_instance.set_to_ok(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->set_to_ok: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_variables**
> SuccessData set_variables(body, server)

Set variable values as defined in json input. Use this API to create new variables or update existing variables.

Set variable values as defined in json input. Use this API to create new variables or update existing variables.

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
body = controlm_py.Variables() # Variables | Variables definition file.
server = 'server_example' # str | The server that hosts the variables.

try:
    # Set variable values as defined in json input. Use this API to create new variables or update existing variables.
    api_response = api_instance.set_variables(body, server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->set_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Variables**](Variables.md)| Variables definition file. | 
 **server** | **str**| The server that hosts the variables. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **undelete_job**
> SuccessData undelete_job(job_id)

recover a mark for deletion job

recover a mark for deletion job

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID

try:
    # recover a mark for deletion job
    api_response = api_instance.undelete_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->undelete_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert**
> SuccessData update_alert(body)

Update alert.

Update alert.

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
body = controlm_py.AlertParam() # AlertParam | File that contains the alert property that want to be update.

try:
    # Update alert.
    api_response = api_instance.update_alert(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->update_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertParam**](AlertParam.md)| File that contains the alert property that want to be update. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alert_status**
> SuccessData update_alert_status(body)

Update alert status.

Update alert status.

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
body = controlm_py.AlertStatusParam() # AlertStatusParam | File that contains the alert status property that want to be update.

try:
    # Update alert status.
    api_response = api_instance.update_alert_status(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->update_alert_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AlertStatusParam**](AlertStatusParam.md)| File that contains the alert status property that want to be update. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_resource**
> SuccessData update_resource(body, server, name)

Update a pool resource.

Update a pool resource.

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
api_instance = controlm_py.RunApi(controlm_py.ApiClient(configuration))
body = controlm_py.ResourceMax() # ResourceMax | The defined resource name.
server = 'server_example' # str | The Control-M Server hosting the resource.
name = 'name_example' # str | Resource name

try:
    # Update a pool resource.
    api_response = api_instance.update_resource(body, server, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunApi->update_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResourceMax**](ResourceMax.md)| The defined resource name. | 
 **server** | **str**| The Control-M Server hosting the resource. | 
 **name** | **str**| Resource name | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

