# coding: utf-8

"""
    Control-M Services

    Provides access to BMC Control-M Services  # noqa: E501

    OpenAPI spec version: 9.21.340
    Contact: customer_support@bmc.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from controlm_py.api_client import ApiClient


class AuthenticationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_token(self, body, **kwargs):  # noqa: E501
        """Creates authentication token  # noqa: E501

        Creates authentication token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_token(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TokenDataRequest body: The JSON file with the token data (required)
        :return: TokenDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_token_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_token_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_token_with_http_info(self, body, **kwargs):  # noqa: E501
        """Creates authentication token  # noqa: E501

        Creates authentication token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_token_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TokenDataRequest body: The JSON file with the token data (required)
        :return: TokenDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/authentication/token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TokenDataResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_token(self, token_name, **kwargs):  # noqa: E501
        """Deletes authentication token data  # noqa: E501

        Deletes authentication token data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_token(token_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token_name: The token name (required)
        :param bool for_agent: is this request for agent purposes
        :param str type: the kind of token to delete, replace forAgent option
        :return: SuccessData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_token_with_http_info(token_name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_token_with_http_info(token_name, **kwargs)  # noqa: E501
            return data

    def delete_token_with_http_info(self, token_name, **kwargs):  # noqa: E501
        """Deletes authentication token data  # noqa: E501

        Deletes authentication token data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_token_with_http_info(token_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token_name: The token name (required)
        :param bool for_agent: is this request for agent purposes
        :param str type: the kind of token to delete, replace forAgent option
        :return: SuccessData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token_name', 'for_agent', 'type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token_name' is set
        if ('token_name' not in params or
                params['token_name'] is None):
            raise ValueError("Missing the required parameter `token_name` when calling `delete_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'token_name' in params:
            path_params['tokenName'] = params['token_name']  # noqa: E501

        query_params = []
        if 'for_agent' in params:
            query_params.append(('forAgent', params['for_agent']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/authentication/token/{tokenName}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuccessData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_token_data(self, token_name, **kwargs):  # noqa: E501
        """Returns authentication token data  # noqa: E501

        Returns authentication token data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_token_data(token_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token_name: The token name (required)
        :param bool for_agent: is this request for agent purposes
        :param str type: the kind of token to get, replace forAgent option
        :return: TokenDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_token_data_with_http_info(token_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_token_data_with_http_info(token_name, **kwargs)  # noqa: E501
            return data

    def get_token_data_with_http_info(self, token_name, **kwargs):  # noqa: E501
        """Returns authentication token data  # noqa: E501

        Returns authentication token data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_token_data_with_http_info(token_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token_name: The token name (required)
        :param bool for_agent: is this request for agent purposes
        :param str type: the kind of token to get, replace forAgent option
        :return: TokenDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token_name', 'for_agent', 'type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_token_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token_name' is set
        if ('token_name' not in params or
                params['token_name'] is None):
            raise ValueError("Missing the required parameter `token_name` when calling `get_token_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'token_name' in params:
            path_params['tokenName'] = params['token_name']  # noqa: E501

        query_params = []
        if 'for_agent' in params:
            query_params.append(('forAgent', params['for_agent']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/authentication/token/{tokenName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TokenDataResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_token_data_by_value(self, body, **kwargs):  # noqa: E501
        """Returns authentication token data  # noqa: E501

        Returns authentication token data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_token_data_by_value(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TokenByValueRequest body: The token value (required)
        :return: TokenDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_token_data_by_value_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.get_token_data_by_value_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def get_token_data_by_value_with_http_info(self, body, **kwargs):  # noqa: E501
        """Returns authentication token data  # noqa: E501

        Returns authentication token data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_token_data_by_value_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TokenByValueRequest body: The token value (required)
        :return: TokenDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_token_data_by_value" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `get_token_data_by_value`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/authentication/tokenbyvalue', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TokenDataResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_token_list(self, **kwargs):  # noqa: E501
        """Returns list of authentication token data for the authorized user  # noqa: E501

        Returns list of authentication token data for the authorized user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_token_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool for_agent: is this request for agent purposes
        :param str type: the kind of tokens to fetch, replace forAgent option
        :return: TokenList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_token_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_token_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_token_list_with_http_info(self, **kwargs):  # noqa: E501
        """Returns list of authentication token data for the authorized user  # noqa: E501

        Returns list of authentication token data for the authorized user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_token_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool for_agent: is this request for agent purposes
        :param str type: the kind of tokens to fetch, replace forAgent option
        :return: TokenList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['for_agent', 'type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_token_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'for_agent' in params:
            query_params.append(('forAgent', params['for_agent']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/authentication/tokens', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TokenList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_token(self, body, **kwargs):  # noqa: E501
        """Updates authentication token data  # noqa: E501

        Updates authentication token data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_token(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TokenDataRequest body: The JSON file with the token data (required)
        :return: TokenDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_token_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_token_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def update_token_with_http_info(self, body, **kwargs):  # noqa: E501
        """Updates authentication token data  # noqa: E501

        Updates authentication token data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_token_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TokenDataRequest body: The JSON file with the token data (required)
        :return: TokenDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/authentication/token', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TokenDataResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
