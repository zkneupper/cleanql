#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Python standard library
import pathlib
import re

# External packages
import sqlparse


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


def format_indentation(sql):

    format_kwargs = {
        "keyword_case": "upper",
        "identifier_case": "lower",
        "strip_comments": False,
        "use_space_around_operators": True,
        "comma_first": False,
        "reindent": True,
        "indent_width": 4,
        "indent_tabs": False,
        "indent_columns": True,
        "strip_whitespace": True,
    }

    sql_output = sql

    # Formatting sometimes doesn't work if you only run it once
    for _ in range(5):
        sql_output = sqlparse.format(sql_output, **format_kwargs)

    return sql_output


def format_sql(sql):

    sql_output = format_indentation(sql)

    return sql_output
