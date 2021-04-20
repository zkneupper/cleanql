#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python standard library
import pathlib
import re
import sys

# External packages
import click


def print_error(message):
    """Print with bold red text for failure messages to stderr"""
    message_red_bold = f"\x1b[1;31m{message}\x1b[0m"
    print(message_red_bold, file=sys.stderr, flush=True)


def check_filename_extension(filename):
    if not filename.suffix.lower() == ".sql":
        message = f"Invalid file type. `{filename}` is not a `.sql` file."
        print_error(message)
        exit(1)


def check_filename_exists(filename):
    if not filename.exists():
        message = f"File `{filename}` not found."
        print_error(message)
        exit(1)


@click.command()
@click.argument("filename")
def cli(filename):

    cwd = pathlib.Path.cwd()
    filename = pathlib.Path(filename)

    check_filename_extension(filename)
    check_filename_exists(filename)


if __name__ == "__main__":
    cli()
