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
import logging
import os
import sys

from wloc import WiFiLocator
from .messages import Messages
from .settings import Settings


class App:
    def __setlogger(self):
        self.__logger = logging.getLogger(__name__)
        self.__logger.setLevel(Settings.log_level)
        e_handler = logging.StreamHandler(sys.stdout)
        e_handler.setFormatter(logging.Formatter(Settings.log_format))
        self.__logger.addHandler(e_handler)

    def __parser_create(self):
        self.__parser = argparse.ArgumentParser()
        self.__parser_add_arguments()

    def __parser_add_arguments(self):
        self.__parser.add_argument('--yandex', '-y', help=Messages.arg_desc_yandex, action="store_true",
                                   required=False)
        self.__parser.add_argument('--google', '-g', help=Messages.arg_desc_google, action="store_true",
                                   required=False)
        self.__parser.add_argument('--mozilla', '-m', help=Messages.arg_desc_mozilla, action="store_true",
                                   required=False)

    def __parse_arguments(self):
        self.__arguments = self.__parser.parse_args()

    def __check_arguments(self):
        return self.__arguments.yandex or self.__arguments.google or self.__arguments.mozilla

    def __set_backends(self):
        self.__locator = WiFiLocator(gg_apikey=os.getenv('APIKEY_GOOGLE'), ya_apikey=os.getenv('APIKEY_YANDEX'),
                                     mm_apikey=os.getenv('APIKEY_MOZILLA'))
        self.__selector = {
            'Yandex': self.__locator.query_yandex,
            'Google': self.__locator.query_google,
            'Mozilla': self.__locator.query_mozilla
        }

    def __get_results(self):
        if self.__arguments.yandex:
            self.__call_backend('Yandex')
        if self.__arguments.google:
            self.__call_backend('Google')
        if self.__arguments.mozilla:
            self.__call_backend('Mozilla')

    def __call_backend(self, name):
        try:
            coords = self.__selector[name]()
            self.__logger.info(Messages.backend_result, name, coords[0], coords[1])
        except Exception:
            self.__logger.exception(Messages.backend_error.format(name))

    def run(self):
        if self.__check_arguments():
            self.__locator.fetch_networks()
            self.__get_results()
        else:
            self.__parser.print_help()

    def __init__(self):
        self.__setlogger()
        self.__parser_create()
        self.__parse_arguments()
        self.__set_backends()
