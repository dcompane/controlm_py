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

class DeploySitestandardpoliciesBody(object):
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
        'site_standard_policies_file': 'str'
    }

    attribute_map = {
        'site_standard_policies_file': 'siteStandardPoliciesFile'
    }

    def __init__(self, site_standard_policies_file=None):  # noqa: E501
        """DeploySitestandardpoliciesBody - a model defined in Swagger"""  # noqa: E501
        self._site_standard_policies_file = None
        self.discriminator = None
        self.site_standard_policies_file = site_standard_policies_file

    @property
    def site_standard_policies_file(self):
        """Gets the site_standard_policies_file of this DeploySitestandardpoliciesBody.  # noqa: E501

        A file that contains definitions of Site Standard Policies  # noqa: E501

        :return: The site_standard_policies_file of this DeploySitestandardpoliciesBody.  # noqa: E501
        :rtype: str
        """
        return self._site_standard_policies_file

    @site_standard_policies_file.setter
    def site_standard_policies_file(self, site_standard_policies_file):
        """Sets the site_standard_policies_file of this DeploySitestandardpoliciesBody.

        A file that contains definitions of Site Standard Policies  # noqa: E501

        :param site_standard_policies_file: The site_standard_policies_file of this DeploySitestandardpoliciesBody.  # noqa: E501
        :type: str
        """
        if site_standard_policies_file is None:
            raise ValueError("Invalid value for `site_standard_policies_file`, must not be `None`")  # noqa: E501

        self._site_standard_policies_file = site_standard_policies_file

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
        if issubclass(DeploySitestandardpoliciesBody, dict):
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
        if not isinstance(other, DeploySitestandardpoliciesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other