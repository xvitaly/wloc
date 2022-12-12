# coding=utf-8

# SPDX-FileCopyrightText: 2015-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

from .netman import NetworkManagerNativeAPI
from ...fetchers import FetcherCommon


class FetcherLinux(FetcherCommon):
    """
    Class for fetching the list of available Wi-Fi networks
    on GNU/Linux operating system.
    """

    def _fetch_networks(self) -> None:
        """
        Connects to the Network Manager. Fetches the list of available
        networks and stores them in a private class field.
        """
        self._netlist = NetworkManagerNativeAPI().get_networks()
