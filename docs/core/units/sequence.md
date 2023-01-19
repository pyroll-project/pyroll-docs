# Pass Sequence Units

```{py:currentmodule} pyroll.core
```

The pass sequence is a unit that contains several other units.
Pass sequences are represented by the {py:class}`PassSequence` class.
They can also be nested.

A single pass sequence is used as root object for defining a rolling process together with an instance of {py:class}`Profile` as the workpiece to be processed.

All units included in a pass sequence will be solved subsequently while forwarding the outgoing profile of the previous unit to the next as incoming profile.
The outgoing profile of the pass sequence will reflect the state of the last unit's outgoing profile, if this behavior is not overriden by provided hook functions.

```{eval-rst} 
.. autoclass:: PassSequence
    :members:
```