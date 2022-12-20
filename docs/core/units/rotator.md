# Rotator Units

```{py:currentmodule} pyroll.core
```

The rotator unit is currently not meant to be used directly.
It is used internally by the [roll pass unit](roll_pass/index) to rotate its incoming profile.
However, if one needs to use it directly, mention to set the {py:attr}`RollPass.in_profile_rotation` hook of the following pass to `0`, to disable the automatic rotation.

```{eval-rst} 
.. autoclass:: Rotator
    :members:
```