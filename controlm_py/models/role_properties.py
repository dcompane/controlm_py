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

class RoleProperties(object):
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
        'new_role_name': 'str'
    }

    attribute_map = {
        'new_role_name': 'newRoleName'
    }

    def __init__(self, new_role_name=None):  # noqa: E501
        """RoleProperties - a model defined in Swagger"""  # noqa: E501
        self._new_role_name = None
        self.discriminator = None
        if new_role_name is not None:
            self.new_role_name = new_role_name

    @property
    def new_role_name(self):
        """Gets the new_role_name of this RoleProperties.  # noqa: E501

        A new authorization role name REQUIRED  # noqa: E501

        :return: The new_role_name of this RoleProperties.  # noqa: E501
        :rtype: str
        """
        return self._new_role_name

    @new_role_name.setter
    def new_role_name(self, new_role_name):
        """Sets the new_role_name of this RoleProperties.

        A new authorization role name REQUIRED  # noqa: E501

        :param new_role_name: The new_role_name of this RoleProperties.  # noqa: E501
        :type: str
        """

        self._new_role_name = new_role_name

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
        if issubclass(RoleProperties, dict):
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
        if not isinstance(other, RoleProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
