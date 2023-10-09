![PyRolL Logo](img/pyroll-logo.svg)

# Home

PyRolL is an OpenSource rolling framework, aimed to provide a fast and extensible base for rolling simulation. The
current focus lies on groove rolling in elongation grooves. The core packages comes with a basic set of models to allow
a first estimation of forces and torques occurring in a pass sequence. There is a flexible plugin system, able to modify
and extend the model set available to describe the process.

## Installation

The PyRolL Core package is installable via [PyPI](https://pypi.org)

```shell
pip install pyroll-core
```

A collection of extension and plugin packages can be installed the same way, the packages' names usually start
with `pyroll-`.
Use the [PyPI search](https://pypi.org/search/?q=pyroll) or look at the
[extensions list](extensions/index) and [plugins list](plugins/index).

A basic ready-to-use configuration can be installed with

```shell
pip install pyroll-basic
```

Read [here](basic/index) for further information on the basic configuration.

## Where to Get Started

There is a [collection of examples](examples/index.md) to ease the start into the usage of PyRolL.
Especially for absolute beginners, it is recommended to start with the [basic example](examples/basic.md), which gives a
tour through the different possible ways of usage.

After following the first examples, you shall read the [recommendations](recommendations.md).

To learn about the data structures used to represent the rolling process, read into
the [documentation of the core package](core/index.md), especially the notes about [profiles](core/profiles.md)
and [units](core/units/index.md).

To explore modelling approaches, see in the [plugins list](plugins/index.md). To explore packages aimed at user interface and application, see the [extensions list](extensions/index.md).

If you encounter problems, please refer first to the [troubleshooting page](troubleshooting.md).
If this does not solve your problem, you may contact us via the following ways:

- If you think you have found a bug, please file an issue in the respective GitHub repository (
  e.g. [here for bugs in the core package](https://github.com/pyroll-project/pyroll-core/issues)).
- If your problem is not likely to be a bug, please open a thread on
  the [discussions board](https://github.com/pyroll-project/pyroll-core/discussions). So the answer to your question is
  available to everyone.
- If your problem contains confidential information, you may contact us
  via [email](mailto:kalibrierzentrum@imf.tu-freiberg.de) directly.

In public correspondence, please stick to English language, so everyone can read it. In private correspondence, you may also use German language.

## Contents

```{toctree}
:maxdepth: 2
   
core/index
extensions/index
plugins/index
basic/index
recommendations
setup/index
examples/index
troubleshooting
```

## Trivia

### What is this flappy bird?

The German name of the [Golden Oriole](https://en.wikipedia.org/wiki/Eurasian_golden_oriole) is *Pirol*, which resembles
the name PyRolL.
