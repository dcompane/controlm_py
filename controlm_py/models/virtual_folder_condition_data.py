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

class VirtualFolderConditionData(object):
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
        'sub_directory': 'str',
        'case_sensitive': 'bool',
        'is_regex': 'bool',
        'virtual_folder_names': 'list[str]',
        'virtual_folder_patterns': 'list[str]'
    }

    attribute_map = {
        'sub_directory': 'subDirectory',
        'case_sensitive': 'caseSensitive',
        'is_regex': 'isRegex',
        'virtual_folder_names': 'virtualFolderNames',
        'virtual_folder_patterns': 'virtualFolderPatterns'
    }

    def __init__(self, sub_directory=None, case_sensitive=None, is_regex=None, virtual_folder_names=None, virtual_folder_patterns=None):  # noqa: E501
        """VirtualFolderConditionData - a model defined in Swagger"""  # noqa: E501
        self._sub_directory = None
        self._case_sensitive = None
        self._is_regex = None
        self._virtual_folder_names = None
        self._virtual_folder_patterns = None
        self.discriminator = None
        if sub_directory is not None:
            self.sub_directory = sub_directory
        if case_sensitive is not None:
            self.case_sensitive = case_sensitive
        if is_regex is not None:
            self.is_regex = is_regex
        if virtual_folder_names is not None:
            self.virtual_folder_names = virtual_folder_names
        if virtual_folder_patterns is not None:
            self.virtual_folder_patterns = virtual_folder_patterns

    @property
    def sub_directory(self):
        """Gets the sub_directory of this VirtualFolderConditionData.  # noqa: E501

        sub directory  # noqa: E501

        :return: The sub_directory of this VirtualFolderConditionData.  # noqa: E501
        :rtype: str
        """
        return self._sub_directory

    @sub_directory.setter
    def sub_directory(self, sub_directory):
        """Sets the sub_directory of this VirtualFolderConditionData.

        sub directory  # noqa: E501

        :param sub_directory: The sub_directory of this VirtualFolderConditionData.  # noqa: E501
        :type: str
        """

        self._sub_directory = sub_directory

    @property
    def case_sensitive(self):
        """Gets the case_sensitive of this VirtualFolderConditionData.  # noqa: E501

        is case sensitive  # noqa: E501

        :return: The case_sensitive of this VirtualFolderConditionData.  # noqa: E501
        :rtype: bool
        """
        return self._case_sensitive

    @case_sensitive.setter
    def case_sensitive(self, case_sensitive):
        """Sets the case_sensitive of this VirtualFolderConditionData.

        is case sensitive  # noqa: E501

        :param case_sensitive: The case_sensitive of this VirtualFolderConditionData.  # noqa: E501
        :type: bool
        """

        self._case_sensitive = case_sensitive

    @property
    def is_regex(self):
        """Gets the is_regex of this VirtualFolderConditionData.  # noqa: E501

        is Regex  # noqa: E501

        :return: The is_regex of this VirtualFolderConditionData.  # noqa: E501
        :rtype: bool
        """
        return self._is_regex

    @is_regex.setter
    def is_regex(self, is_regex):
        """Sets the is_regex of this VirtualFolderConditionData.

        is Regex  # noqa: E501

        :param is_regex: The is_regex of this VirtualFolderConditionData.  # noqa: E501
        :type: bool
        """

        self._is_regex = is_regex

    @property
    def virtual_folder_names(self):
        """Gets the virtual_folder_names of this VirtualFolderConditionData.  # noqa: E501

        virtual folder name  # noqa: E501

        :return: The virtual_folder_names of this VirtualFolderConditionData.  # noqa: E501
        :rtype: list[str]
        """
        return self._virtual_folder_names

    @virtual_folder_names.setter
    def virtual_folder_names(self, virtual_folder_names):
        """Sets the virtual_folder_names of this VirtualFolderConditionData.

        virtual folder name  # noqa: E501

        :param virtual_folder_names: The virtual_folder_names of this VirtualFolderConditionData.  # noqa: E501
        :type: list[str]
        """

        self._virtual_folder_names = virtual_folder_names

    @property
    def virtual_folder_patterns(self):
        """Gets the virtual_folder_patterns of this VirtualFolderConditionData.  # noqa: E501

        virtual folder pattern  # noqa: E501

        :return: The virtual_folder_patterns of this VirtualFolderConditionData.  # noqa: E501
        :rtype: list[str]
        """
        return self._virtual_folder_patterns

    @virtual_folder_patterns.setter
    def virtual_folder_patterns(self, virtual_folder_patterns):
        """Sets the virtual_folder_patterns of this VirtualFolderConditionData.

        virtual folder pattern  # noqa: E501

        :param virtual_folder_patterns: The virtual_folder_patterns of this VirtualFolderConditionData.  # noqa: E501
        :type: list[str]
        """

        self._virtual_folder_patterns = virtual_folder_patterns

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
        if issubclass(VirtualFolderConditionData, dict):
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
        if not isinstance(other, VirtualFolderConditionData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
