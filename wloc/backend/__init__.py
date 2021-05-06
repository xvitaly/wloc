# coding=utf-8

# SPDX-FileCopyrightText: 2015-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import abc


class BackendCommon(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def _execute(self, netlist) -> list:
        """
        Calls backend API and returns coordinates.

        Abstract method. Must be overridden.
        :return: Coordinates (float).
        """

    def get_coords(self, netlist) -> list:
        """
        Calls backend API and returns coordinates.
        :return: Coordinates (float).
        """
        return self._execute(netlist)

    def __init__(self, apikey):
        """
        Main constructor of the BackendCommon class.
        """
        self._apikey = apikey
