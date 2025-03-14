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

class FileOperationActionData(object):
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
        'action_fails_behaviour': 'ActionFailsBehaviourData',
        'file_location_type': 'str',
        'operator': 'str',
        'rename_destination_file': 'str',
        'target_directory': 'str',
        'adjust_variables_to_file_copy': 'bool'
    }

    attribute_map = {
        'action_fails_behaviour': 'actionFailsBehaviour',
        'file_location_type': 'fileLocationType',
        'operator': 'operator',
        'rename_destination_file': 'renameDestinationFile',
        'target_directory': 'targetDirectory',
        'adjust_variables_to_file_copy': 'adjustVariablesToFileCopy'
    }

    def __init__(self, action_fails_behaviour=None, file_location_type=None, operator=None, rename_destination_file=None, target_directory=None, adjust_variables_to_file_copy=False):  # noqa: E501
        """FileOperationActionData - a model defined in Swagger"""  # noqa: E501
        self._action_fails_behaviour = None
        self._file_location_type = None
        self._operator = None
        self._rename_destination_file = None
        self._target_directory = None
        self._adjust_variables_to_file_copy = None
        self.discriminator = None
        if action_fails_behaviour is not None:
            self.action_fails_behaviour = action_fails_behaviour
        if file_location_type is not None:
            self.file_location_type = file_location_type
        if operator is not None:
            self.operator = operator
        if rename_destination_file is not None:
            self.rename_destination_file = rename_destination_file
        if target_directory is not None:
            self.target_directory = target_directory
        if adjust_variables_to_file_copy is not None:
            self.adjust_variables_to_file_copy = adjust_variables_to_file_copy

    @property
    def action_fails_behaviour(self):
        """Gets the action_fails_behaviour of this FileOperationActionData.  # noqa: E501


        :return: The action_fails_behaviour of this FileOperationActionData.  # noqa: E501
        :rtype: ActionFailsBehaviourData
        """
        return self._action_fails_behaviour

    @action_fails_behaviour.setter
    def action_fails_behaviour(self, action_fails_behaviour):
        """Sets the action_fails_behaviour of this FileOperationActionData.


        :param action_fails_behaviour: The action_fails_behaviour of this FileOperationActionData.  # noqa: E501
        :type: ActionFailsBehaviourData
        """

        self._action_fails_behaviour = action_fails_behaviour

    @property
    def file_location_type(self):
        """Gets the file_location_type of this FileOperationActionData.  # noqa: E501

        file location Type  # noqa: E501

        :return: The file_location_type of this FileOperationActionData.  # noqa: E501
        :rtype: str
        """
        return self._file_location_type

    @file_location_type.setter
    def file_location_type(self, file_location_type):
        """Sets the file_location_type of this FileOperationActionData.

        file location Type  # noqa: E501

        :param file_location_type: The file_location_type of this FileOperationActionData.  # noqa: E501
        :type: str
        """

        self._file_location_type = file_location_type

    @property
    def operator(self):
        """Gets the operator of this FileOperationActionData.  # noqa: E501

        operator  # noqa: E501

        :return: The operator of this FileOperationActionData.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this FileOperationActionData.

        operator  # noqa: E501

        :param operator: The operator of this FileOperationActionData.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def rename_destination_file(self):
        """Gets the rename_destination_file of this FileOperationActionData.  # noqa: E501

        rename destination file  # noqa: E501

        :return: The rename_destination_file of this FileOperationActionData.  # noqa: E501
        :rtype: str
        """
        return self._rename_destination_file

    @rename_destination_file.setter
    def rename_destination_file(self, rename_destination_file):
        """Sets the rename_destination_file of this FileOperationActionData.

        rename destination file  # noqa: E501

        :param rename_destination_file: The rename_destination_file of this FileOperationActionData.  # noqa: E501
        :type: str
        """

        self._rename_destination_file = rename_destination_file

    @property
    def target_directory(self):
        """Gets the target_directory of this FileOperationActionData.  # noqa: E501

        target directory  # noqa: E501

        :return: The target_directory of this FileOperationActionData.  # noqa: E501
        :rtype: str
        """
        return self._target_directory

    @target_directory.setter
    def target_directory(self, target_directory):
        """Sets the target_directory of this FileOperationActionData.

        target directory  # noqa: E501

        :param target_directory: The target_directory of this FileOperationActionData.  # noqa: E501
        :type: str
        """

        self._target_directory = target_directory

    @property
    def adjust_variables_to_file_copy(self):
        """Gets the adjust_variables_to_file_copy of this FileOperationActionData.  # noqa: E501

        adjust variables to file copy  # noqa: E501

        :return: The adjust_variables_to_file_copy of this FileOperationActionData.  # noqa: E501
        :rtype: bool
        """
        return self._adjust_variables_to_file_copy

    @adjust_variables_to_file_copy.setter
    def adjust_variables_to_file_copy(self, adjust_variables_to_file_copy):
        """Sets the adjust_variables_to_file_copy of this FileOperationActionData.

        adjust variables to file copy  # noqa: E501

        :param adjust_variables_to_file_copy: The adjust_variables_to_file_copy of this FileOperationActionData.  # noqa: E501
        :type: bool
        """

        self._adjust_variables_to_file_copy = adjust_variables_to_file_copy

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
        if issubclass(FileOperationActionData, dict):
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
        if not isinstance(other, FileOperationActionData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
