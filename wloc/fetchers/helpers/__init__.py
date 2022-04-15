# coding=utf-8

# SPDX-FileCopyrightText: 2015-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later


class Helpers:
    """
    Static class with helper methods.
    """

    @staticmethod
    def percents2dbm(stp: int) -> str:
        """
        Converts Wi-Fi signal strength percents to RSSI (dBm).
        :param stp: Signal strength in percents.
        :return: Signal strength in dBm.
        """
        return '%.0f' % (stp / 2 - 100)
