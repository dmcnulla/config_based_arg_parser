"""Test args_from_config."""
import pytest
import argparse
from config_based_arg_parser import args_from_config


def test_args_from_config_default_filename():
    """Test using the default config file name."""
    p = args_from_config()
    assert isinstance(p, argparse.ArgumentParser)


def test_args_from_config_supply_filename():
    """Test using a supplied config file name."""
    p = args_from_config('config_based_arg_parser/test/data/args.yaml')
    assert isinstance(p, argparse.ArgumentParser)


def test_args_from_bad_config_file():
    """Test using a config file with bad entries."""
    with pytest.raises(KeyError):
        args_from_config('config_based_arg_parser/test/data/bad_args.yaml')


def test_args_from_missing_config_file():
    """Test using a supplied config file name that does not exist."""
    with pytest.raises(IOError):
        args_from_config('config_based_arg_parser/test/data/doesnt_exist_args.yaml')
