# coding=utf-8

# SPDX-FileCopyrightText: 2015-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

from .termux import TermuxNativeAPI
from ...fetchers import FetcherCommon


class FetcherAndroid(FetcherCommon):
    """
    Class for fetching the list of available Wi-Fi networks
    on Android operating system.
    """

    def _fetch_networks(self) -> None:
        """
        Works with the Termux API. Fetches the list of available
        networks and stores them in a private class field.
        """
        self._netlist = TermuxNativeAPI().get_networks()
