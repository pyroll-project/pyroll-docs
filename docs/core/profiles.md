# The Concept of Profiles

```{py:currentmodule} pyroll.core
```

Think of a {py:class}`Profile` object as of a state of the workpiece somewhere in the pass sequence. Every unit
has an incoming and an outgoing profile. Also, you must provide a profile as definition for the initial workpiece being
processed in the pass sequence.

The shape and the extent of the profile is defined by its {py:attr}`Profile.cross_section` hook.
The value type of this hook is a {py:class}`shapely.Polygon` providing all of its functionality in planar geometry.
PyRolL patches a few things within shapely for convenience and user experience, especially while developing plugins.
Other parts of PyRolL use shapely geometry objects, too.

For creating an initial profile, several class methods exist in the {py:class}`Profile` class. One can either derive the
profile shape from an existing groove object by use of the {py:meth}`Profile.from_groove` method, or created some
standard shapes use of the other class methods of {py:class}`Profile`, like {py:meth}`Profile.round`. More values can be
given as keyword arguments and are saved automatically as explict hook values in the instance. Which you may or must provide
depends on the loaded plugins.

```{eval-rst}
.. autoclass:: Profile
    :members:
```

## Derived classes

For the units types, specialized versions of the `Profile` class are defined as nested classes within the respective unit class.
They all maintain their own hooks, so it is possible to specify hooks on profiles only for those places, were they are applicable.