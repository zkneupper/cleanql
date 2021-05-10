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


def is_keyword(string, sql_keywords):
    return string.upper() in sql_keywords


def capitalize_if_keyword(string, sql_keywords):
    if is_keyword(string, sql_keywords):
        return string.upper()
    else:
        return string


def capitalize_keywords(sql, sql_keywords):
    tokens = split_sql(sql)
    tokens_keywords_capitalized = [
        capitalize_if_keyword(token, sql_keywords) for token in tokens
    ]
    return "".join(tokens_keywords_capitalized)


def preserve_case(string):
    pattern = "(\-\-.+\n)|(\".+\")|('.+')"  # |(\$\{.+\})|(\W)"
    return bool(re.fullmatch(pattern, string))


def make_token_lower_case(string, sql_keywords):
    if preserve_case(string):
        return string
    elif is_keyword(string, sql_keywords):
        return string
    else:
        return string.lower()


def apply_lower_case(sql, sql_keywords):
    tokens = split_sql(sql)
    tokens_lowered = [make_token_lower_case(token, sql_keywords) for token in tokens]
    return "".join(tokens_lowered)


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


def remove_trailing_whitespace(string):
    string_output = (x.rstrip() for x in string.split("\n"))
    string_output = "\n".join(string_output)
    return string_output


def format_sql(sql, sql_keywords=None):

    if sql_keywords is None:
        set_keywords = set(sqlparse.keywords.KEYWORDS.keys())
        set_keywords_common = set(sqlparse.keywords.KEYWORDS_COMMON.keys())
        set_keywords = set_keywords.union(set_keywords_common)
        set_keywords = [x.upper() for x in set_keywords]
        sql_keywords = set_keywords

    sql_output = sql
    sql_output = format_indentation(sql_output)

    sql_output = apply_lower_case(sql_output, sql_keywords)
    sql_output = capitalize_keywords(sql_output, sql_keywords)

    sql_output = remove_trailing_whitespace(sql_output)

    return sql_output
