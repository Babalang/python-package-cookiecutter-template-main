from pathlib import Path

from setuptools import find_packages, setup

PROJECT_NAME = "{{ cookiecutter.project_name }}"
DESCRIPTION = "{{ cookiecutter.project_short_description }}"
AUTHOR = "{{ cookiecutter.full_name }}"
AUTHOR_EMAIL = "{{ cookiecutter.email }}"
CURRENT_DIR = Path(__file__).parent
README_FILEPATH = CURRENT_DIR / "README.md"
REQUIREMENTS_FILEPATH = CURRENT_DIR / "requirements.txt"
if README_FILEPATH.is_file():
    LONG_DESCRIPTION = README_FILEPATH.read_text(encoding="utf8")
else:
    LONG_DESCRIPTION = "Unable to load README.md"
if REQUIREMENTS_FILEPATH.is_file():
    REQUIREMENTS = REQUIREMENTS_FILEPATH.read_text().splitlines()
else:
    REQUIREMENTS = []
VERSION = (CURRENT_DIR / "{{ cookiecutter.project_slug }}" / "_version.py").read_text().split('"')[1]

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    project_urls={
        "Source": "{{ cookiecutter.repository_url }}",
        "Documentation": "{{ cookiecutter.documentation_url }}",
    },
    classifiers=[  # https://pypi.org/classifiers/
        "Development Status :: 3 - Alpha",
        "Environment :: Win32 (MS Windows)",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    packages=find_packages(exclude=["tests"]),
    license="MIT",
    # python_requires=">=3.6",
    install_requires=REQUIREMENTS,
    include_package_data=True,
)
