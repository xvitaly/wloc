# coding=utf-8

# SPDX-FileCopyrightText: 2015-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import abc


class FetcherCommon(metaclass=abc.ABCMeta):
    """
    Abstract class for fetching the list of available Wi-Fi networks.
    """

    @abc.abstractmethod
    def _fetch_networks(self) -> None:
        """
        Fetches the list of available networks and stores them to the
        private class property.

        Abstract method. Must be overridden.
        """

    @property
    def networks(self) -> list:
        """
        Gets list of available wireless networks.
        :return: List of available wireless networks.
        """
        return self._netlist

    def _clear_networks(self) -> None:
        """
        Clears the list of available networks if not empty.
        """
        if len(self._netlist) > 0:
            self._netlist.clear()

    def fetch(self) -> None:
        """
        Fetches the list of available networks.
        """
        self._clear_networks()
        self._fetch_networks()

    def __init__(self) -> None:
        """
        Main constructor of the FetcherCommon class.
        """
        self._netlist = []
