#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Python standard library
import pathlib
import sys

# External packages
import click

# Internal modules
import formatter
import handle_paths_input


def read_file(filepath):
    with open(filepath, "r") as file:
        text = file.read()
    return text


def write_file(filepath, text):
    with open(filepath, "w") as file:
        file.write(text)


def print_error(message):
    """Print with bold red text for failure messages to stderr"""
    message_red_bold = f"\x1b[1;31m{message}\x1b[0m"
    print(message_red_bold, file=sys.stderr, flush=True)


def check_filename_extension(filename):
    if not filename.suffix.lower() == ".sql":
        message = f"Invalid file type. `{filename}` is not a `.sql` file."
        print_error(message)
        sys.exit(1)


def check_filename_exists(filename):
    if not filename.exists():
        message = f"File `{filename}` not found."
        print_error(message)
        sys.exit(1)


# Handle multiple files
# .
# or
# no arg


# @click.command()
# @click.argument("filename")
# def cli(filename):

# @click.command()
# @click.argument("path")#, nargs=-1,)


@click.command()
@click.argument("paths", nargs=-1)
def cli(paths):

    # paths will be a tuple, because nargs=-1
    # Convert tuple to list ; list of pathlib paths
    paths = handle_paths_input._preprocess_paths(paths)

    # print(f"paths:\t{paths}")
    # print(f"type(paths):\t{type(paths)}")
    # print(f"bool(paths):\t{bool(paths)}")

    pass

    for filepath in paths:

        check_filename_extension(filepath)
        check_filename_exists(filepath)

        sql = read_file(filepath)

        # print("Before:\n")
        # print(sql)

        sql_output = formatter.format_sql(sql, sql_keywords=None)

        if sql == sql_output:
            print(f"Unchanged: {filepath}")
        else:
            print(f"Formatted: {filepath}")

        # print("\nAfter:\n")
        # print(sql_output)
        # print("\n")

        write_file(filepath, sql_output)


if __name__ == "__main__":
    cli()
