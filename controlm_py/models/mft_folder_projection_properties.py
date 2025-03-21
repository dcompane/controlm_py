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

class MFTFolderProjectionProperties(object):
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
        'name': 'str',
        'allowed_internal_user_names': 'list[str]',
        'allowed_user_names': 'list[str]',
        'allowed_group_names': 'list[str]',
        'access_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'allowed_internal_user_names': 'allowedInternalUserNames',
        'allowed_user_names': 'allowedUserNames',
        'allowed_group_names': 'allowedGroupNames',
        'access_type': 'accessType'
    }

    def __init__(self, name=None, allowed_internal_user_names=None, allowed_user_names=None, allowed_group_names=None, access_type=None):  # noqa: E501
        """MFTFolderProjectionProperties - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._allowed_internal_user_names = None
        self._allowed_user_names = None
        self._allowed_group_names = None
        self._access_type = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if allowed_internal_user_names is not None:
            self.allowed_internal_user_names = allowed_internal_user_names
        if allowed_user_names is not None:
            self.allowed_user_names = allowed_user_names
        if allowed_group_names is not None:
            self.allowed_group_names = allowed_group_names
        if access_type is not None:
            self.access_type = access_type

    @property
    def name(self):
        """Gets the name of this MFTFolderProjectionProperties.  # noqa: E501

        The name of the folder.  # noqa: E501

        :return: The name of this MFTFolderProjectionProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MFTFolderProjectionProperties.

        The name of the folder.  # noqa: E501

        :param name: The name of this MFTFolderProjectionProperties.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def allowed_internal_user_names(self):
        """Gets the allowed_internal_user_names of this MFTFolderProjectionProperties.  # noqa: E501

        Authorized Internal Users.  # noqa: E501

        :return: The allowed_internal_user_names of this MFTFolderProjectionProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_internal_user_names

    @allowed_internal_user_names.setter
    def allowed_internal_user_names(self, allowed_internal_user_names):
        """Sets the allowed_internal_user_names of this MFTFolderProjectionProperties.

        Authorized Internal Users.  # noqa: E501

        :param allowed_internal_user_names: The allowed_internal_user_names of this MFTFolderProjectionProperties.  # noqa: E501
        :type: list[str]
        """

        self._allowed_internal_user_names = allowed_internal_user_names

    @property
    def allowed_user_names(self):
        """Gets the allowed_user_names of this MFTFolderProjectionProperties.  # noqa: E501

        Authorized External Users.  # noqa: E501

        :return: The allowed_user_names of this MFTFolderProjectionProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_user_names

    @allowed_user_names.setter
    def allowed_user_names(self, allowed_user_names):
        """Sets the allowed_user_names of this MFTFolderProjectionProperties.

        Authorized External Users.  # noqa: E501

        :param allowed_user_names: The allowed_user_names of this MFTFolderProjectionProperties.  # noqa: E501
        :type: list[str]
        """

        self._allowed_user_names = allowed_user_names

    @property
    def allowed_group_names(self):
        """Gets the allowed_group_names of this MFTFolderProjectionProperties.  # noqa: E501

        Array of allowed group names.  # noqa: E501

        :return: The allowed_group_names of this MFTFolderProjectionProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_group_names

    @allowed_group_names.setter
    def allowed_group_names(self, allowed_group_names):
        """Sets the allowed_group_names of this MFTFolderProjectionProperties.

        Array of allowed group names.  # noqa: E501

        :param allowed_group_names: The allowed_group_names of this MFTFolderProjectionProperties.  # noqa: E501
        :type: list[str]
        """

        self._allowed_group_names = allowed_group_names

    @property
    def access_type(self):
        """Gets the access_type of this MFTFolderProjectionProperties.  # noqa: E501

        Folder's access type (Limited, Unlimited).  # noqa: E501

        :return: The access_type of this MFTFolderProjectionProperties.  # noqa: E501
        :rtype: str
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        """Sets the access_type of this MFTFolderProjectionProperties.

        Folder's access type (Limited, Unlimited).  # noqa: E501

        :param access_type: The access_type of this MFTFolderProjectionProperties.  # noqa: E501
        :type: str
        """

        self._access_type = access_type

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
        if issubclass(MFTFolderProjectionProperties, dict):
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
        if not isinstance(other, MFTFolderProjectionProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
