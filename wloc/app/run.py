# coding=utf-8

# SPDX-FileCopyrightText: 2015-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

from wloc.app import App


def main():
    """
    The main entry point of the application.
    """
    try:
        app = App()
        app.run()
    except Exception as ex:
        print(f'An error occurred while running application: {ex}')


if __name__ == '__main__':
    main()
