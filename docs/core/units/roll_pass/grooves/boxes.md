# Box-like Grooves

```{py:currentmodule} pyroll.core
```

## The Box Groove

The {py:class}`BoxGroove` class represents a rectangular shaped groove as shown in the figure. For wear reasons, the flanks are
typically inclined by a small angle.

![box groove geometry](/img/box.svg)

Mandatory measures of the box groove are the two radii $r_1$ and $r_2$, as well as the depth $d$. To constrain
geometry fully, any two of the following must be given:

- usable width $w_\mathrm{u}$
- ground width $w_\mathrm{g}$ or even ground width $w'_\mathrm{g}$
- flank angle $\alpha$

The radii are typically small, the depth is $d$ typically $\le \frac{w_\mathrm{u}}{2}$.
$r_3$ and $r_4$ are considered to be zero.

$w_\mathrm{g}$ was chosen in favor of the even ground width $w_\mathrm{g}'$, because it does not change when the radii are modified.
So the overall geometry remains the same if one modifies only the radii.

```{eval-rst} 
.. autoclass:: BoxGroove
    :members:
```

If the depth/width ratio is high, consider to use the {py:class}`UpsetBoxGroove` instead.

```{eval-rst} 
.. autoclass:: UpsetBoxGroove
    :members:
```

## The Constricted Box Groove

The {py:class}`ConstrictedBoxGroove` class represents a [`BoxGroove`](#the-box-groove) but with an indent in the ground as shown in the
figure. The groove has and indent resp. constriction in the ground.

![constricted box groove geometry](/img/constricted_box.svg)

Mandatory measures of the box groove are the two radii $r_1$ and $r_2$, as well as the depth $d$ and the indent
$i$. To constrain geometry fully, any two of the following must be given:

- usable width $w_\mathrm{u}$
- ground width $w_\mathrm{g}$ or even ground width $w'_\mathrm{g}$
- flank angle $\alpha$

The radii are typically small, the depth is $d$ typically $\le \frac{w_\mathrm{u}}{2}$.
$r_3$ and $r_4$ are considered to be zero.

```{eval-rst} 
.. autoclass:: ConstrictedBoxGroove
    :members:
```

If the depth/width ratio is high, consider to use the {py:class}`ConstrictedUpsetBoxGroove` instead.

```{eval-rst} 
.. autoclass:: ConstrictedUpsetBoxGroove
    :members:
```