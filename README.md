# Wi-Fi geolocation tool
Locate user by using global Wi-Fi database from Yandex or/and Google (not implemented yet).

# License
GNU General Public License version 3. You can find it here: https://www.gnu.org/licenses/gpl.html. External libraries can use another licenses, compatible with GNU GPLv3.

# Requirements
 * GNU/Linux;
 * Network Manager;
 * Python 2.7 or 3.x;
 * python-networkmanager;
 * python-lxml.

# Installation
 1. [Get API key](https://tech.yandex.ru/maps/keys/get/) from Yandex.
 2. Clone this repository:
 ```bash
 git clone https://github.com/xvitaly/wloc.git wloc
 ```
 3. Open `wloc/settings.py` in any text editor and set your API keys.
 4. Run:
 ```bash
 cd wloc
 ./wloc.py
 ```
