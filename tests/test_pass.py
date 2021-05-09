#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Python standard library
import sys

# External packages
import pytest

import cleanql


def test_pass():
    "Passing test"
    assert True


# def test_print_error(capsys):
#     print("hello")
#     sys.stderr.write("world\n")
#     captured = capsys.readouterr()
#     assert captured.out == "hello\n"
#     assert captured.err == "world\n"
#     print("next")
#     captured = capsys.readouterr()
#     assert captured.out == "next\n"


# def test_print_error(capsys):
#     assert False


# def remove_nones(iterable):
#     return (x for x in iterable if x is not None)


# def remove_empty_strings(iterable):
#     return (x for x in iterable if x != "")


# def split_sql(sql):
#     pattern = "(\-\-.+\n)|(\".+\")|('.+')|(\$\{.+\})|(\W)"
#     tokens = re.split(pattern, sql)
#     tokens = remove_nones(tokens)
#     tokens = remove_empty_strings(tokens)
#     tokens = list(tokens)
#     return tokens
