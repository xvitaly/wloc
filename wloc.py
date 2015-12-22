#!/usr/bin/env python2

import gi
gi.require_version('NetworkManager', '1.0')
gi.require_version('NMClient', '1.0')
from gi.repository import NetworkManager, NMClient

NMClient = NMClient.Client.new()
NMDevices = NMClient.get_devices()

for NMDevice in NMDevices:
    if NMDevice.get_device_type() == NetworkManager.DeviceType.WIFI:
        for AccessPoint in NMDevice.get_access_points():
            print '%-30s (%s) %dMHz %d%%' % (AccessPoint.get_ssid(), AccessPoint.get_bssid(), AccessPoint.get_frequency(), AccessPoint.get_strength())

