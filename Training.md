# Combined Interview Training Plan: Medtronic + Cirrus Logic

## Target

Prepare for both:

- Medtronic Senior Software Engineer, Hugo RAS / connected surgical
technologies.
- Cirrus Logic Embedded Software Engineer, DSP/MCU firmware.

Total plan: 5 weeks, 80 hours.

Normal week:

- Monday to Friday: 2 hours per day.
- Saturday: 4 hours.
- Sunday: 2 hours review/mock interview.
- Total: 16 hours per week.

If interviews are sooner, prioritise:

1. Modern C++.
2. Linux and debugging.
3. RTOS/concurrency.
4. Testing with Google Test.
5. Medtronic: gRPC/DDS/Zenoh, cloud connectivity, IEC 62304.
6. Cirrus: DSP, fixed-point arithmetic, DMA, performance, bring-up.

## Role Difference

|Area|Medtronic|Cirrus Logic|
|--|--|--|
|Main identity|Modern C++ application software for connected surgical systems|Low-level embedded firmware for DSP/MCU systems|
|Product context|Hugo RAS, operating room, robotics ecosystem, edge/cloud connectivity|Mixed-signal processing, audio/DSP, consumer electronics|
|Most important language|Modern C++17+|C and C++, with stronger low-level focus|
|Operating environment|Unix/Linux, deployed devices, edge systems|MCUs/DSPs, RTOS, bare metal, Zephyr optional|
|Communication focus|gRPC, DDS, Zenoh, device monitoring, cloud connectivity|SPI, I2C, UART, I2S/TDM, DMA, board-level interfaces|
|Quality focus|Regulatory, secure-by-design, maintainability, test evidence|Performance, determinism, HIL, production diagnostics|
|Biggest prep gap|Distributed systems and medical lifecycle|DSP, fixed-point, performance optimisation|


## Your CV Positioning

Your strongest shared story:

"I am an embedded software engineer with experience close to hardware, mainly
on STM32 and Arm Cortex-M systems. At Cyden I worked on medical IPL firmware,
low-level drivers, board bring-up, diagnostics, and hardware validation. At
Dyson I worked on safety-approved bootloaders, CI/HIL tooling, Python test
automation, and OTA firmware update work. That gives me a good base for both
roles: Medtronic because of the medical, safety, and connected-device angle;
Cirrus because of the low-level firmware, debugging, performance, and
production angle."

Be honest about gaps:

- C++: "I have used C++ and understand OOP, but I am actively strengthening
modern C++17 practices such as RAII, move semantics, and testable interface
design."
- Medtronic: "I have not used IEC 62304 directly, but I understand its
software lifecycle principles and have worked with safety-conscious firmware
practices."
- Cirrus: "I have not worked professionally on DSP pipelines, RISC-V, Zephyr,
or I2S/TDM, but I am revising the fundamentals and can connect them to my
existing embedded/debugging experience."

## Weekly Overview

|Week|Hours|Main Focus|Outcome|
|--|--:|--|--|
|1|16|Modern C++ foundation|Speak confidently on C++17, RAII, OOP, design patterns|
|2|16|Linux, testing, debugging|Cover Medtronic application software and shared quality topics|
|3|16|RTOS, low-level firmware, bring-up|Strengthen shared embedded fundamentals and Cirrus-specific depth|
|4|16|Split track: Medtronic connectivity + Cirrus DSP|Cover each role's specialist gaps|
|5|16|Mock interviews and company polish|Turn notes into fluent answers|


## Week 1: Modern C++ Foundation

Total: 16 hours.

Goal: fix the biggest common weakness. Both roles need C++, and Medtronic
explicitly asks for modern C++17+.

### Day 1: C++ core syntax and object model, 2 hours

- Classes, constructors, destructors.
- Stack vs heap.
- References vs pointers.
- `const`, `static`, namespaces.
- Access control and encapsulation.

Practice answer:

"In embedded C++, I use classes to express ownership and responsibility, but I
avoid hiding hardware behaviour behind unnecessary abstraction."

### Day 2: RAII and ownership, 2 hours

- RAII.
- Rule of 0, Rule of 3, Rule of 5.
- `std::unique_ptr`, `std::shared_ptr`, raw pointers.
- Lifetime bugs and deterministic cleanup.

Medtronic angle:

- RAII for robust maintainable service/application code.

Cirrus angle:

- RAII is useful, but be careful with dynamic allocation in firmware.

### Day 3: Move semantics and performance, 2 hours

- Lvalues and rvalues.
- Move constructor and move assignment.
- Avoiding unnecessary copies.
- Passing by value, reference, and `const&`.

Interview question:

"How would you avoid unnecessary copies in a high-throughput data path?"

### Day 4: Polymorphism and interfaces, 2 hours

- Virtual functions.
- Abstract interfaces.
- Composition vs inheritance.
- Runtime polymorphism vs templates.
- Cost of abstraction in embedded systems.

Practice example:

- Sensor interface.
- Fake sensor for tests.
- Real SPI/ADC implementation.

### Day 5: Design patterns, 2 hours

- Strategy: algorithms/filters.
- Factory: board-specific drivers.
- Observer/pub-sub: telemetry/fault events.
- Facade: simplified driver or communication API.
- Singleton: hardware resource, but testing drawback.

### Saturday: C++ mini-project, 4 hours

Build or revise:

- Circular buffer class.
- Moving-average filter.
- State machine with normal/fault states.
- Interface for a sensor or data source.

### Sunday: Review and speaking practice, 2 hours

Speak these answers out loud:

- Explain RAII.
- Explain move semantics.
- Explain how to design testable embedded C++.
- Explain one C++ design pattern you would actually use.

## Week 2: Linux, Testing, Debugging, and Code Quality

Total: 16 hours.

Goal: cover Medtronic's Unix/Linux + testing requirements while strengthening
shared engineering quality.

### Day 1: Linux fundamentals, 2 hours

- Processes vs threads.
- Signals.
- File descriptors.
- Permissions.
- Environment variables.
- Services/daemons.

Medtronic priority:

- Be comfortable describing software running on deployed Linux/edge devices.

### Day 2: Linux debugging, 2 hours

- Logs.
- Core dumps.
- `gdb`.
- `strace`.
- `top`/`htop`.
- Valgrind.
- AddressSanitizer/ThreadSanitizer.

Practice answer:

"If a deployed device service crashes, I would first identify version,
configuration, logs, reproduction conditions, and whether there is a core dump.
Then I would narrow it by recent change, subsystem, memory, threading, or I/O."

### Day 3: Google Test and TDD, 2 hours

- `TEST`.
- `TEST_F`.
- Fixtures.
- `EXPECT_*` vs `ASSERT_*`.
- Test naming.
- Test independence and repeatability.

Practice:

- Add tests for the Week 1 circular buffer or state machine.

### Day 4: Mocking hardware and integration tests, 2 hours

- Interface-based design.
- Fake hardware interfaces.
- Unit vs integration vs HIL.
- Regression tests.

Medtronic angle:

- Tests linked to requirements and release evidence.

Cirrus angle:

- HIL and production diagnostics for real boards.

### Day 5: Secure and maintainable software, 2 hours

- Input validation.
- Authentication/authorisation basics.
- Encryption in transit.
- Least privilege.
- Logging without leaking sensitive data.
- Code reviews and CI.

Medtronic priority:

- Secure-by-design for connected surgical devices.

### Saturday: Debugging scenarios, 4 hours

Prepare answers for:

- Service crash on Linux.
- Memory leak.
- Race condition.
- Failed hardware communication.
- Intermittent timing issue.

### Sunday: Review and speaking practice, 2 hours

Record or rehearse:

- "How do you ensure software quality?"
- "How do you debug a firmware/software issue?"
- "How do you use automated testing?"

## Week 3: RTOS, Low-Level Firmware, and Hardware Bring-up

Total: 16 hours.

Goal: strengthen the embedded core needed by both roles, with extra benefit
for Cirrus.

### Day 1: Boot and startup, 2 hours

- Reset handler.
- Vector table.
- Stack pointer.
- `.text`, `.data`, `.bss`.
- Startup code.
- What happens before `main()`.

### Day 2: Memory maps, linker scripts, and map files, 2 hours

- Flash/RAM layout.
- Heap and stack.
- Linker symbols.
- Map file use.
- Memory placement and optimisation.

Cirrus priority:

- Be able to discuss memory layout and performance implications.

### Day 3: Interrupts and concurrency, 2 hours

- ISR design.
- Volatile.
- Atomicity.
- Race conditions.
- ISR-to-task handoff.
- Critical sections.

### Day 4: RTOS, 2 hours

- Tasks.
- Priorities.
- Scheduling.
- Semaphores.
- Mutexes.
- Queues.
- Priority inversion.
- Determinism and jitter.

### Day 5: Peripherals and DMA, 2 hours

- SPI, I2C, UART, PWM, GPIO, ADC.
- I2S/TDM basics for audio.
- DMA purpose.
- Double buffering.
- Polling vs interrupt vs DMA.

### Saturday: Bring-up and hardware debugging stories, 4 hours

Prepare 3 detailed stories:

1. Cyden board bring-up or hardware/software interface bug.
2. Cyden factory firmware cycle improvement from 4 minutes to 3 minutes.
3. Dyson bootloader or HIL/CI tooling.

For each:

- Situation.
- Task.
- Action.
- Tools used.
- Root cause.
- Result.

### Sunday: Review and speaking practice, 2 hours

Practise:

- "How do you bring up a new board?"
- "How would you debug SPI/I2C/UART not working?"
- "How do you debug a missed real-time deadline?"

## Week 4: Company-Specific Deepening

Total: 16 hours.

Goal: split time between Medtronic and Cirrus specialist gaps.

## Week 4A: Medtronic Track, 8 hours

### Medtronic Day 1: Hugo RAS product context, 2 hours

Revise:

- Hugo RAS is a robotic-assisted surgery ecosystem.
- Modular arms.
- Open surgeon console.
- Vision/tower system.
- Touch Surgery ecosystem.
- Operating-room collaboration and digital insights.

Practice answer:

"Hugo RAS interests me because it combines robotics, surgical workflows,
embedded/edge systems, connectivity, and medical-grade reliability."

### Medtronic Day 2: IPC and distributed systems, 2 hours

Revise:

- gRPC: request/response service APIs, Protocol Buffers.
- DDS: data-centric pub/sub for real-time distributed systems.
- Zenoh: pub/sub/query across edge, cloud, and constrained devices.

Practice comparison:

- Use gRPC for command/query APIs.
- Use pub/sub for telemetry/events.
- Use DDS/Zenoh-style patterns where low-latency distributed data sharing
matters.

### Medtronic Day 3: Remote monitoring and cloud connectivity, 2 hours

Revise:

- Device telemetry.
- Logs and health metrics.
- Secure upload.
- Offline buffering.
- Retry logic.
- Device identity.
- Version reporting.
- Cloud dashboards.

Practice answer:

"A deployed surgical device should report health, software version, hardware
revision, logs, and selected telemetry securely. If offline, it should buffer
data and clearly distinguish stale data from current status."

### Medtronic Day 4: Medical software lifecycle, 2 hours

Revise:

- IEC 62304.
- ISO 14971 risk management link.
- Requirements traceability.
- Verification evidence.
- Change control.
- Problem resolution.
- Secure-by-design.

Practice answer:

"I have not worked directly under IEC 62304, but I understand the mindset:
controlled software lifecycle, traceability, risk controls, verification
evidence, configuration management, and disciplined maintenance."

## Week 4B: Cirrus Track, 8 hours

### Cirrus Day 1: DSP fundamentals, 2 hours

Revise:

- Sampling rate.
- Nyquist.
- Aliasing.
- Quantisation.
- Time domain vs frequency domain.
- Latency vs throughput.

### Cirrus Day 2: Fixed-point arithmetic, 2 hours

Revise:

- Q15/Q31.
- Scaling.
- Saturation vs wraparound.
- Overflow and underflow.
- Precision trade-offs.

Practice answer:

"Fixed-point is useful when hardware lacks fast floating-point or when
deterministic performance matters. The risk is overflow, scaling errors, and
loss of precision, so I would define ranges carefully and test boundary cases."

### Cirrus Day 3: Filters and FFT basics, 2 hours

Revise:

- FIR vs IIR.
- Moving average.
- Low-pass/high-pass concept.
- FFT purpose.
- Buffering samples.
- Cost per sample.

### Cirrus Day 4: Performance optimisation, 2 hours

Revise:

- Cycle counting.
- Profiling.
- Reducing copies.
- Cache behaviour.
- Memory alignment.
- DMA.
- Lookup tables.
- SIMD/vectorisation concept.

Practice answer:

"I would first measure the hot path rather than guessing. Then I would reduce
copies, check memory access patterns, use DMA for transfers, consider
fixed-point or SIMD where appropriate, and verify latency/jitter against the
timing budget."

## Week 5: Interview Simulation and Final Polish

Total: 16 hours.

Goal: make answers sound natural, not like notes.

### Day 1: CV walkthrough, 2 hours

Prepare one general version:

"I am an embedded software engineer with experience close to hardware, mainly
on STM32 and Arm Cortex-M systems. At Cyden I have worked on medical-device
firmware, low-level drivers, board bring-up, diagnostics, and hardware
validation. At Dyson I worked on safety-approved bootloaders, automated test
tooling, HIL, CI/CD, and OTA firmware update work."

Medtronic ending:

"That background fits Medtronic because the role needs software quality,
connectivity, reliability, and safety-conscious engineering for surgical
technology."

Cirrus ending:

"That background fits Cirrus because the role needs firmware close to
hardware, debugging, production discipline, and performance-aware embedded
development."

### Day 2: Why company, 2 hours

Medtronic:

"I want to work at Medtronic because the mission to alleviate pain, restore
health, and extend life is directly meaningful. Hugo RAS also combines areas I
am excited by: robotics, connected devices, edge software, and medical-grade
reliability."

Cirrus:

"I am interested in Cirrus because the role combines low-level firmware,
hardware interaction, performance constraints, and DSP/audio-related systems.
It is close to the hardware but still technically deep in software, which is
where I want to grow."

### Day 3: Technical mock, 2 hours

Mixed questions:

- Explain RAII.
- What happens before `main()`?
- Interrupt vs polling vs DMA.
- How do you debug a race condition?
- gRPC vs DDS.
- Fixed-point overflow.
- How do you test hardware-dependent code?

### Day 4: System design mock, 2 hours

Medtronic:

- Design remote monitoring for a surgical device.
- Design communication between edge device and cloud.

Cirrus:

- Design a real-time audio/DSP processing pipeline.
- Design firmware for a sensor/codec peripheral using DMA.

### Day 5: Behavioural mock, 2 hours

Prepare:

- Conflict.
- Learning quickly.
- Inadequately prepared.
- Technical debt vs feature work.
- Improved process/product quality.
- Tight deadline.

Use Cyden/Dyson examples, not generic stories.

### Saturday: Full mock interviews, 4 hours

Do:

1. 45-minute Medtronic mock.
2. 45-minute Cirrus mock.
3. Mark weak answers.
4. Rewrite weak answers in notes.

### Sunday: Final review, 2 hours

Review:

- `Behaviour_company_questions/medtronic.md`
- `Behaviour_company_questions/Cirrus_Logic.md`
- `Job_training/cpp.md`
- `Job_training/embedded_questions/rtos.md`
- `Job_training/embedded_questions/safety_critical_questions.md`
- `Job_training/embedded_questions/microcontroller_basics.md`
- `Job_training/embedded_questions/toolchain_stuff.md`

## Daily Minimum Plan

If you are busy, do this instead:

- 45 minutes modern C++.
- 30 minutes embedded systems.
- 20 minutes company-specific topic.
- 15 minutes spoken interview practice.

Minimum useful daily total: 1 hour 50 minutes.

## One-Week Crash Plan

Use this if an interview lands suddenly.

Total: 18 hours.

### Day 1: C++, 3 hours

- RAII.
- Smart pointers.
- Move semantics.
- Interfaces.
- Testable design.

### Day 2: Linux/testing, 3 hours

- Linux process/thread basics.
- `gdb`, logs, sanitizers.
- Google Test.
- Mocking hardware.

### Day 3: RTOS/firmware, 3 hours

- Interrupts.
- DMA.
- Race conditions.
- RTOS tasks.
- Memory map.
- Bring-up.

### Day 4: Medtronic, 3 hours

- Hugo RAS.
- gRPC/DDS/Zenoh.
- Remote device monitoring.
- IEC 62304.
- Secure-by-design.

### Day 5: Cirrus, 3 hours

- DSP basics.
- Fixed-point.
- FIR/IIR.
- FFT purpose.
- Cycle counting.
- Cache/DMA.

### Day 6: CV stories, 2 hours

Prepare:

- Cyden medical firmware.
- Cyden production improvement.
- Dyson bootloader/CI/HIL.

### Day 7: Mock interview, 1 hour

- 30 minutes technical.
- 20 minutes behavioural.
- 10 minutes weak-point review.

## Priority Questions to Practise

### Shared

- Tell me about yourself.
- Walk me through an embedded software project.
- Explain C++ RAII.
- How do you make embedded software testable?
- How do you debug an issue seen only on hardware?
- Interrupts vs polling vs DMA.
- What causes race conditions?
- How do you handle version control and configuration management?
- How do you prioritise technical debt?

### Medtronic

- Why Medtronic?
- What do you know about Hugo RAS?
- How would you design remote monitoring for surgical devices?
- gRPC vs DDS vs Zenoh.
- How do you ensure reliability in medical-device software?
- What do you understand about IEC 62304?
- What does secure-by-design mean?

### Cirrus Logic

- Why Cirrus Logic?
- Fixed-point vs floating-point.
- What is saturation arithmetic?
- FIR vs IIR.
- What is an FFT used for?
- How would you optimise a real-time signal-processing pipeline?
- How would you use DMA?
- What would you check during board bring-up?
- How would you read a linker map file?

## Best Use of Existing Notes

Use these notes during the plan:

- Amazon OA active recall: `Job_training/DSA_neetcode_150/active_recall_pattern_sheet.md`
- Amazon behavioural rounds: `Behaviour_company_questions/Amazon.md`
- C++: `Job_training/cpp.md`
- Design patterns: `Job_training/Design_patterns/`
- RTOS: `Job_training/embedded_questions/rtos.md`
- Safety/medical lifecycle: `Job_training/embedded_questions/safety_critical_questions.md`
- Embedded fundamentals: `Job_training/embedded_questions/microcontroller_basics.md`
- Toolchains/build/debug: `Job_training/embedded_questions/toolchain_stuff.md`
- Remote monitoring: `Job_training/embedded_questions/medical_company/remote_patient_monitoring.md`
- Medtronic answers: `Behaviour_company_questions/medtronic.md`
- Cirrus answers: `Behaviour_company_questions/Cirrus_Logic.md`

## Rules for CV and Interview Honesty

- Do not claim professional DSP experience if you have only revised it.
- Do not claim production Zephyr experience if you have only studied it.
- Do not claim RISC-V experience unless you can answer basics.
- It is fine to say "I have not used that professionally, but I understand the
fundamentals and have prepared by studying/practising it."
- Lean heavily on real Cyden and Dyson experience.
- Use numbers where possible, especially the Cyden factory firmware
improvement from about 4 minutes to 3 minutes.

## End Goal

By the end of this plan, you should be able to:

- Explain your CV smoothly in 2 minutes.
- Answer C++ questions without panic.
- Talk through embedded debugging from real experience.
- Explain medical-device software quality for Medtronic.
- Explain DSP/performance firmware fundamentals for Cirrus.
- Give clear, honest answers for areas you have revised but not used
professionally.
