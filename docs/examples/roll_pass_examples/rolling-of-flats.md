# Rolling of Flat Profiles — The IMF Semi-Continuous Rolling Train

Despite PyRolL being originally developed to model groove roll pass, it can also be used to model the rolling of flats in continuous or reversing mills.
As for the simulation of flat profiles using fast methods, the common method is to use the differential equation of von Karmen (Beitrag zur Theorie des Walzvorganges, Zeitschrift für angwandte Mathematik und Mechanik, 1925).

## Theory

Von Karman first published the so-called strip or slab method, derived from the elementary theory of plasticity. 
There are special solutions and extensions of this theory for e.g. rolling of foils, rolling of thick slabs, cold rolling, roll casting or cladding. 
If you need more information on that please contact us by creating an issue.
All of these methods nevertheless are derived from this basic method. 
As of right now, the PyRolL framework provides only the most basic implementation in the plugin `pyroll-karman-force-torque`.
The basic theory is also described in the respective documentation of the plugin.
Here a more in depth view and explanation should be done. 

### Slab Method

The roll gap is divided into slab of infinitely small width along the rolling direction. 
In the remaining dimensions, the extension of the strip remains finite. 
The finite extensions of the strip are assumed to be known. 
The shape change of the strip is assumed to be parallelepipedal. 
External forces and shear forces are applied to these strip elements, as shown in Figure 1.

:::{figure-md} fig:homogeneous-strip-element
:align: center

![Forces and Dimensions of the Slab Element](/docs/img/strip-hom.svg)

Forces and Dimensions of the Slab Element
:::

### Plastic Material Behaviour
Comparative stress according to Mises' deformation hypothesis, the comparative stress in a triaxial principal stress state is given by:

$$
\sigma_V = \sqrt{\frac{1}{2}\left[(\sigma_x - \sigma_y)^2 + (\sigma_y - \sigma_z)^2 + (\sigma_z - \sigma_x)^2\right]}
$$

### Conditions of Material Flow
The material starts to flow plastically, when the comparative stress reaches the flow stress $k_f$

$$
(\sigma_x - \sigma_y)^2 + (\sigma_y - \sigma_z)^2 + (\sigma_z - \sigma_x)^2 \leq 2k_f^2
$$

### Yield Criterion
Using the  Mises-Yield-Criterion the the criterion and the velocity are connected by using the  $\dot{\varepsilon}_{ij}$ and the stress deviator $S_{ij}$.

$$
\dot{\varepsilon}_{ij} = \dot{\lambda}S_{ij} \quad \text{mit} \quad \dot{\lambda} = \frac{3\dot{\varphi}_V}{2k_f}
$$


### Comparative deformation speed
An equivalence analysis of the forming capacity using the Mises yield criterion yields the comparative forming speed according to 
$$
\dot{\varphi}_V = \sqrt{\frac{2}{3}\dot{\varepsilon}_{ij}\dot{\varepsilon}_{ij}}
$$

Keeping these relations in mind, it is possible to solve the differential equation. 


## Usage Example

The rolling train was built as a semi-continuous rolling train which means that it consists of a reversing mill
representing the roughing train of a street and four finishing stands which represent the finishing train.
A speciality of this mill, is that it can be operated in two different configurations. 
One configuration is used to roll long products. 
The other configuration is used to roll flat products. 
As an example, the rolling of a 

