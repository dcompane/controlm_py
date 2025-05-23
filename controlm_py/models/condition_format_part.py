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

class ConditionFormatPart(object):
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
        'part_type': 'str',
        'text': 'str',
        'field_name': 'str'
    }

    attribute_map = {
        'part_type': 'partType',
        'text': 'text',
        'field_name': 'fieldName'
    }

    def __init__(self, part_type=None, text=None, field_name=None):  # noqa: E501
        """ConditionFormatPart - a model defined in Swagger"""  # noqa: E501
        self._part_type = None
        self._text = None
        self._field_name = None
        self.discriminator = None
        self.part_type = part_type
        if text is not None:
            self.text = text
        if field_name is not None:
            self.field_name = field_name

    @property
    def part_type(self):
        """Gets the part_type of this ConditionFormatPart.  # noqa: E501


        :return: The part_type of this ConditionFormatPart.  # noqa: E501
        :rtype: str
        """
        return self._part_type

    @part_type.setter
    def part_type(self, part_type):
        """Sets the part_type of this ConditionFormatPart.


        :param part_type: The part_type of this ConditionFormatPart.  # noqa: E501
        :type: str
        """
        if part_type is None:
            raise ValueError("Invalid value for `part_type`, must not be `None`")  # noqa: E501
        allowed_values = ["SourceField", "TargetField", "FixedText"]  # noqa: E501
        if part_type not in allowed_values:
            raise ValueError(
                "Invalid value for `part_type` ({0}), must be one of {1}"  # noqa: E501
                .format(part_type, allowed_values)
            )

        self._part_type = part_type

    @property
    def text(self):
        """Gets the text of this ConditionFormatPart.  # noqa: E501

        Text to be used in condition format. To be used in FIXED_TEXT parts  # noqa: E501

        :return: The text of this ConditionFormatPart.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ConditionFormatPart.

        Text to be used in condition format. To be used in FIXED_TEXT parts  # noqa: E501

        :param text: The text of this ConditionFormatPart.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def field_name(self):
        """Gets the field_name of this ConditionFormatPart.  # noqa: E501

        The name of the field used in the part. To be used in SourceField and TargetField parts  # noqa: E501

        :return: The field_name of this ConditionFormatPart.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this ConditionFormatPart.

        The name of the field used in the part. To be used in SourceField and TargetField parts  # noqa: E501

        :param field_name: The field_name of this ConditionFormatPart.  # noqa: E501
        :type: str
        """
        allowed_values = ["JobName", "MemName", "Application", "SubApplication", "NodeId", "Owner", "ParentFolder"]  # noqa: E501
        if field_name not in allowed_values:
            raise ValueError(
                "Invalid value for `field_name` ({0}), must be one of {1}"  # noqa: E501
                .format(field_name, allowed_values)
            )

        self._field_name = field_name

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
        if issubclass(ConditionFormatPart, dict):
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
        if not isinstance(other, ConditionFormatPart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
