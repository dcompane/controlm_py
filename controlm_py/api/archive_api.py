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


class ArchiveApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_archive_job_log(self, job_id, run_no, **kwargs):  # noqa: E501
        """Get job log  # noqa: E501

        Get job log by unique job key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_archive_job_log(job_id, run_no, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: The job ID (required)
        :param int run_no: The execution number in case of multiple executions (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_archive_job_log_with_http_info(job_id, run_no, **kwargs)  # noqa: E501
        else:
            (data) = self.get_archive_job_log_with_http_info(job_id, run_no, **kwargs)  # noqa: E501
            return data

    def get_archive_job_log_with_http_info(self, job_id, run_no, **kwargs):  # noqa: E501
        """Get job log  # noqa: E501

        Get job log by unique job key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_archive_job_log_with_http_info(job_id, run_no, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: The job ID (required)
        :param int run_no: The execution number in case of multiple executions (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id', 'run_no']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_archive_job_log" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params or
                params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_archive_job_log`")  # noqa: E501
        # verify the required parameter 'run_no' is set
        if ('run_no' not in params or
                params['run_no'] is None):
            raise ValueError("Missing the required parameter `run_no` when calling `get_archive_job_log`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']  # noqa: E501

        query_params = []
        if 'run_no' in params:
            query_params.append(('runNo', params['run_no']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/archive/{jobId}/log', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_archive_job_output(self, job_id, run_no, **kwargs):  # noqa: E501
        """Get job output  # noqa: E501

        Get job output by unique job key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_archive_job_output(job_id, run_no, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: The job ID (required)
        :param int run_no: The execution number in case of multiple executions (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_archive_job_output_with_http_info(job_id, run_no, **kwargs)  # noqa: E501
        else:
            (data) = self.get_archive_job_output_with_http_info(job_id, run_no, **kwargs)  # noqa: E501
            return data

    def get_archive_job_output_with_http_info(self, job_id, run_no, **kwargs):  # noqa: E501
        """Get job output  # noqa: E501

        Get job output by unique job key  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_archive_job_output_with_http_info(job_id, run_no, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: The job ID (required)
        :param int run_no: The execution number in case of multiple executions (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id', 'run_no']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_archive_job_output" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params or
                params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `get_archive_job_output`")  # noqa: E501
        # verify the required parameter 'run_no' is set
        if ('run_no' not in params or
                params['run_no'] is None):
            raise ValueError("Missing the required parameter `run_no` when calling `get_archive_job_output`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']  # noqa: E501

        query_params = []
        if 'run_no' in params:
            query_params.append(('runNo', params['run_no']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/archive/{jobId}/output', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_jobs(self, **kwargs):  # noqa: E501
        """Search jobs in Archive  # noqa: E501

        Get all the Control-M Archiving jobs that match the search criterias  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_jobs(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: maximum jobs to fetch (default 500).
        :param str jobname: The name of the job.
        :param str jobid:
        :param str ctm: The name of the Control-M server in which the job was ordered from.
        :param str server: The name of the Control-M server in which the job was ordered from.
        :param str folder: The name of the parent folder.
        :param str from_time: Job execution start date. Date format - YYYY-MM-DD.
        :param str to_time: Job execution end date. Date format - YYYY-MM-DD.
        :param str log_contains: Job log must contain the given phrase.
        :param str output_contains: Job output must contain the given phrase.
        :param str application: The name of the application the jobs belong to.
        :param str sub_application: The name of the sub-application the jobs belong to.
        :param str library: The job's library name.
        :param str mem_name: Member name.
        :param str mem_library: Member's library.
        :param str host:
        :param str host_group: Job's host group.
        :param str run_as: Runs as (username on agent machine).
        :param str order_id: Job's order id.
        :param str status: The job's end status.
        :param str order_date_from: Indicating a date by which will look for jobs that their order date started afterwards. Date format - YYYY-MM-DD.
        :param str order_date_to: Indicating a date by which will look for jobs that their order date ended before. Date format - YYYY-MM-DD.
        :param int number_of_runs:
        :return: ArchiveJobsList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_jobs_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_jobs_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_jobs_with_http_info(self, **kwargs):  # noqa: E501
        """Search jobs in Archive  # noqa: E501

        Get all the Control-M Archiving jobs that match the search criterias  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_jobs_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: maximum jobs to fetch (default 500).
        :param str jobname: The name of the job.
        :param str jobid:
        :param str ctm: The name of the Control-M server in which the job was ordered from.
        :param str server: The name of the Control-M server in which the job was ordered from.
        :param str folder: The name of the parent folder.
        :param str from_time: Job execution start date. Date format - YYYY-MM-DD.
        :param str to_time: Job execution end date. Date format - YYYY-MM-DD.
        :param str log_contains: Job log must contain the given phrase.
        :param str output_contains: Job output must contain the given phrase.
        :param str application: The name of the application the jobs belong to.
        :param str sub_application: The name of the sub-application the jobs belong to.
        :param str library: The job's library name.
        :param str mem_name: Member name.
        :param str mem_library: Member's library.
        :param str host:
        :param str host_group: Job's host group.
        :param str run_as: Runs as (username on agent machine).
        :param str order_id: Job's order id.
        :param str status: The job's end status.
        :param str order_date_from: Indicating a date by which will look for jobs that their order date started afterwards. Date format - YYYY-MM-DD.
        :param str order_date_to: Indicating a date by which will look for jobs that their order date ended before. Date format - YYYY-MM-DD.
        :param int number_of_runs:
        :return: ArchiveJobsList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'jobname', 'jobid', 'ctm', 'server', 'folder', 'from_time', 'to_time', 'log_contains', 'output_contains', 'application', 'sub_application', 'library', 'mem_name', 'mem_library', 'host', 'host_group', 'run_as', 'order_id', 'status', 'order_date_from', 'order_date_to', 'number_of_runs']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_jobs" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'jobname' in params:
            query_params.append(('jobname', params['jobname']))  # noqa: E501
        if 'jobid' in params:
            query_params.append(('jobid', params['jobid']))  # noqa: E501
        if 'ctm' in params:
            query_params.append(('ctm', params['ctm']))  # noqa: E501
        if 'server' in params:
            query_params.append(('server', params['server']))  # noqa: E501
        if 'folder' in params:
            query_params.append(('folder', params['folder']))  # noqa: E501
        if 'from_time' in params:
            query_params.append(('fromTime', params['from_time']))  # noqa: E501
        if 'to_time' in params:
            query_params.append(('toTime', params['to_time']))  # noqa: E501
        if 'log_contains' in params:
            query_params.append(('logContains', params['log_contains']))  # noqa: E501
        if 'output_contains' in params:
            query_params.append(('outputContains', params['output_contains']))  # noqa: E501
        if 'application' in params:
            query_params.append(('application', params['application']))  # noqa: E501
        if 'sub_application' in params:
            query_params.append(('subApplication', params['sub_application']))  # noqa: E501
        if 'library' in params:
            query_params.append(('library', params['library']))  # noqa: E501
        if 'mem_name' in params:
            query_params.append(('memName', params['mem_name']))  # noqa: E501
        if 'mem_library' in params:
            query_params.append(('memLibrary', params['mem_library']))  # noqa: E501
        if 'host' in params:
            query_params.append(('host', params['host']))  # noqa: E501
        if 'host_group' in params:
            query_params.append(('hostGroup', params['host_group']))  # noqa: E501
        if 'run_as' in params:
            query_params.append(('runAs', params['run_as']))  # noqa: E501
        if 'order_id' in params:
            query_params.append(('orderId', params['order_id']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'order_date_from' in params:
            query_params.append(('orderDateFrom', params['order_date_from']))  # noqa: E501
        if 'order_date_to' in params:
            query_params.append(('orderDateTo', params['order_date_to']))  # noqa: E501
        if 'number_of_runs' in params:
            query_params.append(('numberOfRuns', params['number_of_runs']))  # noqa: E501

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
            '/archive/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ArchiveJobsList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
