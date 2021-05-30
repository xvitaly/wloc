# About API tokens

This library use API tokens from following third-party geolocation providers:

  * Google Geolocation;
  * Mozilla Geolocation;
  * Yandex.Locator.

# Getting API tokens

In order to use this library, you need to receive API tokens:

  * [Google](https://developers.google.com/maps/documentation/geolocation/get-api-key);
  * [Mozilla](https://ichnaea.readthedocs.io/en/latest/api/index.html);
  * [Yandex](https://yandex.ru/dev/locator/doc/dg/api/geolocation-api.html).

# Forwarding API tokens to library

Library need at least one token from supported providers, forwarded as parameter:

  * `gg_apikey` - Google Geolocation;
  * `mm_apikey` - Mozilla Geolocation;
  * `ya_apikey` - Yandex.Locator.

# Forwarding API tokens to application and tests

Application need at least one token from supported providers, forwarded as environment variables:

  * `APIKEY_GOOGLE` - Google Geolocation;
  * `APIKEY_MOZILLA` - Mozilla Geolocation;
  * `APIKEY_YANDEX` - Yandex.Locator.
