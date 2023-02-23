# Oval-like Grooves

```{py:currentmodule} pyroll.core
```

## The Circular Oval Groove

The {py:class}`CircularOvalGroove` class represents an oval-shaped groove consisting of two radii as shown in the figure.

![circular oval groove geometry](/img/circular_oval.svg)

It is defined by the radius $r_1$ and any two of radius $r_2$, depth $d$ and usable width $w_\mathrm{u}$.
The geometric constraints are $r_1 << r_2$ and $d << r_2$.
$r_3$ and $r_4$ are considered to be zero, as well as $w_\mathrm{g}'$.

The topology of this groove is similar to the [round groove](rounds.md#the-round-groove), with the main difference, that
the center of $r_2$ is not placed in the center of the groove. For this reason $d$ is typically much smaller than $r_2$
$.

```{eval-rst} 
.. autoclass:: CircularOvalGroove
    :members:
```

## The Flat Oval Groove

The {py:class}`FlatOvalGroove` class represents an oval-shaped groove consisting of two radii and an even ground as shown in the
figure.

![flat oval groove geometry](/img/flat_oval.svg)

Mandatory measures of this groove are the two radii $r_1$ and $r_2$, as well as the depth $d$.
Additionally, one of the usable width $w_\mathrm{u}$ and the even ground width $w_\mathrm{g}'$ must be given.
The depth is $d$ typically $\le \frac{w_\mathrm{u}}{2}$.
$r_3$ and $r_4$ are considered to be zero.

```{eval-rst} 
.. autoclass:: FlatOvalGroove
    :members:
```

## The Swedish Oval Groove

The {py:class}`SwedishOvalGroove` class represents a hexagonal-shaped groove as shown in the figure. The term "hexagonal" is also
used for this type of groove, but can be confused with regular hexagon shaped grooves. The current type of groove is
used as an oval and therefore the term swedish oval should be used, which is derived from its origin in swedish steel
plants.

![swedish oval groove geometry](/img/swedish_oval.svg)

Mandatory measures of this groove are the two radii $r_1$ and $r_2$, as well as the depth $d$. To constrain
geometry fully, any two of the following must be given:

- usable width $w_\mathrm{u}$
- ground width $w_g$ or even ground width $w'_\mathrm{g}$
- flank angle $\alpha$

The radii are typically small, the depth is $d$ typically $<< \frac{w_\mathrm{u}}{2}$.
$r_3$ and $r_4$ are considered to be zero.

$b_d$ was chosen in favor of the even ground width $w_\mathrm{g}'$, because it does not change when the radii are modified.
So the overall geometry remains the same if one modifies only the radii.

The topology of this groove is equal to the [box groove](boxes.md#the-box-groove), but typically the flank angles are smaller
and the groove is less deep.

```{eval-rst} 
.. autoclass:: SwedishOvalGroove
    :members:
```

## The Constricted Swedish Oval Groove

The {py:class}`ConstrictedSwedishOvalGroove` class represents a [swedish oval groove](#the-swedish-oval-groove) but with an indent in the
ground as shown in the figure.

![constricted swedish oval groove geometry](/img/constricted_swedish_oval.svg)

Mandatory measures of this groove are the two radii $r_1$ and $r_2$, as well as the depth $d$ and the indent $i$. 
To constrain geometry fully, any two of the following must be given:

- usable width $w_\mathrm{u}$
- ground width $w_\mathrm{g}$ or even ground width $w'_\mathrm{g}$
- flank angle $\alpha$

The radii are typically small, the depth is $d$ typically $<< \frac{w_\mathrm{u}}{2}$.
$r_3$ and $r_4$ are considered to be zero.

```{eval-rst} 
.. autoclass:: ConstrictedSwedishOvalGroove
    :members:
```

## The Three Radii Oval Groove

The {py:class}`Oval3RadiiGroove` class represents an oval-shaped groove consisting of three radii as shown in the figure.

![3 radii oval groove geometry](/img/oval_3radii.svg)

Mandatory measures of this groove are the three radii $r_1$, $r_2$ and $r_3$, as well as the depth $d$ and the
usable width $w_\mathrm{u}$.

The depth is $d$ typically $\le \frac{w_\mathrm{u}}{2}$.
$r_4$ and $b_d'$ are considered to be zero.

```{eval-rst} 
.. autoclass:: Oval3RadiiGroove
    :members:
```

## The Flanked Three Radii Oval Groove

The {py:class}`Oval3RadiiFlankedGroove` class represents an oval-shaped groove consisting of three radii and a small straight
flank as shown in the figure.

![3 radii flanked oval groove geometry](/img/oval_3radii_flanked.svg)

Mandatory measures of this groove are the three radii $r_1$, $r_2$ and $r_3$, as well as the depth $d$ and the
usable width $b_\mathrm{kn}$.
The flank is determined by either one of the flank angle `\phi`, the flank's horizontal width, its vertical height or collinear length.

The depth is $d$ typically $\le \frac{b_\mathrm{kn}}{2}$.
$r_4$ and $b_d'$ are considered to be zero.

```{eval-rst} 
.. autoclass:: Oval3RadiiFlankedGroove
    :members:
```

## The Upset Oval Groove

The {py:class}`UpsetOvalGroove` class represents a square shaped groove with curved edges as shown in the figure.

![square groove geometry](/img/square.svg)

Mandatory measures of this groove are the radii $r_1$, $r_2$ and $r_3$, as well as the usable width $w_\mathrm{u}$ and depth $d$.

The radii $r_1$ and $r_3$ are typically small, the depth $d$ is typically $\approx \frac{w_\mathrm{u}}{2}$. The tip angle
$\delta$ is typically one or two degree larger than 90° for wear reasons.
$r_3$ is much larger than the other radii.

```{eval-rst} 
.. autoclass:: GothicGroove
    :members:
```