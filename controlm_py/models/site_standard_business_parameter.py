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

class SiteStandardBusinessParameter(object):
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
        'parameter_name': 'str',
        'restriction': 'SiteStandardRestriction',
        'validation_error_message': 'str'
    }

    attribute_map = {
        'parameter_name': 'parameterName',
        'restriction': 'restriction',
        'validation_error_message': 'validationErrorMessage'
    }

    def __init__(self, parameter_name=None, restriction=None, validation_error_message=None):  # noqa: E501
        """SiteStandardBusinessParameter - a model defined in Swagger"""  # noqa: E501
        self._parameter_name = None
        self._restriction = None
        self._validation_error_message = None
        self.discriminator = None
        self.parameter_name = parameter_name
        if restriction is not None:
            self.restriction = restriction
        if validation_error_message is not None:
            self.validation_error_message = validation_error_message

    @property
    def parameter_name(self):
        """Gets the parameter_name of this SiteStandardBusinessParameter.  # noqa: E501


        :return: The parameter_name of this SiteStandardBusinessParameter.  # noqa: E501
        :rtype: str
        """
        return self._parameter_name

    @parameter_name.setter
    def parameter_name(self, parameter_name):
        """Sets the parameter_name of this SiteStandardBusinessParameter.


        :param parameter_name: The parameter_name of this SiteStandardBusinessParameter.  # noqa: E501
        :type: str
        """
        if parameter_name is None:
            raise ValueError("Invalid value for `parameter_name`, must not be `None`")  # noqa: E501

        self._parameter_name = parameter_name

    @property
    def restriction(self):
        """Gets the restriction of this SiteStandardBusinessParameter.  # noqa: E501


        :return: The restriction of this SiteStandardBusinessParameter.  # noqa: E501
        :rtype: SiteStandardRestriction
        """
        return self._restriction

    @restriction.setter
    def restriction(self, restriction):
        """Sets the restriction of this SiteStandardBusinessParameter.


        :param restriction: The restriction of this SiteStandardBusinessParameter.  # noqa: E501
        :type: SiteStandardRestriction
        """

        self._restriction = restriction

    @property
    def validation_error_message(self):
        """Gets the validation_error_message of this SiteStandardBusinessParameter.  # noqa: E501

        The validation error message to show the user when this parameter is invalid.<br> If not specified, the default error message will be used.  # noqa: E501

        :return: The validation_error_message of this SiteStandardBusinessParameter.  # noqa: E501
        :rtype: str
        """
        return self._validation_error_message

    @validation_error_message.setter
    def validation_error_message(self, validation_error_message):
        """Sets the validation_error_message of this SiteStandardBusinessParameter.

        The validation error message to show the user when this parameter is invalid.<br> If not specified, the default error message will be used.  # noqa: E501

        :param validation_error_message: The validation_error_message of this SiteStandardBusinessParameter.  # noqa: E501
        :type: str
        """

        self._validation_error_message = validation_error_message

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
        if issubclass(SiteStandardBusinessParameter, dict):
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
        if not isinstance(other, SiteStandardBusinessParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
