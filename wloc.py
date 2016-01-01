#!/usr/bin/env python2

# Importing Network Manager from GI repository...
import gi
gi.require_version('NetworkManager', '1.0')
gi.require_version('NMClient', '1.0')
from gi.repository import NetworkManager, NMClient

# Importing other libs...
import xml.etree.cElementTree as ET
import requests, tempfile

# Setting constants...
APIKey = ''
APIUri = 'http://api.lbs.yandex.net/geolocation'

# Connecting to Network Manager...
NMClient = NMClient.Client.new()
NMDevices = NMClient.get_devices()

# Generating base XML structure...
xml = ET.Element("ya_lbs_request")

# Filling API Keys...
common = ET.SubElement(xml, "common")
ET.SubElement(common, "version").text = "1.0"
ET.SubElement(common, "api_key").text = APIKey

# Creating wifi_networks element...
networks = ET.SubElement(xml, "wifi_networks")

# Retrieving available networks...
for NMDevice in NMDevices:
    if NMDevice.get_device_type() == NetworkManager.DeviceType.WIFI:
        for AccessPoint in NMDevice.get_access_points():
            network = ET.SubElement(networks, "network")
            ET.SubElement(network, "mac").text = AccessPoint.get_bssid()
            ET.SubElement(network, "signal_strength").text = str(int(AccessPoint.get_strength() / 2 - 100))

# Generating temporary file name...
xmlfile = tempfile.NamedTemporaryFile()

# Saving XML...
ET.ElementTree(xml).write(xmlfile.name, 'utf8')

# Reading file...
with open(xmlfile.name, 'r') as XMLFile:
    mf=XMLFile.read().replace('\n', '')

# Sending our XML file to API...
r = requests.post(APIUri, data={'xml': mf})
print(r.text)