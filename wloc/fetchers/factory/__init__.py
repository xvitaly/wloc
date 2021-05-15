# coding=utf-8

# SPDX-FileCopyrightText: 2015-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import sys

from ..linux import FetcherLinux
from ..windows import FetcherWindows
from ...exceptions import PlatformNotSupported


class FetcherFactory:
    """
    Static class with factory methods.
    """

    @staticmethod
    def create():
        """
        Returns the correct instance of the fetcher. Factory method.
        :exception PlatformNotSupported: Current platform is not supported.
        :return: An instance of the desired class.
        :rtype: Any
        """
        if sys.platform.startswith('win32'):
            return FetcherWindows()
        elif sys.platform.startswith('linux'):
            return FetcherLinux()
        raise PlatformNotSupported('Current platform is not supported!')
