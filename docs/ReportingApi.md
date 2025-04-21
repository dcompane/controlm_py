# controlm_py.ReportingApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_report_by_name**](ReportingApi.md#download_report_by_name) | **GET** /reporting/download | Download report by ID
[**get_report_by_name**](ReportingApi.md#get_report_by_name) | **GET** /reporting/report/{name} | Retrieves a report by name.
[**get_report_filters**](ReportingApi.md#get_report_filters) | **GET** /reporting/reportFilters/{name} | Retrieves report filters
[**get_report_status**](ReportingApi.md#get_report_status) | **GET** /reporting/status/{reportId} | Retrieves status information for a report generation request based on the report ID
[**run_report**](ReportingApi.md#run_report) | **POST** /reporting/report | Run a report

# **download_report_by_name**
> InputStreamResource download_report_by_name(report_id=report_id)

Download report by ID

Downloads a report with a given ID

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
api_instance = controlm_py.ReportingApi(controlm_py.ApiClient(configuration))
report_id = 'report_id_example' # str | The ID of the report to download (optional)

try:
    # Download report by ID
    api_response = api_instance.download_report_by_name(report_id=report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingApi->download_report_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| The ID of the report to download | [optional] 

### Return type

[**InputStreamResource**](InputStreamResource.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_by_name**
> ReportResult get_report_by_name(name, format)

Retrieves a report by name.

Retrieves a report by name in the desired format (CSV,PDF ,EXCEL). If the report is shared, add [shared:] before the name. This REST API command will be deprecated soon.

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
api_instance = controlm_py.ReportingApi(controlm_py.ApiClient(configuration))
name = 'name_example' # str | The report name.
format = 'format_example' # str | 

try:
    # Retrieves a report by name.
    api_response = api_instance.get_report_by_name(name, format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingApi->get_report_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The report name. | 
 **format** | **str**|  | 

### Return type

[**ReportResult**](ReportResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_filters**
> RunReport get_report_filters(name)

Retrieves report filters

Retrieves report filters

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
api_instance = controlm_py.ReportingApi(controlm_py.ApiClient(configuration))
name = 'name_example' # str | The report name

try:
    # Retrieves report filters
    api_response = api_instance.get_report_filters(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingApi->get_report_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The report name | 

### Return type

[**RunReport**](RunReport.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_status**
> RunReportInfo get_report_status(report_id)

Retrieves status information for a report generation request based on the report ID

Retrieves status information for a report generation request based on the report ID

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
api_instance = controlm_py.ReportingApi(controlm_py.ApiClient(configuration))
report_id = 'report_id_example' # str | The ID of the report

try:
    # Retrieves status information for a report generation request based on the report ID
    api_response = api_instance.get_report_status(report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingApi->get_report_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| The ID of the report | 

### Return type

[**RunReportInfo**](RunReportInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_report**
> RunReportInfo run_report(body)

Run a report

Sends a request to generate a report asynchronously and returns the request status. If the report is shared, add [shared:] before the name.

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
api_instance = controlm_py.ReportingApi(controlm_py.ApiClient(configuration))
body = controlm_py.RunReport() # RunReport | The report generation parameters

try:
    # Run a report
    api_response = api_instance.run_report(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingApi->run_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RunReport**](RunReport.md)| The report generation parameters | 

### Return type

[**RunReportInfo**](RunReportInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

