# Classes and Objects

## What is a Class in Python?

* A class is a blueprint for creating custom data types and structures .
* Attributes are the data your class holds while methodds are the functions your class can perform.
* An object is an instantiation of a class. Its the actual item once defined and created.
* Objects have a state which is their data and can interact with each other and othe parts of the code base with their methods.

* Self is a poiner to the instance of the object thats passed in as an argument to most methods.
* It lets methods access or modify the data inside the object.
* The `__init__` method is Python’s constructor—called automatically when you create an object.
* It sets up the object’s initial state and always takes self as an argument.
* This is where you define what data every object starts with.

* Instance attributes are unique to each object.
* Class attributes are shared across all instances. They are useful when you want to maintain shared state, such as tracking how many objects have been created.
* Instance methods operate on instances data and take self as the first argument, like the constructors and properties.
* Class methods operate on the class and take cls as the first argument, work well with alternative constructors, class data like count and inheritance. @classmethod.
* Static methods neither take self or cls. These are normal functions usually for organizational purposes. Mostly utility and helper functions.
* Encapsulation is hiding the state and logic of the class and only allowing access through methods.

* In Python, this is a convention (not enforced). Prefixing with `_` indicates that something is "internal" or "private".
* Also in python we have @properties with getters and setters as subtitutes for get and set. Deleters are optional and used for deleting class attributes.
* For example, if a radius must always be non-negative, you can create a protected variable and enforce rules via a setter.


* Inheritence 
* Inheritance models an is a relationship allowing a class to inherit from another.
* Child classes inherit from parent classes and can override methods or use super() to use parent class methods

* Abstraction
* Where encapsulation deals with access to data and how its modifed abstration deals with access to implementaion details and what an object does.
* Internal details are hidden and shows only the essential features of an object.
* Use abc ABC and abstractmethod in python to define a class that cannot be instantiated and contain abstract methods that must be overriden.
* Use interfaces to define a set of methods that must be implemented in child classes.
* Class inherits ABC and abstract methods carry @abtractmethod tag and just have pass.   

* Polymorphism
* Polymorphism allows different classes to be treated through a common interface, and to respond differently to the same method call.
* Usually such is achieved by varying arguments number and data type or return types.
* In Python simply call a parent method passing in the class it should use.

* Composition
* Composition  models a "has-a" relationship and classes contain one or more objects from other classes.
* Examples such as a Linked List has a Node or a Hashmap has a dynamic array. 
* Preferable over inheritance when a relationship isn't strictly hierarchical.

* Operator overloading
* Defines custom behaviour for built in operators like '+', '=' , '>' etc when used with objects.
* Python has the following dunder special methods for implementing operator overloading.
* Example
    def __init__(self, value):
        self.value = value

     Overload +
    def __add__(self, other):
        return Number(self.value + other.value)

     Overload -
    def __sub__(self, other):
        return Number(self.value - other.value)

     Overload *
    def __mul__(self, other):
        return Number(self.value * other.value)

     Overload /
    def __truediv__(self, other):
        if other.value == 0:
            raise ValueError("Cannot divide by zero!")
        return Number(self.value / other.value)

     Overload ==
    def __eq__(self, other):
        return self.value == other.value

     Overload str() for readable output
    def __str__(self):
        return f"Number({self.value})"

     Overload repr() for debugging output
    def __repr__(self):
        return f"Number(value={self.value})"


## Usage examples
* n1 = Number(10)
* n2 = Number(5)

* print(n1 + n2)    # Number(15)
* print(n1 - n2)    # Number(5)
* print(n1 * n2)    # Number(50)
* print(n1 / n2)    # Number(2.0)
* print(n1 == n2)   # False
* print(n1 == Number(10))  # True

* print(str(n1))    # Number(10)
* print(repr(n1))   # Number(value=10)

* __()__ exists for [ne, lt, gt, ge ,le , mul, mod, pow, len, etc...]

