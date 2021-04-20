#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pathlib
import re


def remove_nones(iterable):
    return (x for x in iterable if x is not None)


def remove_empty_strings(iterable):
    return (x for x in iterable if x != "")


def split_sql(sql):
    pattern = "(\-\-.+\n)|(\".+\")|('.+')|(\$\{.+\})|(\W)"
    tokens = re.split(pattern, sql)
    tokens = remove_nones(tokens)
    tokens = remove_empty_strings(tokens)
    tokens = list(tokens)
    return tokens
