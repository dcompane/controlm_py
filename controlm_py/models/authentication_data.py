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

class AuthenticationData(object):
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
        'control_m': 'ControlMAuthenticationData',
        'external_provider': 'ExternalProviderAuthenticationData'
    }

    attribute_map = {
        'control_m': 'ControlM',
        'external_provider': 'ExternalProvider'
    }

    def __init__(self, control_m=None, external_provider=None):  # noqa: E501
        """AuthenticationData - a model defined in Swagger"""  # noqa: E501
        self._control_m = None
        self._external_provider = None
        self.discriminator = None
        if control_m is not None:
            self.control_m = control_m
        if external_provider is not None:
            self.external_provider = external_provider

    @property
    def control_m(self):
        """Gets the control_m of this AuthenticationData.  # noqa: E501


        :return: The control_m of this AuthenticationData.  # noqa: E501
        :rtype: ControlMAuthenticationData
        """
        return self._control_m

    @control_m.setter
    def control_m(self, control_m):
        """Sets the control_m of this AuthenticationData.


        :param control_m: The control_m of this AuthenticationData.  # noqa: E501
        :type: ControlMAuthenticationData
        """

        self._control_m = control_m

    @property
    def external_provider(self):
        """Gets the external_provider of this AuthenticationData.  # noqa: E501


        :return: The external_provider of this AuthenticationData.  # noqa: E501
        :rtype: ExternalProviderAuthenticationData
        """
        return self._external_provider

    @external_provider.setter
    def external_provider(self, external_provider):
        """Sets the external_provider of this AuthenticationData.


        :param external_provider: The external_provider of this AuthenticationData.  # noqa: E501
        :type: ExternalProviderAuthenticationData
        """

        self._external_provider = external_provider

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
        if issubclass(AuthenticationData, dict):
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
        if not isinstance(other, AuthenticationData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
