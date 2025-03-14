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

class JobView(object):
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
        'application': 'str',
        'cyclic': 'str',
        'description': 'str',
        'from_time': 'str',
        'group_name': 'str',
        'interval': 'str',
        'mem_lib': 'str',
        'memname': 'str',
        'nodegroup': 'str',
        'task_type': 'str',
        'to_time': 'str',
        'year': 'list[Year]'
    }

    attribute_map = {
        'application': 'application',
        'cyclic': 'cyclic',
        'description': 'description',
        'from_time': 'from_time',
        'group_name': 'group_name',
        'interval': 'interval',
        'mem_lib': 'mem_lib',
        'memname': 'memname',
        'nodegroup': 'nodegroup',
        'task_type': 'task_type',
        'to_time': 'to_time',
        'year': 'year'
    }

    def __init__(self, application=None, cyclic=None, description=None, from_time=None, group_name=None, interval=None, mem_lib=None, memname=None, nodegroup=None, task_type=None, to_time=None, year=None):  # noqa: E501
        """JobView - a model defined in Swagger"""  # noqa: E501
        self._application = None
        self._cyclic = None
        self._description = None
        self._from_time = None
        self._group_name = None
        self._interval = None
        self._mem_lib = None
        self._memname = None
        self._nodegroup = None
        self._task_type = None
        self._to_time = None
        self._year = None
        self.discriminator = None
        if application is not None:
            self.application = application
        if cyclic is not None:
            self.cyclic = cyclic
        if description is not None:
            self.description = description
        if from_time is not None:
            self.from_time = from_time
        if group_name is not None:
            self.group_name = group_name
        if interval is not None:
            self.interval = interval
        if mem_lib is not None:
            self.mem_lib = mem_lib
        if memname is not None:
            self.memname = memname
        if nodegroup is not None:
            self.nodegroup = nodegroup
        if task_type is not None:
            self.task_type = task_type
        if to_time is not None:
            self.to_time = to_time
        if year is not None:
            self.year = year

    @property
    def application(self):
        """Gets the application of this JobView.  # noqa: E501


        :return: The application of this JobView.  # noqa: E501
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this JobView.


        :param application: The application of this JobView.  # noqa: E501
        :type: str
        """

        self._application = application

    @property
    def cyclic(self):
        """Gets the cyclic of this JobView.  # noqa: E501


        :return: The cyclic of this JobView.  # noqa: E501
        :rtype: str
        """
        return self._cyclic

    @cyclic.setter
    def cyclic(self, cyclic):
        """Sets the cyclic of this JobView.


        :param cyclic: The cyclic of this JobView.  # noqa: E501
        :type: str
        """

        self._cyclic = cyclic

    @property
    def description(self):
        """Gets the description of this JobView.  # noqa: E501


        :return: The description of this JobView.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JobView.


        :param description: The description of this JobView.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def from_time(self):
        """Gets the from_time of this JobView.  # noqa: E501


        :return: The from_time of this JobView.  # noqa: E501
        :rtype: str
        """
        return self._from_time

    @from_time.setter
    def from_time(self, from_time):
        """Sets the from_time of this JobView.


        :param from_time: The from_time of this JobView.  # noqa: E501
        :type: str
        """

        self._from_time = from_time

    @property
    def group_name(self):
        """Gets the group_name of this JobView.  # noqa: E501


        :return: The group_name of this JobView.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this JobView.


        :param group_name: The group_name of this JobView.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def interval(self):
        """Gets the interval of this JobView.  # noqa: E501


        :return: The interval of this JobView.  # noqa: E501
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this JobView.


        :param interval: The interval of this JobView.  # noqa: E501
        :type: str
        """

        self._interval = interval

    @property
    def mem_lib(self):
        """Gets the mem_lib of this JobView.  # noqa: E501


        :return: The mem_lib of this JobView.  # noqa: E501
        :rtype: str
        """
        return self._mem_lib

    @mem_lib.setter
    def mem_lib(self, mem_lib):
        """Sets the mem_lib of this JobView.


        :param mem_lib: The mem_lib of this JobView.  # noqa: E501
        :type: str
        """

        self._mem_lib = mem_lib

    @property
    def memname(self):
        """Gets the memname of this JobView.  # noqa: E501


        :return: The memname of this JobView.  # noqa: E501
        :rtype: str
        """
        return self._memname

    @memname.setter
    def memname(self, memname):
        """Sets the memname of this JobView.


        :param memname: The memname of this JobView.  # noqa: E501
        :type: str
        """

        self._memname = memname

    @property
    def nodegroup(self):
        """Gets the nodegroup of this JobView.  # noqa: E501


        :return: The nodegroup of this JobView.  # noqa: E501
        :rtype: str
        """
        return self._nodegroup

    @nodegroup.setter
    def nodegroup(self, nodegroup):
        """Sets the nodegroup of this JobView.


        :param nodegroup: The nodegroup of this JobView.  # noqa: E501
        :type: str
        """

        self._nodegroup = nodegroup

    @property
    def task_type(self):
        """Gets the task_type of this JobView.  # noqa: E501


        :return: The task_type of this JobView.  # noqa: E501
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this JobView.


        :param task_type: The task_type of this JobView.  # noqa: E501
        :type: str
        """

        self._task_type = task_type

    @property
    def to_time(self):
        """Gets the to_time of this JobView.  # noqa: E501


        :return: The to_time of this JobView.  # noqa: E501
        :rtype: str
        """
        return self._to_time

    @to_time.setter
    def to_time(self, to_time):
        """Sets the to_time of this JobView.


        :param to_time: The to_time of this JobView.  # noqa: E501
        :type: str
        """

        self._to_time = to_time

    @property
    def year(self):
        """Gets the year of this JobView.  # noqa: E501


        :return: The year of this JobView.  # noqa: E501
        :rtype: list[Year]
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this JobView.


        :param year: The year of this JobView.  # noqa: E501
        :type: list[Year]
        """

        self._year = year

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
        if issubclass(JobView, dict):
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
        if not isinstance(other, JobView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
