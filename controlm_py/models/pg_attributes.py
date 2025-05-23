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

class PgAttributes(object):
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
        'replication_status': 'str',
        'replication_mode': 'str',
        'disk_space': 'int',
        'archiving_status': 'int',
        'archiving_disk_space': 'int',
        'database_performance': 'int',
        'postgres_def': 'PostgresDef'
    }

    attribute_map = {
        'replication_status': 'replicationStatus',
        'replication_mode': 'replicationMode',
        'disk_space': 'diskSpace',
        'archiving_status': 'archivingStatus',
        'archiving_disk_space': 'archivingDiskSpace',
        'database_performance': 'databasePerformance',
        'postgres_def': 'postgresDef'
    }

    def __init__(self, replication_status=None, replication_mode=None, disk_space=None, archiving_status=None, archiving_disk_space=None, database_performance=None, postgres_def=None):  # noqa: E501
        """PgAttributes - a model defined in Swagger"""  # noqa: E501
        self._replication_status = None
        self._replication_mode = None
        self._disk_space = None
        self._archiving_status = None
        self._archiving_disk_space = None
        self._database_performance = None
        self._postgres_def = None
        self.discriminator = None
        if replication_status is not None:
            self.replication_status = replication_status
        if replication_mode is not None:
            self.replication_mode = replication_mode
        if disk_space is not None:
            self.disk_space = disk_space
        if archiving_status is not None:
            self.archiving_status = archiving_status
        if archiving_disk_space is not None:
            self.archiving_disk_space = archiving_disk_space
        if database_performance is not None:
            self.database_performance = database_performance
        if postgres_def is not None:
            self.postgres_def = postgres_def

    @property
    def replication_status(self):
        """Gets the replication_status of this PgAttributes.  # noqa: E501


        :return: The replication_status of this PgAttributes.  # noqa: E501
        :rtype: str
        """
        return self._replication_status

    @replication_status.setter
    def replication_status(self, replication_status):
        """Sets the replication_status of this PgAttributes.


        :param replication_status: The replication_status of this PgAttributes.  # noqa: E501
        :type: str
        """

        self._replication_status = replication_status

    @property
    def replication_mode(self):
        """Gets the replication_mode of this PgAttributes.  # noqa: E501


        :return: The replication_mode of this PgAttributes.  # noqa: E501
        :rtype: str
        """
        return self._replication_mode

    @replication_mode.setter
    def replication_mode(self, replication_mode):
        """Sets the replication_mode of this PgAttributes.


        :param replication_mode: The replication_mode of this PgAttributes.  # noqa: E501
        :type: str
        """

        self._replication_mode = replication_mode

    @property
    def disk_space(self):
        """Gets the disk_space of this PgAttributes.  # noqa: E501


        :return: The disk_space of this PgAttributes.  # noqa: E501
        :rtype: int
        """
        return self._disk_space

    @disk_space.setter
    def disk_space(self, disk_space):
        """Sets the disk_space of this PgAttributes.


        :param disk_space: The disk_space of this PgAttributes.  # noqa: E501
        :type: int
        """

        self._disk_space = disk_space

    @property
    def archiving_status(self):
        """Gets the archiving_status of this PgAttributes.  # noqa: E501


        :return: The archiving_status of this PgAttributes.  # noqa: E501
        :rtype: int
        """
        return self._archiving_status

    @archiving_status.setter
    def archiving_status(self, archiving_status):
        """Sets the archiving_status of this PgAttributes.


        :param archiving_status: The archiving_status of this PgAttributes.  # noqa: E501
        :type: int
        """

        self._archiving_status = archiving_status

    @property
    def archiving_disk_space(self):
        """Gets the archiving_disk_space of this PgAttributes.  # noqa: E501


        :return: The archiving_disk_space of this PgAttributes.  # noqa: E501
        :rtype: int
        """
        return self._archiving_disk_space

    @archiving_disk_space.setter
    def archiving_disk_space(self, archiving_disk_space):
        """Sets the archiving_disk_space of this PgAttributes.


        :param archiving_disk_space: The archiving_disk_space of this PgAttributes.  # noqa: E501
        :type: int
        """

        self._archiving_disk_space = archiving_disk_space

    @property
    def database_performance(self):
        """Gets the database_performance of this PgAttributes.  # noqa: E501


        :return: The database_performance of this PgAttributes.  # noqa: E501
        :rtype: int
        """
        return self._database_performance

    @database_performance.setter
    def database_performance(self, database_performance):
        """Sets the database_performance of this PgAttributes.


        :param database_performance: The database_performance of this PgAttributes.  # noqa: E501
        :type: int
        """

        self._database_performance = database_performance

    @property
    def postgres_def(self):
        """Gets the postgres_def of this PgAttributes.  # noqa: E501


        :return: The postgres_def of this PgAttributes.  # noqa: E501
        :rtype: PostgresDef
        """
        return self._postgres_def

    @postgres_def.setter
    def postgres_def(self, postgres_def):
        """Sets the postgres_def of this PgAttributes.


        :param postgres_def: The postgres_def of this PgAttributes.  # noqa: E501
        :type: PostgresDef
        """

        self._postgres_def = postgres_def

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
        if issubclass(PgAttributes, dict):
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
        if not isinstance(other, PgAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
