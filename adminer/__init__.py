"""Adminer package wrapper.

This provides the new package name while delegating execution to the original
Sherlock implementation that remains in the repository.
"""

from sherlock_project import __longname__, __shortname__, __version__, forge_api_latest_release

__all__ = ["__longname__", "__shortname__", "__version__", "forge_api_latest_release"]
