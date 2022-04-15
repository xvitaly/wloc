# coding=utf-8

# SPDX-FileCopyrightText: 2015-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

from NetworkManager import NetworkManager, Wireless
from dbus.mainloop.glib import DBusGMainLoop

from ...helpers import Helpers


class NetworkManagerAPI:
    def _fetch_list(self):
        # Applying workaround to python-networkmanager#84...
        DBusGMainLoop(set_as_default=True)

        # Using DBus to fetch the list of available networks...
        for nmdevice in NetworkManager.GetDevices():
            if isinstance(nmdevice, Wireless):
                for accesspoint in nmdevice.AccessPoints:
                    self._network_list.append([accesspoint.HwAddress, Helpers.percents2dbm(accesspoint.Strength)])

    def get_networks(self) -> list:
        return self._network_list

    def __init__(self) -> None:
        self._network_list: list = []
        self._fetch_list()
