# coding=utf-8

# SPDX-FileCopyrightText: 2015-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

from ..google import BackendGoogle


class BackendMozilla(BackendGoogle):
    def __init__(self, apikey):
        super().__init__(apikey)
        self._endpoint = 'https://location.services.mozilla.com/v1/geolocate?key=%s'
