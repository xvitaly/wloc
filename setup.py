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

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='wloc',
    version='0.4.0',
    packages=find_packages(exclude=['tests']),
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
    install_requires=['requests'],
    test_suite='tests',
    author='Vitaly Zaitsev',
    author_email='vitaly@easycoding.org',
    long_description=long_description,
    long_description_content_type='text/markdown',
    description='Simple Wi-Fi geolocation library and tool',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
