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

class Statistics(object):
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
        'current_period': 'str',
        'calendar_controlm': 'str',
        'calendar_name': 'str',
        'periods': 'list[StatisticsPeriod]'
    }

    attribute_map = {
        'current_period': 'currentPeriod',
        'calendar_controlm': 'calendarControlm',
        'calendar_name': 'calendarName',
        'periods': 'periods'
    }

    def __init__(self, current_period=None, calendar_controlm=None, calendar_name=None, periods=None):  # noqa: E501
        """Statistics - a model defined in Swagger"""  # noqa: E501
        self._current_period = None
        self._calendar_controlm = None
        self._calendar_name = None
        self._periods = None
        self.discriminator = None
        if current_period is not None:
            self.current_period = current_period
        if calendar_controlm is not None:
            self.calendar_controlm = calendar_controlm
        if calendar_name is not None:
            self.calendar_name = calendar_name
        if periods is not None:
            self.periods = periods

    @property
    def current_period(self):
        """Gets the current_period of this Statistics.  # noqa: E501

        Statistics calendar period  # noqa: E501

        :return: The current_period of this Statistics.  # noqa: E501
        :rtype: str
        """
        return self._current_period

    @current_period.setter
    def current_period(self, current_period):
        """Sets the current_period of this Statistics.

        Statistics calendar period  # noqa: E501

        :param current_period: The current_period of this Statistics.  # noqa: E501
        :type: str
        """

        self._current_period = current_period

    @property
    def calendar_controlm(self):
        """Gets the calendar_controlm of this Statistics.  # noqa: E501

        Statistics calendar Control-M  # noqa: E501

        :return: The calendar_controlm of this Statistics.  # noqa: E501
        :rtype: str
        """
        return self._calendar_controlm

    @calendar_controlm.setter
    def calendar_controlm(self, calendar_controlm):
        """Sets the calendar_controlm of this Statistics.

        Statistics calendar Control-M  # noqa: E501

        :param calendar_controlm: The calendar_controlm of this Statistics.  # noqa: E501
        :type: str
        """

        self._calendar_controlm = calendar_controlm

    @property
    def calendar_name(self):
        """Gets the calendar_name of this Statistics.  # noqa: E501

        Statistics calendar name  # noqa: E501

        :return: The calendar_name of this Statistics.  # noqa: E501
        :rtype: str
        """
        return self._calendar_name

    @calendar_name.setter
    def calendar_name(self, calendar_name):
        """Sets the calendar_name of this Statistics.

        Statistics calendar name  # noqa: E501

        :param calendar_name: The calendar_name of this Statistics.  # noqa: E501
        :type: str
        """

        self._calendar_name = calendar_name

    @property
    def periods(self):
        """Gets the periods of this Statistics.  # noqa: E501


        :return: The periods of this Statistics.  # noqa: E501
        :rtype: list[StatisticsPeriod]
        """
        return self._periods

    @periods.setter
    def periods(self, periods):
        """Sets the periods of this Statistics.


        :param periods: The periods of this Statistics.  # noqa: E501
        :type: list[StatisticsPeriod]
        """

        self._periods = periods

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
        if issubclass(Statistics, dict):
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
        if not isinstance(other, Statistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
