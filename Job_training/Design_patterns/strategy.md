# Strategy

- Defines a family of algorithms, encapsulates them and makes them interchangeable.

## When to use

- To choose algorithms at runtime
- To choose large conditional statements 

## Examples

### Python

```python
class Strategy:
    def execute(self, a, b): pass

class Add(Strategy):
    def execute(self, a, b): return a + b

class Multiply(Strategy):
    def execute(self, a, b): return a * b

class Context:
    def __init__(self, strategy): self.strategy = strategy
    def execute(self, a, b): return self.strategy.execute(a, b)

print(Context(Add()).execute(3, 4))
print(Context(Multiply()).execute(3, 4))
```

### Cpp

```Cpp
#include <iostream>
using namespace std;

class Strategy {
public: virtual int execute(int a, int b) = 0; };

class Add : public Strategy {
public: int execute(int a, int b) override { return a + b; } };

class Multiply : public Strategy {
public: int execute(int a, int b) override { return a * b; } };

class Context {
    Strategy* strategy;
public:
    Context(Strategy* s) : strategy(s) {}
    int execute(int a, int b) { return strategy->execute(a, b); }
};

int main() {
    Add add; Multiply mult;
    Context c1(&add), c2(&mult);
    cout << c1.execute(3,4) << endl;
    cout << c2.execute(3,4) << endl;
}
```
