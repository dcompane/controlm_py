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

class PoolVariablesErrorInfo(object):
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
        'ctmvar_error_info': 'list[CtmvarErrorInfo]',
        'pool_name': 'str'
    }

    attribute_map = {
        'ctmvar_error_info': 'ctmvar_error_info',
        'pool_name': 'pool_name'
    }

    def __init__(self, ctmvar_error_info=None, pool_name=None):  # noqa: E501
        """PoolVariablesErrorInfo - a model defined in Swagger"""  # noqa: E501
        self._ctmvar_error_info = None
        self._pool_name = None
        self.discriminator = None
        if ctmvar_error_info is not None:
            self.ctmvar_error_info = ctmvar_error_info
        if pool_name is not None:
            self.pool_name = pool_name

    @property
    def ctmvar_error_info(self):
        """Gets the ctmvar_error_info of this PoolVariablesErrorInfo.  # noqa: E501


        :return: The ctmvar_error_info of this PoolVariablesErrorInfo.  # noqa: E501
        :rtype: list[CtmvarErrorInfo]
        """
        return self._ctmvar_error_info

    @ctmvar_error_info.setter
    def ctmvar_error_info(self, ctmvar_error_info):
        """Sets the ctmvar_error_info of this PoolVariablesErrorInfo.


        :param ctmvar_error_info: The ctmvar_error_info of this PoolVariablesErrorInfo.  # noqa: E501
        :type: list[CtmvarErrorInfo]
        """

        self._ctmvar_error_info = ctmvar_error_info

    @property
    def pool_name(self):
        """Gets the pool_name of this PoolVariablesErrorInfo.  # noqa: E501


        :return: The pool_name of this PoolVariablesErrorInfo.  # noqa: E501
        :rtype: str
        """
        return self._pool_name

    @pool_name.setter
    def pool_name(self, pool_name):
        """Sets the pool_name of this PoolVariablesErrorInfo.


        :param pool_name: The pool_name of this PoolVariablesErrorInfo.  # noqa: E501
        :type: str
        """

        self._pool_name = pool_name

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
        if issubclass(PoolVariablesErrorInfo, dict):
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
        if not isinstance(other, PoolVariablesErrorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
