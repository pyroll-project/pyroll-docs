# Basic Assumptions and Definitions

The following terms shall be defined:

Rolling Direction, Length Direction, Longitudinal Direction
~ direction of principal material flow

Length, $l$
~ extent of the workpiece in rolling direction

Thickness Direction, Height Direction
~ direction of reduction during a roll pass

Thickness, Height, $h$
~ extent of the workpiece cross-section in thickness resp. height direction

Width Direction
~ direction of spreading during a roll pass

Width, $w$
~ extent of the workpiece in width direction

See the following figures for clarification of height and width directions in two-roll and three-roll passes.
Note, that in three-roll passes the measure width and height a rather imaginary measures, since in fact only the half width and half height can be measured, due to the 3-fold rotation symmetry.

:::{figure-md} fig:directions-two-roll
:align: center

![Two-Roll Pass Directions](/img/directions-two-roll.svg)

Directions in Two-Roll Passes
:::

:::{figure-md} fig:directions-three-roll
:align: center

![Three-Roll Pass Directions](/img/directions-three-roll.svg)

Directions in Three-Roll Passes
:::

In the following some basic assumptions that are made within code and design are listed.
Keep them in mind while reading through the documentation.
These assumptions may change in future versions of the framework.

1. **Coordinate System** The $x$-axis equals the rolling direction, while $y$ equals the thickness direction, and $z$ equals the width direction. The coordinate system is right-handed.
2. **Symmetry** Roll passes, profiles, and grooves are symmetric at the $y$ and $z$ axes. Despite defining asymmetric passes is possible to some extent, you should avoid this, as it may lead to wrong results. This is intended to be broken up in future releases.
3. **Stationarity** Only stationary processes are calculated. There are no intrinsic dynamics within the models.
4. **SI-Units** Everywhere basic SI-units are used, without scaling factors (milli, kilo, etc.). Denote orders of magnitude by using the `1.234e3` syntax of Python float literals. Especially imperial units are not supported. Principally, also other coherent unit systems may be used, but for the purpose of material databases and similar the use of basic SI is strongly recommended. Use other units at your own risk.