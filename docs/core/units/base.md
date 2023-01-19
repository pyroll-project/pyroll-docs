# The Base Unit Class

```{py:currentmodule} pyroll.core
```

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