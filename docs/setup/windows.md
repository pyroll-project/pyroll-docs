# Setup on Windows

The following instructions guide through the setup of Python and PyRolL on Windows.
The setup of Python is explained, since we recommend specific settings in the Python setup to avoid issues in use.
The following instructions are known to work on Windows 10 and 11, but shall also work on earlier versions if supported Python versions are available for the respective platform.

## Python

Download the Windows Python Installer from the Python website. Currently, version 3.11 is recommended for use with PyRolL.
You may use [this link](https://www.python.org/ftp/python/3.11.6/python-3.11.6-amd64.exe) for download.

Run the installer and make sure, that you check and uncheck the options as in the images below.

We want to make Python available from the command line, so check the PATH option. But we also want to customize further things, so proceed with the customized installation.

![Windows Python Setup Window 1](/img/setup/windows/1.png)

For installing PyRolL we definitely need pip. The py launcher makes it easier to run scripts directly.

![Windows Python Setup Window 2](/img/setup/windows/2.png)

We want a per-user installation, since a system-wide installation would need admin privileges when installing packages through pip.
Again make sure to check the shortcut and the PATH option to make Python and packages available on the terminal.
Check, that the installation directory is in `AppData\Local`, which means the per-user installation.

![Windows Python Setup Window 3](/img/setup/windows/3.png)

When clicking install the installation starts. Wait until it's finished and quit the installer. Then proceed with the PyRolL installation.

## PyRolL

You have the choice of a global or a local installation of PyRolL.
Global means, that you have one version of PyRolL installed available and used in all your simulation projects.
A local installation is only used in one simulation project and is not available outside the project.
We recommend to not mix both concepts, since that can lead to obscure version conflicts and hard to find errors.
We generally recommend a local installation, since this enables you to reproduce the results of a simulation at a later point, because the simulation is run every time with the same version of PyRolL and plugins installed, no mater if there have been updates since the last time.
Also, you are able to use multiple versions of PyRolL in parallel without any conflicts.

# Global Installation

Open a terminal by right-clicking on the start button and choosing `Terminal`. On some versions this is also called `Command Line` or `Command Prompt`.
On recent Windows versions you can also use `Power Shell`.
A black or blue Window is opened with a command prompt, were we can type the commands for installation of PyRolL.
If a command fails with error like "... is not recognized as an operable programm, script or function", a reboot of the computer is probably necessary.

Install PyRolL Core using pip with the following command. This installs the most recent version of PyRolL.
Other packages for PyRolL can be installed the same way by typing the respective package name instead of `pyroll-core` as listed on [PyPI](https://pypi.org/search/?q=pyroll&o=) or the [plugins](../plugins/index.md) and [extensions](../extensions/index.md) lists.

```shell
pip install pyroll-core
```

# Local Installation

For the local installation we need first a project directory. Create a new empty directory in your desired location and open it in Explorer.
Then, open a terminal in this directory. On Windows 8/10 do this by clicking on the `File` menu in Explorer and choosing `Open PowerShell` or `Open Command Promp`.
On Windows 11 this is possible by right-clicking into the file list and choosing `Open Terminal`.

First we must create a local virtual Python environment were we can install our packages into. We recommend [pipenv](https://pipenv.pypa.io/en/latest/) for this.
Install pipenv to your global Python installation with

```shell
pip install pipenv
```

Then you can install PyRolL Core locally with the following command. Pipenv will automatically create a local virtual environment and the necessary configuration files. You will notice the local environment by the `Pipfile` and `Pipfile.lock` files, which are just textfiles listing your packages and some metadata.

```shell
pipenv install pyroll-core
```

The content of the `Pipfile` shall be something like below. You see the `pyroll-core` package listed. The star represents that no version constraint was given.

```toml
[packages]
pyroll-core = "*"

[dev-packages]

[requires]
python_version = "3.9"
```

You can now activate the environment in your terminal by typing

```shell
pipenv shell
```



