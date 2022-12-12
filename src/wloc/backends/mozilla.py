# coding=utf-8

# SPDX-FileCopyrightText: 2015-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

from .google import BackendGoogle


class BackendMozilla(BackendGoogle):
    """
    Class for working with Mozilla Geolocation API.
    """

    def __init__(self, apikey: str):
        """
        Main constructor of the BackendMozilla class.
        :param apikey: String with the API token (key).
        """
        super().__init__(apikey)
        self._endpoint: str = 'https://location.services.mozilla.com/v1/geolocate?key=%s'
