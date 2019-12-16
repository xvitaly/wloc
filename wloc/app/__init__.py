# coding=utf-8

#
# Wi-Fi simple geolocation library
# Copyright (c) 2015 - 2019 EasyCoding Team
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import argparse
import os
import wloc


class WiFiLocatorApp:
    def __parser_create(self):
        self.__parser = argparse.ArgumentParser()
        self.__parser_add_arguments()

    def __parser_add_arguments(self):
        self.__parser.add_argument('--yandex', '-y', help='Use Yandex Geolocation API.', action="store_true",
                                   required=False)
        self.__parser.add_argument('--google', '-g', help='Use Google Geolocation API.', action="store_true",
                                   required=False)
        self.__parser.add_argument('--mozilla', '-m', help='Use Mozilla Geolocation API.', action="store_true",
                                   required=False)

    def __parse_arguments(self):
        self.__arguments = self.__parser.parse_args()

    def __check_arguments(self):
        return self.__arguments.yandex or self.__arguments.google or self.__arguments.mozilla

    def __print_result(self, coords, service):
        print('%s results:\nLatitude: %.6f\nLongitude: %.6f\n' % (service, coords[0], coords[1]))

    def __print_error(self, service, message):
        print('An error occurred while querying %s backend: %s' % (service, message))

    def __call_yandex(self, name):
        if self.__arguments.yandex:
            try:
                self.__print_result(self.__locator.query_yandex(), name)
            except Exception as ex:
                self.__print_error(name, ex)

    def __call_google(self, name):
        if self.__arguments.google:
            try:
                self.__print_result(self.__locator.query_google(), name)
            except Exception as ex:
                self.__print_error(name, ex)

    def __call_mozilla(self, name):
        if self.__arguments.mozilla:
            try:
                self.__print_result(self.__locator.query_mozilla(), name)
            except Exception as ex:
                self.__print_error(name, ex)

    def run(self):
        if self.__check_arguments():
            self.__locator.fetch_networks()
            self.__call_yandex('Yandex')
            self.__call_google('Google')
            self.__call_mozilla('Mozilla')
        else:
            self.__parser.print_help()

    def __init__(self):
        self.__parser_create()
        self.__parse_arguments()
        self.__locator = wloc.WiFiLocator(gg_apikey=os.getenv('APIKEY_GOOGLE'), ya_apikey=os.getenv('APIKEY_YANDEX'),
                                          mm_apikey=os.getenv('APIKEY_MOZILLA'))