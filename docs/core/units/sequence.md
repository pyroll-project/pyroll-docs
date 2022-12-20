# Pass Sequence Units

```{py:currentmodule} pyroll.core
```

The pass sequence is a unit that contains several other units.
Pass sequences are represented by the {py:class}`PassSequence` class.
They can also be nested.

A single pass sequence is used as root object for defining a rolling process together with an instance of {py:class}`Profile` as the workpiece to be processed.

```{eval-rst} 
.. autoclass:: PassSequence
    :members:
```