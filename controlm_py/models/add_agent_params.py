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

class AddAgentParams(object):
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
        'host': 'str',
        'port': 'int',
        'tag': 'str',
        'ssl_state': 'str',
        'persistent_connection': 'bool',
        'timeout': 'int',
        'suppress_ping': 'bool',
        'agent_type': 'str'
    }

    attribute_map = {
        'host': 'host',
        'port': 'port',
        'tag': 'tag',
        'ssl_state': 'sslState',
        'persistent_connection': 'persistentConnection',
        'timeout': 'timeout',
        'suppress_ping': 'suppressPing',
        'agent_type': 'agentType'
    }

    def __init__(self, host=None, port=None, tag=None, ssl_state=None, persistent_connection=None, timeout=60, suppress_ping=False, agent_type=None):  # noqa: E501
        """AddAgentParams - a model defined in Swagger"""  # noqa: E501
        self._host = None
        self._port = None
        self._tag = None
        self._ssl_state = None
        self._persistent_connection = None
        self._timeout = None
        self._suppress_ping = None
        self._agent_type = None
        self.discriminator = None
        self.host = host
        self.port = port
        if tag is not None:
            self.tag = tag
        if ssl_state is not None:
            self.ssl_state = ssl_state
        if persistent_connection is not None:
            self.persistent_connection = persistent_connection
        if timeout is not None:
            self.timeout = timeout
        if suppress_ping is not None:
            self.suppress_ping = suppress_ping
        if agent_type is not None:
            self.agent_type = agent_type

    @property
    def host(self):
        """Gets the host of this AddAgentParams.  # noqa: E501

        The hostname or alias of the agent machine.  # noqa: E501

        :return: The host of this AddAgentParams.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this AddAgentParams.

        The hostname or alias of the agent machine.  # noqa: E501

        :param host: The host of this AddAgentParams.  # noqa: E501
        :type: str
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def port(self):
        """Gets the port of this AddAgentParams.  # noqa: E501

        The agent's listening port.  # noqa: E501

        :return: The port of this AddAgentParams.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this AddAgentParams.

        The agent's listening port.  # noqa: E501

        :param port: The port of this AddAgentParams.  # noqa: E501
        :type: int
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def tag(self):
        """Gets the tag of this AddAgentParams.  # noqa: E501

        The agent's tag.  # noqa: E501

        :return: The tag of this AddAgentParams.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this AddAgentParams.

        The agent's tag.  # noqa: E501

        :param tag: The tag of this AddAgentParams.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def ssl_state(self):
        """Gets the ssl_state of this AddAgentParams.  # noqa: E501

        The agent's ssl State. HIDDEN.  # noqa: E501

        :return: The ssl_state of this AddAgentParams.  # noqa: E501
        :rtype: str
        """
        return self._ssl_state

    @ssl_state.setter
    def ssl_state(self, ssl_state):
        """Sets the ssl_state of this AddAgentParams.

        The agent's ssl State. HIDDEN.  # noqa: E501

        :param ssl_state: The ssl_state of this AddAgentParams.  # noqa: E501
        :type: str
        """

        self._ssl_state = ssl_state

    @property
    def persistent_connection(self):
        """Gets the persistent_connection of this AddAgentParams.  # noqa: E501

        Is the connection persistent or create each time it is needed. HIDDEN.  # noqa: E501

        :return: The persistent_connection of this AddAgentParams.  # noqa: E501
        :rtype: bool
        """
        return self._persistent_connection

    @persistent_connection.setter
    def persistent_connection(self, persistent_connection):
        """Sets the persistent_connection of this AddAgentParams.

        Is the connection persistent or create each time it is needed. HIDDEN.  # noqa: E501

        :param persistent_connection: The persistent_connection of this AddAgentParams.  # noqa: E501
        :type: bool
        """

        self._persistent_connection = persistent_connection

    @property
    def timeout(self):
        """Gets the timeout of this AddAgentParams.  # noqa: E501

        maximum time in seconds to wait (default 60). HIDDEN  # noqa: E501

        :return: The timeout of this AddAgentParams.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this AddAgentParams.

        maximum time in seconds to wait (default 60). HIDDEN  # noqa: E501

        :param timeout: The timeout of this AddAgentParams.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    @property
    def suppress_ping(self):
        """Gets the suppress_ping of this AddAgentParams.  # noqa: E501

        Suppress ping action to added agent (default false). HIDDEN.  # noqa: E501

        :return: The suppress_ping of this AddAgentParams.  # noqa: E501
        :rtype: bool
        """
        return self._suppress_ping

    @suppress_ping.setter
    def suppress_ping(self, suppress_ping):
        """Sets the suppress_ping of this AddAgentParams.

        Suppress ping action to added agent (default false). HIDDEN.  # noqa: E501

        :param suppress_ping: The suppress_ping of this AddAgentParams.  # noqa: E501
        :type: bool
        """

        self._suppress_ping = suppress_ping

    @property
    def agent_type(self):
        """Gets the agent_type of this AddAgentParams.  # noqa: E501

        The agent's type.  # noqa: E501

        :return: The agent_type of this AddAgentParams.  # noqa: E501
        :rtype: str
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        """Sets the agent_type of this AddAgentParams.

        The agent's type.  # noqa: E501

        :param agent_type: The agent_type of this AddAgentParams.  # noqa: E501
        :type: str
        """

        self._agent_type = agent_type

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
        if issubclass(AddAgentParams, dict):
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
        if not isinstance(other, AddAgentParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
