# coding: utf-8

"""
    ThingsBoard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DomainInfo(object):
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
        'name': 'str',
        'scheme': 'str'
    }

    attribute_map = {
        'name': 'name',
        'scheme': 'scheme'
    }

    def __init__(self, name=None, scheme=None):  # noqa: E501
        """DomainInfo - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._scheme = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if scheme is not None:
            self.scheme = scheme

    @property
    def name(self):
        """Gets the name of this DomainInfo.  # noqa: E501


        :return: The name of this DomainInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DomainInfo.


        :param name: The name of this DomainInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def scheme(self):
        """Gets the scheme of this DomainInfo.  # noqa: E501


        :return: The scheme of this DomainInfo.  # noqa: E501
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this DomainInfo.


        :param scheme: The scheme of this DomainInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["HTTP", "HTTPS", "MIXED"]  # noqa: E501
        if scheme not in allowed_values:
            raise ValueError(
                "Invalid value for `scheme` ({0}), must be one of {1}"  # noqa: E501
                .format(scheme, allowed_values)
            )

        self._scheme = scheme

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
        if issubclass(DomainInfo, dict):
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
        if not isinstance(other, DomainInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other