# coding=utf-8

# SPDX-FileCopyrightText: 2015-2022 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as fr:
    requirements = fr.read().splitlines()

setup(
    name='wloc',
    version='0.9.0',
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
    install_requires=requirements,
    test_suite='tests',
    author='Vitaly Zaitsev',
    author_email='vitaly@easycoding.org',
    long_description=long_description,
    long_description_content_type='text/markdown',
    description='Simple Wi-Fi geolocation library and tool',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'
)
