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

class HostRestriction(object):
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
        'node_prefix': 'str',
        'max_jobs_allowed': 'str',
        'max_cpu_pct': 'str'
    }

    attribute_map = {
        'node_prefix': 'nodePrefix',
        'max_jobs_allowed': 'maxJobsAllowed',
        'max_cpu_pct': 'maxCPUPct'
    }

    def __init__(self, node_prefix=None, max_jobs_allowed=None, max_cpu_pct=None):  # noqa: E501
        """HostRestriction - a model defined in Swagger"""  # noqa: E501
        self._node_prefix = None
        self._max_jobs_allowed = None
        self._max_cpu_pct = None
        self.discriminator = None
        if node_prefix is not None:
            self.node_prefix = node_prefix
        if max_jobs_allowed is not None:
            self.max_jobs_allowed = max_jobs_allowed
        if max_cpu_pct is not None:
            self.max_cpu_pct = max_cpu_pct

    @property
    def node_prefix(self):
        """Gets the node_prefix of this HostRestriction.  # noqa: E501

        the host name . REQUIRED.  # noqa: E501

        :return: The node_prefix of this HostRestriction.  # noqa: E501
        :rtype: str
        """
        return self._node_prefix

    @node_prefix.setter
    def node_prefix(self, node_prefix):
        """Sets the node_prefix of this HostRestriction.

        the host name . REQUIRED.  # noqa: E501

        :param node_prefix: The node_prefix of this HostRestriction.  # noqa: E501
        :type: str
        """

        self._node_prefix = node_prefix

    @property
    def max_jobs_allowed(self):
        """Gets the max_jobs_allowed of this HostRestriction.  # noqa: E501

        the maximum level for concurrent jobs . [UNLIMITED/1-999,999] . REQUIRED.  # noqa: E501

        :return: The max_jobs_allowed of this HostRestriction.  # noqa: E501
        :rtype: str
        """
        return self._max_jobs_allowed

    @max_jobs_allowed.setter
    def max_jobs_allowed(self, max_jobs_allowed):
        """Sets the max_jobs_allowed of this HostRestriction.

        the maximum level for concurrent jobs . [UNLIMITED/1-999,999] . REQUIRED.  # noqa: E501

        :param max_jobs_allowed: The max_jobs_allowed of this HostRestriction.  # noqa: E501
        :type: str
        """

        self._max_jobs_allowed = max_jobs_allowed

    @property
    def max_cpu_pct(self):
        """Gets the max_cpu_pct of this HostRestriction.  # noqa: E501

        maximum level for CPU utilization. [UNLIMITED/1-100%] . REQUIRED.  # noqa: E501

        :return: The max_cpu_pct of this HostRestriction.  # noqa: E501
        :rtype: str
        """
        return self._max_cpu_pct

    @max_cpu_pct.setter
    def max_cpu_pct(self, max_cpu_pct):
        """Sets the max_cpu_pct of this HostRestriction.

        maximum level for CPU utilization. [UNLIMITED/1-100%] . REQUIRED.  # noqa: E501

        :param max_cpu_pct: The max_cpu_pct of this HostRestriction.  # noqa: E501
        :type: str
        """

        self._max_cpu_pct = max_cpu_pct

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
        if issubclass(HostRestriction, dict):
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
        if not isinstance(other, HostRestriction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other