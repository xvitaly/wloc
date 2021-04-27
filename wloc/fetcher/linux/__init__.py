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

from NetworkManager import NetworkManager, Wireless

from ...fetcher import FetcherCommon


class FetcherLinux(FetcherCommon):
    def _fetch_networks(self) -> None:
        """
        Connects to Network Manager, fetching list of available networks
        and stores them in private class property.
        """

        # Using DBus to ask Network Manager for available networks...
        for nmdevice in NetworkManager.GetDevices():
            if type(nmdevice) == Wireless:
                for accesspoint in nmdevice.AccessPoints:
                    self.__netlist.append([accesspoint.HwAddress, self.conv_strength(accesspoint.Strength)])
