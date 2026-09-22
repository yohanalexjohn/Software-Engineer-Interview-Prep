# RTOS

## Difference between task and a process

|Task|Process|
|--|--|
| Basic Unit Of execution | Large unit of execution |
| Runs independently shares same address space  | Isolated from each other and has its own memory space |

## Scheduler

The scheduler maintains the state of runnable tasks and selects which tasks gets CPU time 
based on the scheduling policies, typically priority. In a pre-emptive RTOS, a higher priority 
task can pre-empt a lower priory running task.

## Advantages

- Predictable timing behaviour
- Deterministic response times 
- Bounded Latency
- Resource management
- Interrupt Handling

## Scheduling Policies 

- Preemptive Scheduling
   1. Higher Priority tasks take over than lower priority
   2. Predictable behaviour
- Cooperative Scheduling
   1. Tasks Voluntarily yield control 
   2. Lower overhead
   3. Less Predictable timing
- Round Robin Scheduling
   1. Equal priority tasks share cpu time
   2. Time quantum allocation
   3. Fair Response distribution

## Synchronisation and Communication

Semaphores and mutexes are inter-task synchronisation and signaling mechanisms.

1. Binary semaphore - 0 or 1 signal, often used to wake a task from an ISR or event.
2. Counting semaphore - count represents available events/resources; tasks take/decrement and give/increment.
3. Mutex - ownership lock for shared data/resources; only the owner should unlock it, and RTOS mutexes may support priority inheritance.

## Scheduling and locking failure modes

### Priority inversion

- Definition: high-priority task is blocked by a lower-priority task holding a needed resource.
- Classic example: Low holds a UART mutex. High wakes and needs the UART, but blocks on Low. Medium does not need the UART, but keeps running and prevents Low from releasing the mutex, so High is indirectly delayed by Medium.
- Mitigation: use mutexes with priority inheritance, keep critical sections short, avoid sleeping/logging/slow I/O while holding locks, and avoid unnecessary shared mutexes on hard real-time paths.

### Priority inheritance

- Definition: temporarily boost the resource-owning lower-priority task so it can finish the critical section and release the resource needed by the higher-priority task.
- Classic example: Low owns a UART mutex and High blocks on it. The RTOS temporarily raises Low near High's priority, Low runs, releases the mutex, then drops back to its normal priority.
- Mitigation note: priority inheritance reduces priority inversion, but it is not a fix for bad lock design. Still keep lock scope small and bounded.

### Starvation

- Definition: ready lower-priority task gets little/no CPU time because higher-priority tasks keep running.
- Classic example: High runs a `while (true)` polling loop and never blocks, so a low-priority logging task remains ready but rarely or never runs.
- Mitigation: make high-priority tasks block or sleep when idle, keep high-priority work bounded, choose sensible priorities, use time slicing for equal-priority tasks where appropriate, and avoid busy loops.

### Deadlock

- Definition: cyclic resource wait where tasks cannot progress.
- Classic example: Task A holds Mutex 1 and waits for Mutex 2, while Task B holds Mutex 2 and waits for Mutex 1.
- Mitigation: use consistent lock ordering, scoped locking/RAII where available, timeouts where appropriate, and design to reduce shared locks.

Interview distinction:

- Priority inversion: High is blocked by Low holding a resource.
- Priority inheritance: RTOS temporarily boosts Low so it can release the resource.
- Starvation: Low is ready, but higher-priority work keeps taking the CPU.
- Deadlock: tasks are stuck waiting on resources held by each other.

## Diagnosing occasional missed deadlines

Interview answer:

If average CPU usage looks normal but a periodic RTOS task occasionally misses
its deadline, investigate worst-case latency, not average load. I would
timestamp the task's expected wake time, actual start time, and completion time,
then correlate each miss with what else was running.

Checklist:

- Expected vs actual timing: log expected wake time, actual start time,
  completion time, and deadline miss amount.
- Execution-time spike: measure worst-case execution time, not just average
  execution time. A rare branch, retry loop, cache miss, peripheral timeout, or
  logging path can break the period.
- Higher-priority interference: trace context switches and check whether a
  higher-priority task runs too long near the missed deadline.
- ISR latency: measure interrupt duration and frequency. A long ISR or burst of
  interrupts can delay task scheduling even when average CPU usage is low.
- Mutex blocking: log how long the task waits, which mutex it waits on, and
  which task owns it.
- Scheduler jitter: compare expected wake time against actual run time across
  many cycles.
- Hardware proof: use RTOS trace/timestamp logging, and toggle GPIO at task
  wake/start/completion so the timing can be checked on a scope or logic
  analyser.

Important distinction:

- Temporary mutex blocking: task waits briefly because another task owns the
  lock, then continues.
- Priority inversion: high-priority task waits on a lock held by a lower-priority
  task while medium-priority work prevents the lock owner from running.
- Starvation: task is ready, but other work repeatedly prevents it from getting
  CPU time.
- Deadlock: tasks are stuck forever in a cyclic resource wait.

Likely fixes:

- Shorten critical sections and avoid slow I/O, logging, sleeps, or long blocking
  calls while holding a mutex.
- Use priority inheritance where mutex blocking can affect a high-priority task.
- Bound ISR work; keep ISRs short and move heavier work into a task/work queue.
- Bound task work; split long processing or reduce per-period workload.
- Fix priority assignment so deadline-critical work can pre-empt less important
  work.
- If worst-case execution time approaches the task period, reduce the workload,
  increase the period, optimise the path, or move work out of the hard real-time
  path.

## Designing a 1 ms periodic task

Interview answer:

For a 1 ms periodic task, I would first decide what work genuinely belongs in
the hard periodic path. The task should do only bounded time-critical work, such
as reading a sample, updating a control output, or moving data into a queue.
Slow work such as logging, formatting, communication retries, flash writes, or
large calculations should run in a lower-priority task or worker.

Design checklist:

- Use a hardware timer interrupt, RTOS timer, or absolute-delay API so the
  release time is based on the intended schedule, not on "sleep 1 ms after work
  finishes."
- Keep ISR work tiny: timestamp, set a flag, give a semaphore, or submit work.
- Keep the periodic task short, bounded, and measurable.
- Measure worst-case execution time, not just average execution time.
- Give the task a priority that matches its deadline.
- Avoid mutexes or blocking calls in the hard 1 ms path where possible.
- If shared data crosses ISR/task boundaries, use atomics, queues, or short
  critical sections.
- Prove timing with trace logs or GPIO toggles on a scope/logic analyser.

Common mistake:

- A busy `while (true)` polling loop wastes CPU and can starve lower-priority
  work. A periodic task should normally block until the next release.

Recall prompt:

- What must happen every 1 ms?
- What can be delayed safely?
- What is the worst-case time, including blocking and ISR interference?

## Real-time vs non-real-time operating systems

|Real-time operating system|Non-real-time operating system|
|--|--|
|Designed for deterministic response times|Designed for throughput, usability, and fairness|
|Important tasks can be guaranteed to run within a deadline|Tasks may run quickly on average, but timing is not guaranteed|
|Uses priority-based scheduling, bounded latency, and predictable interrupt handling|Scheduling can be affected by background processes and system load|
|Used in medical devices, automotive systems, industrial control, robotics, and safety-critical systems|Used in desktops, servers, phones, and general-purpose computing|

Key point:

A real-time operating system is not necessarily faster. It is more predictable.
The important question is whether the system can guarantee that a critical task
will run before its deadline.

Interview answer:

In a real-time system, correctness depends on both the result and the timing of
that result. For example, if a medical device must sample a sensor every 1 ms
or trigger an alarm within a defined time, the scheduler needs deterministic
behaviour and bounded latency. A non-real-time OS may be fast on average, but
it cannot normally guarantee that timing under all conditions.
