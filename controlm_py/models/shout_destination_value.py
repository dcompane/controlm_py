# coding: utf-8

"""
    Control-M Services

    Provides access to BMC Control-M Services  # noqa: E501

    OpenAPI spec version: 9.21.325
    Contact: customer_support@bmc.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ShoutDestinationValue(object):
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
        'value': 'str',
        'value_list': 'list[ValueListItem]'
    }

    attribute_map = {
        'value': 'value',
        'value_list': 'valueList'
    }

    def __init__(self, value=None, value_list=None):  # noqa: E501
        """ShoutDestinationValue - a model defined in Swagger"""  # noqa: E501
        self._value = None
        self._value_list = None
        self.discriminator = None
        if value is not None:
            self.value = value
        if value_list is not None:
            self.value_list = value_list

    @property
    def value(self):
        """Gets the value of this ShoutDestinationValue.  # noqa: E501

        Shout Destination value  # noqa: E501

        :return: The value of this ShoutDestinationValue.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ShoutDestinationValue.

        Shout Destination value  # noqa: E501

        :param value: The value of this ShoutDestinationValue.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def value_list(self):
        """Gets the value_list of this ShoutDestinationValue.  # noqa: E501

        Shout Destination value list  # noqa: E501

        :return: The value_list of this ShoutDestinationValue.  # noqa: E501
        :rtype: list[ValueListItem]
        """
        return self._value_list

    @value_list.setter
    def value_list(self, value_list):
        """Sets the value_list of this ShoutDestinationValue.

        Shout Destination value list  # noqa: E501

        :param value_list: The value_list of this ShoutDestinationValue.  # noqa: E501
        :type: list[ValueListItem]
        """

        self._value_list = value_list

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
        if issubclass(ShoutDestinationValue, dict):
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
        if not isinstance(other, ShoutDestinationValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other