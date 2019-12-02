# coding=utf-8

#
# Wi-Fi simple geolocation tool
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


def mkparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--yandex', '-y', help='Use Yandex Geolocation API.', action="store_true", required=False)
    parser.add_argument('--google', '-g', help='Use Google Geolocation API.', action="store_true", required=False)
    parser.add_argument('--mozilla', '-m', help='Use Mozilla Geolocation API.', action="store_true", required=False)
    return parser


def show_result(coords, service):
    print('%s results:\nLatitude: %.6f\nLongitude: %.6f\n' % (service, coords[0], coords[1]))


def show_error(service, message):
    print('An error occurred while querying %s backend: %s' % (service, message))


def main():
    try:
        # Creating parser instance and fetching command-line arguments...
        aparse = mkparser()
        params = aparse.parse_args()

        # Checking selected options...
        if params.yandex or params.google or params.mozilla:

            # Creating WFLoc object...
            locator = wloc.WiFiLocator(gg_apikey=os.getenv('APIKEY_GOOGLE'), ya_apikey=os.getenv('APIKEY_YANDEX'),
                                       mm_apikey=os.getenv('APIKEY_MOZILLA'))

            # Getting list of available Wi-Fi networks...
            locator.fetch_networks()

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

            # Querying Mozilla if selected...
            if params.mozilla:
                try:
                    show_result(locator.query_mozilla(), 'Mozilla')
                except Exception as ex:
                    show_error('Mozilla', ex)
        else:
            # No command-line arguments detected. Show small help...
            aparse.print_help()

    except Exception as ex:
        # Exception detected...
        print('An error occurred while running application: %s' % ex)


if __name__ == '__main__':
    main()
