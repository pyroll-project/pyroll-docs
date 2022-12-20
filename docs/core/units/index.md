# The Concept of Units

```{py:currentmodule} pyroll.core
```

Think of a rolling process as of a sequence of roll passes and intermediate times, called transports. 
Both are subsumed under the term *unit*. 
The `Unit` class is the base class representing this concept.
A unit can most abstractly be considered as a black box transforming the state of a profile, thus taking an incoming profile instance, simulating its evolution within the unit and yielding an outgoing profile instance.

```{toctree}
:maxdepth: 2
roll_pass
transport
sequence
rotator
```

## The Base Unit Class

The unit class defines the method {py:meth}`Unit.solve`, which triggers the solution procedure and accepts a profile object that has to be treated as the incoming profile.
This object is copied and modified and made available in the {py:attr}`Unit.in_profile` attribute.
The outgoing state is available through the {py:attr}`Unit.out_profile` attribute or through the return of the {py:meth}`Unit.solve` method.

Each unit can be supplied a label for human identification at creation or by attribute setting.
It is mostly used in user interfaces later on.

```{eval-rst} 
.. autoclass:: Unit
    :members:
```