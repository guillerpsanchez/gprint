"""Shim for legacy ``python setup.py`` invocations.

All project metadata is defined in ``pyproject.toml``.
This file exists only for backward compatibility with tools that do not yet
support PEP 517 / PEP 621.
"""

from setuptools import setup

setup()

