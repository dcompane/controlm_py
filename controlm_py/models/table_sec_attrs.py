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

class TableSecAttrs(object):
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
        'ctm_sec_table_sec_attr_collection': 'list[CtmSecTableSecAttrType]'
    }

    attribute_map = {
        'ctm_sec_table_sec_attr_collection': 'CtmSecTableSecAttrCollection'
    }

    def __init__(self, ctm_sec_table_sec_attr_collection=None):  # noqa: E501
        """TableSecAttrs - a model defined in Swagger"""  # noqa: E501
        self._ctm_sec_table_sec_attr_collection = None
        self.discriminator = None
        if ctm_sec_table_sec_attr_collection is not None:
            self.ctm_sec_table_sec_attr_collection = ctm_sec_table_sec_attr_collection

    @property
    def ctm_sec_table_sec_attr_collection(self):
        """Gets the ctm_sec_table_sec_attr_collection of this TableSecAttrs.  # noqa: E501


        :return: The ctm_sec_table_sec_attr_collection of this TableSecAttrs.  # noqa: E501
        :rtype: list[CtmSecTableSecAttrType]
        """
        return self._ctm_sec_table_sec_attr_collection

    @ctm_sec_table_sec_attr_collection.setter
    def ctm_sec_table_sec_attr_collection(self, ctm_sec_table_sec_attr_collection):
        """Sets the ctm_sec_table_sec_attr_collection of this TableSecAttrs.


        :param ctm_sec_table_sec_attr_collection: The ctm_sec_table_sec_attr_collection of this TableSecAttrs.  # noqa: E501
        :type: list[CtmSecTableSecAttrType]
        """

        self._ctm_sec_table_sec_attr_collection = ctm_sec_table_sec_attr_collection

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
        if issubclass(TableSecAttrs, dict):
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
        if not isinstance(other, TableSecAttrs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
