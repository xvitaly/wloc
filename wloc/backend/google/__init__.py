# coding=utf-8

# SPDX-FileCopyrightText: 2015-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import json
import requests

from ...backend import BackendCommon


class BackendGoogle(BackendCommon):
    def _execute(self, netlist) -> list:
        """
        Internal implementation of Google-like geolocation API fetcher.
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
        if r.status_code != 200:
            raise Exception('Server returned code: %s. Text message: %s' % (r.status_code, r.text))

        # Parsing JSON response...
        result = json.loads(r.content)

        # Returning result...
        return [result['location']['lat'], result['location']['lng']]

    @property
    def _uri(self) -> str:
        return self._endpoint % self._apikey

    def __init__(self, apikey):
        super().__init__(apikey)
        self._endpoint = 'https://www.googleapis.com/geolocation/v1/geolocate?key=%s'
