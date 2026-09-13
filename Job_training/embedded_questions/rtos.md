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

Semaphores and mutexes are inter-task Synchronisation and signaling mechanisms

1. Binary Semaphore's - 1 & 0
2. Counting Semaphore - Each time task is called count is reduced or increased once hit threshold yield
3. Mutex - wont yield until key is returned or task is completed

### Disadvantage of Binary Semaphores

Lower priority tasks might be holding away the higher priority tasks as it has not released the count.

Eg: Medium task running doesn't allow the task with the semaphore to run and the higher priority task H cant run its UART task as 
Low priority task has access due to binary semaphore

Mutexes are better as the lock boosts the priority of the task. Priority falls back to normal after task is finished. 
Eg: fix problem above by boosting low priority to higher priority therefore L is run and released lock to Higher priority after which medium 
task is run.

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
