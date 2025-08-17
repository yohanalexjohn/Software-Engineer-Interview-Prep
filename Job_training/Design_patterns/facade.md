# Facade

- Provides a simplified interface to a complex subsystem

## When to use 

- Simplify client code
- Reduce coupling between client and subsystem

## Examples

### Python

```python
class DVDPlayer:
    def on(self): print("DVD Player On")
    def play(self): print("Playing DVD")

class Projector:
    def on(self): print("Projector On")

class HomeTheaterFacade:
    def __init__(self):
        self.dvd = DVDPlayer()
        self.projector = Projector()
    def watch_movie(self):
        self.dvd.on()
        self.projector.on()
        self.dvd.play()

theater = HomeTheaterFacade()
theater.watch_movie()
```

### Cpp

```cpp
#include <iostream>
using namespace std;

class DVDPlayer {
public: void on() { cout << "DVD Player On\n"; }
        void play() { cout << "Playing DVD\n"; } };

class Projector {
public: void on() { cout << "Projector On\n"; } };

class HomeTheaterFacade {
    DVDPlayer dvd; Projector proj;
public:
    void watchMovie() {
        dvd.on(); proj.on(); dvd.play();
    }
};

int main() {
    HomeTheaterFacade theater;
    theater.watchMovie();
}
```
