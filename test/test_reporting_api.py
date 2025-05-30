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
from controlm_py.api.reporting_api import ReportingApi  # noqa: E501
from controlm_py.rest import ApiException


class TestReportingApi(unittest.TestCase):
    """ReportingApi unit test stubs"""

    def setUp(self):
        self.api = ReportingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_download_report_by_name(self):
        """Test case for download_report_by_name

        Download report by ID  # noqa: E501
        """
        pass

    def test_get_report_by_name(self):
        """Test case for get_report_by_name

        Retrieves a report by name.  # noqa: E501
        """
        pass

    def test_get_report_filters(self):
        """Test case for get_report_filters

        Retrieves report filters  # noqa: E501
        """
        pass

    def test_get_report_status(self):
        """Test case for get_report_status

        Retrieves status information for a report generation request based on the report ID  # noqa: E501
        """
        pass

    def test_run_report(self):
        """Test case for run_report

        Run a report  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
