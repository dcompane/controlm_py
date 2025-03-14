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

class JobSchedulingPlan(object):
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
        'calculation_status': 'str',
        'job_name': 'str',
        'job_order': 'str',
        'job_order_info': 'JobOrderInfo',
        'job_view': 'JobView',
        'messages': 'list[str]',
        'parent_table': 'str'
    }

    attribute_map = {
        'calculation_status': 'calculation_status',
        'job_name': 'job_name',
        'job_order': 'job_order',
        'job_order_info': 'job_order_info',
        'job_view': 'job_view',
        'messages': 'messages',
        'parent_table': 'parent_table'
    }

    def __init__(self, calculation_status=None, job_name=None, job_order=None, job_order_info=None, job_view=None, messages=None, parent_table=None):  # noqa: E501
        """JobSchedulingPlan - a model defined in Swagger"""  # noqa: E501
        self._calculation_status = None
        self._job_name = None
        self._job_order = None
        self._job_order_info = None
        self._job_view = None
        self._messages = None
        self._parent_table = None
        self.discriminator = None
        if calculation_status is not None:
            self.calculation_status = calculation_status
        if job_name is not None:
            self.job_name = job_name
        if job_order is not None:
            self.job_order = job_order
        if job_order_info is not None:
            self.job_order_info = job_order_info
        if job_view is not None:
            self.job_view = job_view
        if messages is not None:
            self.messages = messages
        if parent_table is not None:
            self.parent_table = parent_table

    @property
    def calculation_status(self):
        """Gets the calculation_status of this JobSchedulingPlan.  # noqa: E501


        :return: The calculation_status of this JobSchedulingPlan.  # noqa: E501
        :rtype: str
        """
        return self._calculation_status

    @calculation_status.setter
    def calculation_status(self, calculation_status):
        """Sets the calculation_status of this JobSchedulingPlan.


        :param calculation_status: The calculation_status of this JobSchedulingPlan.  # noqa: E501
        :type: str
        """
        allowed_values = ["SUCCESS", "ERROR", "UNRECOGNIZED"]  # noqa: E501
        if calculation_status not in allowed_values:
            raise ValueError(
                "Invalid value for `calculation_status` ({0}), must be one of {1}"  # noqa: E501
                .format(calculation_status, allowed_values)
            )

        self._calculation_status = calculation_status

    @property
    def job_name(self):
        """Gets the job_name of this JobSchedulingPlan.  # noqa: E501


        :return: The job_name of this JobSchedulingPlan.  # noqa: E501
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this JobSchedulingPlan.


        :param job_name: The job_name of this JobSchedulingPlan.  # noqa: E501
        :type: str
        """

        self._job_name = job_name

    @property
    def job_order(self):
        """Gets the job_order of this JobSchedulingPlan.  # noqa: E501


        :return: The job_order of this JobSchedulingPlan.  # noqa: E501
        :rtype: str
        """
        return self._job_order

    @job_order.setter
    def job_order(self, job_order):
        """Sets the job_order of this JobSchedulingPlan.


        :param job_order: The job_order of this JobSchedulingPlan.  # noqa: E501
        :type: str
        """

        self._job_order = job_order

    @property
    def job_order_info(self):
        """Gets the job_order_info of this JobSchedulingPlan.  # noqa: E501


        :return: The job_order_info of this JobSchedulingPlan.  # noqa: E501
        :rtype: JobOrderInfo
        """
        return self._job_order_info

    @job_order_info.setter
    def job_order_info(self, job_order_info):
        """Sets the job_order_info of this JobSchedulingPlan.


        :param job_order_info: The job_order_info of this JobSchedulingPlan.  # noqa: E501
        :type: JobOrderInfo
        """

        self._job_order_info = job_order_info

    @property
    def job_view(self):
        """Gets the job_view of this JobSchedulingPlan.  # noqa: E501


        :return: The job_view of this JobSchedulingPlan.  # noqa: E501
        :rtype: JobView
        """
        return self._job_view

    @job_view.setter
    def job_view(self, job_view):
        """Sets the job_view of this JobSchedulingPlan.


        :param job_view: The job_view of this JobSchedulingPlan.  # noqa: E501
        :type: JobView
        """

        self._job_view = job_view

    @property
    def messages(self):
        """Gets the messages of this JobSchedulingPlan.  # noqa: E501


        :return: The messages of this JobSchedulingPlan.  # noqa: E501
        :rtype: list[str]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this JobSchedulingPlan.


        :param messages: The messages of this JobSchedulingPlan.  # noqa: E501
        :type: list[str]
        """

        self._messages = messages

    @property
    def parent_table(self):
        """Gets the parent_table of this JobSchedulingPlan.  # noqa: E501


        :return: The parent_table of this JobSchedulingPlan.  # noqa: E501
        :rtype: str
        """
        return self._parent_table

    @parent_table.setter
    def parent_table(self, parent_table):
        """Sets the parent_table of this JobSchedulingPlan.


        :param parent_table: The parent_table of this JobSchedulingPlan.  # noqa: E501
        :type: str
        """

        self._parent_table = parent_table

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
        if issubclass(JobSchedulingPlan, dict):
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
        if not isinstance(other, JobSchedulingPlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
