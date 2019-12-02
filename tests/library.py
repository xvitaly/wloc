# coding=utf-8

#
# Wi-Fi simple geolocation tool
# Copyright (c) 2015 - 2018 EasyCoding Team
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

import json
import os
import unittest
import wloc


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.testdata = json.loads(os.getenv('TEST_DATA'))
        self.locator = wloc.WiFiLocator(gg_apikey=os.getenv('APIKEY_GOOGLE'), ya_apikey=os.getenv('APIKEY_YANDEX'),
                                        mm_apikey=os.getenv('APIKEY_MOZILLA'))
        for network in self.testdata[0]:
            self.locator.add_network(network[0], network[1])

    def test_yandex(self):
        result = self.locator.query_yandex()
        self.assertAlmostEqual(result[0], self.testdata[1][0], delta=0.00001)
        self.assertAlmostEqual(result[1], self.testdata[1][1], delta=0.00001)


if __name__ == '__main__':
    unittest.main()
