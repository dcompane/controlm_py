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

class GatewayDetails(object):
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
        'current_state': 'str',
        'desired_state': 'str',
        'status': 'str',
        'message': 'str',
        'host': 'str',
        'name': 'str',
        'port': 'int',
        'os_type': 'str',
        'check_interval': 'str',
        'invoke_command': 'str',
        'additional_parameters': 'str'
    }

    attribute_map = {
        'current_state': 'currentState',
        'desired_state': 'desiredState',
        'status': 'status',
        'message': 'message',
        'host': 'host',
        'name': 'name',
        'port': 'port',
        'os_type': 'osType',
        'check_interval': 'checkInterval',
        'invoke_command': 'invokeCommand',
        'additional_parameters': 'additionalParameters'
    }

    def __init__(self, current_state=None, desired_state=None, status=None, message=None, host=None, name=None, port=None, os_type=None, check_interval=None, invoke_command=None, additional_parameters=None):  # noqa: E501
        """GatewayDetails - a model defined in Swagger"""  # noqa: E501
        self._current_state = None
        self._desired_state = None
        self._status = None
        self._message = None
        self._host = None
        self._name = None
        self._port = None
        self._os_type = None
        self._check_interval = None
        self._invoke_command = None
        self._additional_parameters = None
        self.discriminator = None
        if current_state is not None:
            self.current_state = current_state
        if desired_state is not None:
            self.desired_state = desired_state
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if host is not None:
            self.host = host
        if name is not None:
            self.name = name
        if port is not None:
            self.port = port
        if os_type is not None:
            self.os_type = os_type
        if check_interval is not None:
            self.check_interval = check_interval
        if invoke_command is not None:
            self.invoke_command = invoke_command
        if additional_parameters is not None:
            self.additional_parameters = additional_parameters

    @property
    def current_state(self):
        """Gets the current_state of this GatewayDetails.  # noqa: E501

        Current State of this gateway (Up, Down)  # noqa: E501

        :return: The current_state of this GatewayDetails.  # noqa: E501
        :rtype: str
        """
        return self._current_state

    @current_state.setter
    def current_state(self, current_state):
        """Sets the current_state of this GatewayDetails.

        Current State of this gateway (Up, Down)  # noqa: E501

        :param current_state: The current_state of this GatewayDetails.  # noqa: E501
        :type: str
        """

        self._current_state = current_state

    @property
    def desired_state(self):
        """Gets the desired_state of this GatewayDetails.  # noqa: E501

        Desired State of this gateway (Up, Down, Recycle, Ignored)  # noqa: E501

        :return: The desired_state of this GatewayDetails.  # noqa: E501
        :rtype: str
        """
        return self._desired_state

    @desired_state.setter
    def desired_state(self, desired_state):
        """Sets the desired_state of this GatewayDetails.

        Desired State of this gateway (Up, Down, Recycle, Ignored)  # noqa: E501

        :param desired_state: The desired_state of this GatewayDetails.  # noqa: E501
        :type: str
        """

        self._desired_state = desired_state

    @property
    def status(self):
        """Gets the status of this GatewayDetails.  # noqa: E501


        :return: The status of this GatewayDetails.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GatewayDetails.


        :param status: The status of this GatewayDetails.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def message(self):
        """Gets the message of this GatewayDetails.  # noqa: E501


        :return: The message of this GatewayDetails.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this GatewayDetails.


        :param message: The message of this GatewayDetails.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def host(self):
        """Gets the host of this GatewayDetails.  # noqa: E501

        Gateway host  # noqa: E501

        :return: The host of this GatewayDetails.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this GatewayDetails.

        Gateway host  # noqa: E501

        :param host: The host of this GatewayDetails.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def name(self):
        """Gets the name of this GatewayDetails.  # noqa: E501

        Gateway name  # noqa: E501

        :return: The name of this GatewayDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GatewayDetails.

        Gateway name  # noqa: E501

        :param name: The name of this GatewayDetails.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def port(self):
        """Gets the port of this GatewayDetails.  # noqa: E501

        Gateway listen port  # noqa: E501

        :return: The port of this GatewayDetails.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this GatewayDetails.

        Gateway listen port  # noqa: E501

        :param port: The port of this GatewayDetails.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def os_type(self):
        """Gets the os_type of this GatewayDetails.  # noqa: E501

        Operating System of this gateway. Unix is being set by default for distributed and for z/os  # noqa: E501

        :return: The os_type of this GatewayDetails.  # noqa: E501
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this GatewayDetails.

        Operating System of this gateway. Unix is being set by default for distributed and for z/os  # noqa: E501

        :param os_type: The os_type of this GatewayDetails.  # noqa: E501
        :type: str
        """

        self._os_type = os_type

    @property
    def check_interval(self):
        """Gets the check_interval of this GatewayDetails.  # noqa: E501

        Check interval time  # noqa: E501

        :return: The check_interval of this GatewayDetails.  # noqa: E501
        :rtype: str
        """
        return self._check_interval

    @check_interval.setter
    def check_interval(self, check_interval):
        """Sets the check_interval of this GatewayDetails.

        Check interval time  # noqa: E501

        :param check_interval: The check_interval of this GatewayDetails.  # noqa: E501
        :type: str
        """

        self._check_interval = check_interval

    @property
    def invoke_command(self):
        """Gets the invoke_command of this GatewayDetails.  # noqa: E501


        :return: The invoke_command of this GatewayDetails.  # noqa: E501
        :rtype: str
        """
        return self._invoke_command

    @invoke_command.setter
    def invoke_command(self, invoke_command):
        """Sets the invoke_command of this GatewayDetails.


        :param invoke_command: The invoke_command of this GatewayDetails.  # noqa: E501
        :type: str
        """

        self._invoke_command = invoke_command

    @property
    def additional_parameters(self):
        """Gets the additional_parameters of this GatewayDetails.  # noqa: E501

        optional  # noqa: E501

        :return: The additional_parameters of this GatewayDetails.  # noqa: E501
        :rtype: str
        """
        return self._additional_parameters

    @additional_parameters.setter
    def additional_parameters(self, additional_parameters):
        """Sets the additional_parameters of this GatewayDetails.

        optional  # noqa: E501

        :param additional_parameters: The additional_parameters of this GatewayDetails.  # noqa: E501
        :type: str
        """

        self._additional_parameters = additional_parameters

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
        if issubclass(GatewayDetails, dict):
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
        if not isinstance(other, GatewayDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
