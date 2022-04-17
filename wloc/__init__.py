# coding=utf-8

# SPDX-FileCopyrightText: 2015-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import json

from .backends.google import BackendGoogle
from .backends.mozilla import BackendMozilla
from .backends.yandex import BackendYandex
from .exceptions import NetworksNotFoundError
from .fetchers.factory import FetcherFactory
from .helpers import Helpers


class WiFiLocator:
    """
    Wi-Fi simple geolocation class.
    """

    def __check_networks(self) -> None:
        """
        Checks the number of available wireless networks.
        :exception NetworksNotFoundError: No wireless networks were found.
        """
        if len(self.__netlist) < 1:
            raise NetworksNotFoundError('No wireless networks found.')

    def __fetch_networks(self) -> None:
        """
        Receives list of available networks and stores them in a private
        class property.
        """
        netfetcher = FetcherFactory.create()
        netfetcher.fetch()
        self.__netlist = netfetcher.networks

    def fetch_networks(self) -> None:
        """
        Automatically gets list of available Wi-Fi networks.
        """
        self.__fetch_networks()
        self.__check_networks()

    def add_network(self, hwaddress: str, strength: int) -> None:
        """
        Adds a new network to list.
        :param hwaddress: Station hardware address.
        :param strength: Signal strength in percents (positive number) or
        dBm (negative number).
        """
        self.__netlist.append([hwaddress, Helpers.fix_strength(strength)])

    def remove_network(self, hwaddress: str) -> None:
        """
        Removes specified by hardware address network from list.
        :param hwaddress: Station hardware address.
        """
        for network in self.__netlist:
            if network[0] == hwaddress:
                self.__netlist.remove(network)

    def to_json(self) -> str:
        """
        Returns JSON based on list of available networks.
        :return: String with JSON.
        """
        return json.dumps(self.__netlist)

    def from_json(self, new_list: str) -> None:
        """
        Gets network list from JSON string.
        :param new_list: String with JSON.
        """
        self.__netlist = json.loads(new_list)

    @property
    def networks(self) -> list:
        """
        Gets list of available networks.
        :return: List of available networks.
        """
        return [network[0] for network in self.__netlist]

    def query_google(self) -> list:
        """
        Query Google geolocation API.
        :return: Coordinates (float).
        """
        return BackendGoogle(self.__gg_apikey).get_coords(self.__netlist)

    def query_mozilla(self) -> list:
        """
        Query Mozilla geolocation API.
        :return: Coordinates (float).
        """
        return BackendMozilla(self.__mm_apikey).get_coords(self.__netlist)

    def query_yandex(self) -> list:
        """
        Query Yandex geolocation API.
        :return: Coordinates (float).
        """
        return BackendYandex(self.__ya_apikey).get_coords(self.__netlist)

    def __init__(self, gg_apikey: str = None, ya_apikey: str = None, mm_apikey: str = None) -> None:
        """
        Main constructor.
        :param gg_apikey: Google Geolocation API token.
        :param ya_apikey: Yandex Locator API token.
        :param mm_apikey: Mozilla Geolocation API token.
        """
        # Setting API tokens...
        self.__gg_apikey: str = gg_apikey
        self.__mm_apikey: str = mm_apikey
        self.__ya_apikey: str = ya_apikey

        # Creating a new list for networks...
        self.__netlist: list = []
