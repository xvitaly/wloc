# Using application

## Running application

Forward [API tokens](api-tokens.md) as environment variables, then run application:

```bash
export APIKEY_YANDEX=SAMPLE
export APIKEY_GOOGLE=SAMPLE
export APIKEY_MOZILLA=SAMPLE
wloc -y -g -m
```

## Command-line options

```
usage: wloc [-h] [--yandex] [--google] [--mozilla]
```

Optional arguments:

  * `-h` or `--help` - show this help message and exit;
  * `-g` or  `--google` - use the Google Geolocation API;
  * `-m` or  `--mozilla` - use the Mozilla Geolocation API;
  * `-y` or `--yandex` - use the Yandex.Locator API.
