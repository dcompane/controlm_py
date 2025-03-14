# coding: utf-8

"""
    Control-M Services

    Provides access to BMC Control-M Services  # noqa: E501

    OpenAPI spec version: 9.21.340
    Contact: customer_support@bmc.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RunReportInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'report_id': 'str',
        'name': 'str',
        'format': 'str',
        'status': 'str',
        'url': 'str',
        'web_url': 'str'
    }

    attribute_map = {
        'report_id': 'reportId',
        'name': 'name',
        'format': 'format',
        'status': 'status',
        'url': 'url',
        'web_url': 'webUrl'
    }

    def __init__(self, report_id=None, name=None, format=None, status=None, url=None, web_url=None):  # noqa: E501
        """RunReportInfo - a model defined in Swagger"""  # noqa: E501
        self._report_id = None
        self._name = None
        self._format = None
        self._status = None
        self._url = None
        self._web_url = None
        self.discriminator = None
        if report_id is not None:
            self.report_id = report_id
        if name is not None:
            self.name = name
        if format is not None:
            self.format = format
        if status is not None:
            self.status = status
        if url is not None:
            self.url = url
        if web_url is not None:
            self.web_url = web_url

    @property
    def report_id(self):
        """Gets the report_id of this RunReportInfo.  # noqa: E501


        :return: The report_id of this RunReportInfo.  # noqa: E501
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        """Sets the report_id of this RunReportInfo.


        :param report_id: The report_id of this RunReportInfo.  # noqa: E501
        :type: str
        """

        self._report_id = report_id

    @property
    def name(self):
        """Gets the name of this RunReportInfo.  # noqa: E501


        :return: The name of this RunReportInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RunReportInfo.


        :param name: The name of this RunReportInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def format(self):
        """Gets the format of this RunReportInfo.  # noqa: E501


        :return: The format of this RunReportInfo.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this RunReportInfo.


        :param format: The format of this RunReportInfo.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def status(self):
        """Gets the status of this RunReportInfo.  # noqa: E501


        :return: The status of this RunReportInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RunReportInfo.


        :param status: The status of this RunReportInfo.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def url(self):
        """Gets the url of this RunReportInfo.  # noqa: E501


        :return: The url of this RunReportInfo.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this RunReportInfo.


        :param url: The url of this RunReportInfo.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def web_url(self):
        """Gets the web_url of this RunReportInfo.  # noqa: E501


        :return: The web_url of this RunReportInfo.  # noqa: E501
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this RunReportInfo.


        :param web_url: The web_url of this RunReportInfo.  # noqa: E501
        :type: str
        """

        self._web_url = web_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(RunReportInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RunReportInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
