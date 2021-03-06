"""Test the mimetype overlay functionality."""

import os

from . import tmp_dataset_fixture  # NOQA


def test_add_mimetype_overlay(tmp_dataset_fixture):  # NOQA
    from dtoolutils.overlays import add_mimetype

    # Work around issue with git not storing empty directories.
    overlays_dir = os.path.join(
        tmp_dataset_fixture._abs_path,
        ".dtool",
        "overlays")
    if not os.path.isdir(overlays_dir):
        os.mkdir(overlays_dir)

    assert "mimetype" not in tmp_dataset_fixture.access_overlays()

    add_mimetype(tmp_dataset_fixture)

    assert "mimetype" in tmp_dataset_fixture.access_overlays()

    expected_mimetypes = {
        'actually_a_png.txt': 'image/png',
        'actually_a_text_file.jpg': 'text/plain',
        'another_file.txt': 'text/plain',
        'empty_file': 'inode/x-empty',
        'random_bytes': 'application/octet-stream',
        'real_text_file.txt': 'text/plain',
        'tiny.png': 'image/png'
    }

    mimetype_overlay = tmp_dataset_fixture.access_overlays()["mimetype"]
    assert len(mimetype_overlay) == 7

    for i in tmp_dataset_fixture.identifiers:
        fpath = tmp_dataset_fixture.abspath_from_identifier(i)
        fname = os.path.basename(fpath)
        actual = mimetype_overlay[i]
        expected = expected_mimetypes[fname]
        assert expected == actual


def test_add_mimetype_overlay_does_not_raise_when_called_more_than_once(tmp_dataset_fixture):  # NOQA
    from dtoolutils.overlays import add_mimetype

    # Work around issue with git not storing empty directories.
    overlays_dir = os.path.join(
        tmp_dataset_fixture._abs_path,
        ".dtool",
        "overlays")
    if not os.path.isdir(overlays_dir):
        os.mkdir(overlays_dir)

    assert "mimetype" not in tmp_dataset_fixture.access_overlays()

    add_mimetype(tmp_dataset_fixture)
    assert "mimetype" in tmp_dataset_fixture.access_overlays()
    add_mimetype(tmp_dataset_fixture)
