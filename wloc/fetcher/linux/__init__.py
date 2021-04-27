# coding=utf-8

# SPDX-FileCopyrightText: 2015-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

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
                    self._netlist.append([accesspoint.HwAddress, self.conv_strength(accesspoint.Strength)])
