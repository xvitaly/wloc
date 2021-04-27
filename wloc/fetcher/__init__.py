# coding=utf-8

# SPDX-FileCopyrightText: 2015-2021 EasyCoding Team
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
        """

    @staticmethod
    def conv_strength(stp: int) -> str:
        """
        Converts Wi-Fi signal strength percents to RSSI (dBm).
        :param stp: Signal strength in percents.
        :return: Signal strength in dBm.
        """
        return '%.0f' % (stp / 2 - 100)

    @property
    def networks(self) -> list:
        """
        Gets list of available wireless networks.
        :return: List of available wireless networks.
        """
        return self._netlist

    def __init__(self) -> None:
        """
        Main constructor of the Fetcher class.
        """
        self._netlist = []
        self._fetch_networks()
