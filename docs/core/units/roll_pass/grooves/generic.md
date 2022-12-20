# The Generic Elongation Groove

```{py:currentmodule} pyroll.core
```

All elongation grooves can be derived a generic elongation groove consisting of two straights and four radii.
The geometry of this is shown below.

![Geometry of Generalized Groove](/img/general-groove.svg)

All geometric key values like cross-sections and perimeters can be calculated on this generic groove. The
generic groove is implemented in the {py:class}`GrooveBase` class, all classic elongation groove types are derived from that.

In the following the measures of the groove are listed, their names are used in source code and throughout the
documentation. The radii and angles are numbered from outside to inside.

| Symbol            | Description                              |
|-------------------|------------------------------------------|
| $r$               | Radius                                   |
| $\alpha$          | Angle corresponding to a radius          |
| $\beta$, $\gamma$ | Angles useful for coordinate calculation |
| $b_d$             | Ground width                             |
| $b_d'$            | Even ground width                        |
| $b_\mathrm{ks}$   | Tip width                                |
| $b_\mathrm{kn}$   | Usable width                             |
| $d$               | Depth                                    |
| $i$               | Indent                                   |
| $s$               | Roll gap                                 |

The coordinates of the points 1 to 12 shown in the figure can be calculated as follows, where the angles $\beta =
\alpha_4 - \alpha_3 / 2$ and $\gamma = \frac{\pi}{2} - \alpha_2 - \alpha_3 + \alpha_4$.

| number | z                                                                                  | y                                                                                  |
|--------|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| 1      | $z_2 + r_1 \tan \frac{\alpha_2}{2}$                                                | $0$                                                                                |
| 2      | $\frac{b_{kn}}{2}$                                                                 | $0$                                                                                |
| 3      | $z_1 - r_1 \sin \alpha_1$                                                          | $r_1 \left( 1 - \cos \alpha_1 \right)$                                             |
| 4      | $z_{11} + r_2 \cos \gamma$                                                         | $y_{11} + r_2 \sin \gamma$                                                         |
| 5      | $z_{10} + r_3 \sin \left( \frac{\alpha_3}{2} - \beta \right)$                      | $y_{10} + r_3 \cos \frac{\alpha_3}{2}$                                             |
| 6      | $z_8 + r_4 \sin \alpha_4$                                                          | $y_8 - r_4 \sin \alpha_4$                                                          |
| 7      | $\frac{b_d'}{2}$                                                                   | $d - i$                                                                            |
| 8      | $\frac{b_d'}{2}$                                                                   | $y_7 + r_4$                                                                        |
| 9      | $0$                                                                                | $y_7$                                                                              |
| 10     | $z_6 + r_3 \sin \left( \frac{\alpha_3}{2} + \beta \right)$                         | $y_6 + r_3 \cos \left( \frac{\alpha_3}{2} + \beta \right)$                         |
| 11     | $z_{10} + \left( r_3 - r_2 \right) \sin \left( \frac{\alpha_3}{2} - \beta \right)$ | $y_{10} + \left( r_3 - r_2 \right) \cos \left( \frac{\alpha_3}{2} - \beta \right)$ |
| 12     | $z_1$                                                                              | $r_1$                                                                              |

However, in the current implementation the term "groove" is more narrow. From now on, the term should represent only the
shape machined into the roll surface. Therefore, the roll gap $s$ is no measure of the groove itself but of
the [roll pass](../index). Also, the tip width $b_\mathrm{kn}$ is not inherent to the groove, since it
depends on the roll gap.

```{eval-rst} 
.. autoclass:: GenericElongationGroove
    :members:
```