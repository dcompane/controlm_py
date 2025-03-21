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

class UserData(object):
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
        'description': 'str',
        'full_name': 'str',
        'authentication': 'AuthenticationData',
        'roles': 'list[str]',
        'authorization': 'RoleData'
    }

    attribute_map = {
        'name': 'Name',
        'description': 'Description',
        'full_name': 'FullName',
        'authentication': 'Authentication',
        'roles': 'Roles',
        'authorization': 'Authorization'
    }

    def __init__(self, name=None, description=None, full_name=None, authentication=None, roles=None, authorization=None):  # noqa: E501
        """UserData - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._full_name = None
        self._authentication = None
        self._roles = None
        self._authorization = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if full_name is not None:
            self.full_name = full_name
        if authentication is not None:
            self.authentication = authentication
        if roles is not None:
            self.roles = roles
        if authorization is not None:
            self.authorization = authorization

    @property
    def name(self):
        """Gets the name of this UserData.  # noqa: E501

        user name  # noqa: E501

        :return: The name of this UserData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserData.

        user name  # noqa: E501

        :param name: The name of this UserData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this UserData.  # noqa: E501

        user description  # noqa: E501

        :return: The description of this UserData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserData.

        user description  # noqa: E501

        :param description: The description of this UserData.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def full_name(self):
        """Gets the full_name of this UserData.  # noqa: E501

        full user name  # noqa: E501

        :return: The full_name of this UserData.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this UserData.

        full user name  # noqa: E501

        :param full_name: The full_name of this UserData.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def authentication(self):
        """Gets the authentication of this UserData.  # noqa: E501


        :return: The authentication of this UserData.  # noqa: E501
        :rtype: AuthenticationData
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this UserData.


        :param authentication: The authentication of this UserData.  # noqa: E501
        :type: AuthenticationData
        """

        self._authentication = authentication

    @property
    def roles(self):
        """Gets the roles of this UserData.  # noqa: E501


        :return: The roles of this UserData.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this UserData.


        :param roles: The roles of this UserData.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

    @property
    def authorization(self):
        """Gets the authorization of this UserData.  # noqa: E501


        :return: The authorization of this UserData.  # noqa: E501
        :rtype: RoleData
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this UserData.


        :param authorization: The authorization of this UserData.  # noqa: E501
        :type: RoleData
        """

        self._authorization = authorization

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
        if issubclass(UserData, dict):
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
        if not isinstance(other, UserData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
