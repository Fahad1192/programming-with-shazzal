# Class-2
31/06/2021

## Topics Discussed
- Palindrome
- How to learn a new programming language
- Develop mathematical proof of an algorithm

## Assignment-2

## Immutable

Immutable is the when no change is possible over time. In Python, if the value of an object cannot be changed over time, then it is known as immutable. Once created, the value of these objects is permanent.

Objects of built-in type that are immutable are:

* Numbers (Integer, Rational, Float, Decimal, Complex & Booleans)
* Strings
* Tuples
* Frozen Sets
* User-Defined Classes (It purely depends upon the user to define the characteristics)

Example:

Creating a Tuple which contains English name of weekdays

`weekdays = ‘Sunday’, ‘Monday’, ‘Tuesday’, ‘Wednesday’, ‘Thursday’, ‘Friday’, ‘Saturday’`

Printing the elements of tuple weekdays

`print(weekdays)`

`Output [1]:  (‘Sunday’, ‘Monday’, ‘Tuesday’, ‘Wednesday’, ‘Thursday’, ‘Friday’, ‘Saturday’)`


tuples are immutable, so you cannot add new elements, hence, using merge of tuples with the # + operator to add a new imaginary day in the tuple ‘weekdays’

`weekdays  +=  ‘Pythonday’`

Printing the elements of tuple weekdays

`print(weekdays)`

`Output [3]: (‘Sunday’, ‘Monday’, ‘Tuesday’, ‘Wednesday’, ‘Thursday’, ‘Friday’, ‘Saturday’, ‘Pythonday’)`



## Object Oriented Programming

Object-oriented programming combines a group of variables (properties) and functions (methods) into a unit called an "object." These objects are organized into classes where individual objects can be grouped together. OOP can help you consider objects in a program's code and the different actions that could happen in relation to the objects.

### Encapsulation

The different objects inside of each program will try to communicate with each other automatically. If a programmer wants to stop objects from interacting with each other, they need to be encapsulated in individual classes. Through the process of encapsulation, classes cannot change or interact with the specific variables and functions of an object.
Example: Beginning programmers may better understand this concept in relation to how a browser functions. Browsers have local storage objects that allow you to store data locally. These objects have properties, like length, which turns the number of objects into storage, along with methods like (remove item) and (set item).

### Abstraction

Abstraction is like an extension of encapsulation because it hides certain properties and methods from the outside code to make the interface of the objects simpler. Programmers use abstraction for several beneficial reasons. Overall, abstraction helps isolate the impact of changes made to the code so that if something goes wrong, the change will only affect the variables shown and not the outside code.

Example: A way to understand this is to consider the human body. The skin acts as an abstraction to hide the internal body parts responsible for bodily functions like digesting and walking.

### Inheritance

The main object is the superclass and all objects that follow it are subclasses. Subclasses can have separate elements while adding what they need from the superclass.

Example: Consider two classes. One is the superclass (parent) while the subclass (child) will inherit the properties of the parent class and modify its behavior. Programmers applying the technique of inheritance arrange these classes into a hierarchy of "is-a-type-of" relationships.

### Polymorphism

This technique meaning "many forms or shapes" allows programmers to render multiple HTML elements depending on the type of object. This concept allows programmers to redefine the way something works by changing how it is done or by changing the parts in which it is done. Terms of polymorphism are called overriding and overloading.
Example: To better understand the two terms of polymorphism called overloading and overriding, it helps to visualize the process of walking. Babies learn to crawl first by using their arms and legs. Once they learn to stand and walk, they are ultimately changing the body part used to accomplish the act of walking. This term of polymorphism is called overloading.

To understand the next term of overriding, think of how you naturally walk in the direction you are facing. When you stop and walk backward, this changes the direction of your path and also the mechanism of function. You are overriding the natural action that you usually complete.



Reference
- https://www.indeed.com/career-advice/career-development/what-is-object-oriented-programming
- https://www.analyticsvidhya.com/blog/2020/09/object-oriented-programming/#:~:text=Now%2C%20there%20are%20four%20fundamental,in%20order%20to%20understand%20OOPs.
- https://intellipaat.com/community/49903/what-are-immutable-data-types-in-python
