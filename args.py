"""Practice processing arg configurations."""
import argparse
import yaml


def args_from_config(file_name='args.yaml'):
        """Read arg yaml and process."""
        with open(file_name) as f:
            args = yaml.load(f)

        parser = argparse.ArgumentParser(prog=args['prog'],
                                         description=args['description'],
                                         epilog=args['epilog'])
        for name, value in args['arguments'].items():
            parser.add_argument("--" + name,
                                required=value["required"],
                                help=value["help"])
        return parser
