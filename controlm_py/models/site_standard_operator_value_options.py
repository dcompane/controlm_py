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

class SiteStandardOperatorValueOptions(object):
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
        'operator': 'str',
        'value': 'int'
    }

    attribute_map = {
        'operator': 'operator',
        'value': 'value'
    }

    def __init__(self, operator=None, value=None):  # noqa: E501
        """SiteStandardOperatorValueOptions - a model defined in Swagger"""  # noqa: E501
        self._operator = None
        self._value = None
        self.discriminator = None
        self.operator = operator
        if value is not None:
            self.value = value

    @property
    def operator(self):
        """Gets the operator of this SiteStandardOperatorValueOptions.  # noqa: E501


        :return: The operator of this SiteStandardOperatorValueOptions.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this SiteStandardOperatorValueOptions.


        :param operator: The operator of this SiteStandardOperatorValueOptions.  # noqa: E501
        :type: str
        """
        if operator is None:
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501
        allowed_values = ["Equal", "NotEqual", "LessThan", "GreaterThan", "Even", "Odd"]  # noqa: E501
        if operator not in allowed_values:
            raise ValueError(
                "Invalid value for `operator` ({0}), must be one of {1}"  # noqa: E501
                .format(operator, allowed_values)
            )

        self._operator = operator

    @property
    def value(self):
        """Gets the value of this SiteStandardOperatorValueOptions.  # noqa: E501

        Nomeric value, Even and Odd does not need value  # noqa: E501

        :return: The value of this SiteStandardOperatorValueOptions.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SiteStandardOperatorValueOptions.

        Nomeric value, Even and Odd does not need value  # noqa: E501

        :param value: The value of this SiteStandardOperatorValueOptions.  # noqa: E501
        :type: int
        """

        self._value = value

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
        if issubclass(SiteStandardOperatorValueOptions, dict):
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
        if not isinstance(other, SiteStandardOperatorValueOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other