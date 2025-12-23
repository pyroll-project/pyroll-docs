# Rolls

```{py:currentmodule} pyroll.core
```

A roll object represents a working roll within a roll pass.
Its surface shape is defined by a [groove object](grooves/index.md).
The current implementation of roll passes only works with symmetrical roll gaps, therefore only one roll object is needed.
The groove shape is considered to be symmetric, too.
This is especially true for groove types derived from the [generic elongation groove](grooves/generic.md).
For grooves constructed using the [spline groove](grooves/spline.md), this has to be ensured by the user, or results may be wrong.
Due to the presence of a groove, different radii can be defined for the roll object.
These can be seen in the figure below: 


:::{figure-md} fig:roll-radii
:align: center

![Work Roll With Different Radii](/img/working_diameter_models.svg)

Different Radii at a work roll.
:::

The most important radius is the so-called working radius. 
This radius is defined is the corresponding radius for the [equivalent flat pass method](core/units/basic_rolling_theory.md).
Further the nominal radius is defined as the outer radius at the barrel surface. 


```{eval-rst} 
.. autoclass:: Roll
    :members:
```