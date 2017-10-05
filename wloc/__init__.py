#!/usr/bin/python
# coding=utf-8

#
# Wi-Fi simple geolocation library
# Copyright (c) 2015 - 2017 EasyCoding Team
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
        return not(self.__ya_apikey or self.__gg_apikey)

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

    def query_yandex(self):
        """
        Query Yandex Geolocation API.
        :return: Coordinates (float).
        """
        # Importing required modules...
        from xml.etree.cElementTree import Element, SubElement, tostring as XmlToString, fromstring as XMLFromString
        from requests import post

        # Generating base XML structure...
        xml = Element('ya_lbs_request')

        # Filling API Keys...
        common = SubElement(xml, 'common')
        SubElement(common, 'version').text = '1.0'
        SubElement(common, 'api_key').text = self.__ya_apikey

        # Creating wifi_networks element...
        networks = SubElement(xml, 'wifi_networks')

        # Retrieving available networks...
        for arr in self.__netlist:
            network = SubElement(networks, 'network')
            SubElement(network, 'mac').text = arr[0]
            SubElement(network, 'signal_strength').text = arr[1]

        # Sending our XML file to API...
        r = post(self.__ya_apiuri, data={'xml': XmlToString(xml, 'utf8')})

        # Checking return code...
        if r.status_code != 200:
            raise Exception('Server returned code: %s. Text message: %s' % (r.status_code, r.text))

        # Parsing XML response...
        result = XMLFromString(r.content).findall('./position/')

        # Returning result...
        return [float(result[0].text), float(result[1].text)]

    def query_google(self):
        """
        Query Google Geolocation API.
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
        r = post(self.__gg_apiuri % self.__gg_apikey, data=dumps(jdata),
                 headers={'content-type': 'application/json'})

        # Checking return code...
        if r.status_code != 200:
            raise Exception('Server returned code: %s. Text message: %s' % (r.status_code, r.text))

        # Parsing JSON response...
        result = loads(r.content, encoding='utf8')

        # Returning result...
        return [result['location']['lat'], result['location']['lng']]

    def __init__(self):
        """
        Main constructor.
        """
        # Setting constants...
        self.__ya_apikey = consts['ya_apikey']
        self.__ya_apiuri = consts['ya_apiuri']
        self.__gg_apikey = consts['gg_apikey']
        self.__gg_apiuri = consts['gg_apiuri']

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
