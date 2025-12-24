# Roll Pass Design - Rolling Speed Considerations

```{py:currentmodule} pyroll.core
```

A classic task in roll pass design, is to estimate the setpoint or starting point for the rolling velocity or roll rotational frequencies.
This process is often tackled having in mind to limitations.
The first is the desired final speed of the product that ultimately defines the productivity of the mill. 
The second is the maximum heating rate that can be provided by the heating unit. 
Both limitations can be simulated in PyRolL using a designated variant of the {py:attr}`PassSequence.solve` method.

## Speed Calculations of a Single Stand

At first, what is important to consider, is the chosen model for the working radius.
A good first read regarding this topic, is the paper by Lee et al. (An Analytical Study of Mean Roll Radius in Rod Rolling, 2001, ISIJ International).
Per default, PyRolL uses another method to calculate the working radius.
Therefore, the software uses assumes, that the working radius lies in the center of gravity of the groove cross-section.
Further to the radius, the half gap height is added.
Models by different authors often define a so-called groove $\bar{H}$ factor which is the difference between the nominal radius / diameter of the roll and the working radius / diameter.
Generally, the working radius / diameter is then calculated as (the example uses the diameter):

$$
D_{w} = D - \bar{H}
$$

Some examples are e.g: 

- Wusatowski (Fundamentals of Rolling, Pergamon Press, London, (1969) 107.):

$$
\bar{H} = \frac{A_{eq, 1}}{w_1} - s
$$

- Saito et. al. (A new method for calculating deformation and force parameters in steel rod rolling and its application to roll pass design, Y. Saito, Y. Takahashi, M. Moriga and K. Kato: J. Jpn. Soc. Technol. Plast., 24 (1983), 1070 )

$$
\bar{H} = \left( \frac{A_{eq, 1}}{w_{eq, 1}} - s \right)
$$

The difference between the model of Saito et al. and Wusatowski resides in the used equivalent rectangle model. 
While Wusatowski used an area preserving variant of the model (maximum height or maximum width variant) as well as the outgoing width of the profile $w_1$, Saito et al. used the model of  Lendl (Rolled Bars - Part I - Calculation of Spread between non parallel roll surfaces, A. E. Lendl, Iron and Steel, 1948) and the equivalent width of the outgoing profile $w_{eq, 1}$.
  
- Lee (An Analytical Study of Mean Roll Radius in Rod Rolling, ISIJ International, Vol. 41 (2001), No. 11, pp. 1414–1416)

$$
D_{w} = \frac{\sum_{i=1}^{N} D_i}{N}
$$

Here the author evaluates the local roll diameter $D_{i}$ and builds the arithmetic mean. 
Note that the subdivision of the local diameter starts at the so-called detachment points. So the points where to profile height first becomes smaller than the local groove height.
What is further important to remind when using the models. 
PyRolL per default does not consider the forward slip of the material as this hard to estimate for groove roll passes. 
The resulting `profile.velocity` is considered to be at the highpoint of the roll pass. 
According to analysis of Goldhahn (Formänderungsverteilung sowie Kraft- und Arbeitsbedarf beim Walzen in der Streckkaliberreihe Rund-Oval, PhD-Thesis, 1981) this value can reach about 5 to 15% of the roll pass velocity at the high point.


## Basic Algorithm Design

Calculating the speeds of the individual stands, one aims for a constant volume flux in continuous mills. This is defined as: 

$$
A_0 \cdot v_0 = A_1 \cdot v_1
$$

As for the first iteration, where areas are unknown, the grooves usable are is utilized.
Either when the first velocity is given, the algorithm solves in forward manner.

```solve_velocities_forward(self, in_profile: Profile, initial_speed: float)```

When the last speed is given, the algorithm operates in a backward manner. 
When the second variant is used, also the final cross-section area has to be provided to achieve correct results. 

```solve_velocities_backward(self, in_profile: Profile, final_speed: float, final_cross_section_area: float)```

The last method, that should be also mentioned is the {py:attr}`PassSequence.solve_from_elongations` method.
Here PyRolL calculates the single stand velocities based on a finishing speed as well as defined elongations per pass. 

>**_NOTE:_**  The given elongations are not taken into account for calculations regarding the material flow.

## Example and Solve Method usage

In the current example we will analyse different working roll radii methods and their influence on the overall calculation results: 
Therefore we first load the respective modules:

```python
import copy
import numpy as np
import matplotlib.pyplot as plt
import pyroll.core as pr
import pyroll.wusatowski_spreading
```

Further we define a rolling train and a incoming profile. 
Here we use the pass sequence defined by Lee et al. in their respective paper mentioned above.

```python
in_profile = pr.Profile.round(
        radius=30e-3,
        temperature=1200 + 273.15,
        strain=0,
        material=["steel", "C15"],
        flow_stress=100e6,
        density=7.5e3,
        specific_heat_capacity=690,
    )
```

```python
lee_paper_sequence = pr.PassSequence([
    pr.RollPass(
        label="R1",
        roll=pr.Roll(
            groove=pr.CircularOvalGroove(
                r1=2e-3,
                r2=60.5e-3,
                depth=15.5e-3
            ),
            nominal_radius=155e-3,
        ),
        gap=6.5e-3,
    ),
    pr.Transport(label="I->II", length=1e3),
    pr.RollPass(
        label="R2",
        roll=pr.Roll(
            groove=pr.FalseRoundGroove(
                r1=2e-3,
                r2=23.75e-3,
                depth=17.5e-3,
                flank_angle=30
            ),
            nominal_radius=155e-3,
        ),
        gap=6.5e-3,
    ),
    pr.Transport(label="II->III", length=1e3),
    pr.RollPass(
        label="R3",
        roll=pr.Roll(
            groove=pr.CircularOvalGroove(
                r1=2e-3,
                r2=39.28e-3,
                depth=12.25e-3
            ),
            nominal_radius=155e-3,
        ),
        gap=5.5e-3,
    ),
    pr.Transport(label="III->IV", length=1e3),
    pr.RollPass(
        label="R4",
        roll=pr.Roll(
            groove=pr.FalseRoundGroove(
                r1=2e-3,
                r2=18e-3,
                depth=15.25e-3,
                flank_angle=30
            ),
            nominal_radius=155e-3,
        ),
        gap=5.5e-3,
    )
])
```

Now we have to define the compared models. 
Therefore, we have to overwrite the hook implementation of the `working_radius`.
This can be done as following:

```python
@pr.RollPass.Roll.working_radius
def saito_model_for_working_radius(self: pr.RollPass.Roll):
    groove_factor = (self.roll_pass.out_profile.cross_section.area / self.roll_pass.out_profile.width - self.roll_pass.gap) / 2
    return self.max_radius - groove_factor
```

Now PyRolL uses the working diameter model published by Lee et al.
The complete evaluation covering this analysis can be found in this ![notebook](/docs/examples/pyroll-examples/working-diameter-models.ipynb).
The resulting analysis can be summarized in the below figure: 

![Working Diameter Analysis](/docs/img/comparison_working_diameter_models.svg)

Here one can see, that nevertheless the chosen equivalent rectangle method, a noteable difference in the resulting velocities can not be seen.
