## The Coding Concept of PyRolL

Since PyRolL is coded in python, PyRolL is also coded using object-oriented and abstract concepts.
As a technologist who is not keen on learning python but rather wants to use the software to simulate the process, this sentence can be both frightening and deterrent at the same time.
So we wanted to explain what two key concepts one should keep in mined when working with PyRolL.
In the world of software development, these two essential concepts are **Abstraction** and **Object Orientation**. 
While you don't need to become a coding expert, having a basic grasp of these ideas can help you better understand how software works and make more informed decisions when using it.

### Abstraction: Simplifying the Complex

In simple terms, abstraction is a way of simplifying complex things. 
Imagine your process, for example, rolling in grooves. 
As a technologist, you pretty much know the basics of rolling, but you don't know every theoretical and scientific explanation for every subprocess happening.
A bit like driving a car.
When you drive a car, you don't need to know every little detail about how the engine works. 
You just use the steering wheel, pedals, and gear shift to control the car. 
This simplification of the car's inner workings is like abstraction in coding.
In coding, abstraction means hiding the complicated parts of a program and exposing only what's necessary for someone to use it. 
It's like interacting with the user-friendly interface of a smartphone app without needing to know all the coding magic happening behind the scenes.
Abstraction makes software more user-friendly and manageable.

### Object Orientation: Treating Everything as an Object

Object orientation is a way of organizing code to make it more structured and easier to work with. 
In the real world, you encounter objects all the time, like cars, phones, and books. 
Object-oriented programming takes this idea and applies it to code.
In coding, an object is like a self-contained unit that has both data and functions that can work on that data (Also that can be explained and refactored into more detail). 
It's similar to how a car has attributes like color and speed, and it can perform actions like accelerating and braking. 
Object orientation helps break down complex problems into smaller, manageable pieces, making it easier to understand and modify software.

So, when you hear about "object orientation" in the context of software, think of it as a way to make code organized, like arranging tools in a toolbox or organizing items on a shelf for easy access.

**In Summary**

- Abstraction simplifies complex things in coding, making software easier to use.
- Object orientation organizes code into objects, making it more structured and manageable.

These concepts help developers create software that is user-friendly and maintainable, so you can enjoy using it without needing to dive into the technical details.

### How does that help you?

Well, that's a bit more complex since people don't tend to think a like. 
Maybe an easy example will help.
Imagine you stand next to your rolling train, what is repeating?
Right rolling mills as well as transport sections. 
That's the reason why we have the classes `RollPass` as well as `Transport`.
Thinking that concept further, one could then assign different attributes to these objects.
For example, the roll object derived from the `Roll` class holds the attributes `roll_torque` as well as `elastic_modulus` and many more. 
The reason for that is that a roll has an elastic modulus and when used for groove rolling has to provide some torque to roll the material. 