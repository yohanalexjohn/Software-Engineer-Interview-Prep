# Singleton

Ensures only one instance of a class exists with global access

Potential thread safety issues in multithreaded environment

## When to use

Shared resources (logging, config, DB connections)

## Examples

### Python

```python
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()
print(a is b)  # True
```

### Cpp

```cpp
#include <iostream>
using namespace std;

class Singleton {
    static Singleton* instance;
    Singleton() {}
public:
    static Singleton* getInstance() {
        if (!instance) instance = new Singleton();
        return instance;
    }
};

Singleton* Singleton::instance = nullptr;

int main() {
    Singleton* s1 = Singleton::getInstance();
    Singleton* s2 = Singleton::getInstance();
    cout << (s1 == s2) << endl; // 1 (true)
}
```
