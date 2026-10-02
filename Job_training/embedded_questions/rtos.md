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

Semaphores, mutexes, queues, notifications, and event groups are inter-task
synchronisation and communication mechanisms. Pick the primitive based on what
is being transferred or protected.

1. Queue - transfers discrete fixed-size data objects between tasks. RTOS queue
   operations already synchronise access to the queue; do not add a mutex just
   to protect the queue itself.
2. Mutex - ownership lock for shared data/resources; only the owner should
   unlock it, and RTOS mutexes may support priority inheritance.
3. Binary semaphore - 0/1 signal, often used to wake a task from an event.
4. Counting semaphore - tracks N available resources or pending events. A successful take decrements the count; give increments it up to the configured maximum.
5. Direct task notification - lightweight one-to-one task signal, optionally
   counting, when no payload copy is needed.
6. Event group - multiple boolean state/event bits; wait for ANY or ALL bits.
7. Stream buffer - continuous byte stream, useful for UART RX bytes.
8. Message buffer - variable-length message records where boundaries are known.

Recall prompt:

- Am I transferring data, protecting ownership, signalling one task, counting
  events/resources, or waiting for several boolean conditions?

## Scheduling and locking failure modes

### Priority inversion

- Definition: high-priority task is blocked by a lower-priority task holding a
  needed resource.
- Classic example: high-priority `ControlTask` needs an SPI/flash mutex, but
  low-priority `FlashTask` owns it. Medium-priority `LoggingTask` keeps
  pre-empting `FlashTask`, so `ControlTask` is indirectly delayed by
  `LoggingTask`.
- Mitigation: use mutexes with priority inheritance, keep critical sections
  short, do no unrelated work while holding the resource, consider a dedicated
  SPI-owner task, and avoid hard-real-time paths depending on slow flash access.
- Do not simply reshuffle priorities permanently as the default fix; fix the
  lock/resource design first.

### Priority inheritance

- Definition: temporarily boost the resource-owning lower-priority task so it
  can finish the critical section and release the resource needed by the
  higher-priority task.
- Classic example: `FlashTask` owns a mutex and `ControlTask` blocks on it. The
  RTOS temporarily raises `FlashTask` to the blocked high-priority task's
  priority, lets it release the mutex, then restores its original priority.
- Mitigation note: priority inheritance reduces priority inversion, but it is
  not a fix for bad lock design. Still keep lock scope small and bounded.

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
- Critical sections/interrupt masking: find long regions where pre-emption or
  interrupts are disabled.
- Mutex blocking/priority inversion: log wait time, mutex owner, and whether a
  medium-priority task delays the lower-priority owner.
- Queue blocking: check whether a send blocks because a downstream queue is
  full.
- Blocking I/O: look for flash writes, logging, allocation, retries, or driver
  calls in the deadline path.
- Scheduler jitter: compare expected wake time against actual run time across
  many cycles.
- Queue pressure: record queue high-water marks and producer/consumer rates.
- Hardware proof: use RTOS trace/timestamp logging, and toggle GPIO at task
  wake/start/completion so the timing can be checked on a scope or logic
  analyser.

Important distinction:

- BLOCKED means the task is waiting for time, a queue, notification, semaphore,
  mutex, or event.
- READY means the task can run; in a pre-emptive RTOS, a lower-priority task
  cannot normally keep a higher-priority READY task from running.
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
- Prefer `vTaskDelayUntil`-style absolute timing over `vTaskDelay`, because
  `vTaskDelay` sleeps after the current work completes and can accumulate drift.
- Keep ISR work tiny: timestamp, set a flag, give a semaphore, or submit work.
- Keep the periodic task short, bounded, and measurable.
- Measure worst-case execution time, not just average execution time.
- Give the task a priority that matches its deadline.
- Avoid mutexes or blocking calls in the hard 1 ms path where possible.
- Avoid dynamic allocation, heavy logging, flash writes, long mutex waits, and
  blocking I/O in the 1 ms path.
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
- How much jitter do I actually see on a scope or logic analyser?


## Practical sensing, processing, UART, watchdog architecture

Scenario: a sensor must be sampled every 10 ms, processed for 2-3 ms, sent over
UART, and supervised by a watchdog.

Design answer:

- Acquisition task: highest priority if the 10 ms sample deadline is the strict
  requirement. Use `vTaskDelayUntil`-style absolute periodic delay so drift does
  not accumulate. Keep the task short: read/sample, timestamp if useful, queue
  the raw sample, then block until the next release.
- Processing task: blocks on the sensor queue, processes the sample for 2-3 ms,
  then posts processed data to a UART/comms queue.
- UART/comms task: owns outgoing transmission and incoming commands. RX bytes
  are captured by ISR/DMA; parsing and command dispatch happen in task context.
- Watchdog/supervisor task: checks that required tasks have made progress, then
  refreshes the hardware watchdog only if the system is healthy.

Scheduling detail:

- Queue send wakes a blocked receiver by moving it from BLOCKED to READY.
- The scheduler still decides when it actually runs based on priority.
- If the woken task has higher priority than the current task, a context switch
  may happen immediately or on ISR exit.

Recall prompt:

- Which work is deadline-critical, which work can lag, and which task should
  own each queue or peripheral?

## Watchdog supervision

Interview answer:

Do not refresh the watchdog from one arbitrary task such as UART. Use a
supervisor task that checks progress/health from all critical tasks, then kicks
the watchdog only when the required tasks are healthy.

Design checklist:

- Each critical task reports progress using event bits, counters, direct task
  notifications, timestamps, or heartbeat flags.
- The supervisor periodically checks all required health signals.
- Refresh the hardware watchdog only if every required task made progress in
  the supervision window.
- Safely snapshot/check and clear progress indicators for each supervision window; use atomic exchange or an RTOS primitive so reports are not lost during reset.
- Independent task kicks can mask a dead critical task: only the supervisor kicks after all required tasks report meaningful progress within their expected deadlines.
- The watchdog task does not need to be the absolute highest priority; it needs
  enough priority and timing margin to meet the supervision interval.
- Watchdog reset is recovery. It is not root-cause diagnosis; still preserve
  logs/counters/reset reason where possible.

Recall prompt:

- Would this watchdog still be kicked if the sensor task died? If yes, the
  supervision design is wrong.

## Queue backpressure and throughput

Scenario:

UART slows down. The processing-to-UART queue fills. Processing may block trying
to send. Then the sensor-to-processing queue fills, and acquisition can
eventually be affected.

Interview answer:

- If dropping is acceptable, choose the policy from the data semantics:
  latest telemetry may overwrite/drop old data, but historical samples and
  control commands often must not be dropped or reordered.
- If dropping is not acceptable, consumer throughput must sustain producer
  throughput. A larger queue absorbs temporary bursts, not a sustained producer
  > consumer mismatch.
- Temporary burst: buffering can help.
- Sustained mismatch: architecture or throughput must change.

Options:

- Increase baud rate.
- Use DMA to reduce CPU/interruption overhead. DMA does not fix a sustained
  producer-rate greater than the physical UART throughput.
- Batch samples.
- Use a bounded queue/ring with an explicit full policy; drop stale noncritical data if requirements permit.
- Reduce protocol overhead.
- Add flow control.
- Buffer outages in external RAM/flash if the requirement needs it.
- Optimise processing.
- Reduce or aggregate transmitted sample rate if system requirements allow.

Recall prompt:

- Is the queue full because of a short burst, or because average production is
  faster than average consumption?
- Are all buffers busy because the consumer is too slow? If yes, investigate
  throughput instead of overwriting in-use data.

## ISR-to-task handoff

Interview answer:

Keep the UART ISR minimal. Capture the byte/data, put it into a ring
buffer/stream buffer/queue using an ISR-safe API, clear the interrupt source,
and optionally request a context switch if a higher-priority task was woken.

For a simple event with no payload, use a direct notification (or counting
notification when repeated events matter). If a peripheral status/data register
must be read before it changes or clears, capture that minimal register data in
the ISR and pass the payload to task context.

Practical notes:

- Full protocol parsing, CRC checking, header/length validation, retries, and
  command dispatch belong in task context.
- Do not block, sleep, take an ordinary mutex, perform heavy processing, or log
  from the ISR.
- A UART task can run a byte-by-byte parser/state machine and dispatch only
  complete validated frames.
- Long ISRs increase interrupt latency, task jitter, missed deadlines, and can
  delay lower-priority interrupts.
- FreeRTOS examples: `xQueueSendFromISR`, `vTaskNotifyGiveFromISR`, and the
  `portYIELD_FROM_ISR` idea when an ISR wakes a higher-priority task.

Recall prompt:

- What is the smallest ISR action that preserves the data and wakes the right
  task?

## Latest-value sharing

Use this when the consumer only needs the newest sensor value, not every sample.

Good designs:

- Shared latest-value struct protected by a mutex for consistent multi-field
  snapshots.
- Length-1 RTOS queue with overwrite semantics.

Rules:

- Hold the mutex only long enough to copy the shared value.
- Process the local copy outside the critical section.
- Use a mutex for shared data/resource ownership.
- Do not put a mutex around an RTOS queue just for queue access; the queue API
  already synchronises its own operations.

Recall prompt:

- Do I need every sample, or only the newest valid state?

## Direct task notification vs semaphore

Strong fit:

ADC conversion complete interrupt, DMA buffer already contains the data, and
exactly one consumer task should wake.

Why:

- ISR notifies the task.
- The task becomes READY and later runs according to scheduler priority.
- Notification is lighter than a queue/semaphore when no payload copy is needed.
- Binary-style notification can collapse repeated events.
- Counting notification can preserve multiple completions if the semantics need
  it.

Recall prompt:

- Is this one producer waking one known task with no data payload to copy?

## Event groups

Scenario:

Firmware update should start only when `BATTERY_SAFE`, `COMMS_CONNECTED`, and
`DEVICE_IDLE` are all true.

Design answer:

- Use an event group rather than manual shared flags plus a mutex or several
  semaphores.
- Each task sets/clears its bit as state changes.
- The update task blocks until ALL required bits are set.
- Event groups express multi-condition system state and ANY/ALL waits directly.

Recall prompt:

- Am I waiting for several boolean conditions produced by different tasks?

## Event group example: processing task

Scenario:

`ProcessingTask` reacts to sensor data, shutdown, and configuration changes.

Design answer:

- Define event bits such as `SENSOR_DATA`, `SHUTDOWN`, and `CONFIG_CHANGED`.
- Wait for ANY bit when any of those conditions should wake the task.
- Wait for ALL bits when work must start only after several conditions are true.
- Keep payload data elsewhere, for example in a queue or shared protected
  config object; event groups are for boolean state/events.

Recall prompt:

- Do I need ANY event, or must ALL required bits be set?

## Queue vs task notification

- Queue: transfers payload, for example a `SensorSample`, command, or buffer
  descriptor.
- Direct task notification: lightweight one-to-one signal, for example
  DMA-complete where the data already exists in a known buffer.
- Notification wakes the blocked task by making it READY. The scheduler still
  decides when it runs.

Recall prompt:

- Queue or notification here?
- Is there payload to transfer, or just a wake-up?

## Encoder pulse counting

Scenario:

GPIO edge interrupt reports encoder pulses.

Design answer:

- If one task only needs to be woken and missed duplicates do not matter, a
  task notification can be enough.
- If every pulse must be counted, prefer a hardware timer/counter peripheral or
  a counting notification/semaphore.
- Avoid binary-style events when repeated pulses can collapse into one pending
  signal.
- DMA is not the natural first choice for simple GPIO edge counting.

Recall prompt:

- Can repeated pulses collapse safely, or must every pulse be counted?

## Volatile ISR/task shared counter

- `volatile` tells the compiler the value can change outside normal program
  flow. It helps visibility for ISR/MMIO-style access.
- `volatile` does not make increments atomic and does not provide
  synchronisation or memory ordering.
- A 32-bit aligned read/write may be naturally atomic on some 32-bit MCUs, but
  that is a hardware property, not a guarantee from `volatile`.
- On narrower targets, multi-byte reads can tear if an ISR updates the value in
  the middle of the read.
- Use a short critical section, disable interrupts briefly, or use a suitable
  atomic/counter primitive when correctness depends on atomicity.
- Overflow/wraparound is a separate design issue from concurrency.

Recall prompt:

- Do I need visibility, atomicity, or both?

## Buffer-handle passing between tasks

Scenario:

Camera captures large image buffers and storage/upload tasks process them.

Design answer:

- Queue a descriptor, not the image bytes: pointer/handle, length, timestamp,
  and metadata.
- Use a fixed buffer pool and a `freeBufferQueue`.
- Camera takes a free buffer, fills it, and transfers ownership to storage with
  a queue send.
- Storage writes/persists it, then returns the buffer to the free pool when safe.
- Avoid heap allocation in the capture path for predictable memory use.
- Natural backpressure: if no free buffers exist, the producer blocks or drops
  according to explicit requirements.
- After `xQueueSend` transfers ownership, the producer must not reuse that
  buffer until it is returned.

Recall prompt:

- What owns this buffer now?
- Is the queue carrying bytes, or a handle to bytes?

## Shared SPI ownership

Problem:

Several devices share one SPI controller with different chip-select lines.

Design answer:

- Separate chip selects choose devices; they do not make the SPI controller
  usable by multiple tasks at the same time.
- Double buffering can improve throughput, but it does not solve bus
  arbitration.
- Prefer a dedicated SPI-owner task for complex systems:
  - clients queue requests with device/CS, tx/rx pointers, length, and a
    requester/response handle;
  - SPI owner serializes transactions;
  - use DMA where useful;
  - notify or reply to the requester when complete.
- With a dedicated owner task, client tasks do not need their own SPI mutex.
- If tasks access SPI directly, protect the whole transaction with a mutex,
  from chip select assert through transfer to chip select deassert.

Recall prompt:

- Who owns the SPI bus during the whole transaction?

## Motion camera storage upload architecture

Scenario:

Motion triggers a camera capture, storage persists the data, and Wi-Fi upload
sends it later.

Design answer:

- ISR stays minimal: clear interrupt, timestamp if needed, and notify a motion
  task or set an event.
- Motion task performs validation/debounce in task context.
- Camera task captures into a buffer from a fixed pool.
- Transfer buffer ownership explicitly to storage using a descriptor queue.
- Storage persists locally with states such as `UNSENT`, `IN_PROGRESS`, and
  `SENT`.
- Wi-Fi/upload is decoupled from capture and storage; it retries after reconnect
  and does not block the capture path.
- OTA runs lower priority/background and is gated by battery, network,
  device-idle state, flash space, and authenticated image verification.

Recall prompt:

- Which task owns capture, persistence, upload, and buffer return?

## UART packet buffering: queue, stream buffer, message buffer, ring buffer

For `HEADER | LENGTH | PAYLOAD | CRC` arriving as UART bytes, a stream buffer
plus parser task is usually a strong design.

Primitive choice:

- Queue: discrete fixed-size objects.
- Stream buffer: continuous byte stream; parser reconstructs framing.
- Message buffer: variable-length complete messages while preserving boundaries,
  useful when the producer already has complete frames.
- Manual ring buffer: high control/efficiency, but synchronisation, wraparound,
  and overflow correctness become user responsibility.

Parser notes:

- The parser consumes incrementally; it does not need to wait for max packet
  length.
- Validate header, length, payload availability, and CRC before dispatch.
- With DMA double buffering, DMA fills buffer A while the task processes buffer
  B, then they swap.
- At high throughput, avoid unnecessary extra copies if the task can process
  completed DMA buffers directly.

Recall prompt:

- Are bytes arriving gradually, or do I already have complete framed messages?

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

## Traffic-light GPIO, timer, and pedestrian-button design

- Keep timer and GPIO ISRs minimal: acknowledge the interrupt and publish an
  event/notification. Do not debounce, sleep, log, or run the full transition
  policy in the ISR.
- Debounce the button in task/main-loop context. A valid press sets a pending
  pedestrian request; it should not force an unsafe immediate light change.
- One state-machine owner handles all transitions, so timer expiry and button
  events cannot independently write conflicting GPIO states.
- Timer-driven transitions preserve minimum green/amber/all-red intervals.
  Service a pending pedestrian request only at the next safe transition, then
  clear it when accepted or completed according to the design.
- Centralize GPIO output updates in one function that maps a valid state to all
  lamp outputs. This avoids transient or impossible combinations caused by
  scattered pin writes.
- In an RTOS, use ISR-safe notification/queue APIs. In bare metal, atomically
  snapshot/clear event flags in the main loop as required by the MCU.

Recall prompt:

- Who owns the state, what may each ISR do, and when is a pedestrian request
  safe to service?

## Recalled Dyson FreeRTOS OTA flow

Evidence boundary: these are recalled experience details, not a source-code verification.

- RTOS embedded communications used queues between components.
- Linux controller's OTA command was acknowledged; an OTA task/notified context set the mailbox to OTA-in-progress and reset.
- After restart, the bootloader read the mailbox, entered update flow, signalled ready, and received the new application payload.
- State exact queue/notification API names and task priorities only if genuinely remembered; verify them from source later. Do not invent task count, timing, or validation details.
- Scheduler wording: a preemptive RTOS can run the highest-priority ready task; it does not wait for the previously running task to “finish”. A task can block, yield, or be preempted.

## nRF / Zephyr e-paper project status

Work in progress: SPI async/DMA project exists. The TX buffer belongs to the SPI path while active and must not be changed/reused before completion. Verify exact completion handling and display BUSY-pin handling from code before making stronger claims. SPI transfer completion and display-ready status need distinct explanations. Do not present this as a finished production outcome.
