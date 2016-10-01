"""Practice processing arg configurations."""
# import sys
# import os
import argparse
import yaml
import json


def str2bool(str):
    """Return the boolean of the value submitted."""
    return json.loads(str)


def config_arg_parser(file_name):
    """Read arg yaml and process."""
    with open(file_name) as f:
        args = yaml.load(f)
    parser = argparse.ArgumentParser(description='Argument Parser')
    for key, value in args.items():
        print(key)
        print(value["help"])
        print(value["required"])
        parser.add_argument("--" + key,
                            required=str2bool(value["required"]),
                            help=value["help"])
    return parser
