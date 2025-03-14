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

class CtmServerRenameWarning(object):
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
        'title': 'str',
        'item': 'list[str]'
    }

    attribute_map = {
        'title': 'title',
        'item': 'item'
    }

    def __init__(self, title=None, item=None):  # noqa: E501
        """CtmServerRenameWarning - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._item = None
        self.discriminator = None
        if title is not None:
            self.title = title
        if item is not None:
            self.item = item

    @property
    def title(self):
        """Gets the title of this CtmServerRenameWarning.  # noqa: E501

        Subject title  # noqa: E501

        :return: The title of this CtmServerRenameWarning.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CtmServerRenameWarning.

        Subject title  # noqa: E501

        :param title: The title of this CtmServerRenameWarning.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def item(self):
        """Gets the item of this CtmServerRenameWarning.  # noqa: E501

        Subject description  # noqa: E501

        :return: The item of this CtmServerRenameWarning.  # noqa: E501
        :rtype: list[str]
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this CtmServerRenameWarning.

        Subject description  # noqa: E501

        :param item: The item of this CtmServerRenameWarning.  # noqa: E501
        :type: list[str]
        """

        self._item = item

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
        if issubclass(CtmServerRenameWarning, dict):
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
        if not isinstance(other, CtmServerRenameWarning):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
