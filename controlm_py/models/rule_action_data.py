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

class RuleActionData(object):
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
        'action_type': 'str',
        'email_notification_action_data': 'EmailNotificationActionData',
        'file_operation_action_data': 'FileOperationActionData',
        'run_folder_job_action_data': 'RunFolderJobActionData',
        'add_event_action_data': 'AddEventActionData',
        'run_command_action_data': 'RunCommandActionData'
    }

    attribute_map = {
        'action_type': 'actionType',
        'email_notification_action_data': 'emailNotificationActionData',
        'file_operation_action_data': 'fileOperationActionData',
        'run_folder_job_action_data': 'runFolderJobActionData',
        'add_event_action_data': 'addEventActionData',
        'run_command_action_data': 'runCommandActionData'
    }

    def __init__(self, action_type=None, email_notification_action_data=None, file_operation_action_data=None, run_folder_job_action_data=None, add_event_action_data=None, run_command_action_data=None):  # noqa: E501
        """RuleActionData - a model defined in Swagger"""  # noqa: E501
        self._action_type = None
        self._email_notification_action_data = None
        self._file_operation_action_data = None
        self._run_folder_job_action_data = None
        self._add_event_action_data = None
        self._run_command_action_data = None
        self.discriminator = None
        if action_type is not None:
            self.action_type = action_type
        if email_notification_action_data is not None:
            self.email_notification_action_data = email_notification_action_data
        if file_operation_action_data is not None:
            self.file_operation_action_data = file_operation_action_data
        if run_folder_job_action_data is not None:
            self.run_folder_job_action_data = run_folder_job_action_data
        if add_event_action_data is not None:
            self.add_event_action_data = add_event_action_data
        if run_command_action_data is not None:
            self.run_command_action_data = run_command_action_data

    @property
    def action_type(self):
        """Gets the action_type of this RuleActionData.  # noqa: E501

        action type  # noqa: E501

        :return: The action_type of this RuleActionData.  # noqa: E501
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this RuleActionData.

        action type  # noqa: E501

        :param action_type: The action_type of this RuleActionData.  # noqa: E501
        :type: str
        """

        self._action_type = action_type

    @property
    def email_notification_action_data(self):
        """Gets the email_notification_action_data of this RuleActionData.  # noqa: E501


        :return: The email_notification_action_data of this RuleActionData.  # noqa: E501
        :rtype: EmailNotificationActionData
        """
        return self._email_notification_action_data

    @email_notification_action_data.setter
    def email_notification_action_data(self, email_notification_action_data):
        """Sets the email_notification_action_data of this RuleActionData.


        :param email_notification_action_data: The email_notification_action_data of this RuleActionData.  # noqa: E501
        :type: EmailNotificationActionData
        """

        self._email_notification_action_data = email_notification_action_data

    @property
    def file_operation_action_data(self):
        """Gets the file_operation_action_data of this RuleActionData.  # noqa: E501


        :return: The file_operation_action_data of this RuleActionData.  # noqa: E501
        :rtype: FileOperationActionData
        """
        return self._file_operation_action_data

    @file_operation_action_data.setter
    def file_operation_action_data(self, file_operation_action_data):
        """Sets the file_operation_action_data of this RuleActionData.


        :param file_operation_action_data: The file_operation_action_data of this RuleActionData.  # noqa: E501
        :type: FileOperationActionData
        """

        self._file_operation_action_data = file_operation_action_data

    @property
    def run_folder_job_action_data(self):
        """Gets the run_folder_job_action_data of this RuleActionData.  # noqa: E501


        :return: The run_folder_job_action_data of this RuleActionData.  # noqa: E501
        :rtype: RunFolderJobActionData
        """
        return self._run_folder_job_action_data

    @run_folder_job_action_data.setter
    def run_folder_job_action_data(self, run_folder_job_action_data):
        """Sets the run_folder_job_action_data of this RuleActionData.


        :param run_folder_job_action_data: The run_folder_job_action_data of this RuleActionData.  # noqa: E501
        :type: RunFolderJobActionData
        """

        self._run_folder_job_action_data = run_folder_job_action_data

    @property
    def add_event_action_data(self):
        """Gets the add_event_action_data of this RuleActionData.  # noqa: E501


        :return: The add_event_action_data of this RuleActionData.  # noqa: E501
        :rtype: AddEventActionData
        """
        return self._add_event_action_data

    @add_event_action_data.setter
    def add_event_action_data(self, add_event_action_data):
        """Sets the add_event_action_data of this RuleActionData.


        :param add_event_action_data: The add_event_action_data of this RuleActionData.  # noqa: E501
        :type: AddEventActionData
        """

        self._add_event_action_data = add_event_action_data

    @property
    def run_command_action_data(self):
        """Gets the run_command_action_data of this RuleActionData.  # noqa: E501


        :return: The run_command_action_data of this RuleActionData.  # noqa: E501
        :rtype: RunCommandActionData
        """
        return self._run_command_action_data

    @run_command_action_data.setter
    def run_command_action_data(self, run_command_action_data):
        """Sets the run_command_action_data of this RuleActionData.


        :param run_command_action_data: The run_command_action_data of this RuleActionData.  # noqa: E501
        :type: RunCommandActionData
        """

        self._run_command_action_data = run_command_action_data

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
        if issubclass(RuleActionData, dict):
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
        if not isinstance(other, RuleActionData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
