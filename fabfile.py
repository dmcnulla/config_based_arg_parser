"""Default fabfile for project tasks."""
from fabric.api import local, task


@task
def test():
    """Run tests for this project."""
    path = 'PYTHONPATH="$PYTHONPATH:.:./config_based_arg_parser/" '
    local(path + 'py.test -v --cov')
