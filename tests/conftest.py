"""Shared fixtures for gprint tests."""

from __future__ import annotations

import pytest


@pytest.fixture()
def ansi_prefix() -> str:
    """Return the ANSI true-color escape prefix."""
    return "\033[38;2;"


@pytest.fixture()
def ansi_reset() -> str:
    """Return the ANSI reset escape code."""
    return "\033[0m"
