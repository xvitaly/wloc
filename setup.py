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

from setuptools import setup, find_packages

setup(
    name='wloc',
    version='0.3',
    packages=find_packages(),
    package_dir={
        'wloc': 'wloc',
    },
    url='https://github.com/xvitaly/wloc',
    license='GPLv3',
    entry_points={
        'console_scripts': [
            'wloc = wloc.app.run:main',
        ],
    },
    install_requires=['requests', 'python-networkmanager'],
    test_suite='tests',
    author='Vitaly Zaitsev',
    author_email='vitaly@easycoding.org',
    description='Simple Wi-Fi geolocation library and tool'
)
