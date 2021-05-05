# coding=utf-8

# SPDX-FileCopyrightText: 2015-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later


class Settings:
    """
    Class for working with application settings.
    """

    log_level: str = 'INFO'
    """
    Returns current log level.
    """

    log_format: str = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
    """
    Returns log format string.
    """
