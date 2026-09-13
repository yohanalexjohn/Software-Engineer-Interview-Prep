# C++ Notes

## Templates

Templates are a powerful feature that allows you to write generic and reusable
code. They enable you to create functions and classes that work with any data
type, without being limited to a specific type. This is useful for creating
data structures and algorithms that can operate on a variety of types while
maintaining type safety

### Function Templates

Function templates allow you to create functions that
can operate on any data type

```cpp
#include <iostream>

using namespace std;

// Function template
template <typename T> T max(T a, T b)
{
  return (a > b) ? a : b;
}

int main()
{
  // Works with int
  cout << "Max of 10 and 20 is " << max(10, 20) << endl;

  // Works with double
  cout << "Max of 10.5 and 20.5 is " << max(10.5, 20.5) << endl;
  return 0;
}
```

### Class Templates

Class templates allow you to create classes that can operate on any data type

```cpp
#include <iostream>

using namespace std;

// Class template

template <typename T> class Box
{
private:
  T value;

public:
  Box(T val) : value(val)
  {
  }

  T getValue() const
  {
    return value;
  }

  void setValue(T val)
  {
    value = val;
  }
};

int main()
{
  Box<int> intBox(123);
  Box<double> doubleBox(45.67);

  cout << "Int box value: " << intBox.getValue() << endl;
  cout << "Double box value: " << doubleBox.getValue() << endl;

  return 0;
}
```

### Template Specialization

Template specialization allows you to define different implementations of a
template for specific data types

```cpp
#include <iostream> using namespace std;

// Class template for general types
template <typename T> class Box
{
private:
  T value;

public:
  Box(T val) : value(val)
  {
  }
  T getValue() const
  {
    return value;
  }

  void setValue(T val)
  {
    value = val;
  }
};

// Template specialization for bool

template <> class Box<bool>
{
private:
  bool value;

public:
  Box(bool val) : value(val)
  {
  }

  bool getValue() const
  {
    return value;
  }

  void setValue(bool val)
  {
    value = val;
  }

  void printValue() const
  {
    cout << (value ? "True" : "False") << endl;
  }
};

int main()
{
  Box<int> intBox(123);
  Box<double> doubleBox(45.67);
  Box<bool> boolBox(true);

  cout << "Int box value: " << intBox.getValue() << endl;
  cout << "Double box value: " << doubleBox.getValue() << endl;
  cout << "Bool box value: ";

  boolBox.printValue();

  return 0;
}
```

## OOP

### Classes

A class is a blueprint for creating objects. It defines a data structure by
bundling data members and member functions that operate on the data. Classes
can also have access specifiers to control the visibility of its members

An object is an instance of a class. When you create an object, you are
instantiating a class, allocating memory for it, and initializing it

### Encapsulation

Encapsulation is the bundling of data and methods that operate on the data
within a class and restricting access to some of the object's components. This
means the internal representation of an object is hidden from the outside, only
allowing access through public methods

```cpp

class BankAccount
{
private:
  double balance;

public:
  BankAccount(double initialBalance) : balance(initialBalance)
  {
  }

  void deposit(double amount)
  {
    if (amount > 0)
    {
      balance += amount;
    }
  }

  double getBalance()
  {
    return balance;
  }
};
```

### Inheritance

Inheritance allows a class (derived class) to inherit attributes and methods
from another class (base class). This promotes code reusability and establishes
a relationship between classes

```cpp
class Vehicle

{
public:
  string brand;

  void honk()
  {
    cout << "Honk honk!" << endl;
  }
};

class Car : public Vehicle
{
public:
  string model;

  void startEngine()
  {
    cout << "Engine started." << endl;
  }
};
```

### Polymorphism

Polymorphism allows methods to do different things based on the object it is
acting upon. In C++, polymorphism is achieved through function overloading,
operator overloading, and virtual functions.

- **Function overloading:** Multiple functions can have the same name with
different parameters
- **Operator overloading:** Allows you to redefine how operators work for
user-defined types
- **Virtual Functions and Method overriding:** Allows derived classes to
provide a specific implementation of a method that is already defined in its
base class

```cpp
class Shape
{
public:
  virtual void draw()
  {
    cout << "Drawing a shape." << endl;
  }
};

class Circle : public Shape
{
public:
  void draw() override
  {
    cout << "Drawing a circle." << endl;
  }
};

class Rectangle : public Shape
{
public:
  void draw() override
  {
    cout << "Drawing a rectangle." << endl;
  }
};
```

### Abstraction

Abstraction involves representing essential features without including
background details or explanations. It focuses on the interface rather than the
implementation details. In C++, abstraction is typically achieved using
abstract classes and interfaces (pure virtual functions).

```cpp
class Animal
{
public:
  // Pure virtual function
  virtual void makeSound() = 0;
};

class Dog : public Animal
{
public:
  void makeSound() override
  {
    cout << "Woof!" << endl;
  }
};

class Cat : public Animal
{
public:
  void makeSound() override
  {
    cout << "Meow!" << endl;
  }
};
```

## Interview Answer: C++ and object-oriented design patterns

My C++ experience is strongest around the core language features used to build
maintainable embedded software: classes, encapsulation, inheritance,
polymorphism, templates, RAII, and clear interfaces. In embedded C++, I would
be careful not to add abstraction just for the sake of it, because the code
still needs to be predictable, testable, and efficient.

Good embedded example:

```cpp
class TemperatureSensor
{
public:
  virtual float readCelsius()  = 0;
  virtual ~TemperatureSensor() = default;
};

class AdcTemperatureSensor : public TemperatureSensor
{
public:
  float readCelsius() override
  {
    // Read ADC and convert to temperature.
    return 0.0f;
  }
};
```

This lets the higher-level control logic depend on the `TemperatureSensor`
interface instead of being tightly coupled to one ADC implementation. That
makes the code easier to test and easier to change if the hardware changes.

Design patterns worth mentioning:

- Strategy: switch between control algorithms, filtering methods, or
calibration strategies behind one interface.
- Factory: create the correct driver or object depending on board
configuration.
- Observer/pub-sub: notify other modules when sensor data, alarms, or fault
events occur.
- Facade: provide a simple API over a more complex driver, RTOS, or
communication stack.
- Singleton: can represent a single hardware resource, but use carefully
because it can make testing harder.

Interview answer:

I use object-oriented design when it makes the software easier to reason about,
test, and maintain. For example, I might hide a hardware-specific sensor driver
behind a clean interface so the application logic can be tested separately. I
am familiar with patterns such as Strategy, Factory, Observer, Facade, and
Singleton, but I would only use them where they solve a real problem. In
embedded software, clarity and deterministic behaviour matter more than
showing off abstraction.

## What is RAII 

Resource Acquisition is Initalisation

When destructor is called the resource is automatically released by design

## unique_ptr vs shared_ptr vs weak_ptr

unique_ptr - Follows RAII design, reource moves cannot be reasigned 
shared_ptr - Multiple shared owners. On Desctruction each of the shared reseource is called and destrouyed


