#!/usr/bin/env python2
# coding=utf-8


def main():
    try:
        # Querying Yandex...
        coords = query_yandex()

        # Showing result...
        print('Latitude: %s\nLongitude: %s\n' % (coords[0], coords[1]))

    except:
        # Exception detected...
        print('An error occurred while querying backend.')


if __name__ == '__main__':
    main()