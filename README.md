<!--
    =====================================
    generator=datazen
    version=1.9.0
    hash=aca6e910c47898473265cb936ea215d3
    =====================================
-->

# python-package-template

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
$ tree -I venv*|__pycache__|dist|htmlcov|datazen-out|config|build|*.egg-info -- package-name

package-name
├── local
│   ├── configs
│   │   ├── package.yaml
│   │   └── python.yaml
│   ├── templates
│   │   └── README.md.j2
│   └── variables
│       └── package.yaml
├── Makefile
├── manifest.yaml
├── package_name
│   ├── app.py
│   ├── entry.py
│   ├── __init__.py
│   └── py.typed
├── README.md
├── requirements
│   ├── dev_requirements.txt
│   └── requirements.txt
├── setup.py
└── tests
    ├── __init__.py
    └── test_entry.py

7 directories, 16 files

```
