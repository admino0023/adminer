#!/usr/bin/env python3

"""Adminer entry point.

This package keeps the original Sherlock implementation but exposes the Adminer
CLI name for compatibility and new package installs.
"""

from sherlock_project.__main__ import *  # noqa: F401,F403


def main() -> None:
    from sherlock_project import sherlock
    sherlock.main()


if __name__ == "__main__":
    main()
