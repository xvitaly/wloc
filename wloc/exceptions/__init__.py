# coding=utf-8

# SPDX-FileCopyrightText: 2015-2021 EasyCoding Team
#
# SPDX-License-Identifier: GPL-3.0-or-later


class BackendError(Exception):
    """
    Base class for the API backend errors.
    """


class PlatformError(Exception):
    """
    Base class for the platform-dependent errors.
    """


class PlatformNotSupported(PlatformError):
    """
    Base class for the unsupported platform errors.
    """
