# Wi-Fi geolocation library and tool

[![GitHub version](https://badge.fury.io/gh/xvitaly%2Fwloc.svg)](https://github.com/xvitaly/wloc/releases)
[![Build status](https://travis-ci.org/xvitaly/wloc.svg?branch=dev)](https://travis-ci.org/xvitaly/wloc)
[![GitHub issues](https://img.shields.io/github/issues/xvitaly/wloc.svg?label=issues&maxAge=60)](https://github.com/xvitaly/wloc/issues)
---

Locate user by using global Wi-Fi database (no GPS required). Supported backends:
 * [Yandex Maps API](https://tech.yandex.ru/locator/doc/dg/api/json-docpage/);
 * [Google Geolocation API](https://developers.google.com/maps/documentation/geolocation/intro);
 * [Mozilla Geolocation API](https://mozilla.github.io/ichnaea/api/index.html).

# License
[GNU General Public License version 3](COPYING). External libraries can use another compatible licenses.

# Requirements
 * GNU/Linux (any modern distribution) with installed and enabled Network Manager;
 * Python 3.6+;
 * python-networkmanager;
 * python-requests.

# Installation
 1. Clone this repository:
 ```bash
 git clone https://github.com/xvitaly/wloc.git wloc
 ```
 2. Get API keys from [Yandex](https://tech.yandex.ru/maps/keys/get/) or/and [Google](https://developers.google.com/maps/documentation/geolocation/get-api-key).
 3. Open `wloc/settings.py` file in any text editor and set received API keys.
 4. Install (in Python virtual environment):
 ```bash
 python3 setup.py install
 ```
 5. Run application:
 ```bash
 wloc -y -g -m
 ```

# Available options
```
usage: wloc [-h] [--yandex] [--google] [--mozilla]
```

Optional arguments:
 * `-h` or `--help` - Show help message and exit;
 * `-y` or `--yandex` - Use Yandex Geolocation API;
 * `-g` or  `--google` - Use Google Geolocation API;
 * `-m` or  `--mozilla` - Use Mozilla Geolocation API.
