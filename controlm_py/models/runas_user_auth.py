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

class RunasUserAuth(object):
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
        'controlm_server': 'str',
        'runas_user': 'str',
        'host': 'str'
    }

    attribute_map = {
        'controlm_server': 'ControlmServer',
        'runas_user': 'RunasUser',
        'host': 'Host'
    }

    def __init__(self, controlm_server=None, runas_user=None, host=None):  # noqa: E501
        """RunasUserAuth - a model defined in Swagger"""  # noqa: E501
        self._controlm_server = None
        self._runas_user = None
        self._host = None
        self.discriminator = None
        if controlm_server is not None:
            self.controlm_server = controlm_server
        if runas_user is not None:
            self.runas_user = runas_user
        if host is not None:
            self.host = host

    @property
    def controlm_server(self):
        """Gets the controlm_server of this RunasUserAuth.  # noqa: E501

        control-M server name  # noqa: E501

        :return: The controlm_server of this RunasUserAuth.  # noqa: E501
        :rtype: str
        """
        return self._controlm_server

    @controlm_server.setter
    def controlm_server(self, controlm_server):
        """Sets the controlm_server of this RunasUserAuth.

        control-M server name  # noqa: E501

        :param controlm_server: The controlm_server of this RunasUserAuth.  # noqa: E501
        :type: str
        """

        self._controlm_server = controlm_server

    @property
    def runas_user(self):
        """Gets the runas_user of this RunasUserAuth.  # noqa: E501

        runas user  # noqa: E501

        :return: The runas_user of this RunasUserAuth.  # noqa: E501
        :rtype: str
        """
        return self._runas_user

    @runas_user.setter
    def runas_user(self, runas_user):
        """Sets the runas_user of this RunasUserAuth.

        runas user  # noqa: E501

        :param runas_user: The runas_user of this RunasUserAuth.  # noqa: E501
        :type: str
        """

        self._runas_user = runas_user

    @property
    def host(self):
        """Gets the host of this RunasUserAuth.  # noqa: E501

        HOst or host group value  # noqa: E501

        :return: The host of this RunasUserAuth.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this RunasUserAuth.

        HOst or host group value  # noqa: E501

        :param host: The host of this RunasUserAuth.  # noqa: E501
        :type: str
        """

        self._host = host

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
        if issubclass(RunasUserAuth, dict):
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
        if not isinstance(other, RunasUserAuth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
