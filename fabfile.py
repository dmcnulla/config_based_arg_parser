from fabric.api import local, task


@task
def hello():
    print('hello world')


@task
def test():
    local('nosetests -v --with-coverage --cover-erase')


@task
def pytest():
    local('py.test -v --cov')


@task
def test2():
    local('nosetests -v --with-coverage --cover-erase trial.py')


@task
def pytest2():
    local('py.test -v --cov trial.py')
