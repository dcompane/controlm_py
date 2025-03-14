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

class ServiceAuthAction(object):
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
        'drill_down': 'bool',
        'run': 'bool',
        'hold': 'bool',
        'resume': 'bool',
        'view_orderable_service': 'bool'
    }

    attribute_map = {
        'drill_down': 'DrillDown',
        'run': 'Run',
        'hold': 'Hold',
        'resume': 'Resume',
        'view_orderable_service': 'ViewOrderableService'
    }

    def __init__(self, drill_down=None, run=None, hold=None, resume=None, view_orderable_service=None):  # noqa: E501
        """ServiceAuthAction - a model defined in Swagger"""  # noqa: E501
        self._drill_down = None
        self._run = None
        self._hold = None
        self._resume = None
        self._view_orderable_service = None
        self.discriminator = None
        if drill_down is not None:
            self.drill_down = drill_down
        if run is not None:
            self.run = run
        if hold is not None:
            self.hold = hold
        if resume is not None:
            self.resume = resume
        if view_orderable_service is not None:
            self.view_orderable_service = view_orderable_service

    @property
    def drill_down(self):
        """Gets the drill_down of this ServiceAuthAction.  # noqa: E501

        Is DrillDown allowed in service  # noqa: E501

        :return: The drill_down of this ServiceAuthAction.  # noqa: E501
        :rtype: bool
        """
        return self._drill_down

    @drill_down.setter
    def drill_down(self, drill_down):
        """Sets the drill_down of this ServiceAuthAction.

        Is DrillDown allowed in service  # noqa: E501

        :param drill_down: The drill_down of this ServiceAuthAction.  # noqa: E501
        :type: bool
        """

        self._drill_down = drill_down

    @property
    def run(self):
        """Gets the run of this ServiceAuthAction.  # noqa: E501

        Is Run allowed in service  # noqa: E501

        :return: The run of this ServiceAuthAction.  # noqa: E501
        :rtype: bool
        """
        return self._run

    @run.setter
    def run(self, run):
        """Sets the run of this ServiceAuthAction.

        Is Run allowed in service  # noqa: E501

        :param run: The run of this ServiceAuthAction.  # noqa: E501
        :type: bool
        """

        self._run = run

    @property
    def hold(self):
        """Gets the hold of this ServiceAuthAction.  # noqa: E501

        Is Hold allowed in service  # noqa: E501

        :return: The hold of this ServiceAuthAction.  # noqa: E501
        :rtype: bool
        """
        return self._hold

    @hold.setter
    def hold(self, hold):
        """Sets the hold of this ServiceAuthAction.

        Is Hold allowed in service  # noqa: E501

        :param hold: The hold of this ServiceAuthAction.  # noqa: E501
        :type: bool
        """

        self._hold = hold

    @property
    def resume(self):
        """Gets the resume of this ServiceAuthAction.  # noqa: E501

        Is Resume allowed in service  # noqa: E501

        :return: The resume of this ServiceAuthAction.  # noqa: E501
        :rtype: bool
        """
        return self._resume

    @resume.setter
    def resume(self, resume):
        """Sets the resume of this ServiceAuthAction.

        Is Resume allowed in service  # noqa: E501

        :param resume: The resume of this ServiceAuthAction.  # noqa: E501
        :type: bool
        """

        self._resume = resume

    @property
    def view_orderable_service(self):
        """Gets the view_orderable_service of this ServiceAuthAction.  # noqa: E501

        Is View Orderable Service allowed in service  # noqa: E501

        :return: The view_orderable_service of this ServiceAuthAction.  # noqa: E501
        :rtype: bool
        """
        return self._view_orderable_service

    @view_orderable_service.setter
    def view_orderable_service(self, view_orderable_service):
        """Sets the view_orderable_service of this ServiceAuthAction.

        Is View Orderable Service allowed in service  # noqa: E501

        :param view_orderable_service: The view_orderable_service of this ServiceAuthAction.  # noqa: E501
        :type: bool
        """

        self._view_orderable_service = view_orderable_service

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
        if issubclass(ServiceAuthAction, dict):
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
        if not isinstance(other, ServiceAuthAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
