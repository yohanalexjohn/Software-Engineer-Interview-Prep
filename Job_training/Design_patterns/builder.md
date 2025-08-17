# Builder

- Separates construction of a complex object from its representation 
- lets you build step by step with flexible configurations

## When to use 

- When object creation is complex with many optional parts 
- To avoid long telescoping constructors 

## Examples 

### Python

```Python
class Burger:
    def __init__(self):
        self.parts = []
    def add(self, part):
        self.parts.append(part)
    def show(self):
        print("Burger with:", ", ".join(self.parts))

class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()
    def add_patty(self): self.burger.add("patty"); return self
    def add_cheese(self): self.burger.add("cheese"); return self
    def add_lettuce(self): self.burger.add("lettuce"); return self
    def build(self): return self.burger

burger = BurgerBuilder().add_patty().add_cheese().build()
burger.show()
```

### Cpp

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Burger {
    vector<string> parts;
public:
    void add(string p) { parts.push_back(p); }
    void show() {
        cout << "Burger with: ";
        for (auto &p : parts) cout << p << " ";
        cout << endl;
    }
};

class BurgerBuilder {
    Burger burger;
public:
    BurgerBuilder& addPatty() { burger.add("patty"); return *this; }
    BurgerBuilder& addCheese() { burger.add("cheese"); return *this; }
    Burger build() { return burger; }
};

int main() {
    Burger b = BurgerBuilder().addPatty().addCheese().build();
    b.show();
}
```
