# coding: utf-8

"""
    Control-M Services

    Provides access to BMC Control-M Services  # noqa: E501

    OpenAPI spec version: 9.21.325
    Contact: customer_support@bmc.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EMServerSummary(object):
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
        'status': 'str',
        'message': 'str',
        'host': 'str',
        'name': 'str',
        'os': 'str',
        'version': 'str'
    }

    attribute_map = {
        'status': 'status',
        'message': 'message',
        'host': 'host',
        'name': 'name',
        'os': 'os',
        'version': 'version'
    }

    def __init__(self, status=None, message=None, host=None, name=None, os=None, version=None):  # noqa: E501
        """EMServerSummary - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._message = None
        self._host = None
        self._name = None
        self._os = None
        self._version = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if host is not None:
            self.host = host
        if name is not None:
            self.name = name
        if os is not None:
            self.os = os
        if version is not None:
            self.version = version

    @property
    def status(self):
        """Gets the status of this EMServerSummary.  # noqa: E501

        the em server status  # noqa: E501

        :return: The status of this EMServerSummary.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EMServerSummary.

        the em server status  # noqa: E501

        :param status: The status of this EMServerSummary.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def message(self):
        """Gets the message of this EMServerSummary.  # noqa: E501


        :return: The message of this EMServerSummary.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this EMServerSummary.


        :param message: The message of this EMServerSummary.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def host(self):
        """Gets the host of this EMServerSummary.  # noqa: E501

        EM server host  # noqa: E501

        :return: The host of this EMServerSummary.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this EMServerSummary.

        EM server host  # noqa: E501

        :param host: The host of this EMServerSummary.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def name(self):
        """Gets the name of this EMServerSummary.  # noqa: E501

        EM server name  # noqa: E501

        :return: The name of this EMServerSummary.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EMServerSummary.

        EM server name  # noqa: E501

        :param name: The name of this EMServerSummary.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def os(self):
        """Gets the os of this EMServerSummary.  # noqa: E501

        Operating System of this EM server  # noqa: E501

        :return: The os of this EMServerSummary.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this EMServerSummary.

        Operating System of this EM server  # noqa: E501

        :param os: The os of this EMServerSummary.  # noqa: E501
        :type: str
        """

        self._os = os

    @property
    def version(self):
        """Gets the version of this EMServerSummary.  # noqa: E501

        Version of this EM server  # noqa: E501

        :return: The version of this EMServerSummary.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this EMServerSummary.

        Version of this EM server  # noqa: E501

        :param version: The version of this EMServerSummary.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(EMServerSummary, dict):
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
        if not isinstance(other, EMServerSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other