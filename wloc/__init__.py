# coding=utf-8

#
# Wi-Fi simple geolocation library
# Copyright (c) 2015 - 2019 EasyCoding Team
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import json
import os
import requests

from .fetcher import Fetcher
from .fetcher.linux import FetcherLinux
from .fetcher.windows import FetcherWindows
from .settings import Settings


class WiFiLocator:
    """
    Wi-Fi simple geolocation class.
    """

    def __check_tokens(self) -> bool:
        """
        Checks if API tokens set in configuration file.
        :return: Check results
        """
        return not (self.__ya_apikey or self.__gg_apikey or self.__mm_apikey)

    def __check_networks(self) -> None:
        """
        Checks the number of available wireless networks.
        """
        if len(self.__netlist) < 1:
            raise Exception('No wireless networks found.')

    def __fetch_networks(self) -> None:
        """
        Receives list of available networks and stores them in a private
        class property.
        """
        # Retrieving available networks...
        if os.name == 'posix':
            self.__netlist = FetcherLinux().networks
        else:
            self.__netlist = FetcherWindows().networks

        # Checking the number of available networks...
        self.__check_networks()

    def __run_glike(self, auri: str, akey: str) -> list:
        """
        Internal implementation of Google-like geolocation API fetcher.
        :param auri: String with Google API URI
        :param akey: String with Google API key
        :return: Coordinates (float).
        """
        # Checking the number of available networks...
        self.__check_networks()

        # Generating base JSON structure...
        jdata = {'considerIp': 'false', 'wifiAccessPoints': []}

        # Retrieving available networks...
        for arr in self.__netlist:
            jdata['wifiAccessPoints'].append({'macAddress': arr[0], 'signalStrength': arr[1], 'age': 0})

        # Sending our JSON to API...
        r = requests.post(auri % akey, data=json.dumps(jdata), headers={'content-type': 'application/json'})

        # Checking return code...
        if r.status_code != 200:
            raise Exception('Server returned code: %s. Text message: %s' % (r.status_code, r.text))

        # Parsing JSON response...
        result = json.loads(r.content, encoding='utf8')

        # Returning result...
        return [result['location']['lat'], result['location']['lng']]

    def __run_yalike(self, auri: str, akey: str) -> list:
        """
        Internal implementation of Yandex-like geolocation API fetcher.
        :param auri: String with Yandex API URI
        :param akey: String with Yandex API key
        :return: Coordinates (float).
        """
        # Checking the number of available networks...
        self.__check_networks()

        # Generating base JSON structure...
        jdata = {'common': {'version': '1.0', 'api_key': akey}, 'wifi_networks': []}

        # Retrieving available networks...
        for arr in self.__netlist:
            jdata['wifi_networks'].append({'mac': arr[0], 'signal_strength': arr[1], 'age': 0})

        # Sending our JSON to API...
        r = requests.post(auri, data={'json': json.dumps(jdata)}, headers={'content-type': 'application/json'})

        # Checking return code...
        if r.status_code != 200:
            raise Exception('Server returned code: %s. Text message: %s' % (r.status_code, r.text))

        # Parsing JSON response...
        result = json.loads(r.content, encoding='utf8')

        # Returning result...
        return [float(result['position']['latitude']), float(result['position']['longitude'])]

    def fetch_networks(self) -> None:
        """
        Automatically gets list of available Wi-Fi networks.
        """
        self.__fetch_networks()

    def add_network(self, hwaddress: str, strength: int) -> None:
        """
        Adds a new network to list.
        :param hwaddress: Station hardware address.
        :param strength: Signal strength in percents.
        """
        self.__netlist.append([hwaddress, Fetcher.conv_strength(strength)])

    def remove_network(self, hwaddress: str) -> None:
        """
        Removes specified by hardware address network from list.
        :param hwaddress: Station hardware address.
        """
        for network in self.__netlist:
            if network[0] == hwaddress:
                self.__netlist.remove(network)

    def to_json(self) -> str:
        """
        Returns JSON based on list of available networks.
        :return: String with JSON.
        """
        return json.dumps(self.__netlist)

    def from_json(self, new_list: str) -> None:
        """
        Gets network list from JSON string.
        :param new_list: String with JSON.
        """
        self.__netlist = json.loads(new_list)

    @property
    def networks(self) -> list:
        """
        Gets list of available networks.
        :return: List of available networks.
        """
        return [network[0] for network in self.__netlist]

    def query_yandex(self) -> list:
        """
        Query Yandex geolocation API.
        :return: Coordinates (float).
        """
        return self.__run_yalike(self.__ya_apiuri, self.__ya_apikey)

    def query_google(self) -> list:
        """
        Query Google geolocation API.
        :return: Coordinates (float).
        """
        return self.__run_glike(self.__gg_apiuri, self.__gg_apikey)

    def query_mozilla(self) -> list:
        """
        Query Mozilla geolocation API.
        :return: Coordinates (float).
        """
        return self.__run_glike(self.__mm_apiuri, self.__mm_apikey)

    def __init__(self, gg_apikey: str = None, ya_apikey: str = None, mm_apikey: str = None) -> None:
        """
        Main constructor.
        :param gg_apikey: Google Geolocation API token.
        :param ya_apikey: Yandex Locator API token.
        :param mm_apikey: Mozilla Geolocation API token.
        """
        # Setting constants...
        self.__ya_apiuri = Settings.yandex_api_uri
        self.__gg_apiuri = Settings.google_api_uri
        self.__mm_apiuri = Settings.mozilla_api_uri

        # Setting API tokens...
        self.__ya_apikey = ya_apikey
        self.__gg_apikey = gg_apikey
        self.__mm_apikey = mm_apikey

        # Checking tokens...
        if self.__check_tokens():
            raise Exception('No API tokens entered.')

        # Creating a new list for networks...
        self.__netlist = []
