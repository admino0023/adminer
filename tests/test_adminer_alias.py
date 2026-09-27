import importlib

import sherlock_project


def test_adminer_import_alias():
    adminer = importlib.import_module("adminer")

    assert adminer.__version__ == sherlock_project.__version__
    assert adminer.__shortname__ == "Adminer"
    assert adminer.__longname__.startswith("Adminer")
