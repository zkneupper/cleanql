#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Python standard library
import pathlib


def _paths_tuple_to_pathlib_list(paths):

    # paths will be a tuple, because nargs=-1

    # Check if paths is an empty tuple
    if not paths:
        paths = [pathlib.Path.cwd()]

    # Convert tuple [of strings] to list of pathlib paths
    paths = [pathlib.Path(p).resolve() for p in paths]

    return paths


def _check_paths_exist(paths):
    """paths: list of pathlib paths"""
    assert all([p.exists() for p in paths])


def _expand_dirs(paths):

    paths_output = list()

    for path in paths:
        if path.is_dir():
            paths_output += list(path.rglob("*.[sS][qQ][lL]"))
        elif path.is_file():
            paths_output.append(path)

    # Unique values, sorted alphabetically
    paths_output = sorted(set(paths_output))

    return paths_output


def _preprocess_paths(paths):
    paths = _paths_tuple_to_pathlib_list(paths)
    _check_paths_exist(paths)
    paths = _expand_dirs(paths)
    return paths
