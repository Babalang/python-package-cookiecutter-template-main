[![vscode-editor](https://badgen.net/badge/icon/visualstudio?icon=visualstudio&label)](https://code.visualstudio.com/)
[![cookiecutter](https://badgen.net/badge/icon/cookiecutter?icon=github&label&color=yellow)](https://github.com/cookiecutter/cookiecutter)

# Python Package Cookiecutter Template

<p align="center">
  <img src="./resources/logo.png">
</p>

This is my Python Package Cookiecutter template for my future projects.

My Python code formatting will be [Black](https://github.com/psf/black),
with [isort](https://github.com/PyCQA/isort).
I also use [Pylint](https://pypi.org/project/pylint/) for improving code quality.

I use [VSCode](https://code.visualstudio.com/) editor.

I use [automodapi](https://sphinx-automodapi.readthedocs.io/en/latest/) to generate my 
documentation to the Gitlab Pages.

The Gitlab pipeline is configured:

* Code analysis using [Pylint](https://pylint.org).
* [PyTests](https://docs.pytest.org/en/latest/) with [coverage](https://pytest-cov.readthedocs.io/en/latest/).
* [Semantic release](https://github.com/semantic-release/semantic-release).
* Documentation publishing to Gitlab pages.

## Usage

1. Install **Cookiecutter** with pip

```
pip install cookiecutter
```

2. Navigate to your project directory then execute **Cookiecutter** with the following command

```
py -m cookiecutter https://gitlab.com/ameliend/python-package-cookiecutter-template
```
