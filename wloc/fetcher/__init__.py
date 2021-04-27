# coding=utf-8

#
# Wi-Fi simple geolocation tool
# Copyright (c) 2015 - 2019 EasyCoding Team
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
        return self.__netlist

    def __init__(self) -> None:
        """
        Main constructor of the Fetcher class.
        """
        self.__netlist = []
        self._fetch_networks()
