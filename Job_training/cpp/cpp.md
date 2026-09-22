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

## Active recall: RAII and ownership

RAII means **Resource Acquisition Is Initialization**.

- Constructor acquires the resource.
- Destructor releases the resource.
- Useful for heap memory, file handles, sockets, mutex locks, and hardware handles.
- Main benefit: cleanup is automatic even on early return or exceptions.

Interview answer:

> RAII ties resource ownership to object lifetime. A resource is acquired in the
> constructor and released in the destructor, giving deterministic cleanup and
> helping prevent leaks.

## Active recall: unique_ptr vs shared_ptr vs weak_ptr

- `unique_ptr`: one owner only. Move-only. Use by default for exclusive ownership.
- `shared_ptr`: multiple owners. Reference counted. Resource is destroyed when
  the last `shared_ptr` owner is destroyed.
- `weak_ptr`: non-owning observer of a `shared_ptr`. Use it to break circular
  references, for example parent owns child and child points back to parent.

Common mistake:

- `shared_ptr` cycles leak because the reference count never reaches zero.
- Use `weak_ptr` for the back-reference.

## Active recall: copy vs move

- Copy constructor creates a separate object from an lvalue.
- Move constructor transfers resources from an rvalue.
- For owning raw resources, a compiler-generated copy can shallow-copy the
  pointer and cause double-delete.
- After a move, the source object is still valid but should be treated as empty
  or unspecified.
- `std::move` does not move by itself; it allows move construction or move
  assignment to run.

Vector note:

- Vector copy copies all elements, so it is O(n).
- Vector move usually transfers the internal buffer pointer, size, and capacity,
  so it is usually O(1).
- Mark move constructors/assignments `noexcept` when they cannot throw.
  Containers such as `std::vector` prefer `noexcept` moves during reallocation;
  otherwise they may copy elements to preserve strong exception safety.

Recall prompt:

- Does `std::move(x)` move anything by itself?
- After a move, what must still be true about the source object?
- Why does `vector` care whether a move constructor is `noexcept`?

## Active recall: references, pointers, and const

- `const T&`: no copy, read-only view. Good for large read-only parameters.
- `T value`: local copy for lvalues, can move from rvalues. Good when the
  function needs its own modifiable copy or will store it.
- Lvalue: named object or expression with a stable location, such as `x`.
- Rvalue: temporary or expiring value, such as `42`, `makeBuffer()`, or
  `std::move(x)`.
- `T&`: lvalue reference, binds to lvalues.
- `T&&`: rvalue reference, binds to rvalues and is commonly used for move
  construction/assignment.
- Reference: alias to an existing object, must be initialized, cannot be null,
  cannot be reseated.
- Pointer: stores an address, can be null, can be reseated.

Pointer constness:

- `const int* p`: pointer to const int. Can change `p`, cannot change `*p`.
- `int* const p`: const pointer to int. Cannot change `p`, can change `*p`.
- `const int* const p`: const pointer to const int. Cannot change either.

## Active recall: volatile vs atomic

- `volatile`: value may change outside normal program flow, such as a
  memory-mapped register. It does not make threaded code safe.
- `std::atomic`: thread-safe atomic operations with memory-order guarantees.
  Use for shared data between threads.

Common mistake:

- Do not say `volatile` is a locking or thread-synchronisation tool.

## Active recall: lock_guard vs unique_lock

- `std::lock_guard<std::mutex>`:
  - simplest scoped mutex lock
  - locks on construction
  - unlocks on destruction
  - cannot be manually unlocked/relocked
- `std::unique_lock<std::mutex>`:
  - scoped lock with more control
  - can unlock/relock
  - movable
  - required by `std::condition_variable::wait`

Interview answer:

> Use `lock_guard` for simple scope-based locking. Use `unique_lock` when the
> lock needs to be unlocked/relocked, moved, deferred, or passed to a condition
> variable wait.

## Active recall: condition_variable

Use a condition variable when one thread should sleep until another thread
signals that shared state may have changed.

Pattern:

```cpp
std::mutex mutex;
std::condition_variable cv;
bool ready = false;

// waiting thread
std::unique_lock<std::mutex> lock(mutex);
cv.wait(lock, [&] {
    return ready;
});

// notifying thread
{
    std::lock_guard<std::mutex> lock(mutex);
    ready = true;
}
cv.notify_one();
```

Why the predicate matters:

- Wake-ups can be spurious.
- A notification only means "the condition may have changed."
- The waiting thread must re-check the actual shared condition before
  continuing.

Why `wait()` takes `unique_lock`:

- It unlocks the mutex while the thread sleeps.
- It re-locks the mutex when the thread wakes.
- It checks the predicate while protected by the mutex.

Interview answer:

> `std::condition_variable` lets a thread sleep until another thread signals
> that a shared condition may have changed. It avoids polling. I wait with a
> predicate because wake-ups can be spurious and the thread should only proceed
> when the real condition is true.

## Active recall: unordered_map count vs find

- `map.count(key)`: existence check. For `unordered_map`, returns `0` or `1`.
- `map.find(key)`: returns an iterator. Use when I need the value without doing
  another lookup.
- Avoid `count()` followed by `operator[]` when reading, because `operator[]`
  can insert a default value.
