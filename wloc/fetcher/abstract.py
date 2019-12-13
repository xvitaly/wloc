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


class Fetcher:
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
        Main constructor of Fetcher class.
        """
        self.__netlist = []
