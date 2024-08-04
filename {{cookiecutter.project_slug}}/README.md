[![pipeline status]({{cookiecutter.repository_url}}/badges/main/pipeline.svg)]({{cookiecutter.repository_url}}/-/commits/main)
[![pylint]({{cookiecutter.repository_url}}/-/jobs/artifacts/main/raw/public/badges/pylint.svg?job=pylint)]({{cookiecutter.repository_url}}/-/commits/main)
[![coverage]({{cookiecutter.repository_url}}/badges/main/coverage.svg)]({{cookiecutter.repository_url}}/-/commits/main)
[![vscode-editor](https://badgen.net/badge/icon/visualstudio?icon=visualstudio&label)](https://code.visualstudio.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)
[![API Documentation](https://badgen.net/badge/icon/API%20documentation?icon=gitlab&label&color=cyan)]({{cookiecutter.documentation_url}})

{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}

# {{cookiecutter.project_name}}

<p align="center">
  <img src="./{{cookiecutter.project_slug}}/resources/logo.png">
</p>

{{ cookiecutter.project_short_description }}

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [ameliend/cookiecutter-template](https://gitlab.com/ameliend/cookiecutter-template) project template.
