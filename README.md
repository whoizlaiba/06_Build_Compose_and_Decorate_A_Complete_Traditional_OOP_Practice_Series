# 🐍 Python OOP Assignments – Complete Guide with Examples

This repository contains 21 Python assignments demonstrating key concepts in Object-Oriented Programming (OOP). Each example is implemented with clarity to help beginners and intermediate developers grasp foundational and advanced OOP features in Python.

---

## 📋 Table of Contents

1. [Using `self`](#1-using-self)
2. [Using `cls`](#2-using-cls)
3. [Public Variables and Methods](#3-public-variables-and-methods)
4. [Class Variables and Class Methods](#4-class-variables-and-class-methods)
5. [Static Variables and Static Methods](#5-static-variables-and-static-methods)
6. [Constructors and Destructors](#6-constructors-and-destructors)
7. [Access Modifiers: Public, Private, and Protected](#7-access-modifiers-public-private-and-protected)
8. [The `super()` Function](#8-the-super-function)
9. [Abstract Classes and Methods](#9-abstract-classes-and-methods)
10. [Instance Methods](#10-instance-methods)
11. [Class Methods](#11-class-methods)
12. [Static Methods](#12-static-methods)
13. [Composition](#13-composition)
14. [Aggregation](#14-aggregation)
15. [Method Resolution Order (MRO)](#15-method-resolution-order-mro-and-diamond-inheritance)
16. [Function Decorators](#16-function-decorators)
17. [Class Decorators](#17-class-decorators)
18. [Property Decorators](#18-property-decorators-property-setter-and-deleter)
19. [`callable()` and `__call__()`](#19-callable-and-__call__)
20. [Creating a Custom Exception](#20-creating-a-custom-exception)
21. [Make a Custom Class Iterable](#21-make-a-custom-class-iterable)

---

## 🔍 Overview

This project is designed to reinforce key OOP concepts in Python through practical exercises. Each assignment focuses on one specific concept, ensuring clarity and depth of understanding.

---

### 1. **Using `self`**
Defines a `Student` class with a constructor and method using `self` to handle instance attributes.

### 2. **Using `cls`**
A `Counter` class uses a class variable and a class method to track object instantiations.

### 3. **Public Variables and Methods**
Demonstrates how to define and access public variables and methods in a `Car` class.

### 4. **Class Variables and Class Methods**
A `Bank` class with a shared `bank_name` variable and a method to modify it across instances.

### 5. **Static Variables and Static Methods**
Implements a `MathUtils` class with a utility method `add()` that doesn't rely on instance or class data.

### 6. **Constructors and Destructors**
The `Logger` class prints messages during object creation and destruction using `__init__()` and `__del__()`.

### 7. **Access Modifiers**
Illustrates public, protected, and private variable access using an `Employee` class.

### 8. **The `super()` Function**
Shows inheritance with `Person` and `Teacher` classes and demonstrates constructor chaining using `super()`.

### 9. **Abstract Classes and Methods**
Implements the `Shape` abstract base class and a concrete `Rectangle` class overriding `area()`.

### 10. **Instance Methods**
Defines a `Dog` class where each object can use `bark()` to identify itself.

### 11. **Class Methods**
A `Book` class uses a class method to update and access a class-level book counter.

### 12. **Static Methods**
The `TemperatureConverter` class includes a `celsius_to_fahrenheit()` method that does not depend on any object or class state.

### 13. **Composition**
Demonstrates object composition by including an `Engine` object within a `Car`.

### 14. **Aggregation**
Illustrates aggregation by having a `Department` refer to an external `Employee` instance.

### 15. **Method Resolution Order (MRO) and Diamond Inheritance**
Explores multiple inheritance and method resolution using classes `A`, `B`, `C`, and `D`.

### 16. **Function Decorators**
Defines a decorator `log_function_call` and applies it to a function `say_hello()`.

### 17. **Class Decorators**
A `Person` class is modified using a class decorator `add_greeting` that injects a `greet()` method.

### 18. **Property Decorators**
Encapsulates the `_price` attribute of a `Product` class using `@property`, `@setter`, and `@deleter`.

### 19. **`callable()` and `__call__()`**
A `Multiplier` class instance is made callable like a function using the `__call__()` method.

### 20. **Creating a Custom Exception**
Defines a custom exception `InvalidAgeError` and demonstrates its use in an age check function.

### 21. **Make a Custom Class Iterable**
Creates a `Countdown` class that can be iterated over, counting down from a given number to zero.

---

## 🚀 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/whoizlaiba/06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series.git
   cd python-oop-assignments

