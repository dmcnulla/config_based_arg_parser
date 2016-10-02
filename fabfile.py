"""Default fabfile for project tasks."""
from fabric.api import local, task


@task
def test():
    """Run tests for this project."""
    local('PYTHONPATH="$PYTHONPATH:." py.test -v --cov')
