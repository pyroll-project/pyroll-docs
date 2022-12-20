# Recommendations for Using PyRolL

## Create a Project Directory

For each simulation project, create a new directory and work within it.
This enables you to use virtual environments and the default filenames of the CLI.

## Use Virtual Environments

To avoid collisions between installed packages, it is generally recommended with Python to use virtual environments, so with PyRolL.
We recommend creating a new virtual environment for each simulation project.

For example with [pipenv](https://pipenv.pypa.io/en/latest/):

    pipenv install pyroll-core

This will create a new environment in the current directory (preferably the project directory, see above) and a `Pipfile`, which contains the dependencies of your project.
Accordingly install all plugins and extensions you need.

Run a shell with the activated environment using

    pipenv shell

Then you can work with the CLI or Python scripts.

Of course, you can use the environment management tool of your choice.
Other possibilities are [venv](https://docs.python.org/3/library/venv.html), [conda](https://docs.conda.io/en/latest/), [poetry](https://python-poetry.org/) and [hatch](https://hatch.pypa.io/latest/).

## Direct Python Usage

The CLI is somehow comfortable, but also limited.
For advanced usage, it is recommended to use PyRolL directly from Python scripts or [Jupyter notebooks](https://jupyter.org/).
This offers you the full flexibility and power of PyRolL.

PyRolL also integrates well with [IPython](https://ipython.org/) and [Jupyter](https://jupyter.org/), namely implementing pretty printing functionality for most of its objects.
