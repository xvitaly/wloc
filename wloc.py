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

from wloc import WFLoc


def main():
    try:
        # Querying Yandex...
        locator = WFLoc()
        coords = locator.query_yandex()

        # Showing result...
        print('Latitude: %s\nLongitude: %s\n' % (coords[0], coords[1]))

    except Exception as ex:
        # Exception detected...
        print('An error occurred while querying backend: %s' % ex.message)


if __name__ == '__main__':
    main()
