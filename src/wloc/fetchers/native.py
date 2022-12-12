# coding=utf-8

# SPDX-FileCopyrightText: 2015-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import abc


class NativeBackendCommon(metaclass=abc.ABCMeta):
    """
    Abstract class used for platform-dependent fetching the list
    of available Wi-Fi networks.
    """

    @abc.abstractmethod
    def _fetch_list(self) -> None:
        """
        Fetches the list of available networks and stores them in a
        private class property.

        Abstract method. Must be overridden.
        """

    def get_networks(self) -> list:
        """
        Gets the list of available Wi-Fi networks with their BSSID and
        signal strength.
        :return: The list of available Wi-Fi networks.
        """
        self._fetch_list()
        return self._network_list

    def __init__(self) -> None:
        """
        Main constructor of the FetcherBackendCommon class.
        """
        self._network_list: list = []
        self._sleep_seconds: int = 3
