"""Smoke tests so CI has a real tests/ target (flake8 + pytest).

These are deliberately import-light: they must pass in CI before the heavier
suites (which need config/keys) are wired up.
"""


def test_sanity():
    assert 1 + 1 == 2


def test_src_layout_present():
    """The src/ package the app imports from should exist."""
    import os

    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    assert os.path.isdir(os.path.join(here, "src")), "expected a src/ directory"
