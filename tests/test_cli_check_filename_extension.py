#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Python standard library
import pathlib
import sys

# External packages
import pytest

# Internal Modules
from capture_stderr import CaptureStderr

# Tested package
import cleanql


class TestCheckFilenameExtension:

    # Cases for test_check_filename_extension_pass
    testdata_pass = [
        ("filename.sql"),
        ("filename.SQL"),
        ("filename.Sql"),
        ("../query.sql"),
        ("../query.SQL"),
        ("../query.Sql"),
    ]

    # Cases for test_check_filename_extension_fail
    testdata_fail = [
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

    @pytest.mark.parametrize("filename", testdata_pass)
    def test_check_filename_extension_pass(self, capsys, filename):
        filename = pathlib.Path(filename)
        cleanql.check_filename_extension(filename, sys)
        captured = capsys.readouterr()

        assert captured.out == ""
        assert captured.err == ""

    @pytest.mark.parametrize("filename,expected_stderr", testdata_fail)
    def test_check_filename_extension_fail(self, capsys, filename, expected_stderr):
        filename = pathlib.Path(filename)

        with pytest.raises(SystemExit) as pytest_wrapped_e:
            with CaptureStderr() as output:
                cleanql.check_filename_extension(filename, sys)

        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == 1
        assert len(output) == 1

        # Last assert is failing
        assert output[0] == expected_stderr
