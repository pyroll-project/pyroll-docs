# The Concept of Units

```{py:currentmodule} pyroll.core
```

Think of a rolling process as of a sequence of roll passes and intermediate times, called transports. 
Both are subsumed under the term *unit*. 
The `Unit` class is the base class representing this concept.
A unit can most abstractly be considered as a black box transforming the state of a profile, thus taking an incoming profile instance, simulating its evolution within the unit and yielding an outgoing profile instance.
See [The Base Unit Class](base.md) for more detailed information on this concept.

Some units support subdivision into [disk elements](disk_elements.md), to provide finer spatial resolution in rolling resp. length direction.

```{toctree}
:maxdepth: 4
base
roll_pass/index
transport/index
sequence
rotator
disk_elements
```
