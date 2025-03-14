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

class ParticipationTime(object):
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
        'all_hours': 'bool',
        'between_time': 'BetweenTime'
    }

    attribute_map = {
        'all_hours': 'allHours',
        'between_time': 'betweenTime'
    }

    def __init__(self, all_hours=None, between_time=None):  # noqa: E501
        """ParticipationTime - a model defined in Swagger"""  # noqa: E501
        self._all_hours = None
        self._between_time = None
        self.discriminator = None
        if all_hours is not None:
            self.all_hours = all_hours
        if between_time is not None:
            self.between_time = between_time

    @property
    def all_hours(self):
        """Gets the all_hours of this ParticipationTime.  # noqa: E501

        all hours.  # noqa: E501

        :return: The all_hours of this ParticipationTime.  # noqa: E501
        :rtype: bool
        """
        return self._all_hours

    @all_hours.setter
    def all_hours(self, all_hours):
        """Sets the all_hours of this ParticipationTime.

        all hours.  # noqa: E501

        :param all_hours: The all_hours of this ParticipationTime.  # noqa: E501
        :type: bool
        """

        self._all_hours = all_hours

    @property
    def between_time(self):
        """Gets the between_time of this ParticipationTime.  # noqa: E501


        :return: The between_time of this ParticipationTime.  # noqa: E501
        :rtype: BetweenTime
        """
        return self._between_time

    @between_time.setter
    def between_time(self, between_time):
        """Sets the between_time of this ParticipationTime.


        :param between_time: The between_time of this ParticipationTime.  # noqa: E501
        :type: BetweenTime
        """

        self._between_time = between_time

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
        if issubclass(ParticipationTime, dict):
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
        if not isinstance(other, ParticipationTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
