% wloc(1) | General Commands Manual

# NAME

wloc - command-line Wi-Fi geolocation tool

# SYNOPSIS

**wloc** \[-h\] \[--google\] \[--mozilla\] \[--yandex\]

# DESCRIPTION

WLoc is a simple command-line Wi-Fi geolocation tool, which can be used to locate user by using global Wi-Fi database (no GPS required).

# COMMAND-LINE OPTIONS

#### -g, \-\-google
Use the Google Geolocation API.

#### -m, \-\-mozilla
Use the Mozilla Geolocation API.

#### -y, \-\-yandex
Use the Yandex.Locator API.

#### -h, \-\-help
Print help message and exit.

# ENVIRONMENT OPTIONS

WLoc supports of getting API tokens for the third-party geolocation backends with environment variables.

## Supported options

In order to use this application, you need to forward at least one API token:

  * **APIKEY_GOOGLE** - Google Geolocation.
  * **APIKEY_MOZILLA** - Mozilla Geolocation.
  * **APIKEY_YANDEX** - Yandex.Locator.

## Forwarding options

Export environment variables using `export` command:

```
export APIKEY_GOOGLE=ABCDEFG123
export APIKEY_MOZILLA=ABCDEFG123
export APIKEY_YANDEX=ABCDEFG123
```

Start the application with all available backends:

```
wloc -g -m -y
```

# BACKENDS

## Supported backends

This application can use the following third-party geolocation providers:

  * Google Geolocation;
  * Mozilla Geolocation;
  * Yandex.Locator.

## API tokens

You can obtain API tokens from these sources:

  * **Google**: https://developers.google.com/maps/documentation/geolocation/get-api-key
  * **Mozilla**: https://ichnaea.readthedocs.io/en/latest/api/index.html
  * **Yandex**: https://yandex.ru/dev/locator/doc/dg/api/geolocation-api.html

# AUTHORS

Copyright (c) 2015-2022 EasyCoding Team.
