# Virtual Functions 

A virtual function is a member function declared with *virtual* in a base class that allows derived classes 
to override it, with the class resolved dynamically when accessed through a base pointer / reference 

A virtual function allows a derived class to override a base-class function and enables runtime polymorphism 
when the object is accessed through a base-class pointer or reference.

```c 
class Sensor {
public:
    virtual int read() {
        return 0;
    }
};

class TemperatureSensor : public Sensor {
public:
    int read() override {
        return 25;
    }
};


int main ()
{
    Sensor* sensor = new TemperatureSensor();
    sensor->read();
}
```

## Pure Virtual Functions 

A pure virtual function is declared using = 0 and requires derived classes to provide an override if they are to be concrete.

```c 
virtual int read() = 0;
```

## Abstract 

A class is abstract if it has at least one pure virtual function that has not been overridden.

## Vptr and Vtable

Virtual pointers are associated with the object and it points the objects Virtual tables that holds the addresses 
of all the virtual functions.

## Virtual Destructors

A polymorphic base class should generally have a virtual destructor so that deleting a derived object through a base-class 
pointer correctly invokes the derived destructor.

## Runtime polymorphism

Runtime polymorphism means the implementation of a virtual function is selected at runtime based on the actual derived object.

## Virtual Functions bad for embedded

- Compiler cannot make it inline
- Object memory increases due to Vtable and Vptr
- Run Time slow as Virtual dispatches an indirect call
- Less predictable run time behaviour

- In embedded if Virtual used in ISR if read from function is dyanmic dispatch which is bad for unpredicatble hehaviour or data 

