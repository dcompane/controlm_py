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

class FtsUserHomeDirectoryData(object):
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
        'user_name': 'str',
        'home_directory': 'str'
    }

    attribute_map = {
        'user_name': 'userName',
        'home_directory': 'homeDirectory'
    }

    def __init__(self, user_name=None, home_directory=None):  # noqa: E501
        """FtsUserHomeDirectoryData - a model defined in Swagger"""  # noqa: E501
        self._user_name = None
        self._home_directory = None
        self.discriminator = None
        if user_name is not None:
            self.user_name = user_name
        if home_directory is not None:
            self.home_directory = home_directory

    @property
    def user_name(self):
        """Gets the user_name of this FtsUserHomeDirectoryData.  # noqa: E501

        User name  # noqa: E501

        :return: The user_name of this FtsUserHomeDirectoryData.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this FtsUserHomeDirectoryData.

        User name  # noqa: E501

        :param user_name: The user_name of this FtsUserHomeDirectoryData.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def home_directory(self):
        """Gets the home_directory of this FtsUserHomeDirectoryData.  # noqa: E501

        Home directory  # noqa: E501

        :return: The home_directory of this FtsUserHomeDirectoryData.  # noqa: E501
        :rtype: str
        """
        return self._home_directory

    @home_directory.setter
    def home_directory(self, home_directory):
        """Sets the home_directory of this FtsUserHomeDirectoryData.

        Home directory  # noqa: E501

        :param home_directory: The home_directory of this FtsUserHomeDirectoryData.  # noqa: E501
        :type: str
        """

        self._home_directory = home_directory

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
        if issubclass(FtsUserHomeDirectoryData, dict):
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
        if not isinstance(other, FtsUserHomeDirectoryData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
