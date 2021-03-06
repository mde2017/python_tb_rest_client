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


class OAuth2ClientInfo(object):
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
        'created_time': 'int',
        'icon': 'str',
        'id': 'OAuth2IntegrationId',
        'name': 'str',
        'url': 'str'
    }

    attribute_map = {
        'created_time': 'createdTime',
        'icon': 'icon',
        'id': 'id',
        'name': 'name',
        'url': 'url'
    }

    def __init__(self, created_time=None, icon=None, id=None, name=None, url=None):  # noqa: E501
        """OAuth2ClientInfo - a model defined in Swagger"""  # noqa: E501

        self._created_time = None
        self._icon = None
        self._id = None
        self._name = None
        self._url = None
        self.discriminator = None

        if created_time is not None:
            self.created_time = created_time
        if icon is not None:
            self.icon = icon
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if url is not None:
            self.url = url

    @property
    def created_time(self):
        """Gets the created_time of this OAuth2ClientInfo.  # noqa: E501


        :return: The created_time of this OAuth2ClientInfo.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this OAuth2ClientInfo.


        :param created_time: The created_time of this OAuth2ClientInfo.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def icon(self):
        """Gets the icon of this OAuth2ClientInfo.  # noqa: E501


        :return: The icon of this OAuth2ClientInfo.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this OAuth2ClientInfo.


        :param icon: The icon of this OAuth2ClientInfo.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def id(self):
        """Gets the id of this OAuth2ClientInfo.  # noqa: E501


        :return: The id of this OAuth2ClientInfo.  # noqa: E501
        :rtype: OAuth2IntegrationId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OAuth2ClientInfo.


        :param id: The id of this OAuth2ClientInfo.  # noqa: E501
        :type: OAuth2IntegrationId
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this OAuth2ClientInfo.  # noqa: E501


        :return: The name of this OAuth2ClientInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OAuth2ClientInfo.


        :param name: The name of this OAuth2ClientInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this OAuth2ClientInfo.  # noqa: E501


        :return: The url of this OAuth2ClientInfo.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this OAuth2ClientInfo.


        :param url: The url of this OAuth2ClientInfo.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(OAuth2ClientInfo, dict):
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
        if not isinstance(other, OAuth2ClientInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
