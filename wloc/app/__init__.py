# coding=utf-8

# SPDX-FileCopyrightText: 2015-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import argparse
import logging
import os
import sys

from wloc import WiFiLocator
from .settings import Settings


class App:
    def __setlogger(self) -> None:
        """
        Configures logger for internal use.
        """
        self.__logger = logging.getLogger(__name__)
        self.__logger.setLevel(Settings.log_level)
        e_handler = logging.StreamHandler(sys.stdout)
        e_handler.setFormatter(logging.Formatter(Settings.log_format))
        self.__logger.addHandler(e_handler)

    def __parser_create(self) -> None:
        """
        Creates an instance of the command-line arguments parser.
        """
        self.__parser = argparse.ArgumentParser()
        self.__parser_add_arguments()

    def __parser_add_arguments(self) -> None:
        """
        Adds new options to the command-line arguments parser.
        """
        self.__parser.add_argument('--google', '-g', help='Use Google Geolocation API.', action='store_true',
                                   required=False)
        self.__parser.add_argument('--mozilla', '-m', help='Use Mozilla Geolocation API.', action='store_true',
                                   required=False)
        self.__parser.add_argument('--yandex', '-y', help='Use Yandex Geolocation API.', action='store_true',
                                   required=False)

    def __parse_arguments(self) -> None:
        """
        Parses command-line arguments and provides a special object
        to work with.
        """
        self.__arguments = self.__parser.parse_args()

    def __check_arguments(self) -> bool:
        """
        Checks if at least one of the optional command-line arguments present.
        :return: Availability of any optional command-line arguments.
        """
        return self.__arguments.yandex or self.__arguments.google or self.__arguments.mozilla

    def __set_backends(self) -> None:
        """
        Creates an instance of the WiFiLocator class and special switch surrogate.
        """
        self.__locator = WiFiLocator(gg_apikey=os.getenv('APIKEY_GOOGLE'), ya_apikey=os.getenv('APIKEY_YANDEX'),
                                     mm_apikey=os.getenv('APIKEY_MOZILLA'))
        self.__selector = {
            'Google': self.__locator.query_google,
            'Mozilla': self.__locator.query_mozilla,
            'Yandex': self.__locator.query_yandex
        }

    def __get_results(self) -> None:
        """
        Calls enabled by user backends.
        """
        if self.__arguments.google:
            self.__call_backend('Google')
        if self.__arguments.mozilla:
            self.__call_backend('Mozilla')
        if self.__arguments.yandex:
            self.__call_backend('Yandex')

    def __call_backend(self, name: str) -> None:
        """
        Directly calls one of the supported geolocation backend.
        :param name:
        """
        try:
            coords = self.__selector[name]()
            self.__logger.info('%s results:\nLatitude: %.6f\nLongitude: %.6f\n', name, coords[0], coords[1])
        except Exception:
            self.__logger.exception('An error occurred while querying %s backend!', name)

    def run(self) -> None:
        """
        Run the application.
        """
        if self.__check_arguments():
            self.__locator.fetch_networks()
            self.__get_results()
        else:
            self.__parser.print_help()

    def __init__(self) -> None:
        """
        Main constructor of the App class.
        """
        self.__setlogger()
        self.__parser_create()
        self.__parse_arguments()
        self.__set_backends()
