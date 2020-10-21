# coding: utf-8
#      Copyright 2020. ThingsBoard
#  #
#      Licensed under the Apache License, Version 2.0 (the "License");
#      you may not use this file except in compliance with the License.
#      You may obtain a copy of the License at
#  #
#          http://www.apache.org/licenses/LICENSE-2.0
#  #
#      Unless required by applicable law or agreed to in writing, software
#      distributed under the License is distributed on an "AS IS" BASIS,
#      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#      See the License for the specific language governing permissions and
#      limitations under the License.
#

import pprint
import re  # noqa: F401

import six


class DeviceSearchQuery(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'device_types': 'list[str]',
        'parameters': 'RelationsSearchParameters',
        'relation_type': 'str'
    }

    attribute_map = {
        'device_types': 'deviceTypes',
        'parameters': 'parameters',
        'relation_type': 'relationType'
    }

    def __init__(self, device_types=None, parameters=None, relation_type=None):  # noqa: E501
        """DeviceSearchQuery - a model defined in Swagger"""  # noqa: E501

        self._device_types = None
        self._parameters = None
        self._relation_type = None
        self.discriminator = None

        if device_types is not None:
            self.device_types = device_types
        if parameters is not None:
            self.parameters = parameters
        if relation_type is not None:
            self.relation_type = relation_type

    @property
    def device_types(self):
        """Gets the device_types of this DeviceSearchQuery.  # noqa: E501


        :return: The device_types of this DeviceSearchQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._device_types

    @device_types.setter
    def device_types(self, device_types):
        """Sets the device_types of this DeviceSearchQuery.


        :param device_types: The device_types of this DeviceSearchQuery.  # noqa: E501
        :type: list[str]
        """

        self._device_types = device_types

    @property
    def parameters(self):
        """Gets the parameters of this DeviceSearchQuery.  # noqa: E501


        :return: The parameters of this DeviceSearchQuery.  # noqa: E501
        :rtype: RelationsSearchParameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this DeviceSearchQuery.


        :param parameters: The parameters of this DeviceSearchQuery.  # noqa: E501
        :type: RelationsSearchParameters
        """

        self._parameters = parameters

    @property
    def relation_type(self):
        """Gets the relation_type of this DeviceSearchQuery.  # noqa: E501


        :return: The relation_type of this DeviceSearchQuery.  # noqa: E501
        :rtype: str
        """
        return self._relation_type

    @relation_type.setter
    def relation_type(self, relation_type):
        """Sets the relation_type of this DeviceSearchQuery.


        :param relation_type: The relation_type of this DeviceSearchQuery.  # noqa: E501
        :type: str
        """

        self._relation_type = relation_type

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
        if issubclass(DeviceSearchQuery, dict):
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
        if not isinstance(other, DeviceSearchQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other