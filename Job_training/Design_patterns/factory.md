# Factory

Provides an interface for creating objects without exposing creation logic 

Decides which object to initiate

## When to use

- To delegate object creation to subclasses 
- When exact type may vary at runtime

## Examples

### Python

```python
class Shape: pass

class Circle(Shape): 
    def draw(self): print("Circle")
class Square(Shape): 
    def draw(self): print("Square")

class ShapeFactory:
    def get_shape(self, shape_type):
        if shape_type == "circle": return Circle()
        if shape_type == "square": return Square()

shape = ShapeFactory().get_shape("circle")
shape.draw()
```

### Cpp

```Cpp
#include <iostream>
using namespace std;

class Shape { public: virtual void draw() = 0; };

class Circle : public Shape {
public: void draw() override { cout << "Circle\n"; } };

class Square : public Shape {
public: void draw() override { cout << "Square\n"; } };

class ShapeFactory {
public:
    Shape* getShape(string type) {
        if (type == "circle") return new Circle();
        if (type == "square") return new Square();
        return nullptr;
    }
};

int main() {
    ShapeFactory factory;
    Shape* s = factory.getShape("circle");
    s->draw();
    delete s;
}
```
