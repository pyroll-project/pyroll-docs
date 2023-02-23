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

## Profile Classifiers

As profile have an infinite variety of cross-section shapes, for the use of empirical models, the shape must be classified.
This is achieved by the {py:attr}`Profile.classifiers` hook, which returns a set of string classifiers describing the shape of the profile.
Model hook functions can check the contents of this set to determine, if the model approach they provide is suitable to the given profile.
Grooves and roll passes make use of the same classifiers, as they transfer their classifiers to the new outgoing profile.

Currently, the PyRolL Core uses the following classifiers:

`"round"`
~ An approximately circular cross-section.
  Corresponds to the {py:class}`RoundGroove`.

`"false_round"`
~ An approximately circular cross-section with flanks.
  Corresponds to the {py:class}`FalseRoundGroove`.
  Commonly in combination with `"round"`.

`"oval"`
~ An approximately oval-shaped cross-section.
  Umbrella class for all more specific ovals.

`"circular_oval"`
~ An approximately oval-shaped cross-section.
  Corresponds to the {py:class}`CircularOvalGroove`.
  Commonly in combination with `"oval"`.

`"flat_oval"`
~ An approximately oval-shaped cross-section.
  Corresponds to the {py:class}`FlatOvalGroove`.
  Commonly in combination with `"oval"`.

`"swedish_oval"`
~ An approximately oval-shaped cross-section.
  Corresponds to the {py:class}`SwedishOvalGroove`.
  Commonly in combination with `"oval"`.

`"diamond"`
~ An approximately diamond resp. rhombus shaped cross-section, includes squares.
  Corresponds to the {py:class}`DiamondGroove`.

`"square"`
~ An approximately square shaped cross-section.
  Corresponds to the {py:class}`SquareGroove`.
  Commonly in combination with `"diamond"`.

`"box"`
~ An approximately rectangular shaped cross-section.
  Corresponds to the {py:class}`BoxGroove`.

`"flat"`
~ An approximately rectangular shaped cross-section originating from flat rolling.
  Corresponds to the {py:class}`FlatGroove`.

`"3fold"`
~ A cross-section with 3-fold rotation symmetry.
  Such profiles typically originate from three-roll passes.
  Can be combined with other classifiers for further distinguishing.

`"rotated"`
~ Indicates, that the profile has been rotated by a rotator unit and therefore does not have its common orientation anymore.

`"vertical"`
~ Indicates, that the profile has been rotated by 90° relative to its common orientation.

`"edged"`
~ Indicates, that the profile has been rotated by 45° relative to its common orientation.
  Often that means rotating a profile from standing on edge to standing on its side or vice versa.
  Commonly found in square-oval pass sequences.

`"mirrored"`
~ Indicates, that the profile has been rotated by 180° relative to its common orientation.

`"constricted"`
~ Indicates, that the profile has a constriction in its base.
  Corresponds mainly to {py:class}`ConstrictedBoxGroove` and {py:class}`ConstrictedSwedishOvalGroove`.
  Therefore, commonly in combination with `"box"` and `"swedish_oval"`.