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

class AppList(object):
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
        'app_names': 'list[App]',
        'deployed_names': 'list[AppDeployed]'
    }

    attribute_map = {
        'app_names': 'appNames',
        'deployed_names': 'deployedNames'
    }

    def __init__(self, app_names=None, deployed_names=None):  # noqa: E501
        """AppList - a model defined in Swagger"""  # noqa: E501
        self._app_names = None
        self._deployed_names = None
        self.discriminator = None
        if app_names is not None:
            self.app_names = app_names
        if deployed_names is not None:
            self.deployed_names = deployed_names

    @property
    def app_names(self):
        """Gets the app_names of this AppList.  # noqa: E501


        :return: The app_names of this AppList.  # noqa: E501
        :rtype: list[App]
        """
        return self._app_names

    @app_names.setter
    def app_names(self, app_names):
        """Sets the app_names of this AppList.


        :param app_names: The app_names of this AppList.  # noqa: E501
        :type: list[App]
        """

        self._app_names = app_names

    @property
    def deployed_names(self):
        """Gets the deployed_names of this AppList.  # noqa: E501


        :return: The deployed_names of this AppList.  # noqa: E501
        :rtype: list[AppDeployed]
        """
        return self._deployed_names

    @deployed_names.setter
    def deployed_names(self, deployed_names):
        """Sets the deployed_names of this AppList.


        :param deployed_names: The deployed_names of this AppList.  # noqa: E501
        :type: list[AppDeployed]
        """

        self._deployed_names = deployed_names

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
        if issubclass(AppList, dict):
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
        if not isinstance(other, AppList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
