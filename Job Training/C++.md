# Templates

Templates are a powerful feature that allows you to write generic and reusable code. They enable you to create functions and classes that work with any data type, without being limited to a specific type. This is useful for creating data structures and algorithms that can operate on a variety of types while maintaining type safety

### Function Templates
Function templates allow you to create functions that can operate on any data type

```cpp
#include <iostream>
using namespace std;

// Function template
template <typename T>
T max(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    cout << "Max of 10 and 20 is " << max(10, 20) << endl; // Works with int
    cout << "Max of 10.5 and 20.5 is " << max(10.5, 20.5) << endl; // Works with double
    return 0;
}

```

### Class Templates
Class templates allow you to create classes that can operate on any data type

```cpp
#include <iostream>
using namespace std;

// Class template
template <typename T>
class Box {
private:
    T value;

public:
    Box(T val) : value(val) {}

    T getValue() const {
        return value;
    }

    void setValue(T val) {
        value = val;
    }
};

int main() {
    Box<int> intBox(123);
    Box<double> doubleBox(45.67);

    cout << "Int box value: " << intBox.getValue() << endl;
    cout << "Double box value: " << doubleBox.getValue() << endl;

    return 0;
}
```

### Template Specialization
Template specialization allows you to define different implementations of a template for specific data types

```cpp
#include <iostream>
using namespace std;

// Class template for general types
template <typename T>
class Box {
private:
    T value;

public:
    Box(T val) : value(val) {}

    T getValue() const {
        return value;
    }

    void setValue(T val) {
        value = val;
    }
};

// Template specialization for bool
template <>
class Box<bool> {
private:
    bool value;

public:
    Box(bool val) : value(val) {}

    bool getValue() const {
        return value;
    }

    void setValue(bool val) {
        value = val;
    }

    void printValue() const {
        cout << (value ? "True" : "False") << endl;
    }
};

int main() {
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


# OOP

### Classes
A class is a blueprint for creating objects. It defines a data structure by bundling data members and member functions that operate on the data. Classes can also have access specifiers to control the visibility of its members

An object is an instance of a class. When you create an object, you are instantiating a class, allocating memory for it, and initializing it

### Encapsulation
Encapsulation is the bundling of data and methods that operate on the data within a class and restricting access to some of the object's components. This means the internal representation of an object is hidden from the outside, only allowing access through public methods

```cpp
class BankAccount {
private:
    double balance;

public:
    BankAccount(double initialBalance) : balance(initialBalance) {}

    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }

    double getBalance() {
        return balance;
    }
};

```

### Inheritance
Inheritance allows a class (derived class) to inherit attributes and methods from another class (base class). This promotes code reusability and establishes a relationship between classes

```cpp
class Vehicle {
public:
    string brand;

    void honk() {
        cout << "Honk honk!" << endl;
    }
};

class Car : public Vehicle {
public:
    string model;

    void startEngine() {
        cout << "Engine started." << endl;
    }
};
```

### Polymorphism
Polymorphism allows methods to do different things based on the object it is acting upon. In C++, polymorphism is achieved through function overloading, operator overloading, and virtual functions.
- Function overloading: Multiple functions can have the same name with different parameters
- Operator overloading: Allows you to redefine how operators work for user-defined types
- Virtual Functions and Method overriding: Allows derived classes to provide a specific implementation of a method that is already defined in its base class
```cpp
class Shape {
public:
    virtual void draw() {
        cout << "Drawing a shape." << endl;
    }
};

class Circle : public Shape {
public:
    void draw() override {
        cout << "Drawing a circle." << endl;
    }
};

class Rectangle : public Shape {
public:
    void draw() override {
        cout << "Drawing a rectangle." << endl;
    }
};
```

### Abstraction
Abstraction involves representing essential features without including background details or explanations. It focuses on the interface rather than the implementation details. In C++, abstraction is typically achieved using abstract classes and interfaces (pure virtual functions).

```cpp
class Animal {
public:
    virtual void makeSound() = 0; // Pure virtual function
};

class Dog : public Animal {
public:
    void makeSound() override {
        cout << "Woof!" << endl;
    }
};

class Cat : public Animal {
public:
    void makeSound() override {
        cout << "Meow!" << endl;
    }
};
```

