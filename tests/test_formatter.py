#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Python standard library
import sys

# External packages
import pytest

# import formatter


# print(dir(formatter))


def test_print_error(capsys):
    print("hello")
    sys.stderr.write("world\n")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
    assert captured.err == "world\n"
    print("next")
    captured = capsys.readouterr()
    assert captured.out == "next\n"
