#  Microcontroller questions basics

[Github link for the questions](https://github.com/theEmbeddedGeorge/theEmbeddedNewTestament.github.io/tree/master/Interview)

##  Microcontroller basics

### Set up the clock

1. Configure the system oscillator & PLL
2.  Set system clock frequency
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

Signal emitted by the hardware or software to process the task immediately 

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
