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

class UpgradeRecord(object):
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
        'upgrade_id': 'str',
        'ctm': 'str',
        'agent': 'str',
        'package': 'str',
        'from_version': 'str',
        'to_version': 'str',
        'activity': 'str',
        'status': 'str',
        'message': 'str',
        'creation_time': 'str',
        'transfer_start_time': 'str',
        'transfer_end_time': 'str',
        'install_start_time': 'str',
        'install_end_time': 'str',
        'activity_name': 'str',
        'install_user': 'str',
        'notify_address': 'str',
        'description': 'str',
        'external_java_path': 'str'
    }

    attribute_map = {
        'upgrade_id': 'upgradeId',
        'ctm': 'ctm',
        'agent': 'agent',
        'package': 'package',
        'from_version': 'fromVersion',
        'to_version': 'toVersion',
        'activity': 'activity',
        'status': 'status',
        'message': 'message',
        'creation_time': 'creationTime',
        'transfer_start_time': 'transferStartTime',
        'transfer_end_time': 'transferEndTime',
        'install_start_time': 'installStartTime',
        'install_end_time': 'installEndTime',
        'activity_name': 'activityName',
        'install_user': 'installUser',
        'notify_address': 'notifyAddress',
        'description': 'description',
        'external_java_path': 'externalJavaPath'
    }

    def __init__(self, upgrade_id=None, ctm=None, agent=None, package=None, from_version=None, to_version=None, activity=None, status=None, message=None, creation_time=None, transfer_start_time=None, transfer_end_time=None, install_start_time=None, install_end_time=None, activity_name=None, install_user=None, notify_address=None, description=None, external_java_path=None):  # noqa: E501
        """UpgradeRecord - a model defined in Swagger"""  # noqa: E501
        self._upgrade_id = None
        self._ctm = None
        self._agent = None
        self._package = None
        self._from_version = None
        self._to_version = None
        self._activity = None
        self._status = None
        self._message = None
        self._creation_time = None
        self._transfer_start_time = None
        self._transfer_end_time = None
        self._install_start_time = None
        self._install_end_time = None
        self._activity_name = None
        self._install_user = None
        self._notify_address = None
        self._description = None
        self._external_java_path = None
        self.discriminator = None
        if upgrade_id is not None:
            self.upgrade_id = upgrade_id
        if ctm is not None:
            self.ctm = ctm
        if agent is not None:
            self.agent = agent
        if package is not None:
            self.package = package
        if from_version is not None:
            self.from_version = from_version
        if to_version is not None:
            self.to_version = to_version
        if activity is not None:
            self.activity = activity
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if creation_time is not None:
            self.creation_time = creation_time
        if transfer_start_time is not None:
            self.transfer_start_time = transfer_start_time
        if transfer_end_time is not None:
            self.transfer_end_time = transfer_end_time
        if install_start_time is not None:
            self.install_start_time = install_start_time
        if install_end_time is not None:
            self.install_end_time = install_end_time
        if activity_name is not None:
            self.activity_name = activity_name
        if install_user is not None:
            self.install_user = install_user
        if notify_address is not None:
            self.notify_address = notify_address
        if description is not None:
            self.description = description
        if external_java_path is not None:
            self.external_java_path = external_java_path

    @property
    def upgrade_id(self):
        """Gets the upgrade_id of this UpgradeRecord.  # noqa: E501

        upgrade id  # noqa: E501

        :return: The upgrade_id of this UpgradeRecord.  # noqa: E501
        :rtype: str
        """
        return self._upgrade_id

    @upgrade_id.setter
    def upgrade_id(self, upgrade_id):
        """Sets the upgrade_id of this UpgradeRecord.

        upgrade id  # noqa: E501

        :param upgrade_id: The upgrade_id of this UpgradeRecord.  # noqa: E501
        :type: str
        """

        self._upgrade_id = upgrade_id

    @property
    def ctm(self):
        """Gets the ctm of this UpgradeRecord.  # noqa: E501

        Control-M name  # noqa: E501

        :return: The ctm of this UpgradeRecord.  # noqa: E501
        :rtype: str
        """
        return self._ctm

    @ctm.setter
    def ctm(self, ctm):
        """Sets the ctm of this UpgradeRecord.

        Control-M name  # noqa: E501

        :param ctm: The ctm of this UpgradeRecord.  # noqa: E501
        :type: str
        """

        self._ctm = ctm

    @property
    def agent(self):
        """Gets the agent of this UpgradeRecord.  # noqa: E501

        agnet name  # noqa: E501

        :return: The agent of this UpgradeRecord.  # noqa: E501
        :rtype: str
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        """Sets the agent of this UpgradeRecord.

        agnet name  # noqa: E501

        :param agent: The agent of this UpgradeRecord.  # noqa: E501
        :type: str
        """

        self._agent = agent

    @property
    def package(self):
        """Gets the package of this UpgradeRecord.  # noqa: E501

        upgrade package type  # noqa: E501

        :return: The package of this UpgradeRecord.  # noqa: E501
        :rtype: str
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this UpgradeRecord.

        upgrade package type  # noqa: E501

        :param package: The package of this UpgradeRecord.  # noqa: E501
        :type: str
        """

        self._package = package

    @property
    def from_version(self):
        """Gets the from_version of this UpgradeRecord.  # noqa: E501

        upgrade from version  # noqa: E501

        :return: The from_version of this UpgradeRecord.  # noqa: E501
        :rtype: str
        """
        return self._from_version

    @from_version.setter
    def from_version(self, from_version):
        """Sets the from_version of this UpgradeRecord.

        upgrade from version  # noqa: E501

        :param from_version: The from_version of this UpgradeRecord.  # noqa: E501
        :type: str
        """

        self._from_version = from_version

    @property
    def to_version(self):
        """Gets the to_version of this UpgradeRecord.  # noqa: E501

        upgrade to version  # noqa: E501

        :return: The to_version of this UpgradeRecord.  # noqa: E501
        :rtype: str
        """
        return self._to_version

    @to_version.setter
    def to_version(self, to_version):
        """Sets the to_version of this UpgradeRecord.

        upgrade to version  # noqa: E501

        :param to_version: The to_version of this UpgradeRecord.  # noqa: E501
        :type: str
        """

        self._to_version = to_version

    @property
    def activity(self):
        """Gets the activity of this UpgradeRecord.  # noqa: E501

        activity type (Transfer, Install, Rollback)  # noqa: E501

        :return: The activity of this UpgradeRecord.  # noqa: E501
        :rtype: str
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this UpgradeRecord.

        activity type (Transfer, Install, Rollback)  # noqa: E501

        :param activity: The activity of this UpgradeRecord.  # noqa: E501
        :type: str
        """

        self._activity = activity

    @property
    def status(self):
        """Gets the status of this UpgradeRecord.  # noqa: E501

        status tyoe (Cancel, Running Complete,TransferCompleted, Failed,Unavailable)  # noqa: E501

        :return: The status of this UpgradeRecord.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpgradeRecord.

        status tyoe (Cancel, Running Complete,TransferCompleted, Failed,Unavailable)  # noqa: E501

        :param status: The status of this UpgradeRecord.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def message(self):
        """Gets the message of this UpgradeRecord.  # noqa: E501

        massage  # noqa: E501

        :return: The message of this UpgradeRecord.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this UpgradeRecord.

        massage  # noqa: E501

        :param message: The message of this UpgradeRecord.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def creation_time(self):
        """Gets the creation_time of this UpgradeRecord.  # noqa: E501

        creation time  # noqa: E501

        :return: The creation_time of this UpgradeRecord.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this UpgradeRecord.

        creation time  # noqa: E501

        :param creation_time: The creation_time of this UpgradeRecord.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def transfer_start_time(self):
        """Gets the transfer_start_time of this UpgradeRecord.  # noqa: E501

        transfer start time  # noqa: E501

        :return: The transfer_start_time of this UpgradeRecord.  # noqa: E501
        :rtype: str
        """
        return self._transfer_start_time

    @transfer_start_time.setter
    def transfer_start_time(self, transfer_start_time):
        """Sets the transfer_start_time of this UpgradeRecord.

        transfer start time  # noqa: E501

        :param transfer_start_time: The transfer_start_time of this UpgradeRecord.  # noqa: E501
        :type: str
        """

        self._transfer_start_time = transfer_start_time

    @property
    def transfer_end_time(self):
        """Gets the transfer_end_time of this UpgradeRecord.  # noqa: E501

        transfer end time  # noqa: E501

        :return: The transfer_end_time of this UpgradeRecord.  # noqa: E501
        :rtype: str
        """
        return self._transfer_end_time

    @transfer_end_time.setter
    def transfer_end_time(self, transfer_end_time):
        """Sets the transfer_end_time of this UpgradeRecord.

        transfer end time  # noqa: E501

        :param transfer_end_time: The transfer_end_time of this UpgradeRecord.  # noqa: E501
        :type: str
        """

        self._transfer_end_time = transfer_end_time

    @property
    def install_start_time(self):
        """Gets the install_start_time of this UpgradeRecord.  # noqa: E501

        installation start time  # noqa: E501

        :return: The install_start_time of this UpgradeRecord.  # noqa: E501
        :rtype: str
        """
        return self._install_start_time

    @install_start_time.setter
    def install_start_time(self, install_start_time):
        """Sets the install_start_time of this UpgradeRecord.

        installation start time  # noqa: E501

        :param install_start_time: The install_start_time of this UpgradeRecord.  # noqa: E501
        :type: str
        """

        self._install_start_time = install_start_time

    @property
    def install_end_time(self):
        """Gets the install_end_time of this UpgradeRecord.  # noqa: E501

        installation end time  # noqa: E501

        :return: The install_end_time of this UpgradeRecord.  # noqa: E501
        :rtype: str
        """
        return self._install_end_time

    @install_end_time.setter
    def install_end_time(self, install_end_time):
        """Sets the install_end_time of this UpgradeRecord.

        installation end time  # noqa: E501

        :param install_end_time: The install_end_time of this UpgradeRecord.  # noqa: E501
        :type: str
        """

        self._install_end_time = install_end_time

    @property
    def activity_name(self):
        """Gets the activity_name of this UpgradeRecord.  # noqa: E501

        activity name  # noqa: E501

        :return: The activity_name of this UpgradeRecord.  # noqa: E501
        :rtype: str
        """
        return self._activity_name

    @activity_name.setter
    def activity_name(self, activity_name):
        """Sets the activity_name of this UpgradeRecord.

        activity name  # noqa: E501

        :param activity_name: The activity_name of this UpgradeRecord.  # noqa: E501
        :type: str
        """

        self._activity_name = activity_name

    @property
    def install_user(self):
        """Gets the install_user of this UpgradeRecord.  # noqa: E501

        install user  # noqa: E501

        :return: The install_user of this UpgradeRecord.  # noqa: E501
        :rtype: str
        """
        return self._install_user

    @install_user.setter
    def install_user(self, install_user):
        """Sets the install_user of this UpgradeRecord.

        install user  # noqa: E501

        :param install_user: The install_user of this UpgradeRecord.  # noqa: E501
        :type: str
        """

        self._install_user = install_user

    @property
    def notify_address(self):
        """Gets the notify_address of this UpgradeRecord.  # noqa: E501

        notify address  # noqa: E501

        :return: The notify_address of this UpgradeRecord.  # noqa: E501
        :rtype: str
        """
        return self._notify_address

    @notify_address.setter
    def notify_address(self, notify_address):
        """Sets the notify_address of this UpgradeRecord.

        notify address  # noqa: E501

        :param notify_address: The notify_address of this UpgradeRecord.  # noqa: E501
        :type: str
        """

        self._notify_address = notify_address

    @property
    def description(self):
        """Gets the description of this UpgradeRecord.  # noqa: E501

        description  # noqa: E501

        :return: The description of this UpgradeRecord.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpgradeRecord.

        description  # noqa: E501

        :param description: The description of this UpgradeRecord.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def external_java_path(self):
        """Gets the external_java_path of this UpgradeRecord.  # noqa: E501

        Gets the value of the externalJavaPath property.  # noqa: E501

        :return: The external_java_path of this UpgradeRecord.  # noqa: E501
        :rtype: str
        """
        return self._external_java_path

    @external_java_path.setter
    def external_java_path(self, external_java_path):
        """Sets the external_java_path of this UpgradeRecord.

        Gets the value of the externalJavaPath property.  # noqa: E501

        :param external_java_path: The external_java_path of this UpgradeRecord.  # noqa: E501
        :type: str
        """

        self._external_java_path = external_java_path

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
        if issubclass(UpgradeRecord, dict):
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
        if not isinstance(other, UpgradeRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
