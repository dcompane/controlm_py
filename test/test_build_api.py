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
from controlm_py.api.build_api import BuildApi  # noqa: E501
from controlm_py.rest import ApiException


class TestBuildApi(unittest.TestCase):
    """BuildApi unit test stubs"""

    def setUp(self):
        self.api = BuildApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_build_file(self):
        """Test case for build_file

        Compile definitions file to check its validity  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
