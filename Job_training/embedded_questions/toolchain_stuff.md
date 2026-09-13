# Toolchain Files

- Consists of programming tools like compiler, linker, assembler, debugger
- Used in embedded systems to compile code to particular architecture
- CMAKE to automate the build and linking

## linker scripts

- A linker script is a text file used by the linker to control the memory
regions and layout of the executable
- Tells what sections are placed where in the .text , .bss and how much should
be allocated


- The linker script tells the linker how the firmware should be laid out in the target's memory map.

## Startup files

- Startup files are written in assembly or C sets up at runtime to before the
main call
- Initialise the hardware
- Setup the stack pointer vector table
- Initialise the data and bss segments

## .text section

- Has the executable code
- Read only
- Copied at run time in RAM

## .data section

- Contains initialised global and static variables
- Stored in ROM
- Copied at run time in RAM
- .data represents writable objects that must exist in RAM at runtime.
- .data has a load address in Flash and a runtime address in RAM.

## .bss section

- Contains uninitialised global and static variables  
- No space in ROM
- Initial value set to 0 so no space needed

## Memory regions

### ROM

- .text
- .data
- .rodata

### RAM

- .bss
- .stack ( used for functional call management )
- .heap ( Dynamically allocated memory during program execution )

### Memory layout and performance affected

#### Flash

**Potential**:
 - wait states
 - cache/prefetch behaviour
 - bus contention

#### RAM

**Potentially**:
- lower access latency
- deterministic access on some architectures
- faster execution for critical routines

#### DMA

**Memory location can affect**:
- DMA accessibility
- cache coherency
- bus bandwidth

##### DMA corruption

1. Buffer ownership - is the cpu modifying the buffer when the dma is writing
2. Buffer Boundaries - Could DMA write beyond the allocated region
3. DMA capcable memory - is the buffer located somehwere the dma can access
4. cache coherency - on cache enabled mcu .. need appropirate cache clean/ invalidate operations
5. Interrupt Timing -  Could the CPU miss processing a buffer before DMA reuses it
6. Race Conditions - Is the CPU reading a half written buffer
7. Electical Signals - emi ?

#### Alignment

**Poor alignment can affect**:
- Access efficiency
- DMA requirements
- sometimes correctness

This is what Cirrus means by memory layout and performance implications.

## .rodata

.rodata is placed in read-only memory, typically Flash, to avoid consuming RAM and to preserve its read-only nature.
