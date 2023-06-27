# coding=utf-8

# SPDX-FileCopyrightText: 2015-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import gi

from ..native import NativeBackendCommon
from ...helpers import Helpers

gi.require_version('NM', '1.0')
from gi.repository import GLib, NM  # noqa: E402


class NetworkManagerNativeAPI(NativeBackendCommon):
    """
    Class for working with Network Manager using GObject API.
    """

    @staticmethod
    def _scan_networks(device) -> None:
        """
        Forces scanning of available Wi-Fi networks on the specified
        physical network device.
        :param device: A physical network device to use.
        """
        loop = GLib.MainLoop()
        device.request_scan_async(None)

        ts = GLib.timeout_source_new(10000)
        ts.set_callback(lambda x: loop.quit())
        ts.attach(loop.get_context())
        device.connect('notify', lambda x, y: loop.quit())

        loop.run()
        ts.destroy()

    def _fetch_list(self):
        """
        Fetches the list of available Wi-Fi networks using GObject API
        methods.
        """
        nmclient = NM.Client.new()
        for nmdevice in nmclient.get_devices():
            if nmdevice.get_device_type() == NM.DeviceType.WIFI:
                if (NM.utils_get_timestamp_msec() - nmdevice.get_last_scan()) / 1000.0 > 120:
                    self._scan_networks(nmdevice)
                for accesspoint in nmdevice.get_access_points():
                    self._network_list.append(
                        [accesspoint.get_bssid(), Helpers.percents2dbm(accesspoint.get_strength())])
