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

class JobLevelAuth(object):
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
        'privilege': 'str',
        'application': 'str',
        'sub_application': 'str'
    }

    attribute_map = {
        'privilege': 'Privilege',
        'application': 'Application',
        'sub_application': 'SubApplication'
    }

    def __init__(self, privilege=None, application=None, sub_application=None):  # noqa: E501
        """JobLevelAuth - a model defined in Swagger"""  # noqa: E501
        self._privilege = None
        self._application = None
        self._sub_application = None
        self.discriminator = None
        if privilege is not None:
            self.privilege = privilege
        if application is not None:
            self.application = application
        if sub_application is not None:
            self.sub_application = sub_application

    @property
    def privilege(self):
        """Gets the privilege of this JobLevelAuth.  # noqa: E501

        access level (Full, Update, Browse)  # noqa: E501

        :return: The privilege of this JobLevelAuth.  # noqa: E501
        :rtype: str
        """
        return self._privilege

    @privilege.setter
    def privilege(self, privilege):
        """Sets the privilege of this JobLevelAuth.

        access level (Full, Update, Browse)  # noqa: E501

        :param privilege: The privilege of this JobLevelAuth.  # noqa: E501
        :type: str
        """

        self._privilege = privilege

    @property
    def application(self):
        """Gets the application of this JobLevelAuth.  # noqa: E501

        job application  # noqa: E501

        :return: The application of this JobLevelAuth.  # noqa: E501
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this JobLevelAuth.

        job application  # noqa: E501

        :param application: The application of this JobLevelAuth.  # noqa: E501
        :type: str
        """

        self._application = application

    @property
    def sub_application(self):
        """Gets the sub_application of this JobLevelAuth.  # noqa: E501

        job sub application  # noqa: E501

        :return: The sub_application of this JobLevelAuth.  # noqa: E501
        :rtype: str
        """
        return self._sub_application

    @sub_application.setter
    def sub_application(self, sub_application):
        """Sets the sub_application of this JobLevelAuth.

        job sub application  # noqa: E501

        :param sub_application: The sub_application of this JobLevelAuth.  # noqa: E501
        :type: str
        """

        self._sub_application = sub_application

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
        if issubclass(JobLevelAuth, dict):
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
        if not isinstance(other, JobLevelAuth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
