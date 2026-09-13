# Safety Critical questions asked in interviews

## What makes a thread based system firm software or safe software

The ability to handle missed events in an even driven system to mitigate losses
or faults

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

## Interview Answer: Software quality and reliability in safety-critical applications

Start with requirements and traceability. In safety-critical software, quality
comes from being able to show that each requirement has been designed,
implemented, reviewed, tested, and controlled through release.

Good answer:

- Define clear and testable requirements.
- Link software requirements to hazards and risk controls.
- Use simple modular design so each part can be reviewed and tested.
- Follow coding standards such as MISRA C/C++ where appropriate.
- Avoid undefined behaviour, uncontrolled dynamic memory, recursion, and
unbounded execution in critical paths.
- Use code reviews, static analysis, and automated tests.
- Test at unit, integration, system, regression, and hardware-in-the-loop
levels.
- Include fault handling such as range checks, watchdogs, timeouts,
diagnostics, redundancy, and safe states.
- Keep version control, change control, and release evidence.

Key phrase:

Safety-critical quality is not just "does the code work"; it is whether the
team can prove the software satisfies its requirements and fails safely when
something goes wrong.

## Interview Answer: Debugging firmware issue in a medical device

Treat the issue as a safety and evidence problem first, then as a technical
debugging problem.

Steps:

1. Understand the symptom and whether there is any patient-safety impact.
2. Put the system into a safe state or isolate the issue if needed.
3. Gather evidence: logs, fault codes, firmware version, hardware revision,
test setup, input conditions, and reproduction steps.
4. Check recent changes using version control.
5. Narrow down the subsystem: sensor input, communication, timing, memory,
interrupt, RTOS task, state machine, or hardware interface.
6. Use the right tools: debugger, trace logs, oscilloscope, logic analyser,
unit tests, or hardware-in-the-loop tests.
7. Find root cause rather than only masking the symptom.
8. Add a regression test and document the fix, risk impact, and verification.

Medical-device angle:

The fix needs to go through change control, review, traceability, and
verification because the process evidence is part of the product quality.

## IEC 62304 and medical-device software lifecycle

IEC 62304 is the medical device software lifecycle standard. It defines a
structured process for developing and maintaining medical device software.

Main lifecycle areas:

- Software development planning.
- Software requirements analysis.
- Software architecture and detailed design.
- Implementation.
- Unit verification.
- Integration and integration testing.
- System testing.
- Software release.
- Software maintenance.
- Risk management links.
- Configuration management.
- Problem resolution.

Important concepts:

- Traceability from requirement to design, code, tests, and risk controls.
- Software safety classification, commonly Class A, B, and C, based on the
possible harm if the software fails.
- Higher-risk software needs stronger process evidence and verification.
- Works alongside risk management standards such as ISO 14971.

Interview answer:

My understanding is that IEC 62304 makes software development controlled and
auditable. You should be able to show what was required, how it was designed,
how it was implemented, how it was tested, what risks it controls, and exactly
which version was released. I have not worked directly under IEC 62304 before,
but my embedded experience has built the same habits: requirements,
documentation, modular design, testing, review, and controlled changes.

## Version control and configuration management

Version control is about making source changes traceable. Configuration
management is broader: it controls the exact software, tools, build settings,
hardware revision, dependencies, and release artifacts used to create a tested
system.

Good answer:

- Use Git or similar source control.
- Keep commits focused and commit messages clear.
- Use branches for features, fixes, and releases.
- Use code review before merging.
- Tag released firmware versions.
- Track compiler, linker, SDK, RTOS, library, and hardware versions.
- Store build configuration alongside the source when possible.
- Link changes to tickets, requirements, test evidence, or risk controls.
- Use CI to build and run repeatable tests.

Medical-device angle:

For a regulated device, it must be possible to recreate or identify exactly
what was released and prove what verification was performed on that version.

## Automated testing frameworks in embedded software

Automated tests should be used at different levels:

- Unit tests: pure logic, calculations, state machines, boundary checks, and
fault handling.
- Integration tests: drivers, communication stacks, and module interactions.
- Hardware-in-the-loop tests: tests that need real hardware behaviour.
- Regression tests: protect against old bugs returning.
- Static analysis: catch unsafe patterns and coding-standard violations.

Common tools:

- C: Unity, Ceedling, CMock.
- C++: GoogleTest, Catch2, CppUTest.
- Python tooling: pytest.
- Static analysis: compiler warnings, clang-tidy, cppcheck, MISRA tools.

Interview answer:

For embedded software I would test as much logic as possible away from the
hardware, then use integration and hardware-in-the-loop testing for the parts
that depend on real timing, peripherals, or electrical behaviour. In a medical
device, I would also make sure test results are linked to requirements and
recorded against the exact software and hardware version.

## Technical debt vs new features

Prioritise technical debt based on risk and impact.

- Fix immediately if it affects safety, reliability, data integrity, or
verification.
- Prioritise debt that repeatedly slows the team or causes defects.
- Address small refactors during feature work if they reduce risk and keep the
change focused.
- Avoid large refactors close to release unless they are necessary.
- Use evidence such as defect history, test gaps, or maintenance cost to
justify the work.

Interview answer:

I would not treat technical debt as automatically less important than features.
In safety-critical software, debt in requirements, tests, fault handling,
traceability, or configuration management can become a product risk. I would
prioritise it when it reduces safety risk, improves verification confidence, or
removes a repeated blocker for the team.
