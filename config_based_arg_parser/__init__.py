"""Practice processing arg configurations."""
import argparse
import yaml


class ArgParser():
    """Create a config-based arg parser."""

    def __init__(self, file_name='args.yaml'):
        """Read arg yaml then create arg parser."""
        with open(file_name) as f:
            args = yaml.load(f)

        self.parser = argparse.ArgumentParser(prog=args['prog'],
                                              description=args['description'],
                                              epilog=args['epilog'])
        for name, value in args['arguments'].items():
            self.parser.add_argument("--" + name,
                                     required=value["required"],
                                     help=value["help"])

    def parse(self):
        """Parse the arguments now."""
        self.parser.parse_args()
