# Round-like Grooves

```{py:currentmodule} pyroll.core
```

## The Round Groove

The {py:class}`RoundGroove` class represents a groove with a circular cross-section as shown in the figure.

![round groove geometry](/img/round.svg)

It is defined by the radius $r_1$ and any two of radius $r_2$, depth $d$ and usable width $w_\mathrm{u}$.
The geometric constraints are $r_1 << r_2$ and $d < r_2$.
$r_3$ and $r_4$ are considered to be zero, as well as $w_\mathrm{g}'$.

```{eval-rst} 
.. autoclass:: RoundGroove
    :members:
```

## The False Round Groove

The {py:class}`FalseRoundGroove` class represents a groove with a roughly circular cross-section, which shows a small straight
flank, as shown in the figure.

![false round groove geometry](/img/false_round.svg)

It is defined by the radius $r_1$ and any two of radius $r_2$, depth $d$ and usable width $w_\mathrm{u}$.
The flank is determined by either one of the flank angle `\phi`, the flank's horizontal width, its vertical height or collinear length.
The geometric constraints are $r_1 << r_2$, $d < r_2$ and $\alpha_1 < 90°$.
$r_3$ and $r_4$ are considered to be zero, as well as $w_\mathrm{g}'$.

```{eval-rst} 
.. autoclass:: FalseRoundGroove
    :members:
```