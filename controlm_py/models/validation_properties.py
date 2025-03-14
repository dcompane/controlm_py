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

class ValidationProperties(object):
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
        'max': 'int',
        'min': 'int',
        'regex_pattern': 'str',
        'regex_pattern_java': 'str',
        'regex_pattern_java_script': 'str',
        'regex_pattern_no_match_message': 'str',
        'regex_pattern_no_match_message_id': 'str',
        'required': 'bool',
        'required_if': 'ConditionProperties'
    }

    attribute_map = {
        'max': 'max',
        'min': 'min',
        'regex_pattern': 'regexPattern',
        'regex_pattern_java': 'regexPatternJava',
        'regex_pattern_java_script': 'regexPatternJavaScript',
        'regex_pattern_no_match_message': 'regexPatternNoMatchMessage',
        'regex_pattern_no_match_message_id': 'regexPatternNoMatchMessageID',
        'required': 'required',
        'required_if': 'requiredIf'
    }

    def __init__(self, max=None, min=None, regex_pattern=None, regex_pattern_java=None, regex_pattern_java_script=None, regex_pattern_no_match_message=None, regex_pattern_no_match_message_id=None, required=None, required_if=None):  # noqa: E501
        """ValidationProperties - a model defined in Swagger"""  # noqa: E501
        self._max = None
        self._min = None
        self._regex_pattern = None
        self._regex_pattern_java = None
        self._regex_pattern_java_script = None
        self._regex_pattern_no_match_message = None
        self._regex_pattern_no_match_message_id = None
        self._required = None
        self._required_if = None
        self.discriminator = None
        if max is not None:
            self.max = max
        if min is not None:
            self.min = min
        if regex_pattern is not None:
            self.regex_pattern = regex_pattern
        if regex_pattern_java is not None:
            self.regex_pattern_java = regex_pattern_java
        if regex_pattern_java_script is not None:
            self.regex_pattern_java_script = regex_pattern_java_script
        if regex_pattern_no_match_message is not None:
            self.regex_pattern_no_match_message = regex_pattern_no_match_message
        if regex_pattern_no_match_message_id is not None:
            self.regex_pattern_no_match_message_id = regex_pattern_no_match_message_id
        if required is not None:
            self.required = required
        if required_if is not None:
            self.required_if = required_if

    @property
    def max(self):
        """Gets the max of this ValidationProperties.  # noqa: E501


        :return: The max of this ValidationProperties.  # noqa: E501
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this ValidationProperties.


        :param max: The max of this ValidationProperties.  # noqa: E501
        :type: int
        """

        self._max = max

    @property
    def min(self):
        """Gets the min of this ValidationProperties.  # noqa: E501


        :return: The min of this ValidationProperties.  # noqa: E501
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this ValidationProperties.


        :param min: The min of this ValidationProperties.  # noqa: E501
        :type: int
        """

        self._min = min

    @property
    def regex_pattern(self):
        """Gets the regex_pattern of this ValidationProperties.  # noqa: E501


        :return: The regex_pattern of this ValidationProperties.  # noqa: E501
        :rtype: str
        """
        return self._regex_pattern

    @regex_pattern.setter
    def regex_pattern(self, regex_pattern):
        """Sets the regex_pattern of this ValidationProperties.


        :param regex_pattern: The regex_pattern of this ValidationProperties.  # noqa: E501
        :type: str
        """

        self._regex_pattern = regex_pattern

    @property
    def regex_pattern_java(self):
        """Gets the regex_pattern_java of this ValidationProperties.  # noqa: E501


        :return: The regex_pattern_java of this ValidationProperties.  # noqa: E501
        :rtype: str
        """
        return self._regex_pattern_java

    @regex_pattern_java.setter
    def regex_pattern_java(self, regex_pattern_java):
        """Sets the regex_pattern_java of this ValidationProperties.


        :param regex_pattern_java: The regex_pattern_java of this ValidationProperties.  # noqa: E501
        :type: str
        """

        self._regex_pattern_java = regex_pattern_java

    @property
    def regex_pattern_java_script(self):
        """Gets the regex_pattern_java_script of this ValidationProperties.  # noqa: E501


        :return: The regex_pattern_java_script of this ValidationProperties.  # noqa: E501
        :rtype: str
        """
        return self._regex_pattern_java_script

    @regex_pattern_java_script.setter
    def regex_pattern_java_script(self, regex_pattern_java_script):
        """Sets the regex_pattern_java_script of this ValidationProperties.


        :param regex_pattern_java_script: The regex_pattern_java_script of this ValidationProperties.  # noqa: E501
        :type: str
        """

        self._regex_pattern_java_script = regex_pattern_java_script

    @property
    def regex_pattern_no_match_message(self):
        """Gets the regex_pattern_no_match_message of this ValidationProperties.  # noqa: E501


        :return: The regex_pattern_no_match_message of this ValidationProperties.  # noqa: E501
        :rtype: str
        """
        return self._regex_pattern_no_match_message

    @regex_pattern_no_match_message.setter
    def regex_pattern_no_match_message(self, regex_pattern_no_match_message):
        """Sets the regex_pattern_no_match_message of this ValidationProperties.


        :param regex_pattern_no_match_message: The regex_pattern_no_match_message of this ValidationProperties.  # noqa: E501
        :type: str
        """

        self._regex_pattern_no_match_message = regex_pattern_no_match_message

    @property
    def regex_pattern_no_match_message_id(self):
        """Gets the regex_pattern_no_match_message_id of this ValidationProperties.  # noqa: E501


        :return: The regex_pattern_no_match_message_id of this ValidationProperties.  # noqa: E501
        :rtype: str
        """
        return self._regex_pattern_no_match_message_id

    @regex_pattern_no_match_message_id.setter
    def regex_pattern_no_match_message_id(self, regex_pattern_no_match_message_id):
        """Sets the regex_pattern_no_match_message_id of this ValidationProperties.


        :param regex_pattern_no_match_message_id: The regex_pattern_no_match_message_id of this ValidationProperties.  # noqa: E501
        :type: str
        """

        self._regex_pattern_no_match_message_id = regex_pattern_no_match_message_id

    @property
    def required(self):
        """Gets the required of this ValidationProperties.  # noqa: E501


        :return: The required of this ValidationProperties.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this ValidationProperties.


        :param required: The required of this ValidationProperties.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def required_if(self):
        """Gets the required_if of this ValidationProperties.  # noqa: E501


        :return: The required_if of this ValidationProperties.  # noqa: E501
        :rtype: ConditionProperties
        """
        return self._required_if

    @required_if.setter
    def required_if(self, required_if):
        """Sets the required_if of this ValidationProperties.


        :param required_if: The required_if of this ValidationProperties.  # noqa: E501
        :type: ConditionProperties
        """

        self._required_if = required_if

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
        if issubclass(ValidationProperties, dict):
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
        if not isinstance(other, ValidationProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
