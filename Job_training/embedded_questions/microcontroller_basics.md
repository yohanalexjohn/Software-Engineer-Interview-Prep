#  Microcontroller questions basics

[Github link for the questions](https://github.com/theEmbeddedGeorge/theEmbeddedNewTestament.github.io/tree/master/Interview)

## Board Bring up

1. **Check Power Rails**
1. **Prove can flash using JTAG or serial programmer**
1. **Prove Timers and oscillators set up correctly through blinky and gpio**
1. **Check interrupts through spi and i2c**
1. **Memory checks if external flash is present**
1. **ADC,dma**
1. **Debugging and verification**

### How to say it 

I’d start simple — power, clock, and programming. Then verify the basics like GPIO and UART, 
before moving on to more complex peripherals like SPI or CAN. At each stage I’d validate with 
test code and tools like a logic analyzer. Finally, I’d integrate everything into higher-level
tests to prove the board functions as intended. This systematic approach reduces risk and makes 
it easy to isolate issues.

##  Microcontroller basics

### Set up the clock

1. Configure the system oscillator & PLL
2. Set system clock frequency
3. Enable peripheral bus clock

### DMA - Direct Memory Access

1. Configure source and destination addresses 
2. Set transfer size, mode(circular/normal), priority
3. Enable DMA interrupts if necessary
4. Link DMA to peripherals 

### Set up the ADC

1. Enable the ADC clock
2. Configure the ADC parameters -> resolution, data, alignment and sampling time
3. Set the ADC Channel: where to read from
4. Start the ADC
5. Read the ADC value

### GPIO setup

1. Enable the port
2. Set the pin mode: input, output ,alternate function or analog.
3. Configure output type: set as push-pull or open-drain.
4. Set the speed.
5. Configure Pull-up/ Pull-down resistors
6. Set or read pin

### I2C

1. Enable I2C clock
2. Configure I2C pins
3. Set the speed, timing, addressing mode
4. Send and receive data

### SPI

1. Enable SPI clock
2. Configure SPI pins
3. Configure clock polarity, phase and data format
4. Send and receive data

#### SPI > I2C why??

SPI generally offers higher throughput and simpler electrical/protocol timing 
for high - speed point to point peripherals, at the cost of more wires and chip-selects

I²C is useful when multiple lower-speed peripherals need to share two wires.

### Debugging UART / SPI / I2C

Interview answer:

I would debug from the physical layer upward: power, ground, pins, clocks,
alternate functions, then protocol settings, then driver logic. For serial
buses, I would use a logic analyser or scope early, because the waveform can
quickly show whether the problem is wiring, timing, or software.

UART checklist:

- Baud rate, parity, stop bits, word length.
- TX/RX crossed correctly and common ground present.
- Framing/overrun errors.
- Ring buffer overflow or missed interrupt.

SPI checklist:

- CPOL/CPHA mode.
- Chip-select timing and polarity.
- MISO/MOSI wiring.
- Clock speed within device limits.
- Bit order and command/address phase.
- Dummy bytes/reads if the device protocol needs them.

I2C checklist:

- Pull-up resistors present and sensible.
- Correct 7-bit address; avoid shifting it twice.
- ACK/NACK behaviour.
- Bus speed.
- SDA/SCL stuck low.
- Device power/reset state.

Common mistake:

- Do not only stare at code. For bus issues, prove what is happening on the
  pins.

### CAN Controller Area Network

1. Enable the CAN peripheral clock
2. TX and RX pins need to be set as alternate functions with the right speed
3. Set the CAN bit timing, configure baud rate 
4. Set CAN controller into init mode
5. Configure CAN filters, what message ids to accept 
6. Set the Mode 
    - Normal Mode : Communication 
    - Loopback Mode : Self test without physical bus
    - Silent Mode : Listen only monitoring
7. Set up the interrupts
8. Transmit a frame, load ID, DLC (data length code)

### Interrupts

Interrupt is a mechanism where the CPU temporarily halts its current execution and jumps 
to a special function called an Interrupt Service Routine (ISR) when a hardware/software event occurs.

1. ISR (Interrupt Service Routine) are short and sweet ideally sets a flag to check
2. No inputs are taken (function parameters ) and no outputs are returned

### How does CPU handle an interrupt

1. CPU saves the current state (PC/ registers)
2. Jumps to ISR executes it
3. Restores state and continues the process

#### What are the interrupt types

1. Hardware: Occurs by the interrupt request signal from the peripheral circuits.  
Useful for debugging with JTAG

2. Software: Occurs when execution of a dedicated instruction
Useful for debugging with JTAG when not enough hardware pins

### ISR and main-loop shared state

Interview answer:

If an ISR and main loop share data, I would keep the ISR short and make the
shared access explicit. A flag written by an ISR may need `volatile` so the
compiler re-reads it, but `volatile` does not make compound operations atomic.
For counters, buffers, or multi-byte values, I would use atomic operations,
temporarily disable interrupts around a very small critical section, or pass
data through a queue/ring buffer.

Checklist:

- Is the shared object one byte or multi-byte on this MCU?
- Can the ISR update it while main is halfway through reading it?
- Is the operation compound, like read-modify-write?
- Does the buffer need head/tail updates to be atomic?
- Would a queue/semaphore be clearer than a shared flag?

Common mistake:

- `volatile` prevents some compiler caching/reordering assumptions. It does
  not protect against races or make `counter++` atomic.

### Volatile hardware register access

Example:

```cpp
#define STATUS_REG (*(volatile uint32_t*)0x40001000)
```

Interview answer:

`volatile` is appropriate for a memory-mapped hardware register because the
value can change outside normal program flow. Each access should result in a
real register access; the compiler must not assume the value stays the same or
optimize repeated reads away.

Bad pattern:

```cpp
uint32_t cached = STATUS_REG;
```

Then repeatedly using only `cached` later may be wrong, because it reads the
hardware once and then keeps using a stale snapshot. Copying into a local
variable is fine when I intentionally want one stable snapshot for one
calculation; it is wrong when I need fresh hardware state.

### What happens when MCU startsup and main()

1. Reset vector fires - Vector table reset handlers address loads on the pc on power up 
2. startup code runs - Initalises stack pointer , copies .data from flash to ram, zerors .bss, 
3. System clock init - configures clock tree, PLLs, early pheripheral startup before main 
4. C runtime init for c++ - Runtime , static m global consttucturs run 
5. call to main 

The cpu loads the initial stack pointer and reset vector from the two entries in the vector table  as part of reset, before the Reset Handler executes.

Execution enters the reset handler, which performs low level system initialisation
and c/c++ runtime setup. 

Startup code copies intialised .data values from flash to RAM, zeroes the uninitialised variables
in the .bss section. 

The runtime also performs run time static/global constructor initialisation for c++.

Once this is done main() is called. 

So therefore by the time main runs all the static variables have been inisliased correctly. 

Interview debugging clue:

If a static local/global that should have a non-zero initializer prints as `0`,
suspect startup before normal application logic. Check the linker script,
`.data` load address, `.data` copy loop, `.bss` zeroing boundaries, and whether
startup code is using the right symbols.

### Testing firmware without hardware

Interview answer:

You cannot prove every hardware behaviour without hardware, but you can still
test a lot. I would separate hardware access from decision logic, then run host
unit tests for parsers, state machines, algorithms, alarms, safety checks, and
protocol framing. Drivers can be wrapped behind interfaces and replaced with
mocks/fakes. When hardware arrives, I would add integration tests and
hardware-in-the-loop tests for timing, electrical behaviour, and real
peripheral interaction.

Good candidates for host tests:

- packet parsing and length checks
- CRC/checksum handling
- state-machine transitions
- retry/error handling
- control thresholds and alarm logic
- circular buffer edge cases

Common mistake:

- Do not say "we cannot test until hardware exists." Say what can be tested on
  host and what still needs real hardware.

### What is a vector table 
The vector table is located at a defined memory address, commonly the beginning of the boot memory region. 
Its first entry contains the initial MSP and its second entry contains the Reset Handler address.

### Program counter - second value from the vector table 

The PC holds the address of the next instruction to execute. After reset it is loaded from the reset vector.

### ADC 

#### Resolution 

- 12 bit ADC 
- 2 ^ 12 = 4096 levels

EX: 3.3V 
LSB = 3.3 / 4096 = 0.806 mV

Higher resolution means smaller voltage steps

#### Sampling Rate

How frequent we take the measurements

#### Quantisation 

- Analogue signal is continues 
- ADC maps it to one of a finite number of digital levels
- can create quantisation error 

#### Reverence Voltage
