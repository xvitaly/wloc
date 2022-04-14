# coding=utf-8

# SPDX-FileCopyrightText: 2015-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

from ...fetchers import FetcherCommon


class FetcherLinux(FetcherCommon):
    """
    Class for fetching the list of available Wi-Fi networks
    on GNU/Linux operating system.
    """

    def _fetch_networks(self) -> None:
        """
        Connects to the Network Manager. Fetches the list of available
        networks and stores them in a private class field.
        """
        # Importing Network Manager module...
        from NetworkManager import NetworkManager, Wireless

        # Applying workaround to python-networkmanager#84...
        from dbus.mainloop.glib import DBusGMainLoop
        DBusGMainLoop(set_as_default=True)

        # Using DBus to fetch the list of available networks...
        for nmdevice in NetworkManager.GetDevices():
            if isinstance(nmdevice, Wireless):
                for accesspoint in nmdevice.AccessPoints:
                    self._netlist.append([accesspoint.HwAddress, self.conv_strength(accesspoint.Strength)])
