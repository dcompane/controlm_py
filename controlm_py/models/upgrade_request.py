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

class UpgradeRequest(object):
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
        'ctm': 'str',
        'agent': 'str',
        'type': 'str',
        'version': 'str',
        'activity_name': 'str',
        'install_user': 'str',
        'notify_address': 'str',
        'description': 'str',
        'use_network_deployment': 'bool',
        'transfer_only': 'bool',
        'java_home': 'str'
    }

    attribute_map = {
        'ctm': 'ctm',
        'agent': 'agent',
        'type': 'type',
        'version': 'version',
        'activity_name': 'activityName',
        'install_user': 'installUser',
        'notify_address': 'notifyAddress',
        'description': 'description',
        'use_network_deployment': 'useNetworkDeployment',
        'transfer_only': 'transferOnly',
        'java_home': 'javaHome'
    }

    def __init__(self, ctm=None, agent=None, type=None, version=None, activity_name=None, install_user=None, notify_address=None, description=None, use_network_deployment=None, transfer_only=None, java_home=None):  # noqa: E501
        """UpgradeRequest - a model defined in Swagger"""  # noqa: E501
        self._ctm = None
        self._agent = None
        self._type = None
        self._version = None
        self._activity_name = None
        self._install_user = None
        self._notify_address = None
        self._description = None
        self._use_network_deployment = None
        self._transfer_only = None
        self._java_home = None
        self.discriminator = None
        if ctm is not None:
            self.ctm = ctm
        if agent is not None:
            self.agent = agent
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        if activity_name is not None:
            self.activity_name = activity_name
        if install_user is not None:
            self.install_user = install_user
        if notify_address is not None:
            self.notify_address = notify_address
        if description is not None:
            self.description = description
        if use_network_deployment is not None:
            self.use_network_deployment = use_network_deployment
        if transfer_only is not None:
            self.transfer_only = transfer_only
        if java_home is not None:
            self.java_home = java_home

    @property
    def ctm(self):
        """Gets the ctm of this UpgradeRequest.  # noqa: E501

        Control-M name. REQUIRED  # noqa: E501

        :return: The ctm of this UpgradeRequest.  # noqa: E501
        :rtype: str
        """
        return self._ctm

    @ctm.setter
    def ctm(self, ctm):
        """Sets the ctm of this UpgradeRequest.

        Control-M name. REQUIRED  # noqa: E501

        :param ctm: The ctm of this UpgradeRequest.  # noqa: E501
        :type: str
        """

        self._ctm = ctm

    @property
    def agent(self):
        """Gets the agent of this UpgradeRequest.  # noqa: E501

        Agent name. REQUIRED  # noqa: E501

        :return: The agent of this UpgradeRequest.  # noqa: E501
        :rtype: str
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        """Sets the agent of this UpgradeRequest.

        Agent name. REQUIRED  # noqa: E501

        :param agent: The agent of this UpgradeRequest.  # noqa: E501
        :type: str
        """

        self._agent = agent

    @property
    def type(self):
        """Gets the type of this UpgradeRequest.  # noqa: E501

        Product type (Agent, MFT, AppPack). REQUIRED  # noqa: E501

        :return: The type of this UpgradeRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpgradeRequest.

        Product type (Agent, MFT, AppPack). REQUIRED  # noqa: E501

        :param type: The type of this UpgradeRequest.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this UpgradeRequest.  # noqa: E501

        Target version to be installed or version that should be rollback REQUIRED  # noqa: E501

        :return: The version of this UpgradeRequest.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UpgradeRequest.

        Target version to be installed or version that should be rollback REQUIRED  # noqa: E501

        :param version: The version of this UpgradeRequest.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def activity_name(self):
        """Gets the activity_name of this UpgradeRequest.  # noqa: E501

        Name of activity  # noqa: E501

        :return: The activity_name of this UpgradeRequest.  # noqa: E501
        :rtype: str
        """
        return self._activity_name

    @activity_name.setter
    def activity_name(self, activity_name):
        """Sets the activity_name of this UpgradeRequest.

        Name of activity  # noqa: E501

        :param activity_name: The activity_name of this UpgradeRequest.  # noqa: E501
        :type: str
        """

        self._activity_name = activity_name

    @property
    def install_user(self):
        """Gets the install_user of this UpgradeRequest.  # noqa: E501

        User that will install, upgrade or uninstall HIDDEN  # noqa: E501

        :return: The install_user of this UpgradeRequest.  # noqa: E501
        :rtype: str
        """
        return self._install_user

    @install_user.setter
    def install_user(self, install_user):
        """Sets the install_user of this UpgradeRequest.

        User that will install, upgrade or uninstall HIDDEN  # noqa: E501

        :param install_user: The install_user of this UpgradeRequest.  # noqa: E501
        :type: str
        """

        self._install_user = install_user

    @property
    def notify_address(self):
        """Gets the notify_address of this UpgradeRequest.  # noqa: E501

        List of email addresses separated by semicolon HIDDEN  # noqa: E501

        :return: The notify_address of this UpgradeRequest.  # noqa: E501
        :rtype: str
        """
        return self._notify_address

    @notify_address.setter
    def notify_address(self, notify_address):
        """Sets the notify_address of this UpgradeRequest.

        List of email addresses separated by semicolon HIDDEN  # noqa: E501

        :param notify_address: The notify_address of this UpgradeRequest.  # noqa: E501
        :type: str
        """

        self._notify_address = notify_address

    @property
    def description(self):
        """Gets the description of this UpgradeRequest.  # noqa: E501

        Description of activity HIDDEN  # noqa: E501

        :return: The description of this UpgradeRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpgradeRequest.

        Description of activity HIDDEN  # noqa: E501

        :param description: The description of this UpgradeRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def use_network_deployment(self):
        """Gets the use_network_deployment of this UpgradeRequest.  # noqa: E501

        Whether to deploy from a network location HIDDEN  # noqa: E501

        :return: The use_network_deployment of this UpgradeRequest.  # noqa: E501
        :rtype: bool
        """
        return self._use_network_deployment

    @use_network_deployment.setter
    def use_network_deployment(self, use_network_deployment):
        """Sets the use_network_deployment of this UpgradeRequest.

        Whether to deploy from a network location HIDDEN  # noqa: E501

        :param use_network_deployment: The use_network_deployment of this UpgradeRequest.  # noqa: E501
        :type: bool
        """

        self._use_network_deployment = use_network_deployment

    @property
    def transfer_only(self):
        """Gets the transfer_only of this UpgradeRequest.  # noqa: E501

        True means perform only transfer. Install as well as transfer otherwise HIDDEN  # noqa: E501

        :return: The transfer_only of this UpgradeRequest.  # noqa: E501
        :rtype: bool
        """
        return self._transfer_only

    @transfer_only.setter
    def transfer_only(self, transfer_only):
        """Sets the transfer_only of this UpgradeRequest.

        True means perform only transfer. Install as well as transfer otherwise HIDDEN  # noqa: E501

        :param transfer_only: The transfer_only of this UpgradeRequest.  # noqa: E501
        :type: bool
        """

        self._transfer_only = transfer_only

    @property
    def java_home(self):
        """Gets the java_home of this UpgradeRequest.  # noqa: E501

        The JRE location. If specified - will be used by the upgrade process and the upgraded Agent/Managed File Transfer/AppPack HIDDEN  # noqa: E501

        :return: The java_home of this UpgradeRequest.  # noqa: E501
        :rtype: str
        """
        return self._java_home

    @java_home.setter
    def java_home(self, java_home):
        """Sets the java_home of this UpgradeRequest.

        The JRE location. If specified - will be used by the upgrade process and the upgraded Agent/Managed File Transfer/AppPack HIDDEN  # noqa: E501

        :param java_home: The java_home of this UpgradeRequest.  # noqa: E501
        :type: str
        """

        self._java_home = java_home

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
        if issubclass(UpgradeRequest, dict):
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
        if not isinstance(other, UpgradeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
