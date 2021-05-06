# coding=utf-8

# SPDX-FileCopyrightText: 2015-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import json
import requests

from ...backend import BackendCommon


class BackendYandex(BackendCommon):
    def _execute(self, netlist) -> list:
        """
        Internal implementation of Yandex-like geolocation API fetcher.
        :return: Coordinates (float).
        """
        # Generating base JSON structure...
        jdata = {'common': {'version': '1.0', 'api_key': self._apikey}, 'wifi_networks': []}

        # Retrieving available networks...
        for arr in netlist:
            jdata['wifi_networks'].append({'mac': arr[0], 'signal_strength': arr[1], 'age': 0})

        # Sending our JSON to API...
        r = requests.post(self._uri, data={'json': json.dumps(jdata)}, headers={'content-type': 'application/json'})

        # Checking return code...
        if r.status_code != 200:
            raise Exception('Server returned code: %s. Text message: %s' % (r.status_code, r.text))

        # Parsing JSON response...
        result = json.loads(r.content)

        # Returning result...
        return [float(result['position']['latitude']), float(result['position']['longitude'])]

    def __init__(self, apikey):
        super().__init__(apikey)
        self._uri: str = 'https://api.lbs.yandex.net/geolocation'
