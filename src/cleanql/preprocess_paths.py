#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Python standard library
import functools
import pathlib
import sys

# External packages
import click


out = functools.partial(click.secho, bold=True, err=True)


def _check_if_path_provided(paths, ctx: click.Context):
    # paths will be a tuple, because nargs=-1
    if not paths:
        # print("No Path provided. Nothing to do 😴", flush=True)
        out("No Path provided. Nothing to do 😴")
        ctx.exit(0)


def _paths_tuple_to_pathlib_list(paths):

    # paths will be a tuple, because nargs=-1

    # Convert tuple [of strings] to list of pathlib paths
    paths = [pathlib.Path(p).resolve() for p in paths]

    return paths


def _check_paths_exist(paths):
    """paths: list of pathlib paths"""
    assert all(p.exists() for p in paths)


def _expand_dirs(paths):

    paths_output = []

    for path in paths:
        if path.is_dir():
            paths_output += list(path.rglob("*.[sS][qQ][lL]"))
        elif path.is_file():
            paths_output.append(path)

    # Unique values, sorted alphabetically
    paths_output = sorted(set(paths_output))

    return paths_output


def _preprocess_paths(paths, ctx: click.Context):
    _check_if_path_provided(paths, ctx)
    paths = _paths_tuple_to_pathlib_list(paths)
    _check_paths_exist(paths)
    paths = _expand_dirs(paths)
    return paths
