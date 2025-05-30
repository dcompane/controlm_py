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

class FoldersUsersSettingsAndMetadataProperties(object):
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
        'folders': 'list[FolderPropertiesData]',
        'settings': 'list[SettingProperties]',
        'settings_metadata': 'SettingsMetadataProperties',
        'users': 'list[UserAllowedFoldersProperties]',
        'groups': 'list[GroupsAllowedFoldersProperties]'
    }

    attribute_map = {
        'folders': 'folders',
        'settings': 'settings',
        'settings_metadata': 'settingsMetadata',
        'users': 'users',
        'groups': 'groups'
    }

    def __init__(self, folders=None, settings=None, settings_metadata=None, users=None, groups=None):  # noqa: E501
        """FoldersUsersSettingsAndMetadataProperties - a model defined in Swagger"""  # noqa: E501
        self._folders = None
        self._settings = None
        self._settings_metadata = None
        self._users = None
        self._groups = None
        self.discriminator = None
        if folders is not None:
            self.folders = folders
        if settings is not None:
            self.settings = settings
        if settings_metadata is not None:
            self.settings_metadata = settings_metadata
        if users is not None:
            self.users = users
        if groups is not None:
            self.groups = groups

    @property
    def folders(self):
        """Gets the folders of this FoldersUsersSettingsAndMetadataProperties.  # noqa: E501


        :return: The folders of this FoldersUsersSettingsAndMetadataProperties.  # noqa: E501
        :rtype: list[FolderPropertiesData]
        """
        return self._folders

    @folders.setter
    def folders(self, folders):
        """Sets the folders of this FoldersUsersSettingsAndMetadataProperties.


        :param folders: The folders of this FoldersUsersSettingsAndMetadataProperties.  # noqa: E501
        :type: list[FolderPropertiesData]
        """

        self._folders = folders

    @property
    def settings(self):
        """Gets the settings of this FoldersUsersSettingsAndMetadataProperties.  # noqa: E501


        :return: The settings of this FoldersUsersSettingsAndMetadataProperties.  # noqa: E501
        :rtype: list[SettingProperties]
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this FoldersUsersSettingsAndMetadataProperties.


        :param settings: The settings of this FoldersUsersSettingsAndMetadataProperties.  # noqa: E501
        :type: list[SettingProperties]
        """

        self._settings = settings

    @property
    def settings_metadata(self):
        """Gets the settings_metadata of this FoldersUsersSettingsAndMetadataProperties.  # noqa: E501


        :return: The settings_metadata of this FoldersUsersSettingsAndMetadataProperties.  # noqa: E501
        :rtype: SettingsMetadataProperties
        """
        return self._settings_metadata

    @settings_metadata.setter
    def settings_metadata(self, settings_metadata):
        """Sets the settings_metadata of this FoldersUsersSettingsAndMetadataProperties.


        :param settings_metadata: The settings_metadata of this FoldersUsersSettingsAndMetadataProperties.  # noqa: E501
        :type: SettingsMetadataProperties
        """

        self._settings_metadata = settings_metadata

    @property
    def users(self):
        """Gets the users of this FoldersUsersSettingsAndMetadataProperties.  # noqa: E501


        :return: The users of this FoldersUsersSettingsAndMetadataProperties.  # noqa: E501
        :rtype: list[UserAllowedFoldersProperties]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this FoldersUsersSettingsAndMetadataProperties.


        :param users: The users of this FoldersUsersSettingsAndMetadataProperties.  # noqa: E501
        :type: list[UserAllowedFoldersProperties]
        """

        self._users = users

    @property
    def groups(self):
        """Gets the groups of this FoldersUsersSettingsAndMetadataProperties.  # noqa: E501


        :return: The groups of this FoldersUsersSettingsAndMetadataProperties.  # noqa: E501
        :rtype: list[GroupsAllowedFoldersProperties]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this FoldersUsersSettingsAndMetadataProperties.


        :param groups: The groups of this FoldersUsersSettingsAndMetadataProperties.  # noqa: E501
        :type: list[GroupsAllowedFoldersProperties]
        """

        self._groups = groups

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
        if issubclass(FoldersUsersSettingsAndMetadataProperties, dict):
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
        if not isinstance(other, FoldersUsersSettingsAndMetadataProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
