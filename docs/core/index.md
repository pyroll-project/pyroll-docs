# The PyRolL Core Package

```{py:currentmodule} pyroll.core
```

PyRolL Core (the `pyroll-core` package) is basically just a library of data structures and simple iteration logic.
The actual physical model logic is, in contrast, provided by *plugin* packages (see [here](../plugins/index)).
User interfaces and similar are, however, provided by distinct *extension* packages (see [here](../extensions/index)).

The core concepts of data structure are *profiles* and *units*.
Profiles represent the state of a workpiece somewhere in the rolling process and are basically an infinitive thin slice of the workpiece perpendicular to the rolling direction.
Units, however, represent the processing steps applied to the workpiece.
They are basically black boxes that transform profiles from one state to another.

How this transformation is done and how the properties of a profile look like is defined by *hooks*.
Hooks are basically placeholders for properties of the respective profiles or units.
Famous hooks on profiles are f.e. {py:attr}`Profile.temperature` and {py:attr}`Profile.flow_stress`, on units of roll pass type, however, {py:attr}`RollPass.roll_force` and {py:attr}`RollPass.elongation`.
The value of hook can be either set explicitly to a constant value, or determined by evaluating *hook functions* defined for the respective hook.

Read into the sections below for detailed information.
Make sure you understand the core concepts of PyRolL before reading into the matter of models, plugins and extensions.

```{toctree}
:maxdepth: 2
profiles
units/index
plugins
```