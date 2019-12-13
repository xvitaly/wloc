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
    __add_element: str = 'AA:BB:CC:DD:EE:FF'
    __items_count: int = 8

    def __checkcoords(self, result: list):
        """
        Performs checks between master and received coordinates.
        :param result: API result.
        """
        self.assertAlmostEqual(result[0], self.testdata[1][0], delta=self.__delta)
        self.assertAlmostEqual(result[1], self.testdata[1][1], delta=self.__delta)

    def setUp(self):
        """
        Loads test data from environment variables before each test.
        """
        with open(os.getenv('SUITE_FILENAME'), mode='r', encoding='utf8') as source:
            self.testdata = json.load(source)
        self.locator = wloc.WiFiLocator(gg_apikey=os.getenv('APIKEY_GOOGLE'), ya_apikey=os.getenv('APIKEY_YANDEX'),
                                        mm_apikey=os.getenv('APIKEY_MOZILLA'))
        for network in self.testdata[0]:
            self.locator.add_network(network[0], network[1])

    def test_adding(self):
        """
        Tests adding new networks to list.
        """
        self.locator.add_network(self.__add_element, 50)
        self.assertIn(self.__add_element, self.locator.networks)

    def test_removing(self):
        """
        Tests removing of existing network from list.
        """
        self.locator.add_network(self.__add_element, 90)
        self.locator.remove_network(self.__add_element)
        self.assertNotIn(self.__add_element, self.locator.networks)

    def test_network_getter(self):
        """
        Tests if public getter return anything useful.
        """
        self.assertEqual(len(self.locator.networks), self.__items_count)

    def test_yandex(self):
        """
        Tests if Yandex Locator API works and return correct result.
        """
        self.__checkcoords(self.locator.query_yandex())

    def test_google(self):
        """
        Tests if Google geolocation API works and return correct result.
        """
        self.__checkcoords(self.locator.query_google())

    def test_mozilla(self):
        """
        Tests if Mozilla geolocation API works and return correct result.
        """
        self.__checkcoords(self.locator.query_mozilla())

    def test_export(self):
        new_netlist = json.loads(self.locator.to_json())
        self.assertEqual(len(new_netlist), self.__items_count)

    def test_import(self):
        """
        Tests JSON import from string.
        """
        self.locator.from_json(self.locator.to_json())
        self.assertEqual(len(self.locator.networks), self.__items_count)


if __name__ == '__main__':
    unittest.main()
