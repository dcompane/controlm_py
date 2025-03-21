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

class EmComponentDesiredState(object):
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
        'type': 'str',
        'name': 'str',
        'desired_state': 'str',
        'extension': 'str'
    }

    attribute_map = {
        'host': 'host',
        'type': 'type',
        'name': 'name',
        'desired_state': 'desiredState',
        'extension': 'extension'
    }

    def __init__(self, host=None, type=None, name=None, desired_state=None, extension=None):  # noqa: E501
        """EmComponentDesiredState - a model defined in Swagger"""  # noqa: E501
        self._host = None
        self._type = None
        self._name = None
        self._desired_state = None
        self._extension = None
        self.discriminator = None
        self.host = host
        self.type = type
        self.name = name
        self.desired_state = desired_state
        if extension is not None:
            self.extension = extension

    @property
    def host(self):
        """Gets the host of this EmComponentDesiredState.  # noqa: E501

        The hostname of the server where the EM component is running.  # noqa: E501

        :return: The host of this EmComponentDesiredState.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this EmComponentDesiredState.

        The hostname of the server where the EM component is running.  # noqa: E501

        :param host: The host of this EmComponentDesiredState.  # noqa: E501
        :type: str
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def type(self):
        """Gets the type of this EmComponentDesiredState.  # noqa: E501

        The type of the EM component (e.g., Gateway, GUI_Server, ARCHIVE).  # noqa: E501

        :return: The type of this EmComponentDesiredState.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EmComponentDesiredState.

        The type of the EM component (e.g., Gateway, GUI_Server, ARCHIVE).  # noqa: E501

        :param type: The type of this EmComponentDesiredState.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this EmComponentDesiredState.  # noqa: E501

        The logical name of the EM component.  # noqa: E501

        :return: The name of this EmComponentDesiredState.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EmComponentDesiredState.

        The logical name of the EM component.  # noqa: E501

        :param name: The name of this EmComponentDesiredState.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def desired_state(self):
        """Gets the desired_state of this EmComponentDesiredState.  # noqa: E501

        The desired operational state of the EM component (Up, Down, Ignored, Recycle).  # noqa: E501

        :return: The desired_state of this EmComponentDesiredState.  # noqa: E501
        :rtype: str
        """
        return self._desired_state

    @desired_state.setter
    def desired_state(self, desired_state):
        """Sets the desired_state of this EmComponentDesiredState.

        The desired operational state of the EM component (Up, Down, Ignored, Recycle).  # noqa: E501

        :param desired_state: The desired_state of this EmComponentDesiredState.  # noqa: E501
        :type: str
        """
        if desired_state is None:
            raise ValueError("Invalid value for `desired_state`, must not be `None`")  # noqa: E501

        self._desired_state = desired_state

    @property
    def extension(self):
        """Gets the extension of this EmComponentDesiredState.  # noqa: E501

        The service extension type  # noqa: E501

        :return: The extension of this EmComponentDesiredState.  # noqa: E501
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this EmComponentDesiredState.

        The service extension type  # noqa: E501

        :param extension: The extension of this EmComponentDesiredState.  # noqa: E501
        :type: str
        """

        self._extension = extension

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
        if issubclass(EmComponentDesiredState, dict):
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
        if not isinstance(other, EmComponentDesiredState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
