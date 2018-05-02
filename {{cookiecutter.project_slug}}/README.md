{{ cookiecutter.project_name }}
===============================
author: {{ cookiecutter.full_name }}

Overview
--------

{{ cookiecutter.description }}


Change-Log
----------
##### {{ cookiecutter.version }}
* initial version


Installation / Usage
--------------------
clone the repo:

```
git clone <git-url>
```
build the docker image
```
docker build . -t {{ cookiecutter.project_slug }}
```

Example
-------

run a container of the image
```
docker run -v ... -p ... {{ cookiecutter.project_slug }}
```