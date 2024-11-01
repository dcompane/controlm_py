# coding: utf-8

"""
    Control-M Services

    Provides access to BMC Control-M Services  # noqa: E501

    OpenAPI spec version: 9.21.325
    Contact: customer_support@bmc.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from controlm_py.models.job_run_status import JobRunStatus  # noqa: F401,E501

class Job(JobRunStatus):
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
        'duration': 'int',
        'run_as': 'str',
        'archive_rule': 'str'
    }
    if hasattr(JobRunStatus, "swagger_types"):
        swagger_types.update(JobRunStatus.swagger_types)

    attribute_map = {
        'duration': 'duration',
        'run_as': 'runAs',
        'archive_rule': 'archiveRule'
    }
    if hasattr(JobRunStatus, "attribute_map"):
        attribute_map.update(JobRunStatus.attribute_map)

    def __init__(self, duration=None, run_as=None, archive_rule=None, *args, **kwargs):  # noqa: E501
        """Job - a model defined in Swagger"""  # noqa: E501
        self._duration = None
        self._run_as = None
        self._archive_rule = None
        self.discriminator = None
        if duration is not None:
            self.duration = duration
        if run_as is not None:
            self.run_as = run_as
        if archive_rule is not None:
            self.archive_rule = archive_rule
        JobRunStatus.__init__(self, *args, **kwargs)

    @property
    def duration(self):
        """Gets the duration of this Job.  # noqa: E501


        :return: The duration of this Job.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Job.


        :param duration: The duration of this Job.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def run_as(self):
        """Gets the run_as of this Job.  # noqa: E501


        :return: The run_as of this Job.  # noqa: E501
        :rtype: str
        """
        return self._run_as

    @run_as.setter
    def run_as(self, run_as):
        """Sets the run_as of this Job.


        :param run_as: The run_as of this Job.  # noqa: E501
        :type: str
        """

        self._run_as = run_as

    @property
    def archive_rule(self):
        """Gets the archive_rule of this Job.  # noqa: E501


        :return: The archive_rule of this Job.  # noqa: E501
        :rtype: str
        """
        return self._archive_rule

    @archive_rule.setter
    def archive_rule(self, archive_rule):
        """Sets the archive_rule of this Job.


        :param archive_rule: The archive_rule of this Job.  # noqa: E501
        :type: str
        """

        self._archive_rule = archive_rule

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
        if issubclass(Job, dict):
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
        if not isinstance(other, Job):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
