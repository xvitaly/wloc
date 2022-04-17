# Test suite file

## Example

JSON file example:

```json
[
    [
        ["AA:BB:CC:DD:EE:FF", 90],
        ["FF:EE:DD:CC:BB:AA", 87]
    ],
    [11.123456, 22.123456]
]
```

## Format specification

### First list

Each list entry must contains BSSID (Wi-Fi station hardware address) and signal strength in percents.

Example:

  * `AA:BB:CC:DD:EE:FF` - BSSID (station hardware address);
  * `90` - signal strength in percents (90%).

### Second list

Second list contains master coordinates. Received from API data will be compared with them.

Type: **float** with **dot** as delimeter.
