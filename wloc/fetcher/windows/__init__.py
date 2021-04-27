# coding=utf-8

# SPDX-FileCopyrightText: 2015-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

from ...fetcher import FetcherCommon


class FetcherWindows(FetcherCommon):
    def _fetch_networks(self) -> None:
        """
        Connects to WMI, fetching list of available networks and
        stores them in private class property.
        """
        raise Exception('Current platform is not supported yet.')
