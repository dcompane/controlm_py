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

class ShoutDestinationAddressList(object):
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
        'address_type': 'str',
        'is_value_list': 'str',
        'uses_value_of_address': 'str',
        'shout_destinations': 'list[SupportedShoutDestinations]'
    }

    attribute_map = {
        'address_type': 'addressType',
        'is_value_list': 'isValueList',
        'uses_value_of_address': 'usesValueOfAddress',
        'shout_destinations': 'shoutDestinations'
    }

    def __init__(self, address_type=None, is_value_list=None, uses_value_of_address=None, shout_destinations=None):  # noqa: E501
        """ShoutDestinationAddressList - a model defined in Swagger"""  # noqa: E501
        self._address_type = None
        self._is_value_list = None
        self._uses_value_of_address = None
        self._shout_destinations = None
        self.discriminator = None
        if address_type is not None:
            self.address_type = address_type
        if is_value_list is not None:
            self.is_value_list = is_value_list
        if uses_value_of_address is not None:
            self.uses_value_of_address = uses_value_of_address
        if shout_destinations is not None:
            self.shout_destinations = shout_destinations

    @property
    def address_type(self):
        """Gets the address_type of this ShoutDestinationAddressList.  # noqa: E501

        Supported Shout Destination Addresses type  # noqa: E501

        :return: The address_type of this ShoutDestinationAddressList.  # noqa: E501
        :rtype: str
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this ShoutDestinationAddressList.

        Supported Shout Destination Addresses type  # noqa: E501

        :param address_type: The address_type of this ShoutDestinationAddressList.  # noqa: E501
        :type: str
        """

        self._address_type = address_type

    @property
    def is_value_list(self):
        """Gets the is_value_list of this ShoutDestinationAddressList.  # noqa: E501

        Supported Shout Destination Addresses is value list  # noqa: E501

        :return: The is_value_list of this ShoutDestinationAddressList.  # noqa: E501
        :rtype: str
        """
        return self._is_value_list

    @is_value_list.setter
    def is_value_list(self, is_value_list):
        """Sets the is_value_list of this ShoutDestinationAddressList.

        Supported Shout Destination Addresses is value list  # noqa: E501

        :param is_value_list: The is_value_list of this ShoutDestinationAddressList.  # noqa: E501
        :type: str
        """

        self._is_value_list = is_value_list

    @property
    def uses_value_of_address(self):
        """Gets the uses_value_of_address of this ShoutDestinationAddressList.  # noqa: E501

        Supported Shout Destination Addresses uses value of address  # noqa: E501

        :return: The uses_value_of_address of this ShoutDestinationAddressList.  # noqa: E501
        :rtype: str
        """
        return self._uses_value_of_address

    @uses_value_of_address.setter
    def uses_value_of_address(self, uses_value_of_address):
        """Sets the uses_value_of_address of this ShoutDestinationAddressList.

        Supported Shout Destination Addresses uses value of address  # noqa: E501

        :param uses_value_of_address: The uses_value_of_address of this ShoutDestinationAddressList.  # noqa: E501
        :type: str
        """

        self._uses_value_of_address = uses_value_of_address

    @property
    def shout_destinations(self):
        """Gets the shout_destinations of this ShoutDestinationAddressList.  # noqa: E501

        Supported Shout Destination Addresses validations  # noqa: E501

        :return: The shout_destinations of this ShoutDestinationAddressList.  # noqa: E501
        :rtype: list[SupportedShoutDestinations]
        """
        return self._shout_destinations

    @shout_destinations.setter
    def shout_destinations(self, shout_destinations):
        """Sets the shout_destinations of this ShoutDestinationAddressList.

        Supported Shout Destination Addresses validations  # noqa: E501

        :param shout_destinations: The shout_destinations of this ShoutDestinationAddressList.  # noqa: E501
        :type: list[SupportedShoutDestinations]
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
        if issubclass(ShoutDestinationAddressList, dict):
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
        if not isinstance(other, ShoutDestinationAddressList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other