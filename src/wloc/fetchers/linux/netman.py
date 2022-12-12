# coding=utf-8

# SPDX-FileCopyrightText: 2015-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import time

from NetworkManager import NetworkManager, Wireless
from dbus.mainloop.glib import DBusGMainLoop

from ..native import NativeBackendCommon
from ...helpers import Helpers


class NetworkManagerNativeAPI(NativeBackendCommon):
    """
    Class for working with Network Manager API using public D-Bus
    methods.
    """

    def _fetch_list(self):
        """
        Fetches the list of available Wi-Fi networks using public
        D-Bus methods.
        """
        # Applying workaround to python-networkmanager#84...
        DBusGMainLoop(set_as_default=True)

        # Using DBus to fetch the list of available networks...
        for nmdevice in NetworkManager.GetDevices():
            if isinstance(nmdevice, Wireless):
                if len(nmdevice.AccessPoints) < 2:
                    nmdevice.RequestScan({})
                    time.sleep(self._sleep_seconds)
                for accesspoint in nmdevice.AccessPoints:
                    self._network_list.append([accesspoint.HwAddress, Helpers.percents2dbm(accesspoint.Strength)])
