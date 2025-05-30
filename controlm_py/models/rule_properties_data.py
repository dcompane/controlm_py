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

class RulePropertiesData(object):
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
        'name': 'str',
        'description': 'str',
        'priority': 'int',
        'last_updated_timestamp': 'int',
        'status': 'str',
        'rule_type': 'str',
        'conditions': 'RuleConditions',
        'post_actions': 'list[RuleActionData]',
        'pre_actions': 'list[RuleActionData]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'priority': 'priority',
        'last_updated_timestamp': 'lastUpdatedTimestamp',
        'status': 'status',
        'rule_type': 'ruleType',
        'conditions': 'conditions',
        'post_actions': 'postActions',
        'pre_actions': 'preActions'
    }

    def __init__(self, name=None, description=None, priority=None, last_updated_timestamp=None, status=None, rule_type=None, conditions=None, post_actions=None, pre_actions=None):  # noqa: E501
        """RulePropertiesData - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._priority = None
        self._last_updated_timestamp = None
        self._status = None
        self._rule_type = None
        self._conditions = None
        self._post_actions = None
        self._pre_actions = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if priority is not None:
            self.priority = priority
        if last_updated_timestamp is not None:
            self.last_updated_timestamp = last_updated_timestamp
        if status is not None:
            self.status = status
        if rule_type is not None:
            self.rule_type = rule_type
        if conditions is not None:
            self.conditions = conditions
        if post_actions is not None:
            self.post_actions = post_actions
        if pre_actions is not None:
            self.pre_actions = pre_actions

    @property
    def name(self):
        """Gets the name of this RulePropertiesData.  # noqa: E501

        The name of the rule. HIDDEN  # noqa: E501

        :return: The name of this RulePropertiesData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RulePropertiesData.

        The name of the rule. HIDDEN  # noqa: E501

        :param name: The name of this RulePropertiesData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this RulePropertiesData.  # noqa: E501

        Rule description. HIDDEN  # noqa: E501

        :return: The description of this RulePropertiesData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RulePropertiesData.

        Rule description. HIDDEN  # noqa: E501

        :param description: The description of this RulePropertiesData.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def priority(self):
        """Gets the priority of this RulePropertiesData.  # noqa: E501

        Rule priority. HIDDEN  # noqa: E501

        :return: The priority of this RulePropertiesData.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this RulePropertiesData.

        Rule priority. HIDDEN  # noqa: E501

        :param priority: The priority of this RulePropertiesData.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def last_updated_timestamp(self):
        """Gets the last_updated_timestamp of this RulePropertiesData.  # noqa: E501

        Last Updated Timestamp. HIDDEN  # noqa: E501

        :return: The last_updated_timestamp of this RulePropertiesData.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_timestamp

    @last_updated_timestamp.setter
    def last_updated_timestamp(self, last_updated_timestamp):
        """Sets the last_updated_timestamp of this RulePropertiesData.

        Last Updated Timestamp. HIDDEN  # noqa: E501

        :param last_updated_timestamp: The last_updated_timestamp of this RulePropertiesData.  # noqa: E501
        :type: int
        """

        self._last_updated_timestamp = last_updated_timestamp

    @property
    def status(self):
        """Gets the status of this RulePropertiesData.  # noqa: E501

        Rule status. HIDDEN  # noqa: E501

        :return: The status of this RulePropertiesData.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RulePropertiesData.

        Rule status. HIDDEN  # noqa: E501

        :param status: The status of this RulePropertiesData.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def rule_type(self):
        """Gets the rule_type of this RulePropertiesData.  # noqa: E501

        Rule type. HIDDEN  # noqa: E501

        :return: The rule_type of this RulePropertiesData.  # noqa: E501
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """Sets the rule_type of this RulePropertiesData.

        Rule type. HIDDEN  # noqa: E501

        :param rule_type: The rule_type of this RulePropertiesData.  # noqa: E501
        :type: str
        """

        self._rule_type = rule_type

    @property
    def conditions(self):
        """Gets the conditions of this RulePropertiesData.  # noqa: E501


        :return: The conditions of this RulePropertiesData.  # noqa: E501
        :rtype: RuleConditions
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this RulePropertiesData.


        :param conditions: The conditions of this RulePropertiesData.  # noqa: E501
        :type: RuleConditions
        """

        self._conditions = conditions

    @property
    def post_actions(self):
        """Gets the post_actions of this RulePropertiesData.  # noqa: E501

        Rules post actions. HIDDEN  # noqa: E501

        :return: The post_actions of this RulePropertiesData.  # noqa: E501
        :rtype: list[RuleActionData]
        """
        return self._post_actions

    @post_actions.setter
    def post_actions(self, post_actions):
        """Sets the post_actions of this RulePropertiesData.

        Rules post actions. HIDDEN  # noqa: E501

        :param post_actions: The post_actions of this RulePropertiesData.  # noqa: E501
        :type: list[RuleActionData]
        """

        self._post_actions = post_actions

    @property
    def pre_actions(self):
        """Gets the pre_actions of this RulePropertiesData.  # noqa: E501

        Rules pre actions. HIDDEN  # noqa: E501

        :return: The pre_actions of this RulePropertiesData.  # noqa: E501
        :rtype: list[RuleActionData]
        """
        return self._pre_actions

    @pre_actions.setter
    def pre_actions(self, pre_actions):
        """Sets the pre_actions of this RulePropertiesData.

        Rules pre actions. HIDDEN  # noqa: E501

        :param pre_actions: The pre_actions of this RulePropertiesData.  # noqa: E501
        :type: list[RuleActionData]
        """

        self._pre_actions = pre_actions

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
        if issubclass(RulePropertiesData, dict):
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
        if not isinstance(other, RulePropertiesData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
