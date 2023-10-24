# Step-by-Step Tutorial from Core to Basic

```{py:currentmodule} pyroll.core
```

## Preconditioning

### Installing PyRolL Basic

:::{note}
If you already have a working installation of `pyroll-basic`, you can safely skip this section.
:::

The first requirement to follow this tutorial is to have a working Python installation with Python's package
manager `pip`.
Then, install the required packages by running the following in a terminal resp. command prompt:

```shell
pip install pyroll-basic
```

This will install the PyRolL core together with a bunch of PyRolL plugins and extensions as well as their dependencies.
Afterward, the command line interface (CLI) of PyRolL shall be available.
Check this by running.

```shell
pyroll --help
```

You shall see a help message similar to the following:

```text
Usage: pyroll [OPTIONS] COMMAND1 [ARGS]... [COMMAND2 [ARGS]...]...

Options:
  -c, --config-file FILE          The configuration TOML file.
  -C, --global-config / -nC, --no-global-config
                                  Whether use the global config file.
  -p, --plugin TEXT
  -d, --dir DIRECTORY             Change the working directory to the
                                  specified one.  [default: .]
  --help                          Show this message and exit.

Commands:
  create-config    Creates a standard config in FILE that can be used...
  create-input-py  Creates a sample input script in FILE that can be...
  export-csv       Exports the simulation results to JSON and writes them...
  export-json      Exports the simulation results to JSON and writes them...
  export-toml      Exports the simulation results to TOML and writes them...
  export-yaml      Exports the simulation results to YAML and writes them...
  input-py         Reads input data from the Python script FILE.
  new              Creates a new PyRoll simulation project in the...
  report           Generates a HTML report from the simulation results...
  solve            Runs the solution procedure on all loaded roll passes.
```

### Initializing Your Workspace

It is recommended to create a new empty directory somewhere.
Open a terminal resp. a command prompt in this directory to be able to run the input files of the following sections
with the CLI.
Download and save the input files of the following sections in this directory.

## Using Just the Core

The following code block shows the contents of the file [`input_01.py`](input_01.py).
It contains the absolute basic information needed to run a simulation in PyRolL using just the core package for one roll
pass.
The contents will be explained in the following in detail.

```{literalinclude} input_01.py
    :caption: "File: [`input_01.py`](input_01.py)"
```

The first line contains the import statement of the pyroll core package.
The alias `pr` is given to the package to shorten the access to the core classes of PyRolL.

```{literalinclude} input_01.py
    :lines: 1
```

After that, the input profile is defined.
The input profile is an instance of the class {py:class}`Profile`.
The name of the variable `in_profile` is mandatory for the CLI to recognize it as the input profile.
Here, a round shaped profile of 8 mm diameter is created using the {py:meth}`Profile.round` factory method.
A constant flow stress of 100 MPa is given to the profile to enable basic roll force calculation.

```{literalinclude} input_01.py
    :lines: 3-6
```

Now, the pass sequence is defined, although it consists for now of only one roll pass.
The pass sequence is an instance of the class {py:class}`PassSequence`.
It's only argument is usually the list of roll passes and transports it shall consist of.
For now, were are only adding one roll pass, nevertheless we need the pass sequence instance.

```{literalinclude} input_01.py
    :lines: 8-21
```

A roll pass is represented by an instance of the {py:class}`RollPass` class.
For now, we need only two arguments to the roll pass, an object representing the working rolls (only one, since they are
equal) and the size of the roll gap.

```{literalinclude} input_01.py
    :lines: 8-21
    :emphasize-lines: 2-13
```

A roll is represented by an instance of the {py:class}`Roll` class.
The most important properties are here the nominal radius of the roll (radius without the groove indent) and the groove
geometry.
The rotational frequency of the roll is here used to determine the kinetics.
The groove geometry is defined by a groove object.

```{literalinclude} input_01.py
    :lines: 8-21
    :emphasize-lines: 3-11
```

The PyRolL core includes a bunch of classes representing all common elongation groove types.
Here a circular oval (also known as 2-radii-oval) is used.
Here, the geometry is defined using the two radii `r1` and `r2` and the groove depth `depth`.
There are several other possibilities how the geometry can be constrained, see
the [docs of the circular oval groove](../../core/units/roll_pass/grooves/ovals.md#the-circular-oval-groove).

```{literalinclude} input_01.py
    :lines: 8-21
    :emphasize-lines: 4-8
```

With this the first simulation can be run with the CLI, if the file `input_01.py` resides in the current working
directory of the shell:

```shell
pyroll input-py -f input_01.py solve report
```

The command loads the input script named `input_01.py`, runs the simulation procedure and creates a report page.
A new file named `report.html` should appear in the directory.
Open it in your favorite web browser and inspect the simulation results.

The results will generally be quite far from reality, since the core only includes very rough approximations of the
physical relations.
In the following we will go step-by-step to improve our simulation by adding additional model approaches for partial
problems of the process model.

## Adding a Spreading Model

:::{seealso}
[Wusatowski Spreading Plugin Details](../../plugins/index.md#pyroll-wusatowski-spreading)
:::

You can observe, that the outgoing profile of our roll pass takes the ideal shape of the groove, meaning that it has
exactly the same width as the usable width of the groove (filling ratio is 1).
This is the default behavior of the core, if no further models are provides, that may describe the material flow in the
gap.
This may also lead to the strange behavior, that the outgoing profile has a larger cross-section as the incoming one.
Here, we will include Wusatowki's spreading model,
which will calculate the outgoing width of the profile by using an equivalent flass pass approach and an empirical
spreading function.

We have nothing more to do as loading the plugin module with an `import` statement.

```{literalinclude} input_02.py
    :emphasize-lines: 2
    :caption: "File: [`input_02.py`](input_02.py)"
```

If you run the simulation again, you will notice, that the profile does not fill the whole roll pass cross-section
anymore.
We are now approximately simulating the material flow in the pass.

## Adding a Flow Curve

:::{seealso}
[Freiberg Flow Stress Plugin Details](../../plugins/index.md#pyroll-freiberg-flow-stress)
:::

The next improvement will be to include an empirical flow curve instead of the constant flow stress given before.
This is done by importing the Freiberg flow stress plugin and giving some material state data.
The flow stress functions needs the mean workpiece temperature and a set of material coefficients.
Luckily, the plugin comes with some predefined material parameter sets.
We can define the name of the material the workpiece is made of and the flow stress plugin will check its database for
appropriate coefficients.

```{literalinclude} input_03.py
    :emphasize-lines: 3,7,8
    :caption: "File: [`input_03.py`](input_03.py)"
```

If you run the simulation again, you will notice that the flow stress of the incoming and outgoing profile changed and
are now different due to the strain applied in the roll pass.

## Adding Influence of Friction and Shear

:::{seealso}
[Hensel Plugin Details](../../plugins/index.md#pyroll-hensel-power-and-labour)
:::

Currently, the simulation does not respect any influences of process kinetics, friction and shear aside from pure
equivalent strain rate in the flow stress.
The exact consideration of those is quite complicated and high in computational effort.
But there are empirical approaches for approximation as the one by Hensel and coworkers.
We can include these considerations by importing the respective module.

```{literalinclude} input_04.py
    :emphasize-lines: 4
    :caption: "File: [`input_04.py`](input_04.py)"
```

If you run the simulation again, you will notice that roll force and roll torque changed and additional empirical
coefficients like the rolling efficiency and the lever arm coefficient appear.
These are used by the model to approximately take friction and shear into account.

## Adding More Precise Contact Areas

:::{seealso}
[Zouhar Contact Plugin Details](../../plugins/index.md#pyroll-zouhar-contact)
:::

Another huge influence on the calculation of roll forces and torques is the estimation of the contact area between rolls
and workpiece.
Since the geometry of this can be rather complex, often approximations are used.
The core assumes just a trapezoidal or a triangle depending on the roll pass type.
Zouhar developed a set of empirical equations to correct these rather rough approximations depending on the roll pass
type.
We can use these corrections by just loading the module, no further information must be given.

```{literalinclude} input_05.py
    :emphasize-lines: 5
    :caption: "File: [`input_05.py`](input_05.py)"
```

If you run the simulation again, you will notice that the contact area changed and therefore also roll force and roll
torque.
The used correction coefficients are also listed in the report.

## Adding Thermal Calculation

The last model we want to add for now is the calculation of temperature change due to deformation and heat flow through
the roll contact.
Therefore, we import the `pyroll.integral_thermal` module, which gives an integral heat flow and generation balance in
the roll pass.
We must provide the density and the thermal capacity (specific heat capacity) of the workpiece material to be able to
use this plugin.
Additionally, we may change the mean surface temperature of the roll as shown.

```{literalinclude} input_06.py
    :emphasize-lines: 6,12,13,26
    :caption: "File: [`input_06.py`](input_06.py)"
```

If you run the simulation again, you will notice that the temperature of the profile changes now within the roll pass.
The respective contributions to the temperature change are also listed in the report.

## Adding a Second Roll Pass

Simulating one roll pass alone is not appropriate for developing a rolling technology.
So let us add a second roll pass with a round groove of 7 mm diameter.

```{literalinclude} input_07.py
    :emphasize-lines: 29-40
    :caption: "File: [`input_07.py`](input_07.py)"
```

If you run the simulation again, you will notice that the second roll pass now appears in the report and the outgoing profile of the whole sequence is taken as the one of the second pass.

## Adding a Transport

If you look at the input profile of the second pass, you will notice that it is assumed to have the strain and the temperature of the output profile of the first one.
In reality, roll passes are not connected directly, but there is some space between the stands and/or some time lasts until the next pass is performed.
In this time the material may recrystallize and the temperature goes down due to heat transfer by convection and radiation.
This can be described by a transport unit, here assumed with a duration of 1 s.

```{literalinclude} input_08.py
    :emphasize-lines: 29-31
    :caption: "File: [`input_08.py`](input_08.py)"
```

If you run the simulation again, you will notice that the strain is reset to 0 in the transport and the workpiece will cool down a bit.
The first appears since the core assumes complete softening in each transport.
By using appropriate model plugins this behavior can be changed, but this is out of scope for this tutorial.
Search in the [plugins list](../../plugins/index.md) for appropriate plugins.
