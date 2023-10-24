# A Basic Example of PyRolL

```{note}
The following example assumes a UNIX system with an already installed compatible Python version.
On Windows, the main part works accordingly.
```

## Preconditioning

First, we create a new directory for our simulation project and open it.

```shell
mkdir pyroll_proj1
cd pyroll_project1
```

Now we create a `Pipfile` and a virtual environment using pipenv.
We install `pyroll-basic` and IPython.

```shell
pipenv install pyroll-basic ipython
```

Now we activate the environment in a new shell.

```shell
pipenv shell
```

We create a new file named `input.py` with the following content.

```python
import pyroll.basic as pr

# initial profile
in_profile = pr.Profile.square(
    side=45e-3,
    corner_radius=3e-3,
    temperature=1200 + 273.15,
    strain=0,
    material="C45",
    density=7.8e3,
    specific_heat_capacity=690,
)

# mean roll radii
# in reality asymmetrical, but current implementation only for symmetrical problems
mean_roll_radius_1_upper = (328e-3 + 324e-3) / 2 / 2
mean_roll_radius_1_lower = (324e-3 + 320e-3) / 2 / 2
mean_roll_radius_2_upper = (299e-3 + 297e-3) / 2 / 2
mean_roll_radius_2_lower = (297e-3 + 295e-3) / 2 / 2
mean_roll_radius_3_upper = (280e-3 + 278e-3) / 2 / 2
mean_roll_radius_3_lower = (278e-3 + 276e-3) / 2 / 2

transport_duration = 5  # average time to feed workpiece into next pass

# pass sequence
sequence = pr.PassSequence([
    pr.RollPass(
        label="Diamond I",
        roll=pr.Roll(
            groove=pr.DiamondGroove(
                usable_width=76.55e-3,
                tip_depth=22.1e-3,
                r1=12e-3,
                r2=8e-3
            ),
            nominal_radius=mean_roll_radius_1_lower,
        ),
        velocity=1,
        gap=3e-3,
    ),
    pr.Transport(
        duration=transport_duration
    ),
    pr.RollPass(
        label="Square II",
        roll=pr.Roll(
            groove=pr.SquareGroove(
                usable_width=52.7e-3,
                tip_depth=25.95e-3,
                r1=8e-3,
                r2=6e-3
            ),
            nominal_radius=mean_roll_radius_1_upper,
        ),
        velocity=1,
        gap=3e-3,
    ),
    pr.Transport(
        duration=transport_duration
    ),
    pr.RollPass(
        label="Diamond III",
        roll=pr.Roll(
            groove=pr.DiamondGroove(
                usable_width=58.3e-3,
                tip_depth=16.85e-3,
                r1=7e-3,
                r2=8e-3
            ),
            nominal_radius=mean_roll_radius_1_lower,
        ),
        velocity=1,
        gap=3e-3,
    ),
    pr.Transport(
        duration=transport_duration
    ),
    pr.RollPass(
        label="Square IV",
        roll=pr.Roll(
            groove=pr.SquareGroove(
                usable_width=40.74e-3,
                tip_depth=20.05e-3,
                r1=7e-3,
                r2=5e-3
            ),
            nominal_radius=mean_roll_radius_1_upper,
        ),
        velocity=1,
        gap=3e-3,
    ),
    pr.Transport(
        duration=transport_duration
    ),
    pr.RollPass(
        label="Oval V",
        roll=pr.Roll(
            groove=pr.CircularOvalGroove(
                depth=7.25e-3,
                r1=6e-3,
                r2=44.5e-3
            ),
            nominal_radius=mean_roll_radius_1_lower,
        ),
        velocity=1,
        gap=3e-3,
    ),
    pr.Transport(
        duration=transport_duration
    ),
    pr.RollPass(
        label="Square VI",
        roll=pr.Roll(
            groove=pr.SquareGroove(
                usable_width=29.64e-3,
                tip_depth=14.625e-3,
                r1=6e-3,
                r2=4e-3
            ),
            nominal_radius=mean_roll_radius_1_upper,
        ),
        velocity=1,
        gap=3e-3,
    ),
    pr.Transport(
        duration=transport_duration
    ),
    pr.RollPass(
        label="Oval VII",
        roll=pr.Roll(
            groove=pr.CircularOvalGroove(
                depth=5.05e-3,
                r1=7e-3,
                r2=33e-3
            ),
            nominal_radius=mean_roll_radius_1_lower,
        ),
        velocity=1,
        gap=3e-3,
    ),
    pr.Transport(
        duration=transport_duration
    ),
    pr.RollPass(
        label="Square VIII",
        roll=pr.Roll(
            groove=pr.SquareGroove(
                usable_width=21.54e-3,
                tip_depth=10.6e-3,
                r1=5e-3,
                r2=3e-3
            ),
            nominal_radius=mean_roll_radius_1_upper,
        ),
        velocity=1,
        gap=3e-3,
    ),
    pr.Transport(
        duration=transport_duration
    ),
    pr.RollPass(
        label="Oval IX",
        roll=pr.Roll(
            groove=pr.CircularOvalGroove(
                depth=4.43e-3,
                r1=6e-3,
                r2=25.5e-3
            ),
            nominal_radius=mean_roll_radius_2_lower,
        ),
        velocity=1,
        gap=1e-3,
    ),
    pr.Transport(
        duration=transport_duration
    ),
    pr.RollPass(
        label="Round X",
        roll=pr.Roll(
            groove=pr.RoundGroove(
                r1=2e-3,
                r2=15.8e-3 / 2,
                depth=7.65e-3
            ),
            nominal_radius=mean_roll_radius_2_upper,
        ),
        velocity=1,
        gap=0.5e-3,
    ),
])
```

This input file represents a square-diamond and oval-square pass sequence available at the experimental three-high rolling plant at the [Institute of Metal Forming](https://tu-freiberg.de/en/fakult5/imf), where the project is located.

## CLI Usage

We can run the simulation and generate a report using the CLI.

```shell
pyroll input-py solve report
```

Examine the report to analyse the simulation results.

We can run it again and export the data for further processing to JSON.

```shell
pyroll input-py solve export-json
```

## Direct Python Usage

First, we open an IPython shell.

```shell
ipython
```

Then we import the input file as a module and run the solution procedure of the pass sequence.

```python
from input import in_profile, sequence

sequence.solve(in_profile)
```

The solution data is stored directly in the objects, we can access it using attribute syntax.

```python
print("Roll force of first pass:", sequence[0].roll_force)
print("Roll torque of second pass:", sequence[2].roll.roll_torque) # since index 1 is the first transport
```

Report generation is also possible, but we receive the HTML code of the report as string, so we save it to a file.

```python
from pyroll.report import report
from pathlib import Path

r = report(sequence)
Path("report.html").write_text(r)
```

We can also generate JSON.

```python
from pyroll.export import to_json

j = to_json(sequence)
Path("export.json").write_text(j)
```

But we can also modify the objects and simulate again, using the old solution as initial guess of the new one.

```python
print("Old out temperature:", sequence[-1].out_profile.temperature)

in_profile.temperature = 1150 + 273.15 # a bit colder input workpiece
sequence.solve(in_profile)

print("New out temperature:", sequence[-1].out_profile.temperature)
```

This shall give you a glimpse on the capabilities of direct Python usage.