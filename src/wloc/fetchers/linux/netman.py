# coding=utf-8

# SPDX-FileCopyrightText: 2015-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import time

import gi

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
        gi.require_version("NM", "1.0")
        from gi.repository import NM

        # Using DBus to fetch the list of available networks...
        nmclient = NM.Client.new()
        for nmdevice in nmclient.get_devices():
            if nmdevice.get_device_type() == NM.DeviceType.WIFI:
                if len(nmdevice.get_access_points()) < 2:
                    nmdevice.request_scan_async(None)
                    time.sleep(self._sleep_seconds)
                for accesspoint in nmdevice.get_access_points():
                    self._network_list.append(
                        [accesspoint.get_bssid(), Helpers.percents2dbm(accesspoint.get_strength())])
