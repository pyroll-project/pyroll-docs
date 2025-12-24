# Transport Units

```{py:currentmodule} pyroll.core
```

Transport is a multipurpose unit.
They can represent almost every processing step, which is characterized by negligible deformation but by thermal flows or microstructure evolution.
The most used application is the cooling in the clearances between every roll pass further, the {py:class}`CoolingPipe` class is derived from a {py:class}`Transport` being used to model the respective unit inside a water box.

```{toctree}
cooling_pipe
```

But also furnaces or other cooling ranges can be described by transport units.
Transports are represented by the {py:class}`Transport` class.
Create a {py:class}`Transport` object as follows:

```python
Transport(
    duration=10,
    ...
)
```

The hook {py:attr}`Transport.duration` is the most important property of transport.
It defines the temporal extent of the transport.
An alternative way of defining the extent is a combination of the spatial extent {py:attr}`Transport.length` and the material flow velocity.

```python
Transport(
    length=10,
    velocity=1, # can be left out if known from the in profile
    ...
)
```

However, this approach may not be appropriate for all transports, as the velocity may not be constant or the spatial extent may be meaningless.
Therefore, all models for transport are recommended to be defined at the timescale and independent of the length scale, if possible.

```{eval-rst} 
.. autoclass:: Transport
    :members:
```