# coding=utf-8

# SPDX-FileCopyrightText: 2015-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import json
import os
import unittest
import wloc


class TestLibrary(unittest.TestCase):
    __delta: float = 0.002
    __add_element: str = 'AA:BB:CC:DD:EE:FF'
    __items_count: int = 8

    def __checkcoords(self, result: list) -> None:
        """
        Performs checks between master and received coordinates.
        :param result: API result.
        """
        self.assertAlmostEqual(result[0], self.testdata[1][0], delta=self.__delta)
        self.assertAlmostEqual(result[1], self.testdata[1][1], delta=self.__delta)

    def setUp(self) -> None:
        """
        Loads test data from environment variables before each test.
        """
        with open(os.getenv('SUITE_FILENAME'), mode='r', encoding='utf8') as source:
            self.testdata = json.load(source)
        self.locator = wloc.WiFiLocator(gg_apikey=os.getenv('APIKEY_GOOGLE'), ya_apikey=os.getenv('APIKEY_YANDEX'),
                                        mm_apikey=os.getenv('APIKEY_MOZILLA'))
        for network in self.testdata[0]:
            self.locator.add_network(network[0], network[1])

    def test_strength_converter(self) -> None:
        """
        Tests strength converting from percents to dBm.
        """
        self.assertEqual('-75', wloc.Helpers.fix_strength(50))
        self.assertEqual('-75', wloc.Helpers.fix_strength(-75))

    def test_adding_percents(self) -> None:
        """
        Tests adding new networks to list using strength in percents.
        """
        self.locator.add_network(self.__add_element, 50)
        self.assertIn(self.__add_element, self.locator.networks)

    def test_adding_dbm(self) -> None:
        """
        Tests adding new networks to list using strength in dBm.
        """
        self.locator.add_network(self.__add_element, -75)
        self.assertIn(self.__add_element, self.locator.networks)

    def test_removing(self) -> None:
        """
        Tests removing of existing network from list.
        """
        self.locator.add_network(self.__add_element, 90)
        self.locator.remove_network(self.__add_element)
        self.assertNotIn(self.__add_element, self.locator.networks)

    def test_network_getter(self) -> None:
        """
        Tests if public getter return anything useful.
        """
        self.assertEqual(len(self.locator.networks), self.__items_count)

    def test_yandex(self) -> None:
        """
        Tests if Yandex Locator API works and return correct result.
        """
        self.__checkcoords(self.locator.query_yandex())

    def test_google(self) -> None:
        """
        Tests if Google geolocation API works and return correct result.
        """
        self.__checkcoords(self.locator.query_google())

    def test_mozilla(self) -> None:
        """
        Tests if Mozilla geolocation API works and return correct result.
        """
        self.__checkcoords(self.locator.query_mozilla())

    def test_export(self) -> None:
        """
        Tests network list JSON export to string.
        """
        new_netlist = json.loads(self.locator.to_json())
        self.assertEqual(len(new_netlist), self.__items_count)

    def test_import(self) -> None:
        """
        Tests network list JSON import from string.
        """
        self.locator.from_json(self.locator.to_json())
        self.assertEqual(len(self.locator.networks), self.__items_count)


if __name__ == '__main__':
    unittest.main()
