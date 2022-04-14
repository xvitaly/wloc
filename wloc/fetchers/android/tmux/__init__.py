# coding=utf-8

# SPDX-FileCopyrightText: 2015-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import json
import subprocess

from ....exceptions import FetcherError


class TermuxAPI:
    """
    Class for working with Termux API.
    """

    def _fetch_json(self) -> None:
        """
        Fetches JSON from stdout and stores the result in a special
        private field.
        """
        self._json = subprocess.check_output('termux-wifi-scaninfo', encoding='utf8', timeout=5000)

    def _parse_json(self) -> None:
        """
        Parses JSON stored in a special private field and tries to
        extract the required information from it (BSSID and RSSI).
        :exception FetcherError: Termux API error message.
        """
        networks = json.loads(self._json)
        if not isinstance(networks, list):
            raise FetcherError(networks['error'])
        for network in networks:
            self._network_list.append([network['bssid'], network['rssi']])

    def get_networks(self) -> list:
        """
        Gets the list of available Wi-Fi networks with their BSSID and signal strength.
        :return: The list of available Wi-Fi networks.
        """
        self._fetch_json()
        self._parse_json()
        return self._network_list

    def __init__(self) -> None:
        """
        Main constructor of the TermuxAPI class.
        """
        self._json: str = ''
        self._network_list: list = []
