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

class UnOrderedJobsList(object):
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
        'folder_name': 'str',
        'job_name': 'str'
    }

    attribute_map = {
        'folder_name': 'folderName',
        'job_name': 'jobName'
    }

    def __init__(self, folder_name=None, job_name=None):  # noqa: E501
        """UnOrderedJobsList - a model defined in Swagger"""  # noqa: E501
        self._folder_name = None
        self._job_name = None
        self.discriminator = None
        if folder_name is not None:
            self.folder_name = folder_name
        if job_name is not None:
            self.job_name = job_name

    @property
    def folder_name(self):
        """Gets the folder_name of this UnOrderedJobsList.  # noqa: E501


        :return: The folder_name of this UnOrderedJobsList.  # noqa: E501
        :rtype: str
        """
        return self._folder_name

    @folder_name.setter
    def folder_name(self, folder_name):
        """Sets the folder_name of this UnOrderedJobsList.


        :param folder_name: The folder_name of this UnOrderedJobsList.  # noqa: E501
        :type: str
        """

        self._folder_name = folder_name

    @property
    def job_name(self):
        """Gets the job_name of this UnOrderedJobsList.  # noqa: E501


        :return: The job_name of this UnOrderedJobsList.  # noqa: E501
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this UnOrderedJobsList.


        :param job_name: The job_name of this UnOrderedJobsList.  # noqa: E501
        :type: str
        """

        self._job_name = job_name

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
        if issubclass(UnOrderedJobsList, dict):
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
        if not isinstance(other, UnOrderedJobsList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other