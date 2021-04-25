#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from sql_formatter.formatter import (
    remove_nones,
    remove_empty_strings,
    split_sql,
    is_keyword,
    capitalize_if_keyword,
    capitalize_keywords,
    preserve_case,
    make_token_lower_case,
    apply_lower_case,
    format_indentation,
    remove_trailing_whitespace,
    format_sql,
)

from sql_formatter.cli import (
    read_file,
    write_file,
    print_error,
    check_filename_extension,
    check_filename_exists,
    cli,
)

from sql_formatter.preprocess_paths import (
    _paths_tuple_to_pathlib_list,
    _check_paths_exist,
    _expand_dirs,
    _preprocess_paths,
)
