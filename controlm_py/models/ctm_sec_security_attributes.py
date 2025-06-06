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

class CtmSecSecurityAttributes(object):
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
        'table_sec_attrs': 'TableSecAttrs',
        'active_sec_attrs': 'ActiveSecAttrs',
        'entity_sec_attrs': 'CtmSecEntitySecAttrsType'
    }

    attribute_map = {
        'table_sec_attrs': 'TableSecAttrs',
        'active_sec_attrs': 'ActiveSecAttrs',
        'entity_sec_attrs': 'EntitySecAttrs'
    }

    def __init__(self, table_sec_attrs=None, active_sec_attrs=None, entity_sec_attrs=None):  # noqa: E501
        """CtmSecSecurityAttributes - a model defined in Swagger"""  # noqa: E501
        self._table_sec_attrs = None
        self._active_sec_attrs = None
        self._entity_sec_attrs = None
        self.discriminator = None
        if table_sec_attrs is not None:
            self.table_sec_attrs = table_sec_attrs
        if active_sec_attrs is not None:
            self.active_sec_attrs = active_sec_attrs
        if entity_sec_attrs is not None:
            self.entity_sec_attrs = entity_sec_attrs

    @property
    def table_sec_attrs(self):
        """Gets the table_sec_attrs of this CtmSecSecurityAttributes.  # noqa: E501


        :return: The table_sec_attrs of this CtmSecSecurityAttributes.  # noqa: E501
        :rtype: TableSecAttrs
        """
        return self._table_sec_attrs

    @table_sec_attrs.setter
    def table_sec_attrs(self, table_sec_attrs):
        """Sets the table_sec_attrs of this CtmSecSecurityAttributes.


        :param table_sec_attrs: The table_sec_attrs of this CtmSecSecurityAttributes.  # noqa: E501
        :type: TableSecAttrs
        """

        self._table_sec_attrs = table_sec_attrs

    @property
    def active_sec_attrs(self):
        """Gets the active_sec_attrs of this CtmSecSecurityAttributes.  # noqa: E501


        :return: The active_sec_attrs of this CtmSecSecurityAttributes.  # noqa: E501
        :rtype: ActiveSecAttrs
        """
        return self._active_sec_attrs

    @active_sec_attrs.setter
    def active_sec_attrs(self, active_sec_attrs):
        """Sets the active_sec_attrs of this CtmSecSecurityAttributes.


        :param active_sec_attrs: The active_sec_attrs of this CtmSecSecurityAttributes.  # noqa: E501
        :type: ActiveSecAttrs
        """

        self._active_sec_attrs = active_sec_attrs

    @property
    def entity_sec_attrs(self):
        """Gets the entity_sec_attrs of this CtmSecSecurityAttributes.  # noqa: E501


        :return: The entity_sec_attrs of this CtmSecSecurityAttributes.  # noqa: E501
        :rtype: CtmSecEntitySecAttrsType
        """
        return self._entity_sec_attrs

    @entity_sec_attrs.setter
    def entity_sec_attrs(self, entity_sec_attrs):
        """Sets the entity_sec_attrs of this CtmSecSecurityAttributes.


        :param entity_sec_attrs: The entity_sec_attrs of this CtmSecSecurityAttributes.  # noqa: E501
        :type: CtmSecEntitySecAttrsType
        """

        self._entity_sec_attrs = entity_sec_attrs

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
        if issubclass(CtmSecSecurityAttributes, dict):
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
        if not isinstance(other, CtmSecSecurityAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
