# coding=utf-8

# SPDX-FileCopyrightText: 2017 Jiang Sheng-Jhih
# SPDX-FileCopyrightText: 2021 EasyCoding Team
#
# SPDX-License-Identifier: MIT

# Based on pywifi library: https://github.com/awkman/pywifi
# License can be found in the licenses/pywifi.LICENSE.txt file.

import ctypes
import ctypes.wintypes
import time
import comtypes

from . import structures
from ..native import NativeBackendCommon


class WlanNativeAPI(NativeBackendCommon):
    """
    Special class for working with the Windows Native Wi-Fi API.

    MSDN: https://docs.microsoft.com/en-us/windows/win32/api/wlanapi/
    """

    @staticmethod
    def _wlan_open_handle(client_version, negotiated_version, handle) -> int:
        """
        Python implementation of the WlanOpenHandle function from the Windows Native Wi-Fi API.

        MSDN: https://docs.microsoft.com/en-us/windows/win32/api/wlanapi/nf-wlanapi-wlanopenhandle
        :param client_version: The version of the highest WLAN API.
        :param negotiated_version: The version of the WLAN API that will be used.
        :param handle: Handle for the client.
        :return: Return ERROR_SUCCESS on success.
        """
        func = ctypes.windll.wlanapi.WlanOpenHandle
        func.argtypes = [ctypes.wintypes.DWORD, ctypes.c_void_p, ctypes.POINTER(ctypes.wintypes.DWORD),
                         ctypes.POINTER(ctypes.wintypes.HANDLE)]
        func.restypes = [ctypes.wintypes.DWORD]
        return func(client_version, None, negotiated_version, handle)

    @staticmethod
    def _wlan_enum_interfaces(handle, ifaces) -> int:
        """
        Python implementation of the WlanEnumInterfaces function from the Windows Native Wi-Fi API.

        MSDN: https://docs.microsoft.com/en-us/windows/win32/api/wlanapi/nf-wlanapi-wlanenuminterfaces
        :param handle: The client's session handle.
        :param ifaces: A pointer to the WLAN_INTERFACE_INFO_LIST structure.
        :return: Return ERROR_SUCCESS on success.
        """
        func = ctypes.windll.wlanapi.WlanEnumInterfaces
        func.argtypes = [ctypes.wintypes.HANDLE, ctypes.c_void_p,
                         ctypes.POINTER(ctypes.POINTER(structures.WLAN_INTERFACE_INFO_LIST))]
        func.restypes = [ctypes.wintypes.DWORD]
        return func(handle, None, ifaces)

    @staticmethod
    def _wlan_scan(handle, iface_guid):
        """
        Python implementation of the WlanScan function from the Windows Native Wi-Fi API.

        MSDN: https://docs.microsoft.com/en-us/windows/win32/api/wlanapi/nf-wlanapi-wlanscan
        :param handle: The client's session handle.
        :param iface_guid: A pointer to the WLAN_INTERFACE_INFO_LIST structure.
        :return: Return ERROR_SUCCESS on success.
        """
        func = ctypes.windll.wlanapi.WlanScan
        func.argtypes = [ctypes.wintypes.HANDLE, ctypes.POINTER(comtypes.GUID), ctypes.POINTER(structures.DOT11_SSID),
                         ctypes.POINTER(structures.WLAN_RAW_DATA), ctypes.c_void_p]
        func.restypes = [ctypes.wintypes.DWORD]
        return func(handle, iface_guid, None, None, None)

    @staticmethod
    def _wlan_get_available_network_list(handle, iface_guid, network_list) -> int:
        """
        Python implementation of the WlanGetAvailableNetworkList function from the Windows Native Wi-Fi API.

        MSDN: https://docs.microsoft.com/en-us/windows/win32/api/wlanapi/nf-wlanapi-wlangetavailablenetworklist
        :param handle: The client's session handle.
        :param iface_guid: GUID of the wireless interface to be queried.
        :param network_list: A pointer to the WLAN_AVAILABLE_NETWORK_LIST structure.
        :return: Return ERROR_SUCCESS on success.
        """
        func = ctypes.windll.wlanapi.WlanGetAvailableNetworkList
        func.argtypes = [ctypes.wintypes.HANDLE, ctypes.POINTER(comtypes.GUID), ctypes.wintypes.DWORD, ctypes.c_void_p,
                         ctypes.POINTER(ctypes.POINTER(structures.WLAN_AVAILABLE_NETWORK_LIST))]
        func.restypes = [ctypes.wintypes.DWORD]
        return func(handle, iface_guid, 2, None, network_list)

    @staticmethod
    def _wlan_get_network_bss_list(handle, iface_guid, bss_list, ssid=None, security=False) -> int:
        """
        Python implementation of the WlanGetNetworkBssList function from the Windows Native Wi-Fi API.

        MSDN: https://docs.microsoft.com/en-us/windows/win32/api/wlanapi/nf-wlanapi-wlangetnetworkbsslist
        :param handle: The client's session handle.
        :param iface_guid: GUID of the wireless interface to be queried.
        :param bss_list: A pointer to the WLAN_BSS_LIST structure.
        :param ssid: A pointer to a DOT11_SSID structure.
        :param security: Indicates whether security is enabled on the network or not.
        :return: Return ERROR_SUCCESS on success.
        """
        func = ctypes.windll.wlanapi.WlanGetNetworkBssList
        func.argtypes = [ctypes.wintypes.HANDLE, ctypes.POINTER(comtypes.GUID), ctypes.POINTER(structures.DOT11_SSID),
                         ctypes.c_uint, ctypes.c_bool, ctypes.c_void_p,
                         ctypes.POINTER(ctypes.POINTER(structures.WLAN_BSS_LIST))]
        func.restypes = [ctypes.wintypes.DWORD]
        return func(handle, iface_guid, ssid, 1, security, None, bss_list)

    def _get_interfaces(self) -> list:
        """
        Gets the list of available Wi-Fi physical network interfaces.
        :return: The list of available Wi-Fi physical network interfaces.
        """
        ifaces = []
        self._wlan_open_handle(self._client_version, ctypes.byref(self._negotiated_version), ctypes.byref(self._handle))
        self._wlan_enum_interfaces(self._handle, ctypes.byref(self._ifaces))
        interfaces = ctypes.cast(self._ifaces.contents.InterfaceInfo, ctypes.POINTER(structures.WLAN_INTERFACE_INFO))
        for i in range(0, self._ifaces.contents.dwNumberOfItems):
            iface = {'guid': interfaces[i].InterfaceGuid, 'name': interfaces[i].strInterfaceDescription}
            ifaces.append(iface)
        return ifaces

    def _scan_networks(self, interface) -> None:
        """
        Forces scanning of available Wi-Fi networks on the specified network
        interface.
        :param interface: A physical network interface to use.
        """
        self._wlan_scan(self._handle, ctypes.byref(interface['guid']))

    def _get_networks(self, interface) -> list:
        """
        Gets the list of available Wi-Fi networks with their BSSID and signal strength
        from specified network interface.
        :param interface: A physical network interface to use.
        :return: The list of available Wi-Fi networks.
        """
        network_list = []
        avail_network_list = ctypes.pointer(structures.WLAN_AVAILABLE_NETWORK_LIST())
        self._wlan_get_available_network_list(self._handle, ctypes.byref(interface['guid']),
                                              ctypes.byref(avail_network_list))
        networks = ctypes.cast(avail_network_list.contents.Network, ctypes.POINTER(structures.WLAN_AVAILABLE_NETWORK))
        for i in range(avail_network_list.contents.dwNumberOfItems):
            if networks[i].dot11BssType == 1 and networks[i].bNetworkConnectable:
                bss_list = ctypes.pointer(structures.WLAN_BSS_LIST())
                self._wlan_get_network_bss_list(self._handle, ctypes.byref(interface['guid']), ctypes.byref(bss_list),
                                                networks[i].dot11Ssid, networks[i].bSecurityEnabled)
                bsses = ctypes.cast(bss_list.contents.wlanBssEntries, ctypes.POINTER(structures.WLAN_BSS_ENTRY))
                for j in range(bss_list.contents.dwNumberOfItems):
                    network_list.append(
                        [':'.join([f'{bssid:02x}' for bssid in bsses[j].dot11Bssid[0:6]]), bsses[j].lRssi])
        return network_list

    def _fetch_list(self):
        """
        Gets available network interfaces and fetches available wireless
        networks into a special private field.
        """
        for interface in self._get_interfaces():
            networks = self._get_networks(interface)
            if len(networks) < 2:
                self._scan_networks(interface)
                time.sleep(self._sleep_seconds)
                networks = self._get_networks(interface)
            self._network_list += networks

    def __init__(self) -> None:
        """
        Main constructor of the NativeWiFi class.
        """
        super().__init__()
        self._client_version = 2
        self._negotiated_version = ctypes.wintypes.DWORD()
        self._handle = ctypes.wintypes.HANDLE()
        self._ifaces = ctypes.pointer(structures.WLAN_INTERFACE_INFO_LIST())
