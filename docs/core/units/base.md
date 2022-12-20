# The Base Unit Class

```{py:currentmodule} pyroll.core
```

The unit class defines the method {py:meth}`Unit.solve`, which triggers the solution procedure and accepts a profile object that has to be treated as the incoming profile.
This object is copied and modified and made available in the {py:attr}`Unit.in_profile` attribute.
The outgoing state is available through the {py:attr}`Unit.out_profile` attribute or through the return of the {py:meth}`Unit.solve` method.

Each unit can be supplied a label for human identification at creation or by attribute setting.
It is mostly used in user interfaces later on.

```{eval-rst} 
.. autoclass:: Unit
    :members:
```