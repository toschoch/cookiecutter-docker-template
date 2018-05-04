from contextlib import contextmanager
import subprocess
import os

CCDS_ROOT = os.path.abspath(
    os.path.join(
        __file__,
        os.pardir,
        os.pardir
    )
)


def read(filename):
    with open(filename, 'r') as fp:
        s = fp.read()
    return s

@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


def test_project_tree(cookies):
    result = cookies.bake(template=CCDS_ROOT, extra_context={'project_slug': 'test_project'})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'test_project'
    assert read(result.project.join('README.md'))=="""Python Package
===============================
author: Your name

Overview
--------

A python package that can be installed with pip.


Change-Log
----------
##### 0.0.1
* initial version


Installation / Usage
--------------------
clone the repo:

```
git clone <git-url>
```
build the docker image
```
docker build . -t test_project
```

Example
-------

run a container of the image
```
docker run -v ... -p ... test_project
```"""
    assert os.path.exists(result.project.join("Dockerfile"))
