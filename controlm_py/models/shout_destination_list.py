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

class ShoutDestinationList(object):
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
        'shout_destinations': 'list[ShoutDestination]'
    }

    attribute_map = {
        'name': 'name',
        'shout_destinations': 'shoutDestinations'
    }

    def __init__(self, name=None, shout_destinations=None):  # noqa: E501
        """ShoutDestinationList - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._shout_destinations = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if shout_destinations is not None:
            self.shout_destinations = shout_destinations

    @property
    def name(self):
        """Gets the name of this ShoutDestinationList.  # noqa: E501

        Shout Destination List name  # noqa: E501

        :return: The name of this ShoutDestinationList.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShoutDestinationList.

        Shout Destination List name  # noqa: E501

        :param name: The name of this ShoutDestinationList.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def shout_destinations(self):
        """Gets the shout_destinations of this ShoutDestinationList.  # noqa: E501

        Shout Destinations  # noqa: E501

        :return: The shout_destinations of this ShoutDestinationList.  # noqa: E501
        :rtype: list[ShoutDestination]
        """
        return self._shout_destinations

    @shout_destinations.setter
    def shout_destinations(self, shout_destinations):
        """Sets the shout_destinations of this ShoutDestinationList.

        Shout Destinations  # noqa: E501

        :param shout_destinations: The shout_destinations of this ShoutDestinationList.  # noqa: E501
        :type: list[ShoutDestination]
        """

        self._shout_destinations = shout_destinations

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
        if issubclass(ShoutDestinationList, dict):
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
        if not isinstance(other, ShoutDestinationList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
