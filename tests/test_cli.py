#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `cleanql` cli."""

import cleanql
import pytest
from click.testing import CliRunner


def test_cli_no_arguments():
    """Test the `cleanql` CLI with no arguments or options passed."""
    expected_result = "No Path provided. Nothing to do 😴\n"
    runner = CliRunner()
    result = runner.invoke(cleanql.cli)
    assert result.exit_code == 0
    assert result.output == expected_result


@pytest.mark.parametrize("help_flag", ["-h", "--help"])
def test_cli_help(help_flag):
    """Test the `cleanql` help doesn't error."""
    expected_substrings = [
        "The uncompromising SQL formatter.",
        "Pass path(s) to SQL file(s) or folder(s) that contain(s) SQL files.",
        "-f, --flavor [COMMON|HQL|ORACLE|POSTGRESQL]",
        "-v, --verbose",
    ]

    runner = CliRunner()
    result = runner.invoke(cleanql.cli, [help_flag])
    assert result.exit_code == 0
    for substring in expected_substrings:
        assert substring in result.output


################################################################################
################################################################################
################################################################################
################################################################################

# def test_command_line_interface():
#     """Test the CLI."""
#     runner = CliRunner()
#     # result = runner.invoke(cli.main)
#     result = runner.invoke(cleanql.cli)
#     assert result.exit_code == 0
#     # assert "cleanql.cli.main" in result.output
#     assert "cleanql.cli" in result.output
#     help_result = runner.invoke(cli.main, ["--help"])
#     assert help_result.exit_code == 0
#     assert "--help  Show this message and exit." in help_result.output


# @pytest.fixture
# def response():
#     """Sample pytest fixture.

#     See more at: http://doc.pytest.org/en/latest/fixture.html
#     """
#     # import requests
#     # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


# def test_content(response):
#     """Sample pytest test function with the pytest fixture as an argument."""
#     # from bs4 import BeautifulSoup
#     # assert 'GitHub' in BeautifulSoup(response.content).title.string


# def test_command_line_interface():
#     """Test the CLI."""
#     runner = CliRunner()
#     # result = runner.invoke(cli.main)
#     result = runner.invoke(cleanql.cli)
#     assert result.exit_code == 0
#     # assert "cleanql.cli.main" in result.output
#     assert "cleanql.cli" in result.output
#     help_result = runner.invoke(cli.main, ["--help"])
#     assert help_result.exit_code == 0
#     assert "--help  Show this message and exit." in help_result.output
