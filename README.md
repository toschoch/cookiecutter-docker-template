Cookiecutter Docker Template
============================
author: Tobias Schoch

Overview
--------

Cookiecutter template for new docker projects providing a compatible README.md to use with toschoch/python-gittools.

Requirements
------------
Install `cookiecutter` command line: `pip install cookiecutter`    

Change-Log
----------
##### 0.0.3
* added .drone.yml to backed project
* added tagging functionality to template
* fixed jenkinsfile
* fixed bake test
* stupid jenkins user
* fixed pip -r in jenkinsfile
* added jenkins ci/cd files

##### 0.0.2
* fixed default cookiecutter values
* added basic tests
* update readme
* added dockerfile and compatible readme

##### 0.0.1
* initial version

Installation / Usage
--------------------
Create project from template with cookiecutter
```
cookiecutter git+https://github.com/toschoch/cookiecutter-docker-template.git
```
