"""Public package interface for stubsmith."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

from .core import add

try:
    __version__ = version("stubsmith")
except PackageNotFoundError:
    __version__ = "0.0.0+unknown"

__all__ = ["__version__", "add"]
