"""Set up the package."""

from setuptools import setup, find_packages

print(find_packages())
setup(name='ConfBasedArgParser',
      version='0.1.0',
      description='Configuation-based Arg Parser',
      author='Dave McNulla',
      author_email='mcnulla@gmail.com',
      url='https://github.com/dmcnulla/config_based_arg_parser',
      packages=find_packages(),
      )
