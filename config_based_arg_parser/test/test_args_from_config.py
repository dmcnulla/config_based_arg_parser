"""Test args_from_config."""
import pytest
from config_based_arg_parser import ArgParser


def test_args_from_config_default_filename():
    """Test using the default config file name."""
    p = ArgParser()
    assert isinstance(p, ArgParser)


def test_args_from_config_supply_filename():
    """Test using a supplied config file name."""
    arg_file = 'config_based_arg_parser/test/data/args.yaml'
    p = ArgParser(arg_file)
    assert isinstance(p, ArgParser)


def test_args_from_bad_config_file():
    """Test using a config file with bad entries."""
    with pytest.raises(KeyError):
        arg_file = 'config_based_arg_parser/test/data/bad_args.yaml'
        ArgParser(arg_file)


def test_args_from_missing_config_file():
    """Test using a supplied config file name that does not exist."""
    with pytest.raises(IOError):
        arg_file = 'missing.yaml'
        ArgParser(arg_file)
