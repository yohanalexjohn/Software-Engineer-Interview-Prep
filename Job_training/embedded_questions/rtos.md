# RTOS

## Difference between task and a process

|Task|Process|
|--|--|
| Basic Unit Of execution | Large unit of execution |
| Runs independently shares same address space  | Isolated from each other and has its own memory space |


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
