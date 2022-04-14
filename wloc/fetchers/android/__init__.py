# coding=utf-8

# SPDX-FileCopyrightText: 2015-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

from ...fetchers import FetcherCommon


class FetcherAndroid(FetcherCommon):
    def _fetch_networks(self) -> None:
        """
        Works with the Termux API. Fetches the list of available
        networks and stores them in a private class field.
        """
        pass
