# coding=utf-8

# SPDX-FileCopyrightText: 2015-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

import logging
import sys

from .settings import Settings
from ..app import App


def setup_log() -> None:
    """
    Setup root logger of the application.
    """
    root = logging.getLogger()
    root.setLevel(Settings.log_level)
    e_handler = logging.StreamHandler(sys.stdout)
    e_handler.setFormatter(logging.Formatter(Settings.log_format))
    root.addHandler(e_handler)


def main():
    """
    The main entry point of the application.
    """
    try:
        setup_log()
        App().run()
    except Exception as ex:
        print(f'An error occurred while running application: {ex}')


if __name__ == '__main__':
    main()
