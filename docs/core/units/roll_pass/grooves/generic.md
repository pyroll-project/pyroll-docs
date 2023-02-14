# The Generic Elongation Groove

```{py:currentmodule} pyroll.core
```

The classic elongation groove shapes can be derived from a generic elongation groove consisting of two straights and four radii as shown below.
The actual groove types are special cases of this geometry, where some measures are unequal and some are equal zero.

:::{figure-md} fig:generic-elongation-groove
:align: center

![Geometry of Generalized Groove](/img/generic-elongation-groove.svg)

Geometry of the Generic Elongation Groove.
:::

All geometric key values like cross-sections and perimeters can be calculated on this generic groove. The
generic groove is implemented in the {py:class}`GenericElongationGroove` class, all classic elongation groove types are derived from that.
The constructor of this class expects most of the geometric measures to be given.
The calculation of missing measures given others can be a complicated task depending on the segments used, and is therefore implemented in the actual derived groove classes taking advantage of their features and conditions.
The {py:class}`GenericElongationGroove` class is generally not intended to be used directly by the user, but may be, if one is able to provide all necessary measures, for example from a given drawing.

In the following the measures of the groove are listed, their names are used in source code and throughout the
documentation. The radii and angles are numbered from outside to inside.

| Symbol            | Description                              |
|-------------------|------------------------------------------|
| $r_i$             | Radius                                   |
| $\alpha_i$        | Angle corresponding to a radius          |
| $\alpha$          | Groove flank angle                       |
| $\beta$, $\gamma$ | Angles useful for coordinate calculation |
| $\phi$            | Roll face angle                          |
| $w_\mathrm{g}$    | Ground width                             |
| $w_\mathrm{g}'$   | Even ground width                        |
| $w_\mathrm{t}$    | Tip width                                |
| $w_\mathrm{u}$    | Usable width                             |
| $d$               | Depth                                    |
| $i$               | Indent                                   |
| $s$               | Roll gap                                 |
| $p$               | Roll face padding                        |

For grooves with inclined roll faces (like such for 3 and 4-roll passes), the geometry is slightly different like in the figure below.
Note the face line inclined by $\phi$ and the modified radius $r_1$.
The case shown above is the limit case for $\phi \rightarrow 0$.
If the actual groove has no straight flank line, the resulting geometry of the groove can be heavily influenced by changing the face angle $\phi$ or the radius $r_1$.

:::{figure-md} fig:generic-elongation-groove-3fold
:align: center

![Geometry of Generalized Groove for 3-Roll](/img/generic-elongation-groove-3fold.svg)

Geometry of the Generic Elongation Groove for 3-Fold Rolls.
:::

The coordinates of the points 1 to 12 shown in the figure can be calculated as follows, where the angles $\beta =
\alpha_4 - \alpha_3 / 2$ and $\gamma = \frac{\pi}{2} - \alpha_2 - \alpha_3 + \alpha_4$.

| number | z                                                                                  | y                                                                                  |
|--------|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| 0      | $z_1 + p \cos \phi$                                                                | $z_1 + p \sin \phi$                                                                |
| 1      | $z_2 + r_1 \tan \frac{\alpha_1}{2} \cos \phi$                                      | $r_1 \tan \frac{\alpha_1}{2} \sin \phi$                                            |
| 2      | $\frac{w_\mathrm{u}}{2}$                                                           | $0$                                                                                |
| 3      | $z_{12} - r_1 \sin \alpha$                                                         | $y_{12} - r_1 \cos \alpha$                                                         |
| 4      | $z_{11} + r_2 \cos \gamma$                                                         | $y_{11} + r_2 \sin \gamma$                                                         |
| 5      | $z_{10} + r_3 \sin \left( \frac{\alpha_3}{2} - \beta \right)$                      | $y_{10} + r_3 \cos \frac{\alpha_3}{2}$                                             |
| 6      | $z_8 + r_4 \sin \alpha_4$                                                          | $y_8 - r_4 \sin \alpha_4$                                                          |
| 7      | $\frac{w_\mathrm{g}'}{2}$                                                          | $d - i$                                                                            |
| 8      | $\frac{w_\mathrm{g}'}{2}$                                                          | $y_7 + r_4$                                                                        |
| 9      | $0$                                                                                | $y_7$                                                                              |
| 10     | $z_6 + r_3 \sin \left( \frac{\alpha_3}{2} + \beta \right)$                         | $y_6 + r_3 \cos \left( \frac{\alpha_3}{2} + \beta \right)$                         |
| 11     | $z_{10} + \left( r_3 - r_2 \right) \sin \left( \frac{\alpha_3}{2} - \beta \right)$ | $y_{10} + \left( r_3 - r_2 \right) \cos \left( \frac{\alpha_3}{2} - \beta \right)$ |
| 12     | $z_1 - r_1 \sin \phi$                                                              | $y_1 + r_1 \cos \phi$                                                              |


The line between points 1 and 0 is the roll face and is in the narrower sense no part of the groove.
However, it is included in the grooves contour line for numerical reasons.
The extent of this roll face padding is determined by $p$ and can be given to the constructor by the `pad` and `rel_pad` arguments, where `pad` represents the absolute value and `rel_pad` the padding relative to the usable width $w_\mathrm{u}$ of the groove.
The default value of `rel_pad` is given by the `pyroll.core.config.GROOVE_PADDING` config value.
Also, the roll gap $s$ is no measure of the groove itself but of the [roll pass](../index). 
The tip width $w_\mathrm{t}$ is consecutively also not inherent to the groove, since it depends on the roll gap.

```{eval-rst} 
.. autoclass:: GenericElongationGroove
    :members:
```