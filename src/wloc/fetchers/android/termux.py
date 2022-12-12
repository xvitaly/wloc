# coding=utf-8

# SPDX-FileCopyrightText: 2015-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import json
import subprocess

from ..native import NativeBackendCommon
from ...exceptions import FetcherError


class TermuxNativeAPI(NativeBackendCommon):
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
            raise FetcherError(next(iter(networks.values())))
        for network in networks:
            self._network_list.append([network['bssid'], network['rssi']])

    def _fetch_list(self):
        """
        Fetches the list of available Wi-Fi networks using public
        D-Bus methods.
        """
        self._fetch_json()
        self._parse_json()

    def __init__(self) -> None:
        """
        Main constructor of the TermuxAPI class.
        """
        super().__init__()
        self._json: str = ''
