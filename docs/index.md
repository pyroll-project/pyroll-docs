![PyRolL Logo](img/pyroll-logo.svg)

# Home

PyRolL is an OpenSource rolling framework, aimed to provide a fast and extensible base for rolling simulation. The
current focus lies on groove rolling in elongation grooves. The core packages comes with a basic set of models to allow
a first estimation of forces and torques occurring in a pass sequence. There is a flexible plugin system, able to modify
and extend the model set available to describe the process.

```{toctree}
:maxdepth: 2
   
core/index
extensions/index
plugins/index
basic/index
recommendations
examples/index
troubleshooting
```

## Installation

The PyRolL Core package is installable via [PyPI](https://pypi.org)

```shell
pip install pyroll-core
```

A collection of extension and plugin packages can be installed the same way, the packages' names usually start with `pyroll-`.
Use the [PyPI search](https://pypi.org/search/?q=pyroll) or look at the
[extensions list](extensions/index) and [plugins list](plugins/index).

A basic ready-to-use configuration can be installed with

```shell
pip install pyroll-basic
```

Read [here](basic/index) for further information on the basic configuration.

## Trivia

### What is this flappy bird?

The German name of the [Golden Oriole](https://en.wikipedia.org/wiki/Eurasian_golden_oriole) is *Pirol*, which resembles the name PyRolL.