# coding=utf-8

# SPDX-FileCopyrightText: 2015-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

from .wlan import WlanNativeAPI
from ...fetchers import FetcherCommon


class FetcherWindows(FetcherCommon):
    """
    Class for fetching the list of available Wi-Fi networks
    on Microsoft Windows operating system.
    """

    def _fetch_networks(self) -> None:
        """
        Uses Windows Native Wi-Fi API for fetching of available networks
        and stores them in the private class property.
        """
        self._netlist = WlanNativeAPI().get_networks()
