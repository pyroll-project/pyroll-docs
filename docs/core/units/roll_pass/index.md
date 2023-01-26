# Roll Pass Units

```{py:currentmodule} pyroll.core
```

The roll pass is the most important unit, since forming of the workpiece is happening here.
It is represented by the {py:class}`RollPass` class.
The {py:class}`RollPass` constructor takes a {py:class}`Roll` object, which is defining the properties of the working rolls including the groove.
Read the following sections for detailed information on those.

```{toctree}
rolls
grooves/index
three_roll_pass
```

To create a roll pass, one must create three objects: a groove, a roll and finally the roll pass itself.
The [groove](grooves/index.md) object defines the contour line of the roll surface.
The [roll](rolls.md) object defines the geometry and kinetics of the roll and needs a groove object for creation.
The roll object holds also solution data like the contact area and roll torque.
The roll pass object itself defines the placement of the rolls and holds solution logic and data.
A most basic roll pass creation code would look like this:

```python
RollPass(
    label="My First Roll Pass",  # give it a name for human recognition
    roll=Roll(  # the roll object constructor
        groove=CircularOvalGroove(  # the groove object constructor
            # parameters of the groove geometry
            depth=8e-3,
            r1=6e-3,
            r2=40e-3
        ),
        # properties of the roll
        nominal_radius=160e-3,
        rotational_frequency=1,
        ...
    ),
    # properties of the roll pass
    gap=2e-3,
)
```

For information on which keyword arguments can be given, see the respective class documentations of {py:class}`RollPass`, {py:class}`Roll` and the different [grooves](grooves/index.md).

In reversing mills, the workpiece is commonly rotated by 90° before feeding it into the next roll pass.
In continuous mills, however, often rolling stands are constructed alternating in a horizontal/vertical manner.
Currently, PyRolL only supports horizontal rolling stands, since the support for vertical ones would introduce certain complexity for model implementation.
So, the profile must be rotated for reversing, as well as, continuous pass sequences.
For the classic pass sequences, PyRolL knows the common rotation angle and applies it automatically.
However, the user can influence and override this behavior.
Rotation achieved by the use of a helper unit, see the section on [rotators](../rotator.md) for detailed information on this topic.

```{eval-rst} 
.. autoclass:: RollPass
    :members:
    :exclude-members: InProfile, OutProfile, Roll, Profile
```





