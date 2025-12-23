# Cooling Pipe Units

```{py:currentmodule} pyroll.core
```

`CoolingPipes` specialised units.
They represent direct current cooling pipes used e.g. in Waterboxes, Tempcore Boxes, etc. and are represented by the {py:class}`CoolingPipe` class.
Create a {py:class}`CoolingPipe` object as follows:

```python
CoolingPipe(
    label="Demo CoolingPipe", 
    inner_radius=1, 
    coolant_volume_flux=1, 
    length=1
    ...
)
```

As the `CoolingPipe` is derived from the `Transport` class, it can also be defined using {py:attr}`CoolingPipe.duration`
The following image shows a basic drawing of such a unit with the highlighted values.


```{eval-rst} 
.. autoclass:: CoolingPipe
    :members:
```