#!/usr/bin/python
# coding=utf-8

#
# Wi-Fi simple geolocation library
# Copyright (c) 2015 - 2018 EasyCoding Team
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

from .settings import consts


class WFLoc:
    """
    Wi-Fi simple geolocation class.
    """
    @staticmethod
    def conv_strength(stp):
        """
        Converts Wi-Fi signal strength percents to RSSI (dBm).
        :param stp: Signal strength in percents
        :return: Signal strength in dBm
        """
        return '%.0f' % (stp / 2 - 100)

    def __check_tokens(self):
        """
        Checks if API tokens set in configuration file.
        :return: Check results
        """
        return not(self.__ya_apikey or self.__gg_apikey or self.__mm_apikey)

    def __fetch_networks(self):
        """
        Connects to Network Manager, fetching list of available networks
        and stores them in private class property.
        """
        # Importing Network Manager from GI repository and other modules...
        from gi import require_version
        require_version('NetworkManager', '1.0')
        require_version('NMClient', '1.0')
        from gi.repository import NetworkManager, NMClient
        from warnings import filterwarnings

        # Ignoring warnings on new Python versions...
        filterwarnings('ignore')

        # Connecting to Network Manager...
        nmclient = NMClient.Client.new()
        nmdevices = nmclient.get_devices()

        # Retrieving available networks...
        for nmdevice in nmdevices:
            if nmdevice.get_device_type() == NetworkManager.DeviceType.WIFI:
                for accesspoint in nmdevice.get_access_points():
                    self.__netlist.append([accesspoint.get_bssid(), self.conv_strength(accesspoint.get_strength())])

    def __run_glike(self, auri, akey):
        """
        Internal implementation of Google-like geolocation API fetcher.
        :param auri: String with Google API URI
        :param akey: String with Google API key
        :return: Coordinates (float).
        """
        # Importing required modules...
        from requests import post
        from json import dumps, loads

        # Generating base JSON structure...
        jdata = {'considerIp': 'false', 'wifiAccessPoints': []}

        # Retrieving available networks...
        for arr in self.__netlist:
            jdata['wifiAccessPoints'].append({'macAddress': arr[0], 'signalStrength': arr[1], 'age': 0})

        # Sending our JSON to API...
        r = post(auri % akey, data=dumps(jdata), headers={'content-type': 'application/json'})

        # Checking return code...
        if r.status_code != 200:
            raise Exception('Server returned code: %s. Text message: %s' % (r.status_code, r.text))

        # Parsing JSON response...
        result = loads(r.content, encoding='utf8')

        # Returning result...
        return [result['location']['lat'], result['location']['lng']]

    def __run_yalike(self, auri, akey):
        """
        Internal implementation of Yandex-like geolocation API fetcher.
        :param auri: String with Yandex API URI
        :param akey: String with Yandex API key
        :return: Coordinates (float).
        """
        # Importing required modules...
        from requests import post
        from json import dumps, loads

        # Generating base JSON structure...
        jdata = {'common': {'version': '1.0', 'api_key': akey}, 'wifi_networks': []}

        # Retrieving available networks...
        for arr in self.__netlist:
            jdata['wifi_networks'].append({'mac': arr[0], 'signal_strength': arr[1], 'age': 0})

        # Sending our JSON to API...
        r = post(auri, data={'json': dumps(jdata)}, headers={'content-type': 'application/json'})

        # Checking return code...
        if r.status_code != 200:
            raise Exception('Server returned code: %s. Text message: %s' % (r.status_code, r.text))

        # Parsing JSON response...
        result = loads(r.content, encoding='utf8')

        # Returning result...
        return [float(result['position']['latitude']), float(result['position']['longitude'])]

    def query_yandex(self):
        """
        Query Yandex geolocation API.
        :return: Coordinates (float).
        """
        return self.__run_yalike(self.__ya_apiuri, self.__ya_apikey)

    def query_google(self):
        """
        Query Google geolocation API.
        :return: Coordinates (float).
        """
        return self.__run_glike(self.__gg_apiuri, self.__gg_apikey)

    def query_mozilla(self):
        """
        Query Mozilla geolocation API.
        :return: Coordinates (float).
        """
        return self.__run_glike(self.__mm_apiuri, self.__mm_apikey)

    def __init__(self):
        """
        Main constructor.
        """
        # Setting constants...
        self.__ya_apikey = consts['ya_apikey']
        self.__ya_apiuri = consts['ya_apiuri']
        self.__gg_apikey = consts['gg_apikey']
        self.__gg_apiuri = consts['gg_apiuri']
        self.__mm_apikey = consts['mm_apikey']
        self.__mm_apiuri = consts['mm_apiuri']

        # Checking tokens...
        if self.__check_tokens():
            raise Exception('No API tokens entered. Please open settings.py file and set them.')

        # Creating a new list for networks...
        self.__netlist = []

        # Saving list of available networks...
        self.__fetch_networks()

        # Checking number of networks...
        if len(self.__netlist) < 1:
            raise Exception('No wireless networks found. Check wireless adapter settings!')
