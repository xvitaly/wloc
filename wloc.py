#!/usr/bin/python
# coding=utf-8

#
# Wi-Fi simple geolocation tool
# Copyright (c) 2015 - 2017 EasyCoding Team
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

from argparse import ArgumentParser
from wloc import WFLoc


def mkparser():
    parser = ArgumentParser()
    parser.add_argument('--yandex', '-y', help='Use Yandex Geolocation API.', action="store_true", required=False)
    parser.add_argument('--google', '-g', help='Use Google Geolocation API.', action="store_true", required=False)
    return parser


def show_result(coords, service):
    print('%s results:\nLatitude: %.6f\nLongitude: %.6f\n' % (service, coords[0], coords[1]))


def show_error(service, message):
    print('An error occurred while querying %s backend: %s' % (service, message))


def main():
    try:
        # Checking command-line options...
        params = mkparser().parse_args()

        # Creating WFLoc object...
        locator = WFLoc()

        # Querying Yandex if selected...
        if params.yandex:
            try:
                show_result(locator.query_yandex(), 'Yandex')
            except Exception as ex:
                show_error('Yandex', ex)

        # Querying Google if selected...
        if params.google:
            try:
                show_result(locator.query_google(), 'Google')
            except Exception as ex:
                show_error('Google', ex)

    except Exception as ex:
        # Exception detected...
        print('An error occurred while running application: %s' % ex)


if __name__ == '__main__':
    main()
