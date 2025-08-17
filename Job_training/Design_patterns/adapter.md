# Adapter

- Allows incompatible interfaces to work together
- Wraps an existing class with a new interface

## When to use

- When we need to use an existing class but its interface does not match with what is needed
- Reuse legacy code with new systems

## Examples

### Python
```Python
# Existing class (incompatible interface)
class EuropeanPlug:
    def supply_eu_power(self):
        return "220V"

# Target interface
class USPlug:
    def supply_us_power(self):
        pass

# Adapter
class PlugAdapter(USPlug):
    def __init__(self, euro_plug):
        self.euro_plug = euro_plug
    
    def supply_us_power(self):
        return f"Converted {self.euro_plug.supply_eu_power()} to 110V"

# Client
euro_plug = EuropeanPlug()
adapter = PlugAdapter(euro_plug)
print(adapter.supply_us_power())
```

### Cpp

```c++
#include <iostream>
using namespace std;

// Existing class
class EuropeanPlug {
public:
    string supplyEUPower() { return "220V"; }
};

// Target interface
class USPlug {
public:
    virtual string supplyUSPower() = 0;
};

// Adapter
class PlugAdapter : public USPlug {
    EuropeanPlug* euroPlug;
public:
    PlugAdapter(EuropeanPlug* p) : euroPlug(p) {}
    string supplyUSPower() override {
        return "Converted " + euroPlug->supplyEUPower() + " to 110V";
    }
};

// Client
int main() {
    EuropeanPlug euro;
    PlugAdapter adapter(&euro);
    cout << adapter.supplyUSPower() << endl;
}
```
