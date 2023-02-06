# Rotator Units

```{py:currentmodule} pyroll.core
```

The rotator is a helper unit to achieve profile rotation before feeding into the next [roll pass](roll_pass/index).

The angle of rotation is determined {py:attr}`Rotator.rotation` hook, whose value must be in degree (may be negative).
Default implementations of {py:attr}`Rotator.rotation` determine appropriate default values by examining the type classifiers of the incoming profile and the next roll pass in the unit sequence (determined using the {py:attr}`Rotator.next_roll_pass` property).
The default implementations prefer rotation by 90° over no rotation, if both are appropriate.
Currently, there are the following defaults:

| type of in profile | type of roll pass | rotation in ° |
|--------------------|-------------------|---------------|
| diamond            | diamond           | 90            |
| oval               | round             | 90            |
| round              | oval              | 90            |
| oval               | square            | 90            |
| square             | oval              | 45            |
| box                | box               | 90            |
| box                | diamond           | 45            |
| box                | oval              | 90            |
| square             | box               | 45            |
| round              | flat              | 90            |

The recommended way to influence the rotation is by using the {py:attr}`RollPass.rotation` hook, unless one has a concrete need for a dedicated rotator unit.
In contrast to {py:attr}`Rotator.rotation` its value may also be a bool, where `False` equals `0` and `True` means automatic determination by hook functions of {py:attr}`Rotator.rotation` (f.e. using the defaults above).
The roll pass unit will create an appropriate rotator upon its solution initialization and use its outgoing profile as input for itself.
If a dedicated rotator unit is present in the sequence between the current roll pass and its predecessor roll pass, automatic rotation will be disabled, as it is then assumed, that correct rotation has already happened.

To be explicit, one has basically two ways to influence the profile rotation:

1. using {py:attr}`RollPass.rotation`

   ```python
   sequence = PassSequence([
        RollPass(...),
        ...,
        RollPass(
            ...,
            rotation=45,
            ...,        
        ),
        ...,
        RollPass(...)
   ])
   ```

2. using a dedicated rotator and {py:attr}`Rotator.rotation`

   ```python
   sequence = PassSequence([
        RollPass(...),
        ...,
        Rotator(rotation=45),
        RollPass(...), # automatic rotation here is skipped, since upstream Rotator is detected
        ...,
        RollPass(...)
   ])
   ```

Of course, both ways can be used by implementing hook functions to.

```{eval-rst} 
.. autoclass:: Rotator
    :members:
```
