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

class BetweenTime(object):
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
        'from_time': 'str',
        'to_time': 'str'
    }

    attribute_map = {
        'from_time': 'fromTime',
        'to_time': 'toTime'
    }

    def __init__(self, from_time=None, to_time=None):  # noqa: E501
        """BetweenTime - a model defined in Swagger"""  # noqa: E501
        self._from_time = None
        self._to_time = None
        self.discriminator = None
        if from_time is not None:
            self.from_time = from_time
        if to_time is not None:
            self.to_time = to_time

    @property
    def from_time(self):
        """Gets the from_time of this BetweenTime.  # noqa: E501

        From time in format hhmm.  # noqa: E501

        :return: The from_time of this BetweenTime.  # noqa: E501
        :rtype: str
        """
        return self._from_time

    @from_time.setter
    def from_time(self, from_time):
        """Sets the from_time of this BetweenTime.

        From time in format hhmm.  # noqa: E501

        :param from_time: The from_time of this BetweenTime.  # noqa: E501
        :type: str
        """

        self._from_time = from_time

    @property
    def to_time(self):
        """Gets the to_time of this BetweenTime.  # noqa: E501

        To time in format hhmm.  # noqa: E501

        :return: The to_time of this BetweenTime.  # noqa: E501
        :rtype: str
        """
        return self._to_time

    @to_time.setter
    def to_time(self, to_time):
        """Sets the to_time of this BetweenTime.

        To time in format hhmm.  # noqa: E501

        :param to_time: The to_time of this BetweenTime.  # noqa: E501
        :type: str
        """

        self._to_time = to_time

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
        if issubclass(BetweenTime, dict):
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
        if not isinstance(other, BetweenTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
