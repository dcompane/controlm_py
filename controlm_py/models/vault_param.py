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

class VaultParam(object):
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
        'type': 'str',
        'label': 'str',
        'label_api': 'str',
        'name': 'str',
        'is_mandatory': 'bool',
        'min_length': 'int',
        'max_length': 'int',
        'excluded_chars': 'str',
        'is_in_excluded_chars': 'bool',
        'valid_values': 'str',
        'default_visibility': 'str',
        'default_value': 'str'
    }

    attribute_map = {
        'type': 'type',
        'label': 'label',
        'label_api': 'labelApi',
        'name': 'name',
        'is_mandatory': 'isMandatory',
        'min_length': 'minLength',
        'max_length': 'maxLength',
        'excluded_chars': 'excludedChars',
        'is_in_excluded_chars': 'isInExcludedChars',
        'valid_values': 'validValues',
        'default_visibility': 'defaultVisibility',
        'default_value': 'defaultValue'
    }

    def __init__(self, type=None, label=None, label_api=None, name=None, is_mandatory=None, min_length=None, max_length=None, excluded_chars=None, is_in_excluded_chars=None, valid_values=None, default_visibility=None, default_value=None):  # noqa: E501
        """VaultParam - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._label = None
        self._label_api = None
        self._name = None
        self._is_mandatory = None
        self._min_length = None
        self._max_length = None
        self._excluded_chars = None
        self._is_in_excluded_chars = None
        self._valid_values = None
        self._default_visibility = None
        self._default_value = None
        self.discriminator = None
        self.type = type
        self.label = label
        self.label_api = label_api
        if name is not None:
            self.name = name
        if is_mandatory is not None:
            self.is_mandatory = is_mandatory
        if min_length is not None:
            self.min_length = min_length
        if max_length is not None:
            self.max_length = max_length
        if excluded_chars is not None:
            self.excluded_chars = excluded_chars
        if is_in_excluded_chars is not None:
            self.is_in_excluded_chars = is_in_excluded_chars
        if valid_values is not None:
            self.valid_values = valid_values
        if default_visibility is not None:
            self.default_visibility = default_visibility
        if default_value is not None:
            self.default_value = default_value

    @property
    def type(self):
        """Gets the type of this VaultParam.  # noqa: E501

        The UI Control type, could be 'textbox' or 'textarea'  # noqa: E501

        :return: The type of this VaultParam.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VaultParam.

        The UI Control type, could be 'textbox' or 'textarea'  # noqa: E501

        :param type: The type of this VaultParam.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def label(self):
        """Gets the label of this VaultParam.  # noqa: E501

        The displayed name of the field parameter  # noqa: E501

        :return: The label of this VaultParam.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this VaultParam.

        The displayed name of the field parameter  # noqa: E501

        :param label: The label of this VaultParam.  # noqa: E501
        :type: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def label_api(self):
        """Gets the label_api of this VaultParam.  # noqa: E501

        The display name of the parameter in Automation API  # noqa: E501

        :return: The label_api of this VaultParam.  # noqa: E501
        :rtype: str
        """
        return self._label_api

    @label_api.setter
    def label_api(self, label_api):
        """Sets the label_api of this VaultParam.

        The display name of the parameter in Automation API  # noqa: E501

        :param label_api: The label_api of this VaultParam.  # noqa: E501
        :type: str
        """
        if label_api is None:
            raise ValueError("Invalid value for `label_api`, must not be `None`")  # noqa: E501

        self._label_api = label_api

    @property
    def name(self):
        """Gets the name of this VaultParam.  # noqa: E501

        The name of the field parameter  # noqa: E501

        :return: The name of this VaultParam.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VaultParam.

        The name of the field parameter  # noqa: E501

        :param name: The name of this VaultParam.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_mandatory(self):
        """Gets the is_mandatory of this VaultParam.  # noqa: E501

        UI validation (optional) - indicates whether user must fill this parameter  # noqa: E501

        :return: The is_mandatory of this VaultParam.  # noqa: E501
        :rtype: bool
        """
        return self._is_mandatory

    @is_mandatory.setter
    def is_mandatory(self, is_mandatory):
        """Sets the is_mandatory of this VaultParam.

        UI validation (optional) - indicates whether user must fill this parameter  # noqa: E501

        :param is_mandatory: The is_mandatory of this VaultParam.  # noqa: E501
        :type: bool
        """

        self._is_mandatory = is_mandatory

    @property
    def min_length(self):
        """Gets the min_length of this VaultParam.  # noqa: E501

        UI validation (optional) - the minimum allowed value field length  # noqa: E501

        :return: The min_length of this VaultParam.  # noqa: E501
        :rtype: int
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        """Sets the min_length of this VaultParam.

        UI validation (optional) - the minimum allowed value field length  # noqa: E501

        :param min_length: The min_length of this VaultParam.  # noqa: E501
        :type: int
        """

        self._min_length = min_length

    @property
    def max_length(self):
        """Gets the max_length of this VaultParam.  # noqa: E501

        UI validation (optional) - the maximum allowed value field length  # noqa: E501

        :return: The max_length of this VaultParam.  # noqa: E501
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this VaultParam.

        UI validation (optional) - the maximum allowed value field length  # noqa: E501

        :param max_length: The max_length of this VaultParam.  # noqa: E501
        :type: int
        """

        self._max_length = max_length

    @property
    def excluded_chars(self):
        """Gets the excluded_chars of this VaultParam.  # noqa: E501

        UI validation (optional) - indicates to excludes specific chars seperated by ;  # noqa: E501

        :return: The excluded_chars of this VaultParam.  # noqa: E501
        :rtype: str
        """
        return self._excluded_chars

    @excluded_chars.setter
    def excluded_chars(self, excluded_chars):
        """Sets the excluded_chars of this VaultParam.

        UI validation (optional) - indicates to excludes specific chars seperated by ;  # noqa: E501

        :param excluded_chars: The excluded_chars of this VaultParam.  # noqa: E501
        :type: str
        """

        self._excluded_chars = excluded_chars

    @property
    def is_in_excluded_chars(self):
        """Gets the is_in_excluded_chars of this VaultParam.  # noqa: E501

        UI validation (optional) - indicates whether excludedChars is enabled  # noqa: E501

        :return: The is_in_excluded_chars of this VaultParam.  # noqa: E501
        :rtype: bool
        """
        return self._is_in_excluded_chars

    @is_in_excluded_chars.setter
    def is_in_excluded_chars(self, is_in_excluded_chars):
        """Sets the is_in_excluded_chars of this VaultParam.

        UI validation (optional) - indicates whether excludedChars is enabled  # noqa: E501

        :param is_in_excluded_chars: The is_in_excluded_chars of this VaultParam.  # noqa: E501
        :type: bool
        """

        self._is_in_excluded_chars = is_in_excluded_chars

    @property
    def valid_values(self):
        """Gets the valid_values of this VaultParam.  # noqa: E501

        UI validation (optional) - indicates the allowed input types, 'alphanumeric', 'numbers', 'chars' or 'all'  # noqa: E501

        :return: The valid_values of this VaultParam.  # noqa: E501
        :rtype: str
        """
        return self._valid_values

    @valid_values.setter
    def valid_values(self, valid_values):
        """Sets the valid_values of this VaultParam.

        UI validation (optional) - indicates the allowed input types, 'alphanumeric', 'numbers', 'chars' or 'all'  # noqa: E501

        :param valid_values: The valid_values of this VaultParam.  # noqa: E501
        :type: str
        """

        self._valid_values = valid_values

    @property
    def default_visibility(self):
        """Gets the default_visibility of this VaultParam.  # noqa: E501

        UI appearance (optional) - indicates the UI Control visibility,  'visible', 'hidden' or 'readonly'  # noqa: E501

        :return: The default_visibility of this VaultParam.  # noqa: E501
        :rtype: str
        """
        return self._default_visibility

    @default_visibility.setter
    def default_visibility(self, default_visibility):
        """Sets the default_visibility of this VaultParam.

        UI appearance (optional) - indicates the UI Control visibility,  'visible', 'hidden' or 'readonly'  # noqa: E501

        :param default_visibility: The default_visibility of this VaultParam.  # noqa: E501
        :type: str
        """

        self._default_visibility = default_visibility

    @property
    def default_value(self):
        """Gets the default_value of this VaultParam.  # noqa: E501

        UI appearance (optional)- this value automatically sets on the UI Control in-case no other value specified  # noqa: E501

        :return: The default_value of this VaultParam.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this VaultParam.

        UI appearance (optional)- this value automatically sets on the UI Control in-case no other value specified  # noqa: E501

        :param default_value: The default_value of this VaultParam.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

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
        if issubclass(VaultParam, dict):
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
        if not isinstance(other, VaultParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
