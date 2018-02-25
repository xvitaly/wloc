# Wi-Fi geolocation library and tool
Locate user by using global Wi-Fi database (no GPS required). Supported backends:
 * [Yandex Maps API](https://tech.yandex.ru/locator/doc/dg/api/json-docpage/);
 * [Google Geolocation API](https://developers.google.com/maps/documentation/geolocation/intro);
 * [Mozilla Geolocation API](https://mozilla.github.io/ichnaea/api/index.html).

# License
GNU General Public License version 3. You can find it [here](COPYING). External libraries can use another licenses, compatible with GNU GPLv3.

# Requirements
 * GNU/Linux (any modern distribution) with installed and enabled Network Manager;
 * Python 2.7 or 3.x;
 * python-networkmanager;
 * python-requests.

# Installation
No installation required. Just clone repository and set your own API keys:
 1. Clone this repository:
 ```bash
 git clone https://github.com/xvitaly/wloc.git wloc
 ```
 2. Get API keys from [Yandex](https://tech.yandex.ru/maps/keys/get/) or/and [Google](https://developers.google.com/maps/documentation/geolocation/get-api-key).
 3. Open `wloc/settings.py` file in any text editor and set received API keys.
 4. Run:
 ```bash
 ./wloc.py -y -g -m
 ```

# Available options
```
usage: wloc.py [-h] [--yandex] [--google] [--mozilla]
```

Optional arguments:
 * `-h` or `--help` - Show help message and exit;
 * `-y` or `--yandex` - Use Yandex Geolocation API;
 * `-g` or  `--google` - Use Google Geolocation API;
 * `-m` or  `--mozilla` - Use Mozilla Geolocation API.
