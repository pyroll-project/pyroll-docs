# Diamond-like grooves

```{py:currentmodule} pyroll.core
```

## The Diamond Groove

The {py:class}`DiamondGroove` class represents a rhombus shaped groove as shown in the figure.

![diamond groove geometry](/img/diamond.svg)

Mandatory measures of this groove are the two radii $r_1$ and $r_2$. To constrain geometry fully, any two of the
following must be given:

- usable width $w_\mathrm{u}$
- tip depth $d_\mathrm{t}$
- tip angle $\delta$

The radii are typically small, the depth is $d_\mathrm{t}$ typically $< \frac{b_\mathrm{kn}}{2}$ so that the tip angle
$\delta$ is larger than 90°.
$r_3$ and $r_4$ are considered to be zero, as well as $w_\mathrm{g}'$.

The tip depth $d_\mathrm{t}$ was chosen in favor of the real depth $d$, because it does not change, when the radii are
modified. So the overall geometry remains the same if one modifies only the radii. The tip depth can be considered as
the diagonal of the rhombus with sharp corners or the limit of the depth $d$ for $r_2 \rightarrow 0$.

```{eval-rst} 
.. autoclass:: DiamondGroove
    :members:
```

## The Square Groove

The {py:class}`SquareGroove` class represents a square shaped groove as shown in the figure.

![square groove geometry](/img/square.svg)

Mandatory measures of this groove are the two radii $r_1$ and $r_2$. To constrain geometry fully, any two of the
following must be given:

- usable width $w_\mathrm{u}$
- tip depth $d_\mathrm{t}$
- tip angle $\delta$

The radii are typically small, the depth is $d_\mathrm{t}$ typically $\approx \frac{w_\mathrm{u}}{2}$. The tip angle
$\delta$ is typically one or two degree larger than 90° for wear reasons.
$r_3$ and $r_4$ are considered to be zero, as well as $w_\mathrm{g}'$.

The tip depth $d_\mathrm{t}$ was chosen in favor of the real depth $d$, because it does not change, when the radii are
modified. So the overall geometry remains the same if one modifies only the radii. The tip depth can be considered as
the diagonal of the rhombus with sharp corners or the limit of the depth $d$ for $r_2 \rightarrow 0$.

The constructor will raise a warning, if the tip angle significantly deviates from 90°, consider to use
a [`DiamondGroove`](#the-diamond-groove) instead.

```{eval-rst} 
.. autoclass:: SquareGroove
    :members:
```