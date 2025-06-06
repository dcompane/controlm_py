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

class AlertStatusParam(object):
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
        'alert_ids': 'list[int]',
        'status': 'str'
    }

    attribute_map = {
        'alert_ids': 'alertIds',
        'status': 'status'
    }

    def __init__(self, alert_ids=None, status=None):  # noqa: E501
        """AlertStatusParam - a model defined in Swagger"""  # noqa: E501
        self._alert_ids = None
        self._status = None
        self.discriminator = None
        self.alert_ids = alert_ids
        if status is not None:
            self.status = status

    @property
    def alert_ids(self):
        """Gets the alert_ids of this AlertStatusParam.  # noqa: E501

        alertIds. HIDDEN.  # noqa: E501

        :return: The alert_ids of this AlertStatusParam.  # noqa: E501
        :rtype: list[int]
        """
        return self._alert_ids

    @alert_ids.setter
    def alert_ids(self, alert_ids):
        """Sets the alert_ids of this AlertStatusParam.

        alertIds. HIDDEN.  # noqa: E501

        :param alert_ids: The alert_ids of this AlertStatusParam.  # noqa: E501
        :type: list[int]
        """
        if alert_ids is None:
            raise ValueError("Invalid value for `alert_ids`, must not be `None`")  # noqa: E501

        self._alert_ids = alert_ids

    @property
    def status(self):
        """Gets the status of this AlertStatusParam.  # noqa: E501

        modify status. HIDDEN.  # noqa: E501

        :return: The status of this AlertStatusParam.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AlertStatusParam.

        modify status. HIDDEN.  # noqa: E501

        :param status: The status of this AlertStatusParam.  # noqa: E501
        :type: str
        """
        allowed_values = ["Undefined", "Reviewed", "Closed", "New"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

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
        if issubclass(AlertStatusParam, dict):
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
        if not isinstance(other, AlertStatusParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
