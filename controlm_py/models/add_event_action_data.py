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

class AddEventActionData(object):
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
        'action_fails_behaviour': 'ActionFailsBehaviourData',
        'event_name': 'str',
        'event_date': 'str'
    }

    attribute_map = {
        'action_fails_behaviour': 'actionFailsBehaviour',
        'event_name': 'eventName',
        'event_date': 'eventDate'
    }

    def __init__(self, action_fails_behaviour=None, event_name=None, event_date=None):  # noqa: E501
        """AddEventActionData - a model defined in Swagger"""  # noqa: E501
        self._action_fails_behaviour = None
        self._event_name = None
        self._event_date = None
        self.discriminator = None
        if action_fails_behaviour is not None:
            self.action_fails_behaviour = action_fails_behaviour
        if event_name is not None:
            self.event_name = event_name
        if event_date is not None:
            self.event_date = event_date

    @property
    def action_fails_behaviour(self):
        """Gets the action_fails_behaviour of this AddEventActionData.  # noqa: E501


        :return: The action_fails_behaviour of this AddEventActionData.  # noqa: E501
        :rtype: ActionFailsBehaviourData
        """
        return self._action_fails_behaviour

    @action_fails_behaviour.setter
    def action_fails_behaviour(self, action_fails_behaviour):
        """Sets the action_fails_behaviour of this AddEventActionData.


        :param action_fails_behaviour: The action_fails_behaviour of this AddEventActionData.  # noqa: E501
        :type: ActionFailsBehaviourData
        """

        self._action_fails_behaviour = action_fails_behaviour

    @property
    def event_name(self):
        """Gets the event_name of this AddEventActionData.  # noqa: E501

        event name  # noqa: E501

        :return: The event_name of this AddEventActionData.  # noqa: E501
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this AddEventActionData.

        event name  # noqa: E501

        :param event_name: The event_name of this AddEventActionData.  # noqa: E501
        :type: str
        """

        self._event_name = event_name

    @property
    def event_date(self):
        """Gets the event_date of this AddEventActionData.  # noqa: E501

        event Date  # noqa: E501

        :return: The event_date of this AddEventActionData.  # noqa: E501
        :rtype: str
        """
        return self._event_date

    @event_date.setter
    def event_date(self, event_date):
        """Sets the event_date of this AddEventActionData.

        event Date  # noqa: E501

        :param event_date: The event_date of this AddEventActionData.  # noqa: E501
        :type: str
        """

        self._event_date = event_date

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
        if issubclass(AddEventActionData, dict):
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
        if not isinstance(other, AddEventActionData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other