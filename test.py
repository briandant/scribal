# -*- coding: utf-8 -*-

import sys
import os
my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, my_path + '/./')

from scribal import filter_for_files

# import pytest

CONTENT = """
# Header 1\n
This is some normal content.\n
## Header 2\n
This is some content.
"""

DIRNAME = 'datdir'
FILENAMES = ['fileA.md', 'fileB.md', 'fileC.md']


def _write_dummy_files():

    if not os.path.exists(DIRNAME):
        os.makedirs(DIRNAME)

    for f in FILENAMES:
        filename = os.path.join(DIRNAME, f)
        datfile = open(filename, 'w+')
        datfile.write(CONTENT)
        datfile.close()


def test_file_concat():
    """If I call the make_html_files function,
    I'll get a directory of only files."""

    extradir = 'extradirname'
    _write_dummy_files()

    dirname = os.path.join(DIRNAME, extradir)

    if not os.path.exists(dirname):
        os.makedirs(dirname)

    files = filter_for_files(DIRNAME)

    assert extradir not in files
    assert FILENAMES == files
