"""Adminer compatibility module.

The project continues to use the existing Sherlock codebase for behavior,
while exposing the Adminer identity to the package metadata and entry points.
"""

from importlib.metadata import version as pkg_version, PackageNotFoundError
import pathlib
import tomli


def get_version() -> str:
    """Fetch the version number of the installed package."""
    try:
        return pkg_version("adminer")
    except PackageNotFoundError:
        try:
            return pkg_version("sherlock_project")
        except PackageNotFoundError:
            pyproject_path: pathlib.Path = pathlib.Path(__file__).resolve().parent.parent / "pyproject.toml"
            with pyproject_path.open("rb") as f:
                pyproject_data = tomli.load(f)
            return pyproject_data["tool"]["poetry"]["version"]

# This variable is only used to check for ImportErrors induced by users running as script rather than as module or package
import_error_test_var = None

__shortname__   = "Adminer"
__longname__    = "Adminer: Find Usernames Across Online Services"
__version__     = get_version()

forge_api_latest_release = "https://api.github.com/repos/adminer/adminer/releases/latest"
