"""Test version."""
from split_words import __version__


def test_version():
    """Test version."""
    assert __version__.startswith("0.1")
