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

class OrganizationGroupName(object):
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
        'short_domain_name': 'str',
        'long_domain_name': 'str'
    }

    attribute_map = {
        'short_domain_name': 'shortDomainName',
        'long_domain_name': 'longDomainName'
    }

    def __init__(self, short_domain_name=None, long_domain_name=None):  # noqa: E501
        """OrganizationGroupName - a model defined in Swagger"""  # noqa: E501
        self._short_domain_name = None
        self._long_domain_name = None
        self.discriminator = None
        if short_domain_name is not None:
            self.short_domain_name = short_domain_name
        if long_domain_name is not None:
            self.long_domain_name = long_domain_name

    @property
    def short_domain_name(self):
        """Gets the short_domain_name of this OrganizationGroupName.  # noqa: E501

        short domain name  # noqa: E501

        :return: The short_domain_name of this OrganizationGroupName.  # noqa: E501
        :rtype: str
        """
        return self._short_domain_name

    @short_domain_name.setter
    def short_domain_name(self, short_domain_name):
        """Sets the short_domain_name of this OrganizationGroupName.

        short domain name  # noqa: E501

        :param short_domain_name: The short_domain_name of this OrganizationGroupName.  # noqa: E501
        :type: str
        """

        self._short_domain_name = short_domain_name

    @property
    def long_domain_name(self):
        """Gets the long_domain_name of this OrganizationGroupName.  # noqa: E501

        long domain name  # noqa: E501

        :return: The long_domain_name of this OrganizationGroupName.  # noqa: E501
        :rtype: str
        """
        return self._long_domain_name

    @long_domain_name.setter
    def long_domain_name(self, long_domain_name):
        """Sets the long_domain_name of this OrganizationGroupName.

        long domain name  # noqa: E501

        :param long_domain_name: The long_domain_name of this OrganizationGroupName.  # noqa: E501
        :type: str
        """

        self._long_domain_name = long_domain_name

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
        if issubclass(OrganizationGroupName, dict):
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
        if not isinstance(other, OrganizationGroupName):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
