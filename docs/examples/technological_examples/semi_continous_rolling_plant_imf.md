# A Rolling Train Everyone can Talk About

As a common basis when one wants to simply try PyRolL or you need a minimal working example to discuss something with a
person outside of your company, one can always refer to the semi-continous rolling train operated at the Institute of
Metal Forming.
In the upcoming sections we will explain how the mill works and provide the basic implementation of the train in PyRolL

## Plant setup

The rolling train was build as a semi-continuous rolling train which means that it consists of a reversing mill
representing the roughing train of a street and a 4 finishing stands which represent the finishing train.
Finally, the profile is passed to the cooling section which can be operated with up to 4 turbulence cooling sections and
a laying head with a stelmor conveyor or a water bath.
The plant was build in a modular approach, that means that every rolling mill of the finishing train is adjustable in
it's position towards the other mills.
Currently, there are various pass schedules to roll various profiles like rounds, squares, hexagons or rebars.

In its most basic configuration which will be presented here, the mill is operated in the following manner:

| #   | Groove Type   | Groove Width [mm] | Groove Height [mm] | Roll Gap [mm] | Nominal Roll Radius [mm] | Rolling Velocity [ms^-1] |
|-----|---------------|-------------------|--------------------|---------------|--------------------------|--------------------------|
| R1  | Swedish Oval  | 60                | 28.0               | 13.5          | 160.5                    | 1.0                      |
| R2  | Round         | 36.6              | 36.5               | 1.5           | 160.5                    | 1.0                      |
| R3  | Swedish Oval  | 60                | 16.0               | 1.5           | 160.5                    | 2.0                      |
| R4  | Round         | 27.6              | 26.0               | 1.0           | 160.5                    | 2.0                      |
| R5  | Circular Oval | 34.0              | 13.4               | 5.4           | 160.5                    | 2.0                      |
| R6  | Round         | 20.4              | 19.8               | 1.8           | 160.5                    | 2.0                      |
| R7  | Circular Oval | 34                | 8.8                | 0.8           | 160.5                    | 2.0                      |
| R8  | Round         | 14.7              | 14.8               | 3.8           | 160.5                    | 2.0                      |
| R9  | Circular Oval | 20.1              | 8.5                | 3.5           | 160.5                    | 2.0                      |
| R10 | Round         | 11.3              | 12.0               | 4.0           | 160.5                    | 2.0                      |
| F1  | Circular Oval | 15.6              | 8.1                | 2.3           | 107.5                    | 7.8                      |
| F2  | Round         | 10.1              | 10.0               | 1.5           | 107.5                    | 9.3                      |
| F3  | Circular Oval | 12.8              | 6.2                | 2.0           | 107.5                    | 12.1                     |
| F4  | Round         | 8.1               | 8.0                | 1.5           | 85.0                     | 15.8                     |

The distance between the reversing mill and the first finishing stand is 4.5 meters and the distance between the single
finishing stands is 1.5 meters.
Drawings of the grooves are available when contacting the International Center for Groove Pass Design
using `kalibrierzentrum@imf.tu-freiberg.de`.
The presented pass schedule is used to roll a 48 millimeter (cold) round profile made from C45 to a 8 millimeter round profile.
The measurements are given in a cold state.
The example is constructed to use the `pyroll-basic` metapackage.
If you want to know what that means in detail, check our detailed documentation of the `pyroll-basic`
package [here](https://pyroll.readthedocs.io/en/latest/examples/basic.html#).

## Initializing PyRolL as well as the PyRolL Logger

At first, we load the `pyroll-basic` package and configure the logger.

```python
import sys
import logging
import pyroll.basic as pr

logging.basicConfig(stream=sys.stdout, format='[%(levelname)s] %(name)s: %(message)s')
logging.getLogger("pyroll").setLevel(logging.INFO)
```

## Creating the Initial Profile

As already mentioned, the Initial Profile is a 48 mm round profile made from C45.
Additional parameters represented in SI-Units can be seen in the following table:

| Material               | C45              |
|------------------------|------------------|
| Diameter               | 50e-3 [m] (warm) |
| Temperature            | 1473.25 K        |
| Density                | 7500 [kg/m^3]    |
| Specific Heat Capacity | 690 [J/K]        |
| Thermal Conductivity   | 23    [W/mK]     |

Transferring that to python code goes like this.

```python
in_profile = pr.Profile.round(
    diameter=50e-3,
    temperature=1200 + 273.15,
    strain=0,
    material=["C45", "steel"],
    freiberg_flow_stress_coefficients=pr.FreibergFlowStressCoefficients(
        a=2731.39 * 1e6,
        m1=-0.00268,
        m2=0.31076,
        m3=0,
        m4=-0.00056,
        m5=0.00046,
        m6=0,
        m7=-0.98375,
        m8=0.000139,
        m9=0,
        baseStrain=0.1,
        baseStrainRate=0.1
    ),
    density=7.5e3,
    specific_heat_capacity=690,
    thermal_conductivity=23
)
```

## Creating the Rolling Train

The rolling train or plant setup is stored in a object of Type `PassSequence`. 
Want to know what that means? 
Check out the explanation [here](https://pyroll.readthedocs.io/en/latest/examples/technological_examples/extracting_values.html#).
If not just think of it as a list. 

```python
REVERSING_PAUSE_DURATION = 6.1
ROLL_SURFACE_TEMPERATURE = 273.15 + 25
SPARLING_MATERIAL_COEFFICIENT = 0.95

sequence = pr.PassSequence([
    pr.RollPass(
        label="K 02/001 - 1",
        roll=pr.Roll(
            groove=pr.SwedishOvalGroove(
                r1=6e-3,
                r2=26e-3,
                ground_width=38e-3,
                usable_width=60e-3,
                depth=7.25e-3
            ),
            nominal_radius=321e-3 / 2,
            rotational_frequency=0.99,
            temperature=ROLL_SURFACE_TEMPERATURE

        ),
        gap=13.5e-3,
        disk_element_count=15,
        sparling_material_coefficient=SPARLING_MATERIAL_COEFFICIENT,
        coulomb_friction_coefficient=0.4,
        back_tension=0,
        front_tension=0
    ),
    pr.Transport(
        label="I->II",
        duration=REVERSING_PAUSE_DURATION,
        disk_element_count=10,
    ),
    pr.RollPass(
        label="K 05/001 - 2",
        roll=pr.Roll(
            groove=pr.RoundGroove(
                r1=4e-3,
                r2=18e-3,
                depth=17.5e-3
            ),
            nominal_radius=321e-3 / 2,
            rotational_frequency=0.99,
            temperature=ROLL_SURFACE_TEMPERATURE
        ),
        gap=1.5e-3,
        disk_element_count=20,
        sparling_material_coefficient=SPARLING_MATERIAL_COEFFICIENT,
        coulomb_friction_coefficient=0.4,
        back_tension=0,
        front_tension=0
    ),
    pr.Transport(
        label="II->III",
        duration=REVERSING_PAUSE_DURATION,
        disk_element_count=10,
    ),
    pr.RollPass(
        label="K 02/001 - 3",
        roll=pr.Roll(
            groove=pr.SwedishOvalGroove(
                r1=6e-3,
                r2=26e-3,
                ground_width=38e-3,
                usable_width=60e-3,
                depth=7.25e-3
            ),
            nominal_radius=321e-3 / 2,
            rotational_frequency=1.98,
            temperature=ROLL_SURFACE_TEMPERATURE
        ),
        gap=1.5e-3,
        disk_element_count=20,
        sparling_material_coefficient=SPARLING_MATERIAL_COEFFICIENT,
        coulomb_friction_coefficient=0.4,
        back_tension=0,
        front_tension=0
    ),
    pr.Transport(
        label="III->IV",
        duration=REVERSING_PAUSE_DURATION,
        disk_element_count=10,
    ),
    pr.RollPass(
        label="K 05/002 - 4",
        roll=pr.Roll(
            groove=pr.RoundGroove(
                r1=4e-3,
                r2=13.5e-3,
                depth=12.5e-3
            ),
            nominal_radius=321e-3 / 2,
            rotational_frequency=1.98,
            temperature=ROLL_SURFACE_TEMPERATURE
        ),
        gap=1e-3,
        disk_element_count=20,
        sparling_material_coefficient=SPARLING_MATERIAL_COEFFICIENT,
        coulomb_friction_coefficient=0.4,
        back_tension=0,
        front_tension=0
    ),
    pr.Transport(
        label="IV->V",
        duration=REVERSING_PAUSE_DURATION,
        disk_element_count=10,
    ),
    pr.RollPass(
        label="K 03/001 - 5",
        roll=pr.Roll(
            groove=pr.CircularOvalGroove(
                r1=6e-3,
                r2=38e-3,
                depth=4e-3
            ),
            nominal_radius=321e-3 / 2,
            rotational_frequency=1.98,
            temperature=ROLL_SURFACE_TEMPERATURE
        ),
        gap=5.4e-3,
        disk_element_count=20,
        sparling_material_coefficient=SPARLING_MATERIAL_COEFFICIENT,
        coulomb_friction_coefficient=0.4,
        back_tension=0,
        front_tension=0
    ),
    pr.Transport(
        label="V->VI",
        duration=REVERSING_PAUSE_DURATION,
        disk_element_count=10,
    ),
    pr.RollPass(
        label="K 05/003 - 6",
        roll=pr.Roll(
            groove=pr.RoundGroove(
                r1=3e-3,
                r2=10e-3,
                depth=9e-3
            ),
            nominal_radius=321e-3 / 2,
            rotational_frequency=1.98,
            temperature=ROLL_SURFACE_TEMPERATURE
        ),
        gap=1.8e-3,
        disk_element_count=20,
        sparling_material_coefficient=SPARLING_MATERIAL_COEFFICIENT,
        coulomb_friction_coefficient=0.4,
        back_tension=0,
        front_tension=0
    ),
    pr.Transport(
        label="VI->VII",
        duration=REVERSING_PAUSE_DURATION,
        disk_element_count=10,
    ),
    pr.RollPass(
        label="K 03/001 - 7",
        roll=pr.Roll(
            groove=pr.CircularOvalGroove(
                r1=6e-3,
                r2=38e-3,
                depth=4e-3
            ),
            nominal_radius=321e-3 / 2,
            rotational_frequency=1.98,
            temperature=ROLL_SURFACE_TEMPERATURE
        ),
        gap=0.8e-3,
        disk_element_count=20,
        sparling_material_coefficient=SPARLING_MATERIAL_COEFFICIENT,
        coulomb_friction_coefficient=0.4,
        back_tension=0,
        front_tension=0
    ),
    pr.Transport(
        label="VII->VIII",
        duration=REVERSING_PAUSE_DURATION,
        disk_element_count=10,
    ),
    pr.RollPass(
        label="K 05/004 - 8",
        roll=pr.Roll(
            groove=pr.RoundGroove(
                r1=2e-3,
                r2=7.5e-3,
                depth=5.5e-3
            ),
            nominal_radius=321e-3 / 2,
            rotational_frequency=1.98,
            temperature=ROLL_SURFACE_TEMPERATURE
        ),
        gap=3.8e-3,
        disk_element_count=20,
        sparling_material_coefficient=SPARLING_MATERIAL_COEFFICIENT,
        coulomb_friction_coefficient=0.4,
        back_tension=0,
        front_tension=0
    ),
    pr.Transport(
        label="VIII->IX",
        duration=REVERSING_PAUSE_DURATION,
        disk_element_count=10,
    ),
    pr.RollPass(
        label="K 03/002 - 9",
        roll=pr.Roll(
            groove=pr.CircularOvalGroove(
                r1=6e-3,
                r2=21.2e-3,
                depth=2.5e-3
            ),
            nominal_radius=321e-3 / 2,
            rotational_frequency=1.98,
            temperature=ROLL_SURFACE_TEMPERATURE
        ),
        gap=3.5e-3,
        disk_element_count=20,
        sparling_material_coefficient=SPARLING_MATERIAL_COEFFICIENT,
        coulomb_friction_coefficient=0.4,
        back_tension=0,
        front_tension=0
    ),
    pr.Transport(
        label="IX->X",
        duration=REVERSING_PAUSE_DURATION,
        disk_element_count=10,
    ),
    pr.RollPass(
        label="K 05/005 - 10",
        roll=pr.Roll(
            groove=pr.RoundGroove(
                r1=0.5e-3,
                r2=6e-3,
                depth=4e-3
            ),
            nominal_radius=321e-3 / 2,
            rotational_frequency=1.98,
            temperature=ROLL_SURFACE_TEMPERATURE
        ),
        gap=4e-3,
        disk_element_count=20,
        sparling_material_coefficient=SPARLING_MATERIAL_COEFFICIENT,
        coulomb_friction_coefficient=0.4,
        back_tension=0,
        front_tension=0
    ),
    pr.Transport(
        label="->F1",
        duration=REVERSING_PAUSE_DURATION,
        disk_element_count=10,
    ),
    pr.RollPass(
        label="F1 - K 3/50",
        roll=pr.Roll(
            groove=pr.CircularOvalGroove(
                r1=2.5e-3,
                usable_width=15.6e-3,
                depth=(8.1e-3 - 2.3e-3) / 2,
            ),
            nominal_radius=215e-3 / 2,
            rotational_frequency=11.5,
            temperature=ROLL_SURFACE_TEMPERATURE
        ),
        gap=2.3e-3,
        disk_element_count=20,
        sparling_material_coefficient=SPARLING_MATERIAL_COEFFICIENT,
        coulomb_friction_coefficient=0.4,
        back_tension=0,
        front_tension=0
    ),
    pr.Transport(
        label="F1->F2",
        duration=1.5 / 7.8,
        disk_element_count=10
    ),
    pr.RollPass(
        label="F2 - K 9/24",
        roll=pr.Roll(
            groove=pr.RoundGroove(
                r1=0.5e-3,
                r2=5.1e-3,
                depth=(10e-3 - 1.5e-3) / 2
            ),
            nominal_radius=215e-3 / 2,
            rotational_frequency=13.77,
            temperature=ROLL_SURFACE_TEMPERATURE
        ),
        gap=1.5e-3,
        disk_element_count=20,
        sparling_material_coefficient=SPARLING_MATERIAL_COEFFICIENT,
        coulomb_friction_coefficient=0.4,
        back_tension=0,
        front_tension=0
    ),
    pr.Transport(
        label="F2->F3",
        duration=1.5 / 9.3,
        disk_element_count=10
    ),
    pr.RollPass(
        label="F3 - K3/51",
        roll=pr.Roll(
            groove=pr.CircularOvalGroove(
                r1=2.5e-3,
                usable_width=12.8e-3,
                depth=(6.2e-3 - 1.96e-3) / 2,
            ),
            nominal_radius=215e-3 / 2,
            rotational_frequency=17.85,
            temperature=ROLL_SURFACE_TEMPERATURE
        ),
        gap=1.96e-3,
        disk_element_count=20,
        sparling_material_coefficient=SPARLING_MATERIAL_COEFFICIENT,
        coulomb_friction_coefficient=0.4,
        back_tension=0,
        front_tension=0
    ),
    pr.Transport(
        label="F3->F4",
        duration=1.5 / 12.06,
        disk_element_count=10
    ),
    pr.RollPass(
        label="F4 - K 9/23",
        roll=pr.Roll(
            groove=pr.RoundGroove(
                r1=0.5e-3,
                r2=4.1e-3,
                depth=(8e-3 - 1.5e-3) / 2
            ),
            nominal_radius=170e-3 / 2,
            rotational_frequency=29.5,
            temperature=ROLL_SURFACE_TEMPERATURE
        ),
        gap=1.5e-3,
        disk_element_count=20,
        sparling_material_coefficient=SPARLING_MATERIAL_COEFFICIENT,
        coulomb_friction_coefficient=0.4,
        back_tension=0,
        front_tension=0
    ),
])
```

