# Running tests

Clone this repository:
```bash
git clone https://github.com/xvitaly/wloc.git wloc
```

Forward [API tokens](api-tokens.md) as environment variables.

Forward [test suite](test-suite-file.md) file name using `SUITE_FILENAME` environment variable.

Run tests using Python 3:
```bash
cd wloc
export SUITE_FILENAME=/path/to/example.json
export APIKEY_YANDEX=SAMPLE
export APIKEY_GOOGLE=SAMPLE
export APIKEY_MOZILLA=SAMPLE
python3 setup.py test
```
