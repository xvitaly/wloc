#!/usr/bin/python
# coding=utf-8

#
# Wi-Fi simple geolocation tool
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

from wloc.settings import consts


class WFLoc:
    @staticmethod
    def conv_strength(stp):
        # Converting strength percents to RSSI (dBm)...
        return '%.0f' % (stp / 2 - 100)

    def __fetch_networks(self):
        # Importing Network Manager from GI repository and other modules...
        import gi, warnings
        gi.require_version('NetworkManager', '1.0')
        gi.require_version('NMClient', '1.0')
        from gi.repository import NetworkManager, NMClient

        # Ignoring warnings on new Python versions...
        warnings.filterwarnings('ignore')

        # Connecting to Network Manager...
        nmclient = NMClient.Client.new()
        nmdevices = nmclient.get_devices()

        # Retrieving available networks...
        for nmdevice in nmdevices:
            if nmdevice.get_device_type() == NetworkManager.DeviceType.WIFI:
                for accesspoint in nmdevice.get_access_points():
                    self.__netlist.append([accesspoint.get_bssid(), self.conv_strength(accesspoint.get_strength())])

    def query_yandex(self):
        # Importing required modules...
        import xml.etree.cElementTree as et
        import requests as rq

        # Generating base XML structure...
        xml = et.Element('ya_lbs_request')

        # Filling API Keys...
        common = et.SubElement(xml, 'common')
        et.SubElement(common, 'version').text = '1.0'
        et.SubElement(common, 'api_key').text = self.__ya_apikey

        # Creating wifi_networks element...
        networks = et.SubElement(xml, 'wifi_networks')

        # Retrieving available networks...
        for arr in self.__netlist:
            network = et.SubElement(networks, 'network')
            et.SubElement(network, 'mac').text = arr[0]
            et.SubElement(network, 'signal_strength').text = arr[1]

        # Sending our XML file to API...
        r = rq.post(self.__ya_apiuri, data={'xml': et.tostring(xml, 'utf8')})

        # Checking return code...
        if r.status_code != 200:
            raise Exception('Server returned code: %s. Text message: %s' % (r.status_code, r.text))

        # Parsing XML response...
        result = et.fromstring(r.content).findall('./position/')

        # Returning result...
        return [result[0].text, result[1].text]

    def __init__(self):
        # Setting constants...
        self.__ya_apikey = consts['ya_apikey']
        self.__ya_apiuri = consts['ya_apiuri']

        # Creating a new list for networks...
        self.__netlist = []

        # Saving list of available networks...
        self.__fetch_networks()
