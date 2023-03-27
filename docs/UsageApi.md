# controlm_py.UsageApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_usage_jobs**](UsageApi.md#get_usage_jobs) | **GET** /usage/jobs | Enables you to get a count of eligible jobs in the current (active) day from New Day onwards

# **get_usage_jobs**
> object get_usage_jobs()

Enables you to get a count of eligible jobs in the current (active) day from New Day onwards

Enables you to get a count of eligible jobs in the current (active) day from New Day onwards

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
api_instance = controlm_py.UsageApi(controlm_py.ApiClient(configuration))

try:
    # Enables you to get a count of eligible jobs in the current (active) day from New Day onwards
    api_response = api_instance.get_usage_jobs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_usage_jobs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

