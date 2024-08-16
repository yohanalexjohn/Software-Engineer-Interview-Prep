# Domain

## Behavioral Questions

### Tell us about yourself

I'm Nathan, I was most recently an Electronics/Embedded Software Engineer at
Dyson, where I worked on Power electronics schematics and control algorithms
for embedded software. I graduated from the University of Southampton with a
Master's in Electrical and Electronic Engineering in 2023. Learned Python and
Verilog from uni and internships (didn't use them in Dyson). In light of the
recent layoffs at Dyson, I'm looking for a new role in a company where I can
contribute everything I've learned from my prior experiences as well as learn
and grow to be a highly skilled software engineer

### Why Domin

For one, I quite like cars, am a car guy myself and being able to work on
active suspension systems sounds very interesting to me. Furthermore, Domin is
creating something very innovative in this industry and I'd love to be a part
of that.

Apart from that, I want to improve my skills as an embedded software engineer
and thus would like to play a part in a role that allows me to do that.

### What do you know about Domin

Domin is involved in the field of hydraulic systems and digital hydraulics.
They offer a range of products such as high-performance hydraulic valves and
systems designed for aerospace, automotive, and industrial applications, with a
focus on sustainability as the hydraulic systems are very efficient and can
reduce energy consumption compared to traditional hydraulic systems.

For the automotive industry, Domin makes active suspension systems. Active
suspension systems from what I can understand can automatically adjust the
suspension settings in real-time to improve ride-comfort, handling, and
stability. They rely on sensors, actuators, and a control system to actively
manage the suspension's response to changing driving conditions. E.g. soften
the suspension if sensors detect rough road, stiffen the suspension when
cornering at high speeds

### What are your strengths/weaknesses

Strength that has been highlighted to me in my previous workplaces would
definitely be that I am an independent quick learner. I am usually able to
complete tasks with minimal guidance to a high quality on time. I would also
say I have very strong organizational skills/project management skills. I am
very meticulous when it comes to documenting all my work, e.g. I have personal
notes on Obsidian, OneNote, and it makes it easy for me to transfer all my work
into formal documentation on Confluence/JIRA and for presentations. Also avoids
the issue of me explaining stuff to people. When it comes to code I usually
document it very heavily and effectively, I use Doxygen to very quickly create
documentation for the code I'm writing.

One weakness I would say I have ties in to my main strength. Like I said i'm
pretty independent when it comes to my work, and sometimes it's detrimental. I
have a tendency to not ask for help and instead bang my head against the wall
until I come up with a solution. Sometimes it leads to a bit of time wasted.
Another weakness I would say specifically for this role is that I don't really
have work experience outside of uni with like, the entire software/firmware for
a product, only handling a portion of it having been in a big company

## Technical Questions

### What is Memory Mapped IO

Method used in systems to i/o operations by mapping device registers into same
address space as system memory, allowing the CPU to interact with hardware
devices using standard memory instructions as if the device registers were a
part of RAM. Specific ranges of memory addresses are reserved for device
registers which correspond to hardware components. CPU can read or write to
these addresses using standard memory access instructions (load, store). This
means interacting with I/O devices does not require special instructions.

**Advantages:** simplicity, efficient access (faster), uniform address space,
flexibility Disadvantages: Address space usage (less for regular memory),
conflicts (address conflicts between memory and IO), security as improper
handling leads to security vulnerability or crashes

Alternatives are port-mapped I/O (isolated I/O) which uses separate address
space for I/O operation. Often used in x86 architectures

### What Happens before Main (boot process)

- **Power-On Reset**: The system resets and initializes hardware to a default
state.

- **Bootloader Execution (if present)**: The bootloader may configure essential
system settings, including preliminary hardware setup.

- **Startup Code Initialization**:

  - **Stack Pointer Setup**: The stack pointer (SP) is initialized to point to
  the end of the stack memory area, as defined by the linker script.
  - **Interrupt Vector Table Setup**: The interrupt vector table is populated
  with addresses of interrupt service routines (ISRs) to handle hardware and
  software interrupts.
- **C Runtime Initialization**:

  - **Variable Initialization**: Static and global variables are set to their
  initial values, and uninitialized variables (BSS segment) are zeroed out.

- **Calling `main()`**: With the stack and interrupt system properly set up,
the `main()` function is invoked to start the application.

###  Watchdog Timer Configuration

- Sets up the watchdog timer if used, to ensure the system can recover from
software faults.

### Runtime Library Initialization

- **Standard Library Initialization**: If using a standard C/C++ library,
initializes the library components such as memory allocation functions and IO
libraries.

### What happens during ISR

Is a function that is executed in response to an interrupt. When an interrupt
occurs, the normal flow of the program is halted, and the ISR is executed to
handle the interrupt. The processor saves the current state (program counter,
registers) so that it can resume later, this state is saved on the stack. The
processor then identifies which ISR to execute (unique interrupt vector).

The processor then jumps to the memory address of the ISR and begins executing
the code within the ISR, e.g. read/write data, clear interrupt flag. Once the
interrupt is handled, it clears the interrupt flag or signal to indicate the
interrupt has been handled (prevents ISR from being called again from the same
interrupt).

After the ISR is finished executing, the processor restores the saved state
from the stack, including program counters and registers. Processor then
resumes execution of the interrupted program, continuing from where it left off
before the interrupt occurred

### Disadvantages of Interrupt

- Code complexity: Makes code harder to maintain, debug, the logic flow is
disrupted by async events
- Interrupt latency: There is delay to interrupts, between interrupt and ISR
starting. If system is handling higher-priority interrupt or if interrupts are
temporarily disabled, latency can increase
- Priority Inversion: Low priority ISR taking too long can block higher
priority tasks or interrupts
- Resource contention: Interrupts need to access shared resources such as
variables, memory. Without careful synchronisation can lead to race conditions
- Context switching overhead: Processor saves current state and loads ISR every
time interrupt occurs which introduces overhead which reduces overall system
perf
- Non-deterministic: Interrupts can occur at any time, which can be problematic
in real-time systems where timing guarantees are critical

### Alternatives to Interrupt

- Polling: repeated checks the status of device or condition in a loop to see
if event has occurred. Simple, predictable timing, but inefficient CPU usage as
CPU spends time continuously checking of events
- Event loops: Run a loop that checks for events or messages and processes them
sequentially.
- Task Scheduling + RTOS: RTOS manages multiple tasks or threads, ensuring that
each task gets executed according to its priority and timing requirements.
Tasks are scheduled based on priority and other criteria, with RTOS handling
context switching between tasks. Easier to manage complex systems, but
complexity and overhead

###  RTOS vs Bare Metal

|                        | RTOS                                                                                                                                                                                   | Bare Metal                                                                                                                                                                     |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Complexity             | Higher complexity<br>- Introduces additional layers (task scheduling, resource management)                                                                                             | Simplicity<br>- No operating system layer, code written directly controls hardware, less overhead<br>- Tight control over timing and hardware                                  |
| Performance            | - Task switching overhead impacts performance<br>- Predictable execution as RTOS provides deterministic behaviour                                                                      | - Minimal overhead since no OS layer, can be highly optimized<br>- Faster execution since there's no context switching or OS overhead                                          |
| Real-time requirements | - Designed to handle real-time constraints, tasks need to be executed within strict deadlines<br>-Task prioritization makes it ideal for apps where certain tasks must respond quickly | - Direct control over timing, beneficial for simple real-time applications<br>- Limited scalability as managing real-time tasks without RTOS is hard when complexity increases |
| Use case               | Better for complex, multitasking, or real-time systems where scalability, determinism, and maintainability are important                                                               | Appropriate for simple, highly optimized systems where direct control over hardware and minimal resource usage are critical                                                    |

### Layers of Abstraction

- Hardware Layer - Lowest level, includes physical components such as
microcontrollers, sensors, actuators, and other peripherals.
- Microcontroller (Device Driver) Layer - Contains firmware and device drivers
that provide interface between hardware and higher-level software. Firmware
controls hardware components and device drivers allow OS or apps to interact
with hardware
- Operating System/Kernel Layer - If OS is used, this OS manages system
resources, multitasking, memory management, scheduling, communication between
system parts
- Middleware Layer - Provides set of services protocols that act as bridge
between OS and app layer, including communication stacks, data management, and
other utilities that simplify app development by abstracting hardware details
- Application Layer - Uses services provided by lower layers to perform its
functionalities, such as data processing, decision-making, and user interaction
- User Interface Layer - GUI, touchscreen, other IO

###  HAL

- Reside between microcontroller layer and operating system/Kernel layer or App
layer
- Serve as intermediary layer that abstracts specifics of hardware from the
higher-level software layers allowing the software to be developed
independently of the hardware specifics
- Provide uniform interface to access different hardware components, such as
timers, comm peripherals, and GPIO pins
- HALs define set of functions and protocols for interacting with the hardware.
These APIs are designed to be generic, covering a range of functionalities
provided by different hardware components
- HALs work with device drivers by providing a higher-level abstraction for the
interactions with hardware peripherals
- Middleware and app layers rely on HAL to perform hardware interactions
without needing to know the specific details of the hardware, allowing for
easier development and maintenance of the application code

### API

- Set of functions, protocols, and tools for building software and apps. Define
how different software components should interact and what operations can be
performed
- At the lowest level, APIs provide access to hardware features through
firmware or device drivers.
- APIs in the HAL provide a consistent interface for higher-level software to
interact with the hardware. This abstraction ensures that the same high-level
code can run on different hardware platforms by using the same API calls, even
if the underlying hardware differs
- In the top level, APIs are used to develop apps that leverage the
capabilities of the underlying hardware and software layers.
- E.g. an API in the HAL might provide functions like `HAL_GPIO_ReadPin()` or
`HAL_UART_Transmit()`, abstracting the details of reading a GPIO pin or
transmitting data over UART.

### Example of HAL API

```c
// gpio_hal.h
#ifndef GPIO_HAL_H
#define GPIO_HAL_H

#include <stdint.h>

// GPIO Pin Modes
typedef enum {
    GPIO_MODE_INPUT,
    GPIO_MODE_OUTPUT,
    GPIO_MODE_ALT,
    GPIO_MODE_ANALOG
} GPIO_Mode;

// GPIO Pin States
typedef enum {
    GPIO_PIN_RESET = 0,
    GPIO_PIN_SET
} GPIO_PinState;

// API to initialize a GPIO pin
void HAL_GPIO_Init(uint16_t pin, GPIO_Mode mode);

// API to write to a GPIO pin
void HAL_GPIO_WritePin(uint16_t pin, GPIO_PinState state);

// API to read from a GPIO pin
GPIO_PinState HAL_GPIO_ReadPin(uint16_t pin);

// API to toggle a GPIO pin
void HAL_GPIO_TogglePin(uint16_t pin);

#endif // GPIO_HAL_H

```

### Example of HAL Implementation

```c
// gpio_hal.c
#include "gpio_hal.h"

// Assume these are memory-mapped hardware register addresses
#define GPIO_BASE_ADDR 0x40020000
#define GPIO_MODE_OFFSET 0x00
#define GPIO_OUT_OFFSET  0x04
#define GPIO_IN_OFFSET   0x08

volatile uint32_t* GPIO_MODE_REG = (volatile uint32_t*)(GPIO_BASE_ADDR + GPIO_MODE_OFFSET);
volatile uint32_t* GPIO_OUT_REG  = (volatile uint32_t*)(GPIO_BASE_ADDR + GPIO_OUT_OFFSET);
volatile uint32_t* GPIO_IN_REG   = (volatile uint32_t*)(GPIO_BASE_ADDR + GPIO_IN_OFFSET);

void HAL_GPIO_Init(uint16_t pin, GPIO_Mode mode) {
    // Configure the mode of the specified pin
    // For simplicity, assume one mode bit per pin
    if (mode == GPIO_MODE_OUTPUT) {
        *GPIO_MODE_REG |= (1 << pin);
    } else {
        *GPIO_MODE_REG &= ~(1 << pin);
    }
}

void HAL_GPIO_WritePin(uint16_t pin, GPIO_PinState state) {
    // Set or reset the specified pin
    if (state == GPIO_PIN_SET) {
        *GPIO_OUT_REG |= (1 << pin);
    } else {
        *GPIO_OUT_REG &= ~(1 << pin);
    }
}

GPIO_PinState HAL_GPIO_ReadPin(uint16_t pin) {
    // Read the state of the specified pin
    return ((*GPIO_IN_REG & (1 << pin)) != 0) ? GPIO_PIN_SET : GPIO_PIN_RESET;
}

void HAL_GPIO_TogglePin(uint16_t pin) {
    // Toggle the state of the specified pin
    *GPIO_OUT_REG ^= (1 << pin);
}

```

### ADC in Embedded

#### Protocols

UART

- Universal Asynchronous Receiver/Transmitter. Allows two devices to send and
receive data serially without needing to share clock signal (simple but
sacrifices precision)
- Has own clock/baud rate
- Data transmitted in frames, containing start bit, data bit, optional parity
bit, one or more stop bits

- Example Code:

```c
// uart_hal.c

#include "uart_hal.h"
#include <avr/io.h>
#include <avr/interrupt.h>

void UART_HAL_Init(uint32_t baudrate) {
    uint16_t ubrr_value = (F_CPU / (16UL * baudrate)) - 1;

    // Set baud rate
    UBRR0H = (uint8_t)(ubrr_value >> 8);
    UBRR0L = (uint8_t)ubrr_value;

    // Enable receiver and transmitter
    UCSR0B = (1 << RXEN0) | (1 << TXEN0);

    // Set frame format: 8 data bits, 1 stop bit, no parity
    UCSR0C = (1 << UCSZ01) | (1 << UCSZ00);
}

void UART_HAL_Send(uint8_t data) {
    // Wait for the transmit buffer to be empty
    while (!(UCSR0A & (1 << UDRE0)));

    // Put data into the buffer, sends the data
    UDR0 = data;
}

uint8_t UART_HAL_Receive(void) {
    // Wait for data to be received
    while (!(UCSR0A & (1 << RXC0)));

    // Get and return received data from buffer
    return UDR0;
}
```

CAN

- Controller Area Network is a robust, efficient, and widely used protocol
designed to communicate without host computer, originally developed for
automotive
- Operates in harsh environments with high electromagnetic interference
- Multi-master: multiple nodes can initiate communication and the bus is
prioritized based on message ID, efficient bus arbitration
- Error Detection + handling: Includes mechanism and error detection and
correction, ensuring data integrity and reliability, e.g. bit monitoring, bit
stuffing , acknowledgement error, error counters
- Efficient: Frames limited to 8 bytes of data, quick transmission of small
data packets
- Standard and Extended Frames: Supports both 11-bit and 29-bit identifiers,
flexibility in addressing
- Frame contains Start of Frame, IDentifier, Remote Transmission request,
Control field, Data field, Cyclic Redundancy check, Acknowledgement field, end
of frame

- Example Code

```c
// can_hal.c

#include "can_hal.h"
#include "stm32f4xx_hal.h" // Include the HAL header for the specific MCU family

CAN_HandleTypeDef hcan;

void CAN_HAL_Init(void) {
    // Configure the CAN peripheral
    hcan.Instance = CAN1;
    hcan.Init.Prescaler = 16;
    hcan.Init.Mode = CAN_MODE_NORMAL;
    hcan.Init.SyncJumpWidth = CAN_SJW_1TQ;
    hcan.Init.TimeSeg1 = CAN_BS1_1TQ;
    hcan.Init.TimeSeg2 = CAN_BS2_1TQ;
    hcan.Init.TimeTriggeredMode = DISABLE;
    hcan.Init.AutoBusOff = DISABLE;
    hcan.Init.AutoWakeUp = DISABLE;
    hcan.Init.AutoRetransmission = ENABLE;
    hcan.Init.ReceiveFifoLocked = DISABLE;
    hcan.Init.TransmitFifoPriority = DISABLE;

    if (HAL_CAN_Init(&hcan) != HAL_OK) {
        // Initialization Error
        Error_Handler();
    }
}

void CAN_HAL_Send(uint32_t id, uint8_t *data, uint8_t length) {
    CAN_TxHeaderTypeDef txHeader;
    uint32_t txMailbox;

    txHeader.StdId = id;
    txHeader.ExtId = 0;
    txHeader.RTR = CAN_RTR_DATA; // Remote Transmission Request
    txHeader.IDE = CAN_ID_STD; 
    txHeader.DLC = length; // Data Length Code, indicating number of bytes of data
    txHeader.TransmitGlobalTime = DISABLE;

    if (HAL_CAN_AddTxMessage(&hcan, &txHeader, data, &txMailbox) != HAL_OK) {
        // Transmission Error
        Error_Handler();
    }
}

uint8_t CAN_HAL_Receive(uint32_t *id, uint8_t *data) {
    CAN_RxHeaderTypeDef rxHeader;

    if (HAL_CAN_GetRxMessage(&hcan, CAN_RX_FIFO0, &rxHeader, data) != HAL_OK) {
        // Reception Error
        Error_Handler();
    }

    *id = rxHeader.StdId;
    return rxHeader.DLC;
}

void Error_Handler(void) {
    // Implement error handling (e.g., log the error, reset the system, etc.)
    while (1) {
        // Stay here for debug purposes
    }
}
```

SPI

- Serial Peripheral Interface, synchronous serial communication protocol used
to connect mcu to one or more peripherals. Widely used due to simplicity,
speed, and versatility. Full duplex
- Uses clock line to synchronize data transmission between devices, ensuring
accurate timing
- Master-slave: Single master device controls the clock and initiates
communication with one or more slave devices
- Simple wiring: MOSI, MISO, SCLK, SS
- Flexible data size, can be configured to send/receive any number of bits per
word

- Different modes, clock polarity, clock phase

```c
// spi_hal.c

#include "spi_hal.h"
#include <avr/io.h>

void SPI_HAL_Init(void) {
    // Set MOSI and SCK as output, MISO as input
    DDRB = (1 << DDB3) | (1 << DDB5);
    // Enable SPI, 
    // Set as Master, Prescaler: Fosc/16,
    // Clock Polarity Low, Clock Phase Leading Edge
    SPCR = (1 << SPE) | (1 << MSTR) | (1 << SPR0);
}

void SPI_HAL_Send(uint8_t data) {
    // Start transmission by writing data to SPDR
    SPDR = data; // Data register
    // Wait for transmission complete
    while (!(SPSR & (1 << SPIF))); // SPIF = Interrupt flag
}

uint8_t SPI_HAL_Receive(void) {
    // Send dummy byte to receive data
    SPDR = 0xFF;
    // Wait for reception complete
    while (!(SPSR & (1 << SPIF)));
    // Return received data
    return SPDR;
}

uint8_t SPI_HAL_Transfer(uint8_t data) {
    // Send data
    SPDR = data;
    // Wait for transmission complete
    while (!(SPSR & (1 << SPIF)));
    // Return received data
    return SPDR;
}

```

I2C

###  Safety critical Development Process

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

### Experience with IEC 61508 Class B

####  Example of a temperature sensor/ADC

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

####  Examples of MISRA Concepts

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

##### Memory Safety

- Ensure program does not access invalid memory regions, leading to undefined behaviour, system crashes, or vulnerabilities exploitable by attackers
- Bounds checking: ensure all array accesses are within valid range to prevent buffer overflow

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
- Initialization and deallocation: properly initialize all variables and clear or deallocate memorry when it is no longer needed to avoid memory leak issues

```c
void InitBuffer(uint8_t* buffer, size_t size) {
    memset(buffer, 0, size);  // Clear buffer to prevent use of uninitialized memory
}

```

- Pointer Validity Checks: always check pointers before dereferencing them to prevent null pointer dereferences or accesses to freed memory

```c
void ProcessData(uint8_t* data) {
    if (data != NULL) {
        // Safe to use data
    } else {
        // Handle null pointer error
    }
}
```

##### Thread Safety

- Threading introduces concurrency, which can complicate control flow and
introduce new safety issues
- Race conditions: multiple threads access and modify shared data concurrently,
leading to inconsistent or incorrect behaviour
  - Fix using mutexes or semaphores to ensure only one thread can access
  critical section of code at a time

```c
#include <pthread.h>

pthread_mutex_t data_mutex = PTHREAD_MUTEX_INITIALIZER;
uint16_t shared_data = 0;

void UpdateSharedData(uint16_t value) {
    pthread_mutex_lock(&data_mutex);  // Acquire the lock
    shared_data = value;
    pthread_mutex_unlock(&data_mutex);  // Release the lock
}
```

- Deadlocks: Occur when two or more threads are blocked forever, each waiting
for the other to release a lock
  - Design system to avoid circular wait conditions and ensure consistent lock
  acquisition order

```c
void Thread1Function(void) {
    pthread_mutex_lock(&mutex1);
    pthread_mutex_lock(&mutex2);
    // Critical section
    pthread_mutex_unlock(&mutex2);
    pthread_mutex_unlock(&mutex1);
}

void Thread2Function(void) {
    pthread_mutex_lock(&mutex1);  // Same lock order as Thread1Function
    pthread_mutex_lock(&mutex2);
    // Critical section
    pthread_mutex_unlock(&mutex2);
    pthread_mutex_unlock(&mutex1);
}
```

- Missed Critical Events: Threads may miss critical events if they are
preempted or blocked when the event occurs
  - Use RTOS features like priority scheduling and avoid blocking calls in
  high-priority threads

```c
void HighPriorityTask(void) {
    while (1) {
        if (CheckForEvent()) {
            // Process event
        }
        // Avoid blocking calls
    }
}
```

### Why static over dynamic in embedded?

#### memory fragmentation

##### Stack overflow, how to detect

- Add values above and below the stack, bootloader checks the stack
periodically
- If anything overwritten, stack overflow, stop the system?
- To clear a stack, turn it off and on
- To prevent, don't pass structures, might have big shit inside (don't pass by
value, pass by reference)

##### Mutex vs Semaphore

###### Volatile

Prevent optimizations. Compiler optimizes code assuming variables are not
changed in probram won't change their value. However in embedded certain
variables can be changed by external events like interrupts, DMA. Compiler
might optimize out repeated reads or writes, incorrect behaviour. For MMIO, the
values of the registers can change due to hardware events, without volatile
compiler might assume value of register hasn't changed since last access,
causing program to miss critical events. Doesn't prevent race conditions or
guarantee atomicity (completed in single step without possiblity of
interruption).

###### Static

In a function, static variable retains value between function calls, meaning
the variable is initialized only once, and its value persists across multiple
invocations of fcn. Scope is limited to the function so cannot be accessed from
outside. Useful for maintaining state information without using global
variables. Outisde function, is initiatlized only once and exists for duration
of the program. Scope is limited to the file in which it is declared, making it
a file-level static variable. It is not visible to other files, even if they
are part of same program. Useful for encapsulating data within a file, prevent
naming conflicts Static function is visible only within the file. Useful for
creating helper/private functions that should not be exposed to other files,
reduce name collisions

