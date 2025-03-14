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

class ConnectionProfileStatus(object):
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
        'type': 'str',
        'description': 'str',
        'time_modified': 'str',
        'time_created': 'str',
        'creator_name': 'str',
        'modifier_name': 'str',
        'sync_status': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'time_modified': 'timeModified',
        'time_created': 'timeCreated',
        'creator_name': 'creatorName',
        'modifier_name': 'modifierName',
        'sync_status': 'syncStatus'
    }

    def __init__(self, name=None, type=None, description=None, time_modified=None, time_created=None, creator_name=None, modifier_name=None, sync_status=None):  # noqa: E501
        """ConnectionProfileStatus - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._type = None
        self._description = None
        self._time_modified = None
        self._time_created = None
        self._creator_name = None
        self._modifier_name = None
        self._sync_status = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if time_modified is not None:
            self.time_modified = time_modified
        if time_created is not None:
            self.time_created = time_created
        if creator_name is not None:
            self.creator_name = creator_name
        if modifier_name is not None:
            self.modifier_name = modifier_name
        if sync_status is not None:
            self.sync_status = sync_status

    @property
    def name(self):
        """Gets the name of this ConnectionProfileStatus.  # noqa: E501

        connection profile name  # noqa: E501

        :return: The name of this ConnectionProfileStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConnectionProfileStatus.

        connection profile name  # noqa: E501

        :param name: The name of this ConnectionProfileStatus.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this ConnectionProfileStatus.  # noqa: E501

        connection profile type  # noqa: E501

        :return: The type of this ConnectionProfileStatus.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConnectionProfileStatus.

        connection profile type  # noqa: E501

        :param type: The type of this ConnectionProfileStatus.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def description(self):
        """Gets the description of this ConnectionProfileStatus.  # noqa: E501

        connection profile description  # noqa: E501

        :return: The description of this ConnectionProfileStatus.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConnectionProfileStatus.

        connection profile description  # noqa: E501

        :param description: The description of this ConnectionProfileStatus.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def time_modified(self):
        """Gets the time_modified of this ConnectionProfileStatus.  # noqa: E501

        UTC date of the modification  # noqa: E501

        :return: The time_modified of this ConnectionProfileStatus.  # noqa: E501
        :rtype: str
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """Sets the time_modified of this ConnectionProfileStatus.

        UTC date of the modification  # noqa: E501

        :param time_modified: The time_modified of this ConnectionProfileStatus.  # noqa: E501
        :type: str
        """

        self._time_modified = time_modified

    @property
    def time_created(self):
        """Gets the time_created of this ConnectionProfileStatus.  # noqa: E501

        UTC date of the creation  # noqa: E501

        :return: The time_created of this ConnectionProfileStatus.  # noqa: E501
        :rtype: str
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """Sets the time_created of this ConnectionProfileStatus.

        UTC date of the creation  # noqa: E501

        :param time_created: The time_created of this ConnectionProfileStatus.  # noqa: E501
        :type: str
        """

        self._time_created = time_created

    @property
    def creator_name(self):
        """Gets the creator_name of this ConnectionProfileStatus.  # noqa: E501

        creator's name  # noqa: E501

        :return: The creator_name of this ConnectionProfileStatus.  # noqa: E501
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this ConnectionProfileStatus.

        creator's name  # noqa: E501

        :param creator_name: The creator_name of this ConnectionProfileStatus.  # noqa: E501
        :type: str
        """

        self._creator_name = creator_name

    @property
    def modifier_name(self):
        """Gets the modifier_name of this ConnectionProfileStatus.  # noqa: E501

        modifier's name  # noqa: E501

        :return: The modifier_name of this ConnectionProfileStatus.  # noqa: E501
        :rtype: str
        """
        return self._modifier_name

    @modifier_name.setter
    def modifier_name(self, modifier_name):
        """Sets the modifier_name of this ConnectionProfileStatus.

        modifier's name  # noqa: E501

        :param modifier_name: The modifier_name of this ConnectionProfileStatus.  # noqa: E501
        :type: str
        """

        self._modifier_name = modifier_name

    @property
    def sync_status(self):
        """Gets the sync_status of this ConnectionProfileStatus.  # noqa: E501

        Status calculated by the server according to the list of statuses with each server  # noqa: E501

        :return: The sync_status of this ConnectionProfileStatus.  # noqa: E501
        :rtype: str
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        """Sets the sync_status of this ConnectionProfileStatus.

        Status calculated by the server according to the list of statuses with each server  # noqa: E501

        :param sync_status: The sync_status of this ConnectionProfileStatus.  # noqa: E501
        :type: str
        """

        self._sync_status = sync_status

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
        if issubclass(ConnectionProfileStatus, dict):
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
        if not isinstance(other, ConnectionProfileStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
