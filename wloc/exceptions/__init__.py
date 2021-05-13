# coding=utf-8

# SPDX-FileCopyrightText: 2015-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later

__all__ = ['BackendError', 'MissingTokenError', 'NetworksNotFoundError', 'PlatformError', 'PlatformNotSupported']


class BackendError(Exception):
    """
    Base class for the API backend errors.
    """


class MissingTokenError(Exception):
    """
    Base class for the missing API tokens events.
    """


class NetworksNotFoundError(Exception):
    """
    Base class for the missing wireless nerworks events.
    """


class PlatformError(Exception):
    """
    Base class for the platform-dependent errors.
    """


class PlatformNotSupported(PlatformError):
    """
    Base class for the unsupported platform errors.
    """
