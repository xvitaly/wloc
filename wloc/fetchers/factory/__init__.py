# coding=utf-8

# SPDX-FileCopyrightText: 2015-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import os

from ..linux import FetcherLinux
from ..windows import FetcherWindows


class FetcherFactory:
    """
    Static class with factory methods.
    """

    @staticmethod
    def create():
        """
        Get the correct instance of the fetcher. Factory method.
        :return: An instance of the desired class.
        :rtype: Any
        """
        return FetcherLinux() if os.name == 'posix' else FetcherWindows()
