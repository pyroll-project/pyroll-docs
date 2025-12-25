# Rolling Theory and Basics

PyRolL was built and developed with a clear theoretical concept;
however,
the following section should provide some deeper explanation about basic modeling approaches
which are embedded into the software. 

## Material Flow and Plastomechanical Basics

To describe the material flow, the hot groove rolling process is treated as a mass-preserving forming process, which in reality is only partially fulfilled for hot rolling of steel because of material losses due to oxidation.
Since the mass loss is small in comparison to the total mass of the material, the difference is neglected and the law of mass-preservation is applied.
This yields that the following equations which are used to describe the global system:


```{math}
V_0 &= V_1 \\
A_0 \cdot l_0 &= A_1 \cdot l_1 \\
h_0 \cdot b_0 \cdot l_0 &= h_1 \cdot b_1 \cdot l_1
```


Further, the following conditions have to be fulfilled.
In special cases, the change in width of a profile can be close to zero.

```{math}
h_0 &\gg h_1 \\
b_0 &\leq b_1 \\
 l_0 &\ll l_1
```

To further characterize the forming process, relative and absolute characteristic values are used.
The values used below are the relative draught, spread, and elongation.


```{math}
\varepsilon_h &= \frac{h_0 - h_1}{h_0} \\
\varepsilon_b &= \frac{b_0 - b_1}{b_0}  \\
\varepsilon_l &= \frac{l_0 - l_1}{l_0}
```

Usage of relative values has the disadvantage that they are only suitable for characterization of single-step forming processes.
Since groove rolling is often a multistep forming process, the variables spread ($\beta$), elongation ($\lambda$) and draught ($\gamma$) are used.
These three values are also known as coefficients of draught, spread, and elongation and mark the most important characteristic forming values.

```{math}
\gamma &= \frac{h_1}{h_0} \\
\beta &= \frac{b_1}{b_0}  \\
\lambda &= \frac{l_1}{l_0} = \frac{A_0}{A_1}
```

If the change of shape is related to the current shape, the values yield the so-called natural or logarithmic draught, spread, and elongation.

```{math}
\varphi_h &= \ln(\gamma) \\
\varphi_b &= \ln(\beta)  \\
\varphi_l &= \ln(\lambda)
```

To complete the description of the material flow, it is necessary to also include the equivalent strain $\varphi$ as well as the strain-rate $\dot{\varphi}$ as those two variables are the most significant of all further submodules used.
Lee et al. (1999) presented a study where he compared various methods to calculate the strain of the workpiece during rolling.
Resulting from this study, Lee found that due to the complex three-dimensional forming zone, only two variable methods to calculate the strain yield good results for groove roll passes.
The first one was originally published by von Mises (1928):

$$
\varphi = \sqrt{\frac{2}{3} \cdot \left( \varphi_h^2 + \varphi_l^2 + \varphi_b^2 \right)}
$$

The second was developed by using the condition of mass perseverance (Lee et al., 1999):

$$
\varphi = \sqrt{\frac{2}{3} \cdot \left( \varphi_h^2 + \varphi_b^2 + \varphi_h \cdot \varphi_b \right)}
$$

As for the strain-rate $\dot{\varphi}$, which can generally be equated by the equation below, the situation is also very complex for the case of groove rolling.

$$
\dot{\varphi} = \frac{\partial \varphi}{\partial t}
$$

Solving of this equation, even using numerical methods, is often complex or not possible, as mentioned by Schmidt (1997).
Therefore, commonly the model of Hoff and Dahl (1957) is used:

$$
\dot{\varphi} = \frac{v_{\mathrm{p}}}{l_{\mathrm{c}}} \cdot \varphi
$$

As one can see, the equations above only use global profile and groove values.
Calculation of these values is challenging due to the complex geometry of the groove as explained in the section on representing groove shapes.
To solve this task, suitable mapping and direct calculation methods are used for hot groove rolling processes.

## Mapping and Calculation Methods for Groove Rolling

For hot groove rolling, three major methods were developed to enable calculation of the material flow inside the grooves.
PyRolL offers two methods for this topic. 
First the equivalent rectangle method which is partially implemented in the `pyroll-core` package and also in the `pyroll-lendl-equivalent-method` plugin.
Another method is the so-called pillar model explained in the documentation of the respective `pyroll-pillar-model` plugin.
The most common method used for hot groove rolling is the so-called "equivalent-rectangle" or "equivalent-flat-pass" method.
It was developed by Siebel (1925) and maps the complex groove roll pass to a simpler flat roll pass.

Hereby, both the profile and the used groove are converted into an equivalent flat profile and an equivalent flat pass.
Overall, there are four conversion methods of which three are area preserving.
These three methods are:

- A rectangle with equivalent width as the profile / groove width (maximum width method)
- A rectangle with equivalent height as the profile / groove height (maximum height method)
- A rectangle having the same aspect ratio as the profile / groove (similar aspect method)

The figure below represents the conversion of the groove into the equivalent flat pass.

![Equivalent Rectangle Methods Exemplary Derived for an Oval Groove](/img/equivalent_rectangle.svg)

Additionally, Lendl (1948) developed another method while investigating the spreading behavior of various types of simple irregular groove roll passes.
This method is explained in the documentation of the respective plugin `pyroll-lendl-equivalent-method`.




