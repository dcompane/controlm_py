# coding: utf-8

"""
    Control-M Services

    Provides access to BMC Control-M Services  # noqa: E501

    OpenAPI spec version: 9.21.340
    Contact: customer_support@bmc.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import controlm_py
from controlm_py.api.authentication_api import AuthenticationApi  # noqa: E501
from controlm_py.rest import ApiException


class TestAuthenticationApi(unittest.TestCase):
    """AuthenticationApi unit test stubs"""

    def setUp(self):
        self.api = AuthenticationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_token(self):
        """Test case for create_token

        Creates authentication token  # noqa: E501
        """
        pass

    def test_delete_token(self):
        """Test case for delete_token

        Deletes authentication token data  # noqa: E501
        """
        pass

    def test_get_token_data(self):
        """Test case for get_token_data

        Returns authentication token data  # noqa: E501
        """
        pass

    def test_get_token_data_by_value(self):
        """Test case for get_token_data_by_value

        Returns authentication token data  # noqa: E501
        """
        pass

    def test_get_token_list(self):
        """Test case for get_token_list

        Returns list of authentication token data for the authorized user  # noqa: E501
        """
        pass

    def test_update_token(self):
        """Test case for update_token

        Updates authentication token data  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
