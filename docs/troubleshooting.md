# Troubleshooting

```{py:currentmodule} pyroll.core
```

## Find Out Which Plugins Are Loaded

Most errors in usage (not development) have their origin in missing or excess plugins.

First step is to check the loaded modules.

```python
import sys

pyroll_modules = [m for m in sys.modules if "pyroll" in m]
```

If some plugin is missing, import it.
If there is some undesired plugin loaded, find out where it is imported.

## Use a Debugger

Due to the dynamic nature of the PyRolL objects, it is sometimes hard to determine what's going on.
Connect a debugger to your process and examine the current object instances.
You may be interested in the functions registered in the hook descriptors ({py:attr}`Hook.functions` attribute) and the contents of the objects `__dict__` and `__cache__`.
Read [here](core/plugins) for details.

## AttributeError "Hook call for '...' on '...' could not provide a value."

Most common reason is missing data in the input.
For the requested hook, no explicit value was set in the input and there was no function returning other than `None`.
Set an explicit value on the respective object or define a hook function providing the value.

## AttributeError "Hook call for '...' on '...' resulted in a RecursionError."

The calling of hook functions produced a `RecursionError`.
Most common reason is missing data like above.
If you are developing your own plugin, while this error occurs, you may have to implement a check for recursion using helpers like {py:meth}`HookHost.has_set_or_cached` or {py:meth}`HookFunction.cycle`.

## ValueError "Hook call for '...' on '...' resulted in an infinite value."

Typical reason is problem with the units of measure.
Have you accidentally forgotten to add a suffix for the order of magnitude somewhere (like in `1.234e3`)? 
This often results in negative roots, divisions by zero or alike, which are not raised as error by numpy, but represented by {py:data}`numpy.nan` or {py:data}`numpy.inf`.
Check all your inputs.

## ValueError "Profile's width can not be larger than its contour lines. May be caused by critical overfilling."

Occurs when the calculated width of the profile is larger than 1.1 times the width of the grooves contour lines, which is considered as critical overfilling.
This may have several reasons:

- an error in your input data (magnitudes, typos, ...)
- the pass sequence you try to simulate is not realistic
- the material flow model is not suitable for your current conditions

First check your inputs, then try to alter the roll gap of the respective pass to make it work.
It this does not work, try to use different material flow resp. spreading models.

## Warning "Solution iteration of ... exceeded the maximum iteration count of ..."

The iteration procedure within a units {py:meth}`Unit.solve` method exited because the maximum iteration was exceeded.
Usually, increasing the iteration count with {py:attr}`Unit.max_iteration_count` does not solve the problem, because the iteration was trapped in a cycle.
The desired precision was not reached, but you may use the results anyway, but be careful.
Small alteration of the input data often circumvents the problem, also try to use other models.
Sometimes, the problem lies in plugins, that are loaded, but not needed, see [above](#find-out-which-plugins-are-loaded).