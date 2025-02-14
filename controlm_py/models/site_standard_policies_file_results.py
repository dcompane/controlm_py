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

class SiteStandardPoliciesFileResults(object):
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
        'site_standard_policies_file': 'str',
        'success_site_standard_policies_count': 'int',
        'is_deploy_descriptor_valid': 'bool',
        'added_site_standard_policies': 'list[str]',
        'errors': 'list[str]'
    }

    attribute_map = {
        'site_standard_policies_file': 'siteStandardPoliciesFile',
        'success_site_standard_policies_count': 'successSiteStandardPoliciesCount',
        'is_deploy_descriptor_valid': 'isDeployDescriptorValid',
        'added_site_standard_policies': 'addedSiteStandardPolicies',
        'errors': 'errors'
    }

    def __init__(self, site_standard_policies_file=None, success_site_standard_policies_count=None, is_deploy_descriptor_valid=None, added_site_standard_policies=None, errors=None):  # noqa: E501
        """SiteStandardPoliciesFileResults - a model defined in Swagger"""  # noqa: E501
        self._site_standard_policies_file = None
        self._success_site_standard_policies_count = None
        self._is_deploy_descriptor_valid = None
        self._added_site_standard_policies = None
        self._errors = None
        self.discriminator = None
        if site_standard_policies_file is not None:
            self.site_standard_policies_file = site_standard_policies_file
        if success_site_standard_policies_count is not None:
            self.success_site_standard_policies_count = success_site_standard_policies_count
        if is_deploy_descriptor_valid is not None:
            self.is_deploy_descriptor_valid = is_deploy_descriptor_valid
        if added_site_standard_policies is not None:
            self.added_site_standard_policies = added_site_standard_policies
        if errors is not None:
            self.errors = errors

    @property
    def site_standard_policies_file(self):
        """Gets the site_standard_policies_file of this SiteStandardPoliciesFileResults.  # noqa: E501

        The name of a specific site standard policies file.  # noqa: E501

        :return: The site_standard_policies_file of this SiteStandardPoliciesFileResults.  # noqa: E501
        :rtype: str
        """
        return self._site_standard_policies_file

    @site_standard_policies_file.setter
    def site_standard_policies_file(self, site_standard_policies_file):
        """Sets the site_standard_policies_file of this SiteStandardPoliciesFileResults.

        The name of a specific site standard policies file.  # noqa: E501

        :param site_standard_policies_file: The site_standard_policies_file of this SiteStandardPoliciesFileResults.  # noqa: E501
        :type: str
        """

        self._site_standard_policies_file = site_standard_policies_file

    @property
    def success_site_standard_policies_count(self):
        """Gets the success_site_standard_policies_count of this SiteStandardPoliciesFileResults.  # noqa: E501

        Determines the number of successfully added site standard policies.  # noqa: E501

        :return: The success_site_standard_policies_count of this SiteStandardPoliciesFileResults.  # noqa: E501
        :rtype: int
        """
        return self._success_site_standard_policies_count

    @success_site_standard_policies_count.setter
    def success_site_standard_policies_count(self, success_site_standard_policies_count):
        """Sets the success_site_standard_policies_count of this SiteStandardPoliciesFileResults.

        Determines the number of successfully added site standard policies.  # noqa: E501

        :param success_site_standard_policies_count: The success_site_standard_policies_count of this SiteStandardPoliciesFileResults.  # noqa: E501
        :type: int
        """

        self._success_site_standard_policies_count = success_site_standard_policies_count

    @property
    def is_deploy_descriptor_valid(self):
        """Gets the is_deploy_descriptor_valid of this SiteStandardPoliciesFileResults.  # noqa: E501

        Determines if the site standard policies file file is a valid deploy descriptor file.  # noqa: E501

        :return: The is_deploy_descriptor_valid of this SiteStandardPoliciesFileResults.  # noqa: E501
        :rtype: bool
        """
        return self._is_deploy_descriptor_valid

    @is_deploy_descriptor_valid.setter
    def is_deploy_descriptor_valid(self, is_deploy_descriptor_valid):
        """Sets the is_deploy_descriptor_valid of this SiteStandardPoliciesFileResults.

        Determines if the site standard policies file file is a valid deploy descriptor file.  # noqa: E501

        :param is_deploy_descriptor_valid: The is_deploy_descriptor_valid of this SiteStandardPoliciesFileResults.  # noqa: E501
        :type: bool
        """

        self._is_deploy_descriptor_valid = is_deploy_descriptor_valid

    @property
    def added_site_standard_policies(self):
        """Gets the added_site_standard_policies of this SiteStandardPoliciesFileResults.  # noqa: E501


        :return: The added_site_standard_policies of this SiteStandardPoliciesFileResults.  # noqa: E501
        :rtype: list[str]
        """
        return self._added_site_standard_policies

    @added_site_standard_policies.setter
    def added_site_standard_policies(self, added_site_standard_policies):
        """Sets the added_site_standard_policies of this SiteStandardPoliciesFileResults.


        :param added_site_standard_policies: The added_site_standard_policies of this SiteStandardPoliciesFileResults.  # noqa: E501
        :type: list[str]
        """

        self._added_site_standard_policies = added_site_standard_policies

    @property
    def errors(self):
        """Gets the errors of this SiteStandardPoliciesFileResults.  # noqa: E501


        :return: The errors of this SiteStandardPoliciesFileResults.  # noqa: E501
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this SiteStandardPoliciesFileResults.


        :param errors: The errors of this SiteStandardPoliciesFileResults.  # noqa: E501
        :type: list[str]
        """

        self._errors = errors

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
        if issubclass(SiteStandardPoliciesFileResults, dict):
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
        if not isinstance(other, SiteStandardPoliciesFileResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
