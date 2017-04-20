"""Test the mimetype overlay functionality."""

import os

from . import tmp_dataset_fixture  # NOQA


def test_mimetype_overlay(tmp_dataset_fixture):  # NOQA
    from dtoolutils.overlays import add_mimetype

    assert "mimetype" not in tmp_dataset_fixture.overlays

    add_mimetype(tmp_dataset_fixture)

    assert "mimetype" in tmp_dataset_fixture.overlays

    expected_mimetypes = {
        'actually_a_png.txt': 'image/png',
        'actually_a_text_file.jpg': 'text/plain',
        'another_file.txt': 'text/plain',
        'empty_file': 'inode/x-empty',
        'random_bytes': 'application/octet-stream',
        'real_text_file.txt': 'text/plain',
        'tiny.png': 'image/png'
    }

    mimetype_overlay = tmp_dataset_fixture.overlays["mimetype"]

    for i in tmp_dataset_fixture.identifiers:
        fpath = tmp_dataset_fixture.item_path_from_hash(i)
        fname = os.path.basename(fpath)
        actual = mimetype_overlay[i]
        expected = expected_mimetypes[fname]
        assert expected == actual
