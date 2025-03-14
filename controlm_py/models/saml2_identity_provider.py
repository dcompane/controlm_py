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

class Saml2IdentityProvider(object):
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
        'metadata_url': 'str',
        'enabled': 'bool',
        'service_provider_information': 'ServiceProviderInformation',
        'force_authentication': 'bool'
    }

    attribute_map = {
        'metadata_url': 'metadataUrl',
        'enabled': 'enabled',
        'service_provider_information': 'serviceProviderInformation',
        'force_authentication': 'forceAuthentication'
    }

    def __init__(self, metadata_url=None, enabled=None, service_provider_information=None, force_authentication=None):  # noqa: E501
        """Saml2IdentityProvider - a model defined in Swagger"""  # noqa: E501
        self._metadata_url = None
        self._enabled = None
        self._service_provider_information = None
        self._force_authentication = None
        self.discriminator = None
        self.metadata_url = metadata_url
        self.enabled = enabled
        if service_provider_information is not None:
            self.service_provider_information = service_provider_information
        if force_authentication is not None:
            self.force_authentication = force_authentication

    @property
    def metadata_url(self):
        """Gets the metadata_url of this Saml2IdentityProvider.  # noqa: E501


        :return: The metadata_url of this Saml2IdentityProvider.  # noqa: E501
        :rtype: str
        """
        return self._metadata_url

    @metadata_url.setter
    def metadata_url(self, metadata_url):
        """Sets the metadata_url of this Saml2IdentityProvider.


        :param metadata_url: The metadata_url of this Saml2IdentityProvider.  # noqa: E501
        :type: str
        """
        if metadata_url is None:
            raise ValueError("Invalid value for `metadata_url`, must not be `None`")  # noqa: E501

        self._metadata_url = metadata_url

    @property
    def enabled(self):
        """Gets the enabled of this Saml2IdentityProvider.  # noqa: E501


        :return: The enabled of this Saml2IdentityProvider.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Saml2IdentityProvider.


        :param enabled: The enabled of this Saml2IdentityProvider.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def service_provider_information(self):
        """Gets the service_provider_information of this Saml2IdentityProvider.  # noqa: E501


        :return: The service_provider_information of this Saml2IdentityProvider.  # noqa: E501
        :rtype: ServiceProviderInformation
        """
        return self._service_provider_information

    @service_provider_information.setter
    def service_provider_information(self, service_provider_information):
        """Sets the service_provider_information of this Saml2IdentityProvider.


        :param service_provider_information: The service_provider_information of this Saml2IdentityProvider.  # noqa: E501
        :type: ServiceProviderInformation
        """

        self._service_provider_information = service_provider_information

    @property
    def force_authentication(self):
        """Gets the force_authentication of this Saml2IdentityProvider.  # noqa: E501


        :return: The force_authentication of this Saml2IdentityProvider.  # noqa: E501
        :rtype: bool
        """
        return self._force_authentication

    @force_authentication.setter
    def force_authentication(self, force_authentication):
        """Sets the force_authentication of this Saml2IdentityProvider.


        :param force_authentication: The force_authentication of this Saml2IdentityProvider.  # noqa: E501
        :type: bool
        """

        self._force_authentication = force_authentication

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
        if issubclass(Saml2IdentityProvider, dict):
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
        if not isinstance(other, Saml2IdentityProvider):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
