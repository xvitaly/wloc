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

import json
import os
import unittest
import wloc


class TestLibrary(unittest.TestCase):
    __delta: float = 0.001

    def setUp(self):
        """
        Loads test data from environment variables before each test.
        """
        self.testdata = json.loads(os.getenv('DATA'))
        self.locator = wloc.WiFiLocator(gg_apikey=os.getenv('APIKEY_GOOGLE'), ya_apikey=os.getenv('APIKEY_YANDEX'),
                                        mm_apikey=os.getenv('APIKEY_MOZILLA'))
        for network in self.testdata[0]:
            self.locator.add_network(network[0], network[1])

    def test_adding(self):
        """
        Tests adding new networks to list.
        """
        test_element = 'AA:BB:CC:DD:EE:FF'
        self.locator.add_network(test_element, 50)
        self.assertIn(test_element, self.locator.networks)

    def test_removing(self):
        """
        Tests removing of existing network from list.
        """
        test_element = 'AA:BB:CC:DD:EE:FF'
        self.locator.add_network(test_element, 90)
        self.locator.remove_network(test_element)
        self.assertNotIn(test_element, self.locator.networks)

    def test_network_getter(self):
        """
        Tests if public getter return anything useful.
        """
        self.assertEqual(len(self.locator.networks), 8)

    def test_yandex(self):
        """
        Tests if Yandex Locator API works and return correct result.
        """
        result = self.locator.query_yandex()
        self.assertAlmostEqual(result[0], self.testdata[1][0], delta=self.__delta)
        self.assertAlmostEqual(result[1], self.testdata[1][1], delta=self.__delta)

    def test_google(self):
        """
        Tests if Google geolocation API works and return correct result.
        """
        result = self.locator.query_google()
        self.assertAlmostEqual(result[0], self.testdata[1][0], delta=self.__delta)
        self.assertAlmostEqual(result[1], self.testdata[1][1], delta=self.__delta)

    def test_mozilla(self):
        """
        Tests if Mozilla geolocation API works and return correct result.
        """
        result = self.locator.query_mozilla()
        self.assertAlmostEqual(result[0], self.testdata[1][0], delta=self.__delta)
        self.assertAlmostEqual(result[1], self.testdata[1][1], delta=self.__delta)


if __name__ == '__main__':
    unittest.main()
