#!/usr/bin/env python
# -*- coding: utf-8 -*-


# External packages
import pytest

# Internal Modules
from capture_stderr import CaptureStderr

# Tested package
import cleanql


class TestPrintError:

    # Cases for test_print_error
    testdata = [
        ("Hello, World!", "\x1b[1;31mHello, World!\x1b[0m"),
        ("True", "\x1b[1;31mTrue\x1b[0m"),
        (True, "\x1b[1;31mTrue\x1b[0m"),
        ("False", "\x1b[1;31mFalse\x1b[0m"),
        (False, "\x1b[1;31mFalse\x1b[0m"),
        ("42", "\x1b[1;31m42\x1b[0m"),
        (42, "\x1b[1;31m42\x1b[0m"),
        ("-42", "\x1b[1;31m-42\x1b[0m"),
        (-42, "\x1b[1;31m-42\x1b[0m"),
        ("Goodbye, World!", "\x1b[1;31mGoodbye, World!\x1b[0m"),
    ]

    @pytest.mark.parametrize("message,expected_stderr", testdata)
    def test_check_filename_extension_fail(self, message, expected_stderr):

        with CaptureStderr() as output:
            cleanql.print_error(message)

        assert len(output) == 1
        assert output[0] == expected_stderr
