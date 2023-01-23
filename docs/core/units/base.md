# The Base Unit Class

```{py:currentmodule} pyroll.core
```

```{py:currentclass} pyroll.core.Unit
```

![illustration of the unit concept](/img/unit.svg)

A unit can most abstractly be considered as a black box transforming the state of a profile, thus taking an incoming profile instance, simulating its evolution within the unit and yielding an outgoing profile instance.
The figure illustrates the concept of a unit.
At its core, a unit consists of the two profile instances, `in_profile` and `out_profile`, represented in the figure by their cross-section planes.
These are in parallel to each other and located on a common, perpendicular center line.
The length of this line is called the `length` of the unit (its extent in rolling direction).
The length can be converted to timescale via the material flow `velocity` within the unit.
The extent of the unit in time is called its `duration`.
The `volume` of the unit is bounded by the profile planes and the lateral surface, whose area is represented by `surface_area`.
The `surface_perimeter` is tightly bound to the surface area, but is a mean perimeter of the lateral surface used when the length scale is not fixed.
This is for example the case for the transport units in reversing mills or lateral material transport, since the material flow direction is not equal to the rolling direction.
If the length scale is defined, the `surface_perimeter` times the `length` should be approximately equal the `surface_area`.
Models should avoid dependence on the length scale, if possible, since the timescale is the more general approach.

The unit class defines the method {py:meth}`Unit.solve`, which triggers the solution procedure and accepts a profile object that has to be treated as the incoming profile.
This object is copied and modified and made available in the {py:attr}`Unit.in_profile` attribute.
The outgoing state is available through the {py:attr}`Unit.out_profile` attribute or through the return of the {py:meth}`Unit.solve` method.

Each unit can be supplied a label for human identification at creation or by attribute setting.
It is mostly used in user interfaces later on.

A unit instance also has a {py:attr}`Unit.parent` property, which returns a reference to the containing unit, if there is one.
This offers the possibility to access attributes of the pass sequence, or, in case of disk elements, of the actual unit currently solved.
The return of this property is `None`, if there is no parent unit (for example on the root pass sequence).

```{eval-rst} 
.. autoclass:: Unit
    :members:
```