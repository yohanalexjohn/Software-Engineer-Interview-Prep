# Observer

- Defines one-to-many dependency: when subject changes, observers get notified

## When to use

- Event Handling systems
- Decoupling between subject and listeners

## Example

### Python

```python
class Subject:
    def __init__(self): self._observers = []
    def attach(self, obs): self._observers.append(obs)
    def notify(self, msg):
        for obs in self._observers: obs.update(msg)

class Observer:
    def update(self, msg): pass

class User(Observer):
    def __init__(self, name): self.name = name
    def update(self, msg): print(f"{self.name} got: {msg}")

subj = Subject()
subj.attach(User("Alice"))
subj.attach(User("Bob"))
subj.notify("New video uploaded!")
```

### Cpp

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Observer {
public: virtual void update(string msg) = 0; };

class Subject {
    vector<Observer*> observers;
public:
    void attach(Observer* o) { observers.push_back(o); }
    void notify(string msg) {
        for (auto o : observers) o->update(msg);
    }
};

class User : public Observer {
    string name;
public:
    User(string n) : name(n) {}
    void update(string msg) override { cout << name << " got: " << msg << endl; }
};

int main() {
    Subject subj;
    User a("Alice"), b("Bob");
    subj.attach(&a); subj.attach(&b);
    subj.notify("New video uploaded!");
}
```
