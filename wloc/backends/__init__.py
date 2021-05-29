# coding=utf-8

# SPDX-FileCopyrightText: 2015-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import abc

from ..exceptions import MissingTokenError, NetworksNotFoundError


class BackendCommon(metaclass=abc.ABCMeta):
    """
    Abstract class for working with geolocation backends.
    """

    @abc.abstractmethod
    def _execute(self, netlist) -> list:
        """
        Calls the backend API and returns the coordinates.

        Abstract method. Must be overridden.
        :param netlist: The list of available Wi-Fi networks.
        :return: Coordinates (float).
        """

    @property
    @abc.abstractmethod
    def _uri(self) -> str:
        """
        Gets fully-qualified geolocation API URI.

        Abstract property. Must be overridden.
        :return: Fully-qualified geolocation API URI.
        """

    def get_coords(self, netlist) -> list:
        """
        Calls the backend API and returns the coordinates.
        :param netlist: The list of available Wi-Fi networks.
        :exception MissingTokenError: API token not entered or is not valid.
        :exception NetworksNotFoundError: The wireless networks list is empty.
        :return: Coordinates (float).
        """
        if not self._apikey:
            raise MissingTokenError('API token not entered or is not valid!')
        if len(netlist) < 1:
            raise NetworksNotFoundError('The wireless networks list is empty!')
        return self._execute(netlist)

    def __init__(self, apikey: str):
        """
        Main constructor of the BackendCommon class.
        :param apikey: String with the API token (key).
        """
        self._apikey: str = apikey
