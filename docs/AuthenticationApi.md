# controlm_py.AuthenticationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token**](AuthenticationApi.md#create_token) | **POST** /authentication/token | Creates authentication token
[**delete_token**](AuthenticationApi.md#delete_token) | **DELETE** /authentication/token/{tokenName} | Deletes authentication token data
[**get_token_data**](AuthenticationApi.md#get_token_data) | **GET** /authentication/token/{tokenName} | Returns authentication token data
[**get_token_data_by_value**](AuthenticationApi.md#get_token_data_by_value) | **POST** /authentication/tokenbyvalue | Returns authentication token data
[**get_token_list**](AuthenticationApi.md#get_token_list) | **GET** /authentication/tokens | Returns list of authentication token data for the authorized user
[**update_token**](AuthenticationApi.md#update_token) | **PUT** /authentication/token | Updates authentication token data

# **create_token**
> TokenDataResponse create_token(body)

Creates authentication token

Creates authentication token

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
api_instance = controlm_py.AuthenticationApi(controlm_py.ApiClient(configuration))
body = controlm_py.TokenDataRequest() # TokenDataRequest | The JSON file with the token data

try:
    # Creates authentication token
    api_response = api_instance.create_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->create_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenDataRequest**](TokenDataRequest.md)| The JSON file with the token data | 

### Return type

[**TokenDataResponse**](TokenDataResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token**
> SuccessData delete_token(token_name, for_agent=for_agent, type=type)

Deletes authentication token data

Deletes authentication token data

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
api_instance = controlm_py.AuthenticationApi(controlm_py.ApiClient(configuration))
token_name = 'token_name_example' # str | The token name
for_agent = false # bool | is this request for agent purposes (optional) (default to false)
type = 'type_example' # str | the kind of token to delete, replace forAgent option (optional)

try:
    # Deletes authentication token data
    api_response = api_instance.delete_token(token_name, for_agent=for_agent, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->delete_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_name** | **str**| The token name | 
 **for_agent** | **bool**| is this request for agent purposes | [optional] [default to false]
 **type** | **str**| the kind of token to delete, replace forAgent option | [optional] 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_data**
> TokenDataResponse get_token_data(token_name, for_agent=for_agent, type=type)

Returns authentication token data

Returns authentication token data

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
api_instance = controlm_py.AuthenticationApi(controlm_py.ApiClient(configuration))
token_name = 'token_name_example' # str | The token name
for_agent = false # bool | is this request for agent purposes (optional) (default to false)
type = 'type_example' # str | the kind of token to get, replace forAgent option (optional)

try:
    # Returns authentication token data
    api_response = api_instance.get_token_data(token_name, for_agent=for_agent, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->get_token_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_name** | **str**| The token name | 
 **for_agent** | **bool**| is this request for agent purposes | [optional] [default to false]
 **type** | **str**| the kind of token to get, replace forAgent option | [optional] 

### Return type

[**TokenDataResponse**](TokenDataResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_data_by_value**
> TokenDataResponse get_token_data_by_value(body)

Returns authentication token data

Returns authentication token data

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
api_instance = controlm_py.AuthenticationApi(controlm_py.ApiClient(configuration))
body = controlm_py.TokenByValueRequest() # TokenByValueRequest | The token value

try:
    # Returns authentication token data
    api_response = api_instance.get_token_data_by_value(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->get_token_data_by_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenByValueRequest**](TokenByValueRequest.md)| The token value | 

### Return type

[**TokenDataResponse**](TokenDataResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_list**
> TokenList get_token_list(for_agent=for_agent, type=type)

Returns list of authentication token data for the authorized user

Returns list of authentication token data for the authorized user

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
api_instance = controlm_py.AuthenticationApi(controlm_py.ApiClient(configuration))
for_agent = false # bool | is this request for agent purposes (optional) (default to false)
type = 'type_example' # str | the kind of tokens to fetch, replace forAgent option (optional)

try:
    # Returns list of authentication token data for the authorized user
    api_response = api_instance.get_token_list(for_agent=for_agent, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->get_token_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **for_agent** | **bool**| is this request for agent purposes | [optional] [default to false]
 **type** | **str**| the kind of tokens to fetch, replace forAgent option | [optional] 

### Return type

[**TokenList**](TokenList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_token**
> TokenDataResponse update_token(body)

Updates authentication token data

Updates authentication token data

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
api_instance = controlm_py.AuthenticationApi(controlm_py.ApiClient(configuration))
body = controlm_py.TokenDataRequest() # TokenDataRequest | The JSON file with the token data

try:
    # Updates authentication token data
    api_response = api_instance.update_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->update_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenDataRequest**](TokenDataRequest.md)| The JSON file with the token data | 

### Return type

[**TokenDataResponse**](TokenDataResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

