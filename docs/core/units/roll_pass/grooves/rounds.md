# Round-like Grooves

```{py:currentmodule} pyroll.core
```

## The Round Groove

The {py:class}`RoundGroove` class represents a groove with a circular cross-section as shown in the figure.

![round groove geometry](/img/round.svg)

It is defined by two radii $r_1$ and $r_2$ and the depth $d$.
The geometric constraints are $r_1 << r_2$ and $d < r_2$.
$r_3$ and $r_4$ are considered to be zero, as well as $b_d$ and $b_d'$.

The angles can be calculated as following:

$$ \alpha_1 = \alpha_2 = \arccos \left( 1 - \frac{d}{r_1 + r_2} \right)
$$

The usable width is then:

$$ b_\mathrm{kn} = 2 \left( r_1 \sin \alpha_1 + r2 \sin \alpha_2 - r_1 \tan \frac{\alpha_1}{2} \right)
$$

```{eval-rst} 
.. autoclass:: RoundGroove
    :members:
```

## The False Round Groove

The {py:class}`FalseRoundGroove` class represents a groove with a roughly circular cross-section, which shows a small straight
flank, as shown in the figure.

![false round groove geometry](/img/false_round.svg)

It is defined by two radii $r_1$ and $r_2$, the depth $d$ and the flank angle $\alpha_1$.
The geometric constraints are $r_1 << r_2$, $d < r_2$ and $\alpha_1 < 90°$ .
$r_3$ and $r_4$ are considered to be zero, as well as $b_d$ and $b_d'$.

The usable width can be calculated as:

$$ b_\mathrm{kn} = 2 \frac{d + \frac{r_2}{\cos \alpha_1} - r_2}{\tan \alpha_1} $$

```{eval-rst} 
.. autoclass:: FalseRoundGroove
    :members:
```