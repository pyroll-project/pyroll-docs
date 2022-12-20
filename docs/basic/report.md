# HTML Report Generation

The `pyroll-report` package provides a function to generate a HTML report page displaying the simulation results as tables and plots.
The content of the report is extendable by using pluggy hooks (see [here](https://pluggy.readthedocs.io/) for information about pluggy in general).
The {py:func}`pyroll.report.report` function takes a {py:class}`PassSequence` object to generate the report from.

```{eval-rst}
.. autofunction:: pyroll.report.report
```

## Command Line Usage

If the `pyroll-cli` package is also installed, the `pyroll-report` package provide an additional CLI command `report`, which can be used to generate the report page and save it to a file.
The file can be specified by the `-f`/`--file` option, which defaults to `./report.html`.

To create a report file using the CLI, execute f.e.

    pyroll input-py solve report -f my-report.html

## Extensibility

### Unit Displays

The main building block of the report are *unit displays*.
A unit display is a piece of HTML code presenting the state of the unit object or parts of it.
One may implement own displays by use of the pluggy hook `unit_display`.

Currently, four implementations of this hook are predefined.

:unit_heading: displays a heading line including the unit's label
:unit_properties_display: displays a table containing the representations of the unit's properties
:unit_plots_display: displays plots or other graphical presentations of the unit defined by the `unit_plot` hook
:sequence_units: displays the units a {py:class}`PassSequence` consists of sequentially

Anew new implementation can be defined as follows.

```python
import sys
from pyroll.report.pluggy import plugin_manager, hookimpl
from pyroll.core import Unit


@hookimpl(specname="unit_display")
def my_unit_display(unit: Unit, level: int):
    return f"<div>My display of unit {unit.label}</div>"


plugin_manager.register(sys.modules[__name__])
```

The function is marked as hook implementation by use of the `hookimpl` decorator.
Functions in a module must be registered to pluggy by use of the {py:meth}`pluggy.PluginManager.register` method.
The return of an implementation of this hook must be valid HTML code.
The `level` argument may be used for formatting purposes if nested calls to this hook are executed (it is used f.e. by the `unit_heading` hook to lower the heading level for units within a {py:class}`PassSequence`, also in nested ones).

### Unit Plots

Additionally, the `unit_plot` hook is available to conveniently include plots into the report.
The return of an implementation of this hook must be a {py:class}`matplotlib.figure.Figure` object or HTML code as string.
The results of this hook are displayed beneath other plots within the `plots_display`.
The plots display automatically converts the figure object to SVG code and scales it to 100 % width and height to fit responsively into the layout.
It is recommended to rely on this, instead of returning your own HTML.

```python
import sys
from pyroll.report.pluggy import plugin_manager, hookimpl
from pyroll.core import Unit, RollPass
import matplotlib.pyplot as plt


@hookimpl(specname="unit_plot")
def my_unit_plot(unit: Unit, level: int):
    if isinstance(unit, RollPass):
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3], [4, 5, 6])
        return fig


plugin_manager.register(sys.modules[__name__])
```