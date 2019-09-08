#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `imperial_walker` package."""

import pytest
from click.testing import CliRunner

from imperial_walker import cli
from imperial_walker.walker import ScoutWalker, Walker

# @pytest.fixture
# def response():
#     """Sample pytest fixture.

#     See more at: http://doc.pytest.org/en/latest/fixture.html
#     """
#     # import requests
#     # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_walker_lists_leaves():
    data = {"a": 1, "b": [{"c": 2, "d": 3}], "e": {"f": 4}}
    walker = Walker()
    result = list(walker.walk(data))
    assert sorted(result) == [1, 2, 3, 4]


def test_walker_works_with_tuples():
    data = {"a": 1, "b": ({"c": 2, "d": 3}), "e": {"f": 4}}
    walker = Walker()
    result = list(walker.walk(data))
    assert sorted(result) == [1, 2, 3, 4]


def test_scout_walker_lists_leaf_paths():

    data = {"a": 1, "b": [{"c": 2, "d": 3}], "e": {"f": 4}}
    walker = ScoutWalker()
    result = list(walker.walk(data))
    assert sorted(result) == [".a", ".b[].c", ".b[].d", ".e.f"]


def test_scout_walker_lists_leaf_paths_separately():

    data = {"b": [{"c": 2, "d": 3}, {"c": 22, "g": 5}]}
    walker = ScoutWalker()
    result = list(walker.walk(data))
    assert sorted(result) == [".b[].c", ".b[].d", ".b[].c", ".b[].g"]


# def test_command_line_interface():
#     """Test the CLI."""
#     runner = CliRunner()
#     result = runner.invoke(cli.main)
#     assert result.exit_code == 0
#     assert 'imperial_walker.cli.main' in result.output
#     help_result = runner.invoke(cli.main, ['--help'])
#     assert help_result.exit_code == 0
#     assert '--help  Show this message and exit.' in help_result.output
