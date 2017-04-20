"""Test the dtoolutils package."""


def test_version_is_string():
    import dtoolutils
    assert isinstance(dtoolutils.__version__, str)
