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

class PoolVariablesName(object):
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
        'pool_name': 'str',
        'variable_name': 'list[str]'
    }

    attribute_map = {
        'pool_name': 'pool_name',
        'variable_name': 'variable_name'
    }

    def __init__(self, pool_name=None, variable_name=None):  # noqa: E501
        """PoolVariablesName - a model defined in Swagger"""  # noqa: E501
        self._pool_name = None
        self._variable_name = None
        self.discriminator = None
        if pool_name is not None:
            self.pool_name = pool_name
        if variable_name is not None:
            self.variable_name = variable_name

    @property
    def pool_name(self):
        """Gets the pool_name of this PoolVariablesName.  # noqa: E501


        :return: The pool_name of this PoolVariablesName.  # noqa: E501
        :rtype: str
        """
        return self._pool_name

    @pool_name.setter
    def pool_name(self, pool_name):
        """Sets the pool_name of this PoolVariablesName.


        :param pool_name: The pool_name of this PoolVariablesName.  # noqa: E501
        :type: str
        """

        self._pool_name = pool_name

    @property
    def variable_name(self):
        """Gets the variable_name of this PoolVariablesName.  # noqa: E501


        :return: The variable_name of this PoolVariablesName.  # noqa: E501
        :rtype: list[str]
        """
        return self._variable_name

    @variable_name.setter
    def variable_name(self, variable_name):
        """Sets the variable_name of this PoolVariablesName.


        :param variable_name: The variable_name of this PoolVariablesName.  # noqa: E501
        :type: list[str]
        """

        self._variable_name = variable_name

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
        if issubclass(PoolVariablesName, dict):
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
        if not isinstance(other, PoolVariablesName):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
