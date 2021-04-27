# coding=utf-8

# SPDX-FileCopyrightText: 2015-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later


class Settings:
    yandex_api_uri: str = 'https://api.lbs.yandex.net/geolocation'
    google_api_uri: str = 'https://www.googleapis.com/geolocation/v1/geolocate?key=%s'
    mozilla_api_uri: str = 'https://location.services.mozilla.com/v1/geolocate?key=%s'
