# controlm_py.StatusApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_status**](StatusApi.md#get_status) | **GET** /status | Get AAPI server status.

# **get_status**
> str get_status()

Get AAPI server status.

Get AAPI server status.

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
api_instance = controlm_py.StatusApi(controlm_py.ApiClient(configuration))

try:
    # Get AAPI server status.
    api_response = api_instance.get_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->get_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

