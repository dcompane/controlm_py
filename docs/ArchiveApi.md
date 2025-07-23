# controlm_py.ArchiveApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_archive_job_log**](ArchiveApi.md#get_archive_job_log) | **GET** /archive/{jobId}/log | Get job log
[**get_archive_job_output**](ArchiveApi.md#get_archive_job_output) | **GET** /archive/{jobId}/output | Get job output
[**search_jobs**](ArchiveApi.md#search_jobs) | **GET** /archive/search | Search jobs in Archive

# **get_archive_job_log**
> str get_archive_job_log(job_id, run_no)

Get job log

Get job log by unique job key

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
api_instance = controlm_py.ArchiveApi(controlm_py.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID
run_no = 789 # int | The execution number in case of multiple executions

try:
    # Get job log
    api_response = api_instance.get_archive_job_log(job_id, run_no)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->get_archive_job_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 
 **run_no** | **int**| The execution number in case of multiple executions | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_archive_job_output**
> str get_archive_job_output(job_id, run_no)

Get job output

Get job output by unique job key

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
api_instance = controlm_py.ArchiveApi(controlm_py.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID
run_no = 789 # int | The execution number in case of multiple executions

try:
    # Get job output
    api_response = api_instance.get_archive_job_output(job_id, run_no)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->get_archive_job_output: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID | 
 **run_no** | **int**| The execution number in case of multiple executions | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_jobs**
> ArchiveJobsList search_jobs(limit=limit, jobname=jobname, jobid=jobid, ctm=ctm, server=server, folder=folder, from_time=from_time, to_time=to_time, log_contains=log_contains, output_contains=output_contains, application=application, sub_application=sub_application, library=library, mem_name=mem_name, mem_library=mem_library, host=host, host_group=host_group, run_as=run_as, order_id=order_id, status=status, order_date_from=order_date_from, order_date_to=order_date_to, number_of_runs=number_of_runs)

Search jobs in Archive

Get all the Control-M Archiving jobs that match the search criterias

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
api_instance = controlm_py.ArchiveApi(controlm_py.ApiClient(configuration))
limit = 500 # int | maximum jobs to fetch (default 500). (optional) (default to 500)
jobname = 'jobname_example' # str | The name of the job. (optional)
jobid = 'jobid_example' # str |  (optional)
ctm = 'ctm_example' # str | The name of the Control-M server in which the job was ordered from. (optional)
server = 'server_example' # str | The name of the Control-M server in which the job was ordered from. (optional)
folder = 'folder_example' # str | The name of the parent folder. (optional)
from_time = 'from_time_example' # str | Job execution start date. Date format - YYYY-MM-DD. (optional)
to_time = 'to_time_example' # str | Job execution end date. Date format - YYYY-MM-DD. (optional)
log_contains = 'log_contains_example' # str | Job log must contain the given phrase. (optional)
output_contains = 'output_contains_example' # str | Job output must contain the given phrase. (optional)
application = 'application_example' # str | The name of the application the jobs belong to. (optional)
sub_application = 'sub_application_example' # str | The name of the sub-application the jobs belong to. (optional)
library = 'library_example' # str | The job's library name. (optional)
mem_name = 'mem_name_example' # str | Member name. (optional)
mem_library = 'mem_library_example' # str | Member's library. (optional)
host = 'host_example' # str |  (optional)
host_group = 'host_group_example' # str | Job's host group. (optional)
run_as = 'run_as_example' # str | Runs as (username on agent machine). (optional)
order_id = 'order_id_example' # str | Job's order id. (optional)
status = 'All' # str | The job's end status. (optional) (default to All)
order_date_from = 'order_date_from_example' # str | Indicating a date by which will look for jobs that their order date started afterwards. Date format - YYYY-MM-DD. (optional)
order_date_to = 'order_date_to_example' # str | Indicating a date by which will look for jobs that their order date ended before. Date format - YYYY-MM-DD. (optional)
number_of_runs = 789 # int |  (optional)

try:
    # Search jobs in Archive
    api_response = api_instance.search_jobs(limit=limit, jobname=jobname, jobid=jobid, ctm=ctm, server=server, folder=folder, from_time=from_time, to_time=to_time, log_contains=log_contains, output_contains=output_contains, application=application, sub_application=sub_application, library=library, mem_name=mem_name, mem_library=mem_library, host=host, host_group=host_group, run_as=run_as, order_id=order_id, status=status, order_date_from=order_date_from, order_date_to=order_date_to, number_of_runs=number_of_runs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->search_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| maximum jobs to fetch (default 500). | [optional] [default to 500]
 **jobname** | **str**| The name of the job. | [optional] 
 **jobid** | **str**|  | [optional] 
 **ctm** | **str**| The name of the Control-M server in which the job was ordered from. | [optional] 
 **server** | **str**| The name of the Control-M server in which the job was ordered from. | [optional] 
 **folder** | **str**| The name of the parent folder. | [optional] 
 **from_time** | **str**| Job execution start date. Date format - YYYY-MM-DD. | [optional] 
 **to_time** | **str**| Job execution end date. Date format - YYYY-MM-DD. | [optional] 
 **log_contains** | **str**| Job log must contain the given phrase. | [optional] 
 **output_contains** | **str**| Job output must contain the given phrase. | [optional] 
 **application** | **str**| The name of the application the jobs belong to. | [optional] 
 **sub_application** | **str**| The name of the sub-application the jobs belong to. | [optional] 
 **library** | **str**| The job&#x27;s library name. | [optional] 
 **mem_name** | **str**| Member name. | [optional] 
 **mem_library** | **str**| Member&#x27;s library. | [optional] 
 **host** | **str**|  | [optional] 
 **host_group** | **str**| Job&#x27;s host group. | [optional] 
 **run_as** | **str**| Runs as (username on agent machine). | [optional] 
 **order_id** | **str**| Job&#x27;s order id. | [optional] 
 **status** | **str**| The job&#x27;s end status. | [optional] [default to All]
 **order_date_from** | **str**| Indicating a date by which will look for jobs that their order date started afterwards. Date format - YYYY-MM-DD. | [optional] 
 **order_date_to** | **str**| Indicating a date by which will look for jobs that their order date ended before. Date format - YYYY-MM-DD. | [optional] 
 **number_of_runs** | **int**|  | [optional] 

### Return type

[**ArchiveJobsList**](ArchiveJobsList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

