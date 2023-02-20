<!--
    =====================================
    generator=datazen
    version=3.1.0
    hash=5fe794c2a39253238c435bba61f7aaad
    =====================================
-->

# python-package-template

![Build Status](https://github.com/vkottler/python-package-template/workflows/Build%20Template/badge.svg)

*This is a template intended to be used with
[Cookiecutter](https://github.com/cookiecutter/cookiecutter).*

# Usage

Invoke `cookiecutter` and fill out information about your project:

```
$ cookiecutter git@github.com:vkottler/python-package-template.git
name [Vaughn Kottler]: <Your Name>
email [vaughnkottler@gmail.com]: <your@email.com>
...
```

## Platform Support

This template is tested on the following platforms:

* `macos-latest`
* `windows-latest`
* `ubuntu-latest`

and Python versions:

* `python3.7`
* `python3.8`
* `python3.9`
* `python3.10`

## Structure

The resulting template is a [git](https://git-scm.com/) repository with a
[config](https://github.com/vkottler/config) repository added as a top-level
[submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

Once the base template is generated,
[datazen](https://github.com/vkottler/datazen) runs because this package uses
it for many useful code generation and other static file generation tasks.

The package is then linted, statically analyzed, tested and built into
a distribution using [vmklib](https://github.com/vkottler/vmklib). These are
the core tasks that will be performed regularly during the package's
life-cycle, so their initial success demonstrates that the package is already
in a clean state and doesn't require additional boilerplate or setup. Simply
begin adding code and continuing to perform these workflow tasks.

```
$ tree -a -I venv*|__pycache__|dist|*cov*|*-out|config|build|*.egg-info|tags|.git*|.*cache* -- package-name

package-name
├── .flake8
├── im
│   └── pydeps.svg
├── .isort.cfg
├── LICENSE
├── local
│   ├── configs
│   │   ├── license.yaml
│   │   ├── package.yaml
│   │   └── python.yaml
│   ├── templates
│   │   └── README.md.j2
│   └── variables
│       └── package.yaml
├── Makefile
├── manifest.yaml
├── mypy.ini
├── package_name
│   ├── app.py
│   ├── dev_requirements.txt
│   ├── entry.py
│   ├── __init__.py
│   ├── __main__.py
│   ├── py.typed
│   └── requirements.txt
├── pyproject.toml
├── pytest.ini
├── README.md
├── setup.py
├── tasks
│   ├── conf.py
│   └── __init__.py
└── tests
    ├── data
    │   ├── invalid
    │   │   └── test.txt
    │   └── valid
    │       └── test.txt
    ├── __init__.py
    ├── resources.py
    ├── test_entry.py
    └── test_resources.py

11 directories, 31 files

```
