# The Plugin System

```{py:currentmodule} pyroll.core
```

```{note}
The plugin system has drastically changed in Version 2.0.
For the old version see [here](https://pyroll.readthedocs.io/en/v1/plugins.html).
```

Plugin packages are mainly meant to provided model logic to PyRolL, which does only ship with most basic relations at its core.
Simulating rolling processes is only possible by using plugin packages, without, PyRolL runs, of course, but the results are extremely rough estimations.
Plugins for PyRolL work through hooks.

A hook is a attribute of a class resp. an object, whose value can be explicitly set or computed from a set of functions.
A plugin can supply functions to hooks to represent a physical model approach.
The user, however, can always override the function logic by defining a value on the object itself by classic attribute syntax.

Let's give an example for clarification.

The {py:class}`.Profile` class defines the hook {py:attr}`.Profile.flow_stress`, which represents the flow stress of the profile's material.

```python

class Profile(HookHost):
    ...
    flow_stress = Hook[float]()
    ...
```

Classes using hooks have to be derived from {py:class}`HookHost`.
The {py:class}`Hook` instance is a descriptor providing logic and storage for a hooks value and functions.
It can be used as decorator for defining a function.

```python
@Profile.flow_stress
def flow_stress1(self: Profile):
    return 2 * self.strain
```

This function is now registered for calculating flow stresses of all profiles, if no explicit value is set.
The functions must have classic method signature, so the `self` argument always refers to the actual object instance.
The functions registered are evaluated in reverse order of their registration, so the last registered is the first executed.
The first result other than `None` is taken as the hook's actual value.
The value is cached until the cache is cleared using the {py:meth}`HookHost.clear_hook_cache` method.

The user may override hook function evaluation totally by setting an explicit value at object creation...

```python
profile = Profile.round(
    ...,
    flow_stress=100e6,
    ...,
)
```

...or later using attribute syntax.

```python
profile.flow_stress = 100e6
```

```{eval-rst}
.. autoclass:: Hook
    :members:
    :special-members: __get__, __set__, __delete__, __call__
```

```{eval-rst}
.. autoclass:: HookFunction
    :members:
    :special-members: __call__
```

```{eval-rst}
.. autoclass:: HookHost
    :members:
    :special-members: __cache__
```