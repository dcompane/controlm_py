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

class OrderInfo(object):
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
        'next_order_date': 'str',
        'order_action': 'str',
        'order_date': 'str',
        'prev_order_date': 'str'
    }

    attribute_map = {
        'next_order_date': 'next_order_date',
        'order_action': 'order_action',
        'order_date': 'order_date',
        'prev_order_date': 'prev_order_date'
    }

    def __init__(self, next_order_date=None, order_action=None, order_date=None, prev_order_date=None):  # noqa: E501
        """OrderInfo - a model defined in Swagger"""  # noqa: E501
        self._next_order_date = None
        self._order_action = None
        self._order_date = None
        self._prev_order_date = None
        self.discriminator = None
        if next_order_date is not None:
            self.next_order_date = next_order_date
        if order_action is not None:
            self.order_action = order_action
        if order_date is not None:
            self.order_date = order_date
        if prev_order_date is not None:
            self.prev_order_date = prev_order_date

    @property
    def next_order_date(self):
        """Gets the next_order_date of this OrderInfo.  # noqa: E501


        :return: The next_order_date of this OrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._next_order_date

    @next_order_date.setter
    def next_order_date(self, next_order_date):
        """Sets the next_order_date of this OrderInfo.


        :param next_order_date: The next_order_date of this OrderInfo.  # noqa: E501
        :type: str
        """

        self._next_order_date = next_order_date

    @property
    def order_action(self):
        """Gets the order_action of this OrderInfo.  # noqa: E501


        :return: The order_action of this OrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._order_action

    @order_action.setter
    def order_action(self, order_action):
        """Sets the order_action of this OrderInfo.


        :param order_action: The order_action of this OrderInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["SHOULD_ORDER", "SHOULD_NOT_ORDER", "ORDER_NOT_ALLOWED", "ORDER_REFERENCED", "UNRECOGNIZED"]  # noqa: E501
        if order_action not in allowed_values:
            raise ValueError(
                "Invalid value for `order_action` ({0}), must be one of {1}"  # noqa: E501
                .format(order_action, allowed_values)
            )

        self._order_action = order_action

    @property
    def order_date(self):
        """Gets the order_date of this OrderInfo.  # noqa: E501


        :return: The order_date of this OrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._order_date

    @order_date.setter
    def order_date(self, order_date):
        """Sets the order_date of this OrderInfo.


        :param order_date: The order_date of this OrderInfo.  # noqa: E501
        :type: str
        """

        self._order_date = order_date

    @property
    def prev_order_date(self):
        """Gets the prev_order_date of this OrderInfo.  # noqa: E501


        :return: The prev_order_date of this OrderInfo.  # noqa: E501
        :rtype: str
        """
        return self._prev_order_date

    @prev_order_date.setter
    def prev_order_date(self, prev_order_date):
        """Sets the prev_order_date of this OrderInfo.


        :param prev_order_date: The prev_order_date of this OrderInfo.  # noqa: E501
        :type: str
        """

        self._prev_order_date = prev_order_date

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
        if issubclass(OrderInfo, dict):
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
        if not isinstance(other, OrderInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
