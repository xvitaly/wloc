# coding=utf-8

# SPDX-FileCopyrightText: 2015-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import json
import requests

from ..backends import BackendCommon


class BackendGoogle(BackendCommon):
    """
    Class for working with the Google Geolocation API.
    """

    def _execute(self, netlist: list) -> list:
        """
        Internal implementation of the Google Geolocation API fetcher.
        :param netlist: The list of available Wi-Fi networks.
        :return: Coordinates (float).
        """
        # Generating base JSON structure...
        jdata = {'considerIp': 'false', 'wifiAccessPoints': []}

        # Retrieving available networks...
        for arr in netlist:
            jdata['wifiAccessPoints'].append({'macAddress': arr[0], 'signalStrength': arr[1], 'age': 0})

        # Sending our JSON to API...
        r = requests.post(self._uri, data=json.dumps(jdata), headers={'content-type': 'application/json'})

        # Checking return code...
        self._check_response(r)

        # Parsing JSON response...
        result = json.loads(r.content)

        # Returning result...
        return [result['location']['lat'], result['location']['lng']]

    @property
    def _uri(self) -> str:
        """
        Gets fully-qualified geolocation API URI.
        :return: Fully-qualified geolocation API URI.
        """
        return self._endpoint % self._apikey

    def __init__(self, apikey: str) -> None:
        """
        Main constructor of the BackendGoogle class.
        :param apikey: String with the API token (key).
        """
        super().__init__(apikey)
        self._endpoint: str = 'https://www.googleapis.com/geolocation/v1/geolocate?key=%s'
