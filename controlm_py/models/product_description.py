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

class ProductDescription(object):
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
        'product_name': 'str',
        'product_description': 'str',
        'is_section_open': 'bool',
        'static_text': 'bool',
        'token_component': 'bool'
    }

    attribute_map = {
        'product_name': 'productName',
        'product_description': 'productDescription',
        'is_section_open': 'isSectionOpen',
        'static_text': 'staticText',
        'token_component': 'tokenComponent'
    }

    def __init__(self, product_name=None, product_description=None, is_section_open=None, static_text=None, token_component=None):  # noqa: E501
        """ProductDescription - a model defined in Swagger"""  # noqa: E501
        self._product_name = None
        self._product_description = None
        self._is_section_open = None
        self._static_text = None
        self._token_component = None
        self.discriminator = None
        if product_name is not None:
            self.product_name = product_name
        if product_description is not None:
            self.product_description = product_description
        if is_section_open is not None:
            self.is_section_open = is_section_open
        if static_text is not None:
            self.static_text = static_text
        if token_component is not None:
            self.token_component = token_component

    @property
    def product_name(self):
        """Gets the product_name of this ProductDescription.  # noqa: E501

        The product name.  # noqa: E501

        :return: The product_name of this ProductDescription.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this ProductDescription.

        The product name.  # noqa: E501

        :param product_name: The product_name of this ProductDescription.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def product_description(self):
        """Gets the product_description of this ProductDescription.  # noqa: E501

        The product description.  # noqa: E501

        :return: The product_description of this ProductDescription.  # noqa: E501
        :rtype: str
        """
        return self._product_description

    @product_description.setter
    def product_description(self, product_description):
        """Sets the product_description of this ProductDescription.

        The product description.  # noqa: E501

        :param product_description: The product_description of this ProductDescription.  # noqa: E501
        :type: str
        """

        self._product_description = product_description

    @property
    def is_section_open(self):
        """Gets the is_section_open of this ProductDescription.  # noqa: E501

        is Section open.  # noqa: E501

        :return: The is_section_open of this ProductDescription.  # noqa: E501
        :rtype: bool
        """
        return self._is_section_open

    @is_section_open.setter
    def is_section_open(self, is_section_open):
        """Sets the is_section_open of this ProductDescription.

        is Section open.  # noqa: E501

        :param is_section_open: The is_section_open of this ProductDescription.  # noqa: E501
        :type: bool
        """

        self._is_section_open = is_section_open

    @property
    def static_text(self):
        """Gets the static_text of this ProductDescription.  # noqa: E501

        is static text section.  # noqa: E501

        :return: The static_text of this ProductDescription.  # noqa: E501
        :rtype: bool
        """
        return self._static_text

    @static_text.setter
    def static_text(self, static_text):
        """Sets the static_text of this ProductDescription.

        is static text section.  # noqa: E501

        :param static_text: The static_text of this ProductDescription.  # noqa: E501
        :type: bool
        """

        self._static_text = static_text

    @property
    def token_component(self):
        """Gets the token_component of this ProductDescription.  # noqa: E501

        is token component added.  # noqa: E501

        :return: The token_component of this ProductDescription.  # noqa: E501
        :rtype: bool
        """
        return self._token_component

    @token_component.setter
    def token_component(self, token_component):
        """Sets the token_component of this ProductDescription.

        is token component added.  # noqa: E501

        :param token_component: The token_component of this ProductDescription.  # noqa: E501
        :type: bool
        """

        self._token_component = token_component

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
        if issubclass(ProductDescription, dict):
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
        if not isinstance(other, ProductDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
