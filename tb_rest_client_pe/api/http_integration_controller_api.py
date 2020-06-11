# coding: utf-8

"""
    ThingsBoard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tb_rest_client_pe.api_client import ApiClient


class HttpIntegrationControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def check_status_using_get(self, routing_key, request_params, request_headers, **kwargs):  # noqa: E501
        """checkStatus  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_status_using_get(routing_key, request_params, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param object request_params: requestParams (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.check_status_using_get_with_http_info(routing_key, request_params, request_headers, **kwargs)  # noqa: E501
        else:
            (data) = self.check_status_using_get_with_http_info(routing_key, request_params, request_headers, **kwargs)  # noqa: E501
            return data

    def check_status_using_get_with_http_info(self, routing_key, request_params, request_headers, **kwargs):  # noqa: E501
        """checkStatus  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_status_using_get_with_http_info(routing_key, request_params, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param object request_params: requestParams (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['routing_key', 'request_params', 'request_headers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_status_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'routing_key' is set
        if ('routing_key' not in params or
                params['routing_key'] is None):
            raise ValueError("Missing the required parameter `routing_key` when calling `check_status_using_get`")  # noqa: E501
        # verify the required parameter 'request_params' is set
        if ('request_params' not in params or
                params['request_params'] is None):
            raise ValueError("Missing the required parameter `request_params` when calling `check_status_using_get`")  # noqa: E501
        # verify the required parameter 'request_headers' is set
        if ('request_headers' not in params or
                params['request_headers'] is None):
            raise ValueError("Missing the required parameter `request_headers` when calling `check_status_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'routing_key' in params:
            path_params['routingKey'] = params['routing_key']  # noqa: E501

        query_params = []
        if 'request_params' in params:
            query_params.append(('requestParams', params['request_params']))  # noqa: E501

        header_params = {}
        if 'request_headers' in params:
            header_params['requestHeaders'] = params['request_headers']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/integrations/http/{routingKey}{?requestParams}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def process_request_using_post2(self, routing_key, suffix, request_params, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.process_request_using_post2(routing_key, suffix, request_params, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str suffix: suffix (required)
        :param object request_params: requestParams (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.process_request_using_post2_with_http_info(routing_key, suffix, request_params, request_headers, **kwargs)  # noqa: E501
        else:
            (data) = self.process_request_using_post2_with_http_info(routing_key, suffix, request_params, request_headers, **kwargs)  # noqa: E501
            return data

    def process_request_using_post2_with_http_info(self, routing_key, suffix, request_params, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.process_request_using_post2_with_http_info(routing_key, suffix, request_params, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str suffix: suffix (required)
        :param object request_params: requestParams (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['routing_key', 'suffix', 'request_params', 'request_headers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method process_request_using_post2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'routing_key' is set
        if ('routing_key' not in params or
                params['routing_key'] is None):
            raise ValueError("Missing the required parameter `routing_key` when calling `process_request_using_post2`")  # noqa: E501
        # verify the required parameter 'suffix' is set
        if ('suffix' not in params or
                params['suffix'] is None):
            raise ValueError("Missing the required parameter `suffix` when calling `process_request_using_post2`")  # noqa: E501
        # verify the required parameter 'request_params' is set
        if ('request_params' not in params or
                params['request_params'] is None):
            raise ValueError("Missing the required parameter `request_params` when calling `process_request_using_post2`")  # noqa: E501
        # verify the required parameter 'request_headers' is set
        if ('request_headers' not in params or
                params['request_headers'] is None):
            raise ValueError("Missing the required parameter `request_headers` when calling `process_request_using_post2`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'routing_key' in params:
            path_params['routingKey'] = params['routing_key']  # noqa: E501
        if 'suffix' in params:
            path_params['suffix'] = params['suffix']  # noqa: E501

        query_params = []

        header_params = {}
        if 'request_headers' in params:
            header_params['requestHeaders'] = params['request_headers']  # noqa: E501

        form_params = []
        local_var_files = {}
        if 'request_params' in params:
            form_params.append(('requestParams', params['request_params']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/integrations/http/{routingKey}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def process_request_using_post3(self, routing_key, suffix, request_params, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.process_request_using_post3(routing_key, suffix, request_params, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str suffix: suffix (required)
        :param object request_params: requestParams (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.process_request_using_post3_with_http_info(routing_key, suffix, request_params, request_headers, **kwargs)  # noqa: E501
        else:
            (data) = self.process_request_using_post3_with_http_info(routing_key, suffix, request_params, request_headers, **kwargs)  # noqa: E501
            return data

    def process_request_using_post3_with_http_info(self, routing_key, suffix, request_params, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.process_request_using_post3_with_http_info(routing_key, suffix, request_params, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str suffix: suffix (required)
        :param object request_params: requestParams (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['routing_key', 'suffix', 'request_params', 'request_headers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method process_request_using_post3" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'routing_key' is set
        if ('routing_key' not in params or
                params['routing_key'] is None):
            raise ValueError("Missing the required parameter `routing_key` when calling `process_request_using_post3`")  # noqa: E501
        # verify the required parameter 'suffix' is set
        if ('suffix' not in params or
                params['suffix'] is None):
            raise ValueError("Missing the required parameter `suffix` when calling `process_request_using_post3`")  # noqa: E501
        # verify the required parameter 'request_params' is set
        if ('request_params' not in params or
                params['request_params'] is None):
            raise ValueError("Missing the required parameter `request_params` when calling `process_request_using_post3`")  # noqa: E501
        # verify the required parameter 'request_headers' is set
        if ('request_headers' not in params or
                params['request_headers'] is None):
            raise ValueError("Missing the required parameter `request_headers` when calling `process_request_using_post3`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'routing_key' in params:
            path_params['routingKey'] = params['routing_key']  # noqa: E501
        if 'suffix' in params:
            path_params['suffix'] = params['suffix']  # noqa: E501

        query_params = []

        header_params = {}
        if 'request_headers' in params:
            header_params['requestHeaders'] = params['request_headers']  # noqa: E501

        form_params = []
        local_var_files = {}
        if 'request_params' in params:
            form_params.append(('requestParams', params['request_params']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/integrations/http/{routingKey}/{suffix}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)