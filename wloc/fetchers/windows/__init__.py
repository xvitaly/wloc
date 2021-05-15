# coding=utf-8

# SPDX-FileCopyrightText: 2015-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

from ...fetchers import FetcherCommon


class FetcherWindows(FetcherCommon):
    def _fetch_networks(self) -> None:
        """
        Uses Windows Native Wi-Fi API for fetching of available networks
        and stores them in the private class property.
        """
        # Importing Native WiFi class...
        from .native import NativeWiFi

        # Using NativeWiFi to fetch the list of available networks...
        wifi = NativeWiFi()
        for interface in wifi.get_interfaces():
            self._netlist += wifi.get_networks(interface)
