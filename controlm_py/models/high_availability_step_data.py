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

class HighAvailabilityStepData(object):
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
        'step_name': 'str',
        'step_title': 'str',
        'step_status': 'str',
        'step_start_time': 'str',
        'step_end_time': 'str',
        'step_message': 'str'
    }

    attribute_map = {
        'step_name': 'stepName',
        'step_title': 'stepTitle',
        'step_status': 'stepStatus',
        'step_start_time': 'stepStartTime',
        'step_end_time': 'stepEndTime',
        'step_message': 'stepMessage'
    }

    def __init__(self, step_name=None, step_title=None, step_status=None, step_start_time=None, step_end_time=None, step_message=None):  # noqa: E501
        """HighAvailabilityStepData - a model defined in Swagger"""  # noqa: E501
        self._step_name = None
        self._step_title = None
        self._step_status = None
        self._step_start_time = None
        self._step_end_time = None
        self._step_message = None
        self.discriminator = None
        if step_name is not None:
            self.step_name = step_name
        if step_title is not None:
            self.step_title = step_title
        if step_status is not None:
            self.step_status = step_status
        if step_start_time is not None:
            self.step_start_time = step_start_time
        if step_end_time is not None:
            self.step_end_time = step_end_time
        if step_message is not None:
            self.step_message = step_message

    @property
    def step_name(self):
        """Gets the step_name of this HighAvailabilityStepData.  # noqa: E501


        :return: The step_name of this HighAvailabilityStepData.  # noqa: E501
        :rtype: str
        """
        return self._step_name

    @step_name.setter
    def step_name(self, step_name):
        """Sets the step_name of this HighAvailabilityStepData.


        :param step_name: The step_name of this HighAvailabilityStepData.  # noqa: E501
        :type: str
        """

        self._step_name = step_name

    @property
    def step_title(self):
        """Gets the step_title of this HighAvailabilityStepData.  # noqa: E501


        :return: The step_title of this HighAvailabilityStepData.  # noqa: E501
        :rtype: str
        """
        return self._step_title

    @step_title.setter
    def step_title(self, step_title):
        """Sets the step_title of this HighAvailabilityStepData.


        :param step_title: The step_title of this HighAvailabilityStepData.  # noqa: E501
        :type: str
        """

        self._step_title = step_title

    @property
    def step_status(self):
        """Gets the step_status of this HighAvailabilityStepData.  # noqa: E501


        :return: The step_status of this HighAvailabilityStepData.  # noqa: E501
        :rtype: str
        """
        return self._step_status

    @step_status.setter
    def step_status(self, step_status):
        """Sets the step_status of this HighAvailabilityStepData.


        :param step_status: The step_status of this HighAvailabilityStepData.  # noqa: E501
        :type: str
        """

        self._step_status = step_status

    @property
    def step_start_time(self):
        """Gets the step_start_time of this HighAvailabilityStepData.  # noqa: E501


        :return: The step_start_time of this HighAvailabilityStepData.  # noqa: E501
        :rtype: str
        """
        return self._step_start_time

    @step_start_time.setter
    def step_start_time(self, step_start_time):
        """Sets the step_start_time of this HighAvailabilityStepData.


        :param step_start_time: The step_start_time of this HighAvailabilityStepData.  # noqa: E501
        :type: str
        """

        self._step_start_time = step_start_time

    @property
    def step_end_time(self):
        """Gets the step_end_time of this HighAvailabilityStepData.  # noqa: E501


        :return: The step_end_time of this HighAvailabilityStepData.  # noqa: E501
        :rtype: str
        """
        return self._step_end_time

    @step_end_time.setter
    def step_end_time(self, step_end_time):
        """Sets the step_end_time of this HighAvailabilityStepData.


        :param step_end_time: The step_end_time of this HighAvailabilityStepData.  # noqa: E501
        :type: str
        """

        self._step_end_time = step_end_time

    @property
    def step_message(self):
        """Gets the step_message of this HighAvailabilityStepData.  # noqa: E501


        :return: The step_message of this HighAvailabilityStepData.  # noqa: E501
        :rtype: str
        """
        return self._step_message

    @step_message.setter
    def step_message(self, step_message):
        """Sets the step_message of this HighAvailabilityStepData.


        :param step_message: The step_message of this HighAvailabilityStepData.  # noqa: E501
        :type: str
        """

        self._step_message = step_message

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
        if issubclass(HighAvailabilityStepData, dict):
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
        if not isinstance(other, HighAvailabilityStepData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
