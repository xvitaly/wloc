# coding=utf-8

# SPDX-FileCopyrightText: 2015-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import json
import subprocess

from ....exceptions import FetcherError


class TermuxAPI:
    def _fetch_json(self):
        self._json = subprocess.check_output('termux-wifi-scaninfo', encoding='utf8', timeout=5000)

    def _parse_json(self):
        networks = json.loads(self._json)
        if not isinstance(networks, list):
            raise FetcherError(networks['error'])
        for network in networks:
            self._network_list.append([network['bssid'], network['rssi']])

    def get_networks(self):
        self._fetch_json()
        self._parse_json()
        return self._network_list

    def __init__(self):
        self._json = ''
        self._network_list = []
