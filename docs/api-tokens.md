# About API tokens

This library use API tokens from following third-party geolocation provides:

  * Yandex.Locator;
  * Google Geolocation;
  * Mozilla Geolocation.

# Getting API tokens

In order to use this library, you need to receive API tokens:

  * [Yandex](https://tech.yandex.ru/maps/keys/get/);
  * [Google](https://developers.google.com/maps/documentation/geolocation/get-api-key);
  * [Mozilla](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API).

# Forwarding API tokens to library

Library need at least one token from supported providers, forwarded as parameter:

  * `ya_apikey` - Yandex.Locator;
  * `gg_apikey` - Google Geolocation;
  * `mm_apikey` - Mozilla Geolocation.

# Forwarding API tokens to application

Application need at least one token from supported providers, forwarded as environment variables:

  * `APIKEY_YANDEX` - Yandex.Locator;
  * `APIKEY_GOOGLE` - Google Geolocation;
  * `APIKEY_MOZILLA` - Mozilla Geolocation.
