#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Python standard library
import io
import pathlib
import subprocess
import sys

# External packages
import pytest

# Tested package
import sql_formatter


class CaptureStderr(list):
    """A context manager for capturing stderr"""

    def __enter__(self):
        self._stderr = sys.stderr
        sys.stderr = self._stringio = io.StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stderr = self._stderr


# Cases for test_check_filename_extension_pass
testdata = [
    ("filename.sql"),
    ("filename.SQL"),
    ("filename.Sql"),
    ("../query.sql"),
    ("../query.SQL"),
    ("../query.Sql"),
]


@pytest.mark.parametrize("filename", testdata)
def test_check_filename_extension_pass(capsys, filename):
    filename = pathlib.Path(filename)
    sql_formatter.check_filename_extension(filename)
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""


# Cases for test_check_filename_extension_fail
testdata = [
    (
        "filename.txt",
        "\x1b[1;31mInvalid file type. `filename.txt` is not a `.sql` file.\x1b[0m",
    ),
    (
        "query.sql_2",
        "\x1b[1;31mInvalid file type. `query.sql_2` is not a `.sql` file.\x1b[0m",
    ),
    (
        "badfile.py",
        "\x1b[1;31mInvalid file type. `badfile.py` is not a `.sql` file.\x1b[0m",
    ),
    (
        "$ecretpassword123",
        "\x1b[1;31mInvalid file type. `$ecretpassword123` is not a `.sql` file.\x1b[0m",
    ),
    (".", "\x1b[1;31mInvalid file type. `.` is not a `.sql` file.\x1b[0m"),
    ("..", "\x1b[1;31mInvalid file type. `..` is not a `.sql` file.\x1b[0m"),
]


@pytest.mark.parametrize("filename,expected_stderr", testdata)
def test_check_filename_extension_fail(capsys, filename, expected_stderr):
    filename = "filename.txt"
    expected_stderr = (
        "\x1b[1;31mInvalid file type. `filename.txt` is not a `.sql` file.\x1b[0m"
    )

    filename = pathlib.Path(filename)

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        with CaptureStderr() as output:
            sql_formatter.check_filename_extension(filename)

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1
    assert len(output) == 1
    assert output[0] == expected_stderr
