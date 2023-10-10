# Extraction and Visualization Examples

```{note}
The following example assumes a sucess run pyroll simulation, if you don't know how to setup and run a pyroll simulation, checkout the [Basic Tutorial](https://pyroll.readthedocs.io/en/latest/examples/basic.html#).
```

Assuming you have a solved pyroll simulation stored inside a `PassSequence` object called `sequence`.
Therefore, you will have at some point a line of code looking like this:

```python
sequence.solve(in_profile) 
```

Now, one wants to extract various values from the sequence object.
Generally, the sequence object is of type `PassSequence` which is derived from the `Sequenece` class.
This means, that the sequence in that case is a iterable with random access. 
You can ask for any item of the sequence without having to consume the items before it.
To ease up here is a quick and easy explanation of that.

```{note}
Imagine you have a list of items, like a shopping list. 
This list is like a sequence, and you can think of it as a line of items. 
Normally, when you go through a line, you have to pick up items one by one in order, starting from the first one and going to the last one. 
This is called consuming the items in order.

Now, think about a special type of list, like a magical shopping list. 
With this list, you can instantly jump to any item on the list without going through the ones before it. 
It's like you have super-fast access to any item you want, no matter where it is on the list. 
This is what they mean by "random access."

So, in simple words, when we say a "sequence object is of type PassSequence derived from the Sequence class," 
it means we have a special kind of list that allows you to get any item from it instantly, without going through the ones before it. 
It's like having a superpower for lists!
```

Okay, having that sorted out now lets extract some values. 
Our classic method is at first to separate the units in the list by their type, because a lot of units don't share similar attributes.
In a pythonic manner (meaning a very suitable way to do it in python) this is done through so called `list comprehension`.
This will look like this:

```python
roll_passes = [unit for unit in sequence if isinstance(unit, pr.RollPass)]
```
A short explanation of what is done here.
We have the sequence object which is iterated, and every unit inside this sequence is checked.
If it is of type `RollPass` it is added to the list, if not then not.
Now that we have all the roll passes stored inside a list, we can create several more lists that contain various variables which can be plotted. 
What is often of interest are the characteristic forming values of a rolling schedule.
Therefore, we first extract the values and store them into separate lists.

```python
stand_numbers = range(1, len(roll_passes) + 1, 1)
strains = []
strain_rates = []
temperatures = []
reductions = []
for rp in roll_passes:
    strains.append(rp.strain)
    strain_rates.append(rp.strain_rate)
    temperatures.append(rp.out_profile.temperature - 273.15)
    reductions.append((1 - rp.draught) * 100)
```

Now let's plot our results.


```python
fig = plt.figure(figsize=(8.3, 6))
grid = fig.add_gridspec(3, 1, height_ratios=[1, 0.3, 0.001])
ax = fig.add_subplot(grid[0])
fig.subplots_adjust(hspace=0, right=0.75)

twin1 = ax.twinx()
twin2 = ax.twinx()
twin3 = ax.twinx()
twin1.spines.right.set_position(("axes", 1.2))
twin3.spines.right.set_position(("axes", 1.4))

ax.set_title(r"Evolution of characteristic forming values along the rolling train")
ax.set_xlabel(r"Stand number", fontsize=14)
ax.set_ylabel(r"$\dot{\varphi}$ in $\mathrm{\frac{1}{s}}$", fontsize=14)
ax.grid(True)

p1, = ax.plot(stand_numbers, temperatures, color='C0', label="Temperature")
p2, = twin1.plot(stand_numbers, strain_rates, color='C1', label="Strain-rate")
p3, = twin2.plot(stand_numbers, strains, color='C2', label="Strain")
p4, = twin3.plot(stand_numbers, reductions, color='C3', label="Reductions")

ax.yaxis.label.set_color(p1.get_color())
twin1.yaxis.label.set_color(p2.get_color())
twin2.yaxis.label.set_color(p3.get_color())
twin3.yaxis.label.set_color(p4.get_color())

ax.set_ylabel(r"$\vartheta$ in $\mathrm{°C}$", fontsize=14, color='C0')
twin1.set_ylabel(r"$\dot{\varphi}$ in $\mathrm{\frac{1}{s}}$", fontsize=14, color='C1')
twin2.set_ylabel(r"$\varphi$ in $\mathrm{-}$", fontsize=14, color='C2')
twin3.set_ylabel(r"$\epsilon$ in $\mathrm{\%}$", fontsize=14, color='C3')
ax.set_xticks(stand_numbers)

_handles = [
    plt.Line2D([], [], color='C0', label='Temperature'),
    plt.Line2D([], [], color='C1', label='Strain-rate'),
    plt.Line2D([], [], color='C2', label='Strain'),
    plt.Line2D([], [], color='C3', label='Reductions')
]

fig.legend(handles=_handles, loc="lower center", bbox_to_anchor=(0.45, 0.125), ncol=4, frameon=True)

plt.show()
```

When you use the basic example which resembles the semi-continuous rolling train of the Institute of Metal Forming your plot should look something like this:







