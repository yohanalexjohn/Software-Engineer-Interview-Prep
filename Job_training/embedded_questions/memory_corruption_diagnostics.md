# Memory Corruption Diagnostics

Use this for interview answers about intermittent embedded crashes caused by
stack overflow, heap corruption, or buffer overrun.

## Interview answer shape

- First preserve evidence: reset reason, logs, fault status registers, task name,
  stack pointer, recent inputs, and firmware version.
- Then separate the likely failure modes:
  - stack overflow
  - heap corruption
  - buffer overrun
- Watchdog reset can recover the device into a safe state, but it is not the
  root-cause fix. Still need to find what corrupted memory.

## Stack overflow

- Fill unused stack memory with a known pattern at startup.
- Later inspect how much pattern remains. This gives stack high-water mark.
- Add stack canaries / guard words at stack boundaries.
- Use RTOS stack high-water-mark APIs if available.
- On HardFault, inspect:
  - fault registers
  - stacked PC/LR
  - active stack pointer
  - which task was running
- Check linker map and linker-defined stack regions.
- Do not assume stack direction or exact address layout; use the actual
  architecture/linker/RTOS information.
- If available, use MPU guard regions so stack overflow faults immediately.

## Heap corruption

- Run heap integrity checks if the allocator/RTOS supports them.
- Trace allocation and free calls.
- Look for:
  - memory leaks
  - double-free
  - use-after-free
  - allocation-size mismatch
  - writing past the end of allocated blocks
- Add guard patterns before/after heap blocks.
- Where code can run off-target, use AddressSanitizer or Valgrind-style tools to
  reproduce memory bugs faster.
- In embedded/safety code, consider reducing or avoiding dynamic allocation in
  critical paths.

## Buffer overrun

- Put canaries around suspicious buffers:

```text
CANARY | buffer | CANARY
```

- Check whether either canary changes.
- Review every:
  - length check
  - array index
  - copy size
  - packet/parser boundary
  - signed/unsigned conversion
- Check input length before parsing fields.
- Use bounds-checked helper functions where possible.
- Use MPU guard regions where available to catch invalid memory access
  immediately.

## Short interview version

If the crash is intermittent, I would first preserve evidence from the fault or
reset, then check whether memory is being overwritten. For stack overflow, I
would use a fill pattern to measure high-water mark, stack canaries, RTOS
high-water APIs, and HardFault register plus stack-pointer inspection. I would
also confirm the real stack region from the linker map. For heap corruption, I
would use heap integrity checks, allocation/free tracing, guard patterns, and
look for double-free or use-after-free. If the code can run off-target, I would
use AddressSanitizer. For buffer overruns, I would add canaries around buffers,
review all bounds and length checks, and use MPU guard regions where available.
A watchdog reset is useful recovery, but it does not fix the root cause.
