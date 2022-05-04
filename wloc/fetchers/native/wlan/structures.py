# coding=utf-8

# SPDX-FileCopyrightText: 2017 Jiang Sheng-Jhih
# SPDX-FileCopyrightText: 2021 EasyCoding Team
#
# SPDX-License-Identifier: MIT

# Based on pywifi library: https://github.com/awkman/pywifi
# License can be found in the licenses/pywifi.LICENSE.txt file.

import ctypes.wintypes
import comtypes

__all__ = ['DOT11_SSID', 'WLAN_RAW_DATA', 'WLAN_RATE_SET', 'WLAN_AVAILABLE_NETWORK', 'WLAN_AVAILABLE_NETWORK_LIST',
           'WLAN_BSS_ENTRY', 'WLAN_BSS_LIST', 'WLAN_INTERFACE_INFO', 'WLAN_INTERFACE_INFO_LIST']


class DOT11_SSID(ctypes.Structure):
    """
    Python prototype of the DOT11_SSID structure from the
    Windows Native Wi-Fi API.

    MSDN: https://docs.microsoft.com/en-us/windows/win32/api/wlanapi/
    """
    _fields_ = [('uSSIDLength', ctypes.c_ulong),
                ('ucSSID', ctypes.c_char * 32)]


class WLAN_RAW_DATA(ctypes.Structure):
    """
    Python prototype of the WLAN_RAW_DATA structure from the
    Windows Native Wi-Fi API.

    MSDN: https://docs.microsoft.com/en-us/windows/win32/api/wlanapi/
    """
    _fields_ = [
        ("dwDataSize", ctypes.wintypes.DWORD),
        ("DataBlob", ctypes.c_byte * 1)
    ]


class WLAN_RATE_SET(ctypes.Structure):
    """
    Python prototype of the WLAN_RATE_SET structure from the
    Windows Native Wi-Fi API.

    MSDN: https://docs.microsoft.com/en-us/windows/win32/api/wlanapi/
    """
    _fields_ = [
        ('uRateSetLength', ctypes.c_ulong),
        ('usRateSet', ctypes.c_ushort * 126)
    ]


class WLAN_AVAILABLE_NETWORK(ctypes.Structure):
    """
    Python prototype of the WLAN_AVAILABLE_NETWORK structure from the
    Windows Native Wi-Fi API.

    MSDN: https://docs.microsoft.com/en-us/windows/win32/api/wlanapi/
    """
    _fields_ = [
        ('strProfileName', ctypes.c_wchar * 256),
        ('dot11Ssid', DOT11_SSID),
        ('dot11BssType', ctypes.c_uint),
        ('uNumberOfBssids', ctypes.c_ulong),
        ('bNetworkConnectable', ctypes.c_bool),
        ('wlanNotConnectableReason', ctypes.c_uint),
        ('uNumberOfPhyTypes', ctypes.c_ulong * 8),
        ('dot11PhyTypes', ctypes.c_uint),
        ('bMorePhyTypes', ctypes.c_bool),
        ('wlanSignalQuality', ctypes.c_ulong),
        ('bSecurityEnabled', ctypes.c_bool),
        ('dot11DefaultAuthAlgorithm', ctypes.c_uint),
        ('dot11DefaultCipherAlgorithm', ctypes.c_uint),
        ('dwFlags', ctypes.wintypes.DWORD),
        ('dwReserved', ctypes.wintypes.DWORD)
    ]


class WLAN_AVAILABLE_NETWORK_LIST(ctypes.Structure):
    """
    Python prototype of the WLAN_AVAILABLE_NETWORK_LIST structure from the
    Windows Native Wi-Fi API.

    MSDN: https://docs.microsoft.com/en-us/windows/win32/api/wlanapi/
    """
    _fields_ = [
        ('dwNumberOfItems', ctypes.wintypes.DWORD),
        ('dwIndex', ctypes.wintypes.DWORD),
        ('Network', WLAN_AVAILABLE_NETWORK * 1)
    ]


class WLAN_BSS_ENTRY(ctypes.Structure):
    """
    Python prototype of the WLAN_BSS_ENTRY structure from the
    Windows Native Wi-Fi API.

    MSDN: https://docs.microsoft.com/en-us/windows/win32/api/wlanapi/
    """
    _fields_ = [
        ('dot11Ssid', DOT11_SSID),
        ('uPhyId', ctypes.c_ulong),
        ('dot11Bssid', ctypes.c_ubyte * 6),
        ('dot11BssType', ctypes.c_uint),
        ('dot11BssPhyType', ctypes.c_uint),
        ('lRssi', ctypes.c_long),
        ('uLinkQuality', ctypes.c_ulong),
        ('bInRegDomain', ctypes.c_bool),
        ('usBeaconPeriod', ctypes.c_ushort),
        ('ullTimestamp', ctypes.c_ulonglong),
        ('ullHostTimestamp', ctypes.c_ulonglong),
        ('usCapabilityInformation', ctypes.c_ushort),
        ('ulChCenterFrequency', ctypes.c_ulong),
        ('wlanRateSet', WLAN_RATE_SET),
        ('ulIeOffset', ctypes.c_ulong),
        ('ulIeSize', ctypes.c_ulong)
    ]


class WLAN_BSS_LIST(ctypes.Structure):
    """
    Python prototype of the WLAN_BSS_LIST structure from the
    Windows Native Wi-Fi API.

    MSDN: https://docs.microsoft.com/en-us/windows/win32/api/wlanapi/
    """
    _fields_ = [
        ('dwTotalSize', ctypes.wintypes.DWORD),
        ('dwNumberOfItems', ctypes.wintypes.DWORD),
        ('wlanBssEntries', WLAN_BSS_ENTRY * 1)
    ]


class WLAN_INTERFACE_INFO(ctypes.Structure):
    """
    Python prototype of the WLAN_INTERFACE_INFO structure from the
    Windows Native Wi-Fi API.

    MSDN: https://docs.microsoft.com/en-us/windows/win32/api/wlanapi/
    """
    _fields_ = [
        ('InterfaceGuid', comtypes.GUID),
        ('strInterfaceDescription', ctypes.c_wchar * 256),
        ('isState', ctypes.c_uint)
    ]


class WLAN_INTERFACE_INFO_LIST(ctypes.Structure):
    """
    Python prototype of the WLAN_INTERFACE_INFO_LIST structure from the
    Windows Native Wi-Fi API.

    MSDN: https://docs.microsoft.com/en-us/windows/win32/api/wlanapi/
    """
    _fields_ = [
        ('dwNumberOfItems', ctypes.wintypes.DWORD),
        ('dwIndex', ctypes.wintypes.DWORD),
        ('InterfaceInfo', WLAN_INTERFACE_INFO * 1)
    ]
