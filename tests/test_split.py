"""Test split."""
from split_words import Splitter

splitter = Splitter()


def test_split():
    """Test split."""
    res = splitter.split_compound("Behördenangaben")

    assert res[0][0] > 0.8
    assert "Beh" in res[0][1]
    assert "ang" not in res[0][1].lower()

    assert "Ang" in res[0][2]
    assert "beh" not in res[0][2].lower()
