# Roll Pass Units

```{py:currentmodule} pyroll.core
```

The roll pass is the most important unit, since forming of the workpiece is happening here.
It is represented by the {py:class}`RollPass` class.
The {py:class}`RollPass` constructor takes a {py:class}`Roll` object, which is defining the properties of the working rolls including the groove.
Read the following sections for detailed information on those.

In reversing mills, the workpiece is commonly rotated by 90° before feeding it into the next roll pass.
In continuous mills, however, often rolling stands are constructed alternating in a horizontal/vertical manner.
Currently, PyRolL only supports horizontal rolling stands, since the support for vertical ones would introduce certain complexity for model implementation.
So, the profile must be rotated for reversing, as well as, continuous pass sequences.
For the classic pass sequences, PyRolL knows the common rotation angle and applies it automatically.
However, the user can influence and override this behavior.
Rotation achieved by the use of a helper unit, see the section on [rotators](../rotator.md) for detailed information on this topic.

```{toctree}
rolls
grooves/index
```

```{eval-rst} 
.. autoclass:: RollPass
    :members:
    :exclude-members: InProfile, OutProfile, Roll, Profile
```





