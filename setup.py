#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from __future__ import print_function
from glob import glob
from os.path import join as pjoin


from setupbase import (
    create_cmdclass,
    install_npm,
    ensure_targets,
    find_packages,
    combine_commands,
    ensure_python,
    get_version,
    HERE,
)

from setuptools import setup


# The name of the project
name = "ipylab"

# Ensure a valid python version
ensure_python(">=3.4")

# Get our version
version = get_version(pjoin(name, "_version.py"))

lab_path = pjoin(HERE, name, "labextension")

# Representative files that should exist after a successful build
jstargets = [
    pjoin(HERE, "lib", "plugin.js"),
]

package_data_spec = {name: ["labextension/*.tgz"]}

data_files_spec = [
    ("share/jupyter/lab/extensions", lab_path, "*.tgz"),
]


cmdclass = create_cmdclass(
    "jsdeps", package_data_spec=package_data_spec, data_files_spec=data_files_spec
)
cmdclass["jsdeps"] = combine_commands(
    install_npm(HERE, build_cmd="build"), ensure_targets(jstargets),
)


setup_args = dict(
    name=name,
    description="Control JupyterLab from Python notebooks",
    version=version,
    scripts=glob(pjoin("scripts", "*")),
    cmdclass=cmdclass,
    packages=find_packages(),
    author="Jeremy Tuloup",
    author_email="jeremy@jtp.io",
    url="https://github.com/jtpio/ipylab",
    license="BSD",
    platforms="Linux, Mac OS X, Windows",
    keywords=["Jupyter", "Widgets", "IPython"],
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Framework :: Jupyter",
    ],
    include_package_data=True,
    install_requires=["ipywidgets>=7.0.0",],
    extras_require={
        "test": ["pytest>=3.6", "pytest-cov", "nbval",],
        "dev": ["pre-commit", "black"],
        "examples": [
            # Any requirements for the examples to run
        ],
        "docs": [
            "sphinx>=1.5",
            "recommonmark",
            "sphinx_rtd_theme",
            "nbsphinx>=0.2.13,<0.4.0",
            "jupyter_sphinx",
            "nbsphinx-link",
            "pytest_check_links",
            "pypandoc",
        ],
    },
    entry_points={},
)

if __name__ == "__main__":
    setup(**setup_args)
