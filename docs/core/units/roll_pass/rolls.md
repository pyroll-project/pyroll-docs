# Rolls

```{py:currentmodule} pyroll.core
```

A roll object represents a working roll within a roll pass.
Its surface shape is defined by a [groove object](grooves/index.md).
The current implementation of roll passes only works with symmetrical roll gaps, therefore only one roll object is needed.
The groove shape is considered to be symmetric, too.
This is especially true for groove types derived from the [generic elongation groove](grooves/generic.md).
For grooves constructed using the [spline groove](grooves/spline.md), this has to be ensured by the user, or results may be wrong.

```{eval-rst} 
.. autoclass:: Roll
    :members:
```