# controlm_py.SessionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**do_login**](SessionApi.md#do_login) | **POST** /session/login | login user to Control-M
[**do_logout**](SessionApi.md#do_logout) | **POST** /session/logout | logout user from Control-M
[**update_my_password**](SessionApi.md#update_my_password) | **POST** /session/user/password/update | Change my password

# **do_login**
> LoginResult do_login(body)

login user to Control-M

Authenticate the user with the specified password and return a token that can be used later in subsequent requests to access Control-M.

### Example
```python
from __future__ import print_function
import time
import controlm_py
from controlm_py.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = controlm_py.SessionApi()
body = controlm_py.LoginCredentials() # LoginCredentials | The credentials to use for login.

try:
    # login user to Control-M
    api_response = api_instance.do_login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->do_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginCredentials**](LoginCredentials.md)| The credentials to use for login. | 

### Return type

[**LoginResult**](LoginResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_logout**
> SuccessData do_logout()

logout user from Control-M

Disconnects the user session specified by the request authentication token, and removes it from the server memory.

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
api_instance = controlm_py.SessionApi(controlm_py.ApiClient(configuration))

try:
    # logout user from Control-M
    api_response = api_instance.do_logout()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->do_logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_my_password**
> SuccessData update_my_password(body)

Change my password

Change my password

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
api_instance = controlm_py.SessionApi(controlm_py.ApiClient(configuration))
body = controlm_py.PasswordsObject() # PasswordsObject | The new password.

try:
    # Change my password
    api_response = api_instance.update_my_password(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->update_my_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PasswordsObject**](PasswordsObject.md)| The new password. | 

### Return type

[**SuccessData**](SuccessData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

