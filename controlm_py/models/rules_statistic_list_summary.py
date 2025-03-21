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

class RulesStatisticListSummary(object):
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
        'rules_statistic_list': 'RulesStatisticList',
        'summary': 'Summary'
    }

    attribute_map = {
        'rules_statistic_list': 'rulesStatisticList',
        'summary': 'summary'
    }

    def __init__(self, rules_statistic_list=None, summary=None):  # noqa: E501
        """RulesStatisticListSummary - a model defined in Swagger"""  # noqa: E501
        self._rules_statistic_list = None
        self._summary = None
        self.discriminator = None
        if rules_statistic_list is not None:
            self.rules_statistic_list = rules_statistic_list
        if summary is not None:
            self.summary = summary

    @property
    def rules_statistic_list(self):
        """Gets the rules_statistic_list of this RulesStatisticListSummary.  # noqa: E501


        :return: The rules_statistic_list of this RulesStatisticListSummary.  # noqa: E501
        :rtype: RulesStatisticList
        """
        return self._rules_statistic_list

    @rules_statistic_list.setter
    def rules_statistic_list(self, rules_statistic_list):
        """Sets the rules_statistic_list of this RulesStatisticListSummary.


        :param rules_statistic_list: The rules_statistic_list of this RulesStatisticListSummary.  # noqa: E501
        :type: RulesStatisticList
        """

        self._rules_statistic_list = rules_statistic_list

    @property
    def summary(self):
        """Gets the summary of this RulesStatisticListSummary.  # noqa: E501


        :return: The summary of this RulesStatisticListSummary.  # noqa: E501
        :rtype: Summary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this RulesStatisticListSummary.


        :param summary: The summary of this RulesStatisticListSummary.  # noqa: E501
        :type: Summary
        """

        self._summary = summary

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
        if issubclass(RulesStatisticListSummary, dict):
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
        if not isinstance(other, RulesStatisticListSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
