"""Custom exceptions for the gprint module."""

from __future__ import annotations


class GprintError(Exception):
    """Base exception for all gprint-related errors."""


class InvalidRGBError(GprintError, ValueError):
    """Raised when an invalid RGB color value is provided.

    This error occurs when:
        - The RGB value doesn't contain exactly 3 components.
        - Any component is not an integer.
        - Any component is outside the 0-255 range.
    """
