# Disk Elements

```{py:currentmodule} pyroll.core
```

The disk element is a unit used to subdivide other units into discrete steps.
The disk element theory (strip element or slab element in flat rolling) is a common approach in rolling simulation.
The basic idea is to define an element which is infinitesimal only in one direction, commonly the rolling direction, to construct 1D differential equations.
In the other directions the element has finite boundaries, here defined by the profile contour.
In numerical differential equation solving, of course, the disk element is also finite in rolling direction, as one uses a finite difference quotient as approximation of the differential quotient.

![disk element geometry](/img/disk_element.svg)

So in terms of PyRolL, a disk element is a small unit of finite length resp. duration (in terms of temporal differential equations), with an incoming and outgoing profile as usual.
Other units, currently roll passes and transports, may create a number of disk elements during initialization of the solution procedure.
These are available through the `disk_elements` property, which returns a list of disk elements.
The number of disk elements created is determined by the value of the `disk_element_count` hook.
If this value is zero, no disk elements are created and only one-step models can be used.

During the solution procedure, the disk elements are solved subsequently similar to the solution of a pass sequence.
The outgoing profile of the former element is always used as incoming profile of the following.
By defining hook functions on the disk elements of the respective units, one is able to define incremental models.
Hook values of the unit's outgoing profile are copied from the last disk element, if available.
This behavior is realized by predefined hook functions for all core profile hooks, but must be implemented for additional hooks yourself.

Incremental models and one-step models can be used together.
So there is no problem using an incremental model for thermal evolution together with a one-step empirical roll force model.
Note, that if two plugins providing functions for the same hook, the one-step model will likely take precedence on the units outgoing profile, since the copy-from-disk-element function has low precedence.
Of course, the disk elements will be solved incrementally, but the state of the last disk element's outgoing profile will likely not be reflected in the parent unit's outgoing profile.
Consider to provide a new implementation doing this task to be sure the incremental model is used.

Disk elements of roll passes and transports share the largest part of their hook set with their parent units, so the respective values can be accessed under the same names.
However, hook function definitions are independent on each other.
See the class documentations of {py:class}`Transport.DiskElement` and {py:class}`RollPass.DiskElement` for details.

The class {py:class}`DiskElementUnit` is a base class for units supporting the subdivision in disk elements.
It is not meant for direct use, except for hook definitions, that are of use for all derived units.
{py:class}`Transport` and {py:class}`RollPass` are both subclasses of this.
The class {py:class}`DiskElementUnit.DiskElement` is the base class of all disk elements.

```{eval-rst} 
.. autoclass:: DiskElementUnit
    :members:
```