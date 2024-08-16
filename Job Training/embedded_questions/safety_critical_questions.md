# Safety Critical questions asked in interviews

## What makes a thread based system firm software or safe software

The ability to handle missed events in an even driven system to mitigate losses or faults

## Where was the ClassB safety standard derived from

IET LEC 61508

##  Safety critical Development Process

- Define clear, unambiguous, testable requirements
- Use formal methods. model-based design and safety analysis techniques to
develop a robust architecture
- Write code according to strict coding standards (MISRA C) focusing on
simplicity, clarity, maintainability
- Implement multiple level of testing, such as unit testing, integration
testing, system testing, an acceptance testing, using both static and dynamic
analysis tools
- Demonstrate through rigorous evidence and analysis that software meets all
safety requirements and obtaining certification
- Carefully manage updates and changes, ongoing compliance with safety
standards

##  Example of a temperature sensor/ADC

```c
// temperature_monitor.c
#include "temperature_monitor.h"

static bool alarm_triggered = false;

void TemperatureMonitor_Init(void) {
    // Initialize the alarm status
    alarm_triggered = false;
}

void TemperatureMonitor_Update(float temperature) {
    // Check if the temperature exceeds the threshold
    if (temperature > TEMPERATURE_THRESHOLD) {
        alarm_triggered = true; // Set the alarm flag
        // Here, you might also log an error or perform additional actions
    } else {
        alarm_triggered = false;
    }
}

bool TemperatureMonitor_IsAlarmTriggered(void) {
    return alarm_triggered;
}

```

- Error is handled by the software by setting an alarm when the temperature
exceeds a threshold. In a real system you might need more sophisticated error
handling and recovery mechanisms, e.g. logging, redundancy checks, timeouts and
failsafe states (like sensor disconnect)
- Comprehensive testing should be conducted, include boundary conditions and
invalid inputs, test results should be documented
- Detailed documentation should be maintained, including design specs, code
comments, and test plans to demonstrate compliance
- Safety analysis (FMEA) should be performed to understand and document
potential failure modes and their impacts

## Examples of MISRA Concepts

- Safe types: Using fixed-width integer types, like uint16_t ensures size and
range of variables are defined, avoiding issues with portability and overflow
- Avoid recursion/deep nesting that can complicate code logic and increase risk
of bugs
- Error handling via logging for sensor read errors so it doesn't silently fail
- Modularity by dividing code into small, testable functions (detectCollision,
deployAirbag), each performing a specific task, simplifies verification and
validation against requirements
- Initialization to initialize system state, ensuring predictable starting
point for system
- No dynamic memory allocation
- No implicit type conversions
- Limit pointers

## Memory Safety

- Ensure program does not access invalid memory regions, leading to undefined
behaviour, system crashes, or vulnerabilities exploitable by attackers
- Bounds checking: ensure all array accesses are within valid range to prevent
buffer overflow

```c
#define MAX_SENSORS 10
uint16_t sensor_values[MAX_SENSORS];

void ReadSensorValues(void) {
    for (uint8_t i = 0; i < MAX_SENSORS; i++) {
        if (i < MAX_SENSORS) {  // Explicit bounds check
            sensor_values[i] = ReadSensor(i);
        }
    }
}
```

- Safe data types: uint8_t, uint16_t, etc
- Initialization and deallocation: properly initialize all variables and clear
or deallocate memorry when it is no longer needed to avoid memory leak issues

```c
void InitBuffer(uint8_t* buffer, size_t size) {
    memset(buffer, 0, size);  // Clear buffer to prevent use of uninitialized memory
}

```

- Pointer Validity Checks: always check pointers before dereferencing them to
prevent null pointer dereferences or accesses to freed memory

```c
void ProcessData(uint8_t* data) {
    if (data != NULL) {
        // Safe to use data
    } else {
        // Handle null pointer error
    }
}
```

## Thread Safety

- Threading introduces concurrency, which can complicate control flow and
introduce new safety issues
- Race conditions: multiple threads access and modify shared data concurrently,
leading to inconsistent or incorrect behaviour
  - Fix using mutexes or semaphores to ensure only one thread can access
  critical section of code at a time
