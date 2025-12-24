# Three Roll Pass Units

```{py:currentmodule} pyroll.core
```

Nowadays, groove rolling in stands with 3 rolls aligned in 120° angle gain more and more importance, especially for round rods and tubes.
PyRolL supports the simulation of three-roll rolling stands via the {py:class}`ThreeRollPass` class.
The {py:class}`ThreeRollPass` is derived from {py:class}`RollPass`, so hook functions defined for {py:class}`RollPass` also apply for three-roll passes, although they may not always be appropriate, but many are.
Always pay attention when simulating three-roll passes, that appropriate models are use, or the results may be heavily incorrect, which is not guaranteed to throw an error.

The main difference is that the dimensions of a three-roll pass are not right-angled, due to the 3-fold symmetry.
As the figure shows, the width and height are under an angle of odd multiples of 60°.
The caveat is, that width and height can not directly be measured here, but only their half.
This measure is implemented as hook functions for profiles featuring the type `"3fold"` (see [Profile Classifiers](../../profiles.md#profile-classifiers) for further information).

The width of ideal filling of the roll pass is here also dependent on the roll gap, as it is not for two-roll passes.
The width of ideal filling $w_{i=1}$ is given by the equation below, with the usable width of the groove $w_\mathrm{u}$ and the roll gap $s$.
As for two-roll passes the pass is always ideally filled, if no spreading resp. material flow model is loaded.

$$
w_{i=1} = \frac{w_\mathrm{u}}{\cos 30°} + s \tan 30°
$$

:::{figure-md} fig:demo-directions-three-roll
:align: center

![Three-Roll Pass Directions](/img/directions-three-roll.svg)

Dimensions of Three-Roll Passes
:::

For definition of a three-roll pass the same groove and roll objects as for two-roll passes are used.
The magic happens in {py:class}`ThreeRollPass.Roll` after creation of the instance.
So defining three-roll passes is straightforward.
Roll gap means the height of the clearing between the roll faces outside the actual groove hole, similar to two-roll passes.

```python
ThreeRollPass(
    label="My Three-Roll Pass",
    roll=Roll(
        groove=CircularOvalGroove(
            depth=8e-3,
            r1=6e-3,
            r2=40e-3
        ),
        nominal_radius=160e-3,
        rotational_frequency=1
    ),
    gap=2e-3,
),
```

Profiles originating from three-roll passes are marked with the special type classifier `"3fold"` (see [Profile Classifiers](../../profiles.md#profile-classifiers)), which indicated that the profile has a 3-fold symmetry instead of the common 2-fold symmetry of two-roll produced profiles.

```{eval-rst} 
.. autoclass:: ThreeRollPass
    :members:
    :exclude-members: InProfile, OutProfile, Roll, Profile
```