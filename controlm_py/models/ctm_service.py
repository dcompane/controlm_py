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

class CtmService(object):
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
        'name': 'str',
        'host': 'str',
        'version': 'str',
        'os_type': 'str',
        'desired_state': 'str',
        'message': 'str',
        'last_update': 'str',
        'state': 'str',
        'status': 'str'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'host': 'host',
        'version': 'version',
        'os_type': 'osType',
        'desired_state': 'desiredState',
        'message': 'message',
        'last_update': 'lastUpdate',
        'state': 'state',
        'status': 'status'
    }

    def __init__(self, type=None, name=None, host=None, version=None, os_type=None, desired_state=None, message=None, last_update=None, state=None, status=None):  # noqa: E501
        """CtmService - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._name = None
        self._host = None
        self._version = None
        self._os_type = None
        self._desired_state = None
        self._message = None
        self._last_update = None
        self._state = None
        self._status = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if host is not None:
            self.host = host
        if version is not None:
            self.version = version
        if os_type is not None:
            self.os_type = os_type
        if desired_state is not None:
            self.desired_state = desired_state
        if message is not None:
            self.message = message
        if last_update is not None:
            self.last_update = last_update
        if state is not None:
            self.state = state
        if status is not None:
            self.status = status

    @property
    def type(self):
        """Gets the type of this CtmService.  # noqa: E501

        Service extension type  # noqa: E501

        :return: The type of this CtmService.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CtmService.

        Service extension type  # noqa: E501

        :param type: The type of this CtmService.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this CtmService.  # noqa: E501

        Service Name  # noqa: E501

        :return: The name of this CtmService.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CtmService.

        Service Name  # noqa: E501

        :param name: The name of this CtmService.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def host(self):
        """Gets the host of this CtmService.  # noqa: E501

        Service Host  # noqa: E501

        :return: The host of this CtmService.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this CtmService.

        Service Host  # noqa: E501

        :param host: The host of this CtmService.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def version(self):
        """Gets the version of this CtmService.  # noqa: E501

        Service version  # noqa: E501

        :return: The version of this CtmService.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CtmService.

        Service version  # noqa: E501

        :param version: The version of this CtmService.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def os_type(self):
        """Gets the os_type of this CtmService.  # noqa: E501

        Service Operating System  # noqa: E501

        :return: The os_type of this CtmService.  # noqa: E501
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this CtmService.

        Service Operating System  # noqa: E501

        :param os_type: The os_type of this CtmService.  # noqa: E501
        :type: str
        """

        self._os_type = os_type

    @property
    def desired_state(self):
        """Gets the desired_state of this CtmService.  # noqa: E501

        Service desired state  # noqa: E501

        :return: The desired_state of this CtmService.  # noqa: E501
        :rtype: str
        """
        return self._desired_state

    @desired_state.setter
    def desired_state(self, desired_state):
        """Sets the desired_state of this CtmService.

        Service desired state  # noqa: E501

        :param desired_state: The desired_state of this CtmService.  # noqa: E501
        :type: str
        """

        self._desired_state = desired_state

    @property
    def message(self):
        """Gets the message of this CtmService.  # noqa: E501

        Service status message  # noqa: E501

        :return: The message of this CtmService.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CtmService.

        Service status message  # noqa: E501

        :param message: The message of this CtmService.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def last_update(self):
        """Gets the last_update of this CtmService.  # noqa: E501

        Service LastUpdated  # noqa: E501

        :return: The last_update of this CtmService.  # noqa: E501
        :rtype: str
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this CtmService.

        Service LastUpdated  # noqa: E501

        :param last_update: The last_update of this CtmService.  # noqa: E501
        :type: str
        """

        self._last_update = last_update

    @property
    def state(self):
        """Gets the state of this CtmService.  # noqa: E501

        Service state  # noqa: E501

        :return: The state of this CtmService.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CtmService.

        Service state  # noqa: E501

        :param state: The state of this CtmService.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def status(self):
        """Gets the status of this CtmService.  # noqa: E501

        Service Status  # noqa: E501

        :return: The status of this CtmService.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CtmService.

        Service Status  # noqa: E501

        :param status: The status of this CtmService.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(CtmService, dict):
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
        if not isinstance(other, CtmService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
