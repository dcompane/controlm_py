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

class CtlRequestParams(object):
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
        'ctype': 'str',
        'host': 'str',
        'command': 'str',
        'em': 'bool',
        'extension': 'str'
    }

    attribute_map = {
        'ctype': 'ctype',
        'host': 'host',
        'command': 'command',
        'em': 'em',
        'extension': 'extension'
    }

    def __init__(self, ctype=None, host=None, command=None, em=None, extension=None):  # noqa: E501
        """CtlRequestParams - a model defined in Swagger"""  # noqa: E501
        self._ctype = None
        self._host = None
        self._command = None
        self._em = None
        self._extension = None
        self.discriminator = None
        self.ctype = ctype
        self.host = host
        self.command = command
        self.em = em
        if extension is not None:
            self.extension = extension

    @property
    def ctype(self):
        """Gets the ctype of this CtlRequestParams.  # noqa: E501

        Component type  # noqa: E501

        :return: The ctype of this CtlRequestParams.  # noqa: E501
        :rtype: str
        """
        return self._ctype

    @ctype.setter
    def ctype(self, ctype):
        """Sets the ctype of this CtlRequestParams.

        Component type  # noqa: E501

        :param ctype: The ctype of this CtlRequestParams.  # noqa: E501
        :type: str
        """
        if ctype is None:
            raise ValueError("Invalid value for `ctype`, must not be `None`")  # noqa: E501

        self._ctype = ctype

    @property
    def host(self):
        """Gets the host of this CtlRequestParams.  # noqa: E501

        Component host  # noqa: E501

        :return: The host of this CtlRequestParams.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this CtlRequestParams.

        Component host  # noqa: E501

        :param host: The host of this CtlRequestParams.  # noqa: E501
        :type: str
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def command(self):
        """Gets the command of this CtlRequestParams.  # noqa: E501

        Command to run  # noqa: E501

        :return: The command of this CtlRequestParams.  # noqa: E501
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this CtlRequestParams.

        Command to run  # noqa: E501

        :param command: The command of this CtlRequestParams.  # noqa: E501
        :type: str
        """
        if command is None:
            raise ValueError("Invalid value for `command`, must not be `None`")  # noqa: E501

        self._command = command

    @property
    def em(self):
        """Gets the em of this CtlRequestParams.  # noqa: E501

        true for EM false for Zos  # noqa: E501

        :return: The em of this CtlRequestParams.  # noqa: E501
        :rtype: bool
        """
        return self._em

    @em.setter
    def em(self, em):
        """Sets the em of this CtlRequestParams.

        true for EM false for Zos  # noqa: E501

        :param em: The em of this CtlRequestParams.  # noqa: E501
        :type: bool
        """
        if em is None:
            raise ValueError("Invalid value for `em`, must not be `None`")  # noqa: E501

        self._em = em

    @property
    def extension(self):
        """Gets the extension of this CtlRequestParams.  # noqa: E501

        Only used in case of Service  # noqa: E501

        :return: The extension of this CtlRequestParams.  # noqa: E501
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this CtlRequestParams.

        Only used in case of Service  # noqa: E501

        :param extension: The extension of this CtlRequestParams.  # noqa: E501
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
        if issubclass(CtlRequestParams, dict):
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
        if not isinstance(other, CtlRequestParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
