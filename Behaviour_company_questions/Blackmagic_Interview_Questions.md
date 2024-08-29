# Blackmagic 

## Tell us about yourself

I'm Nathan, I was most recently an Electronics/Embedded Software Engineer at
Dyson, where I worked on Power electronics schematics and control algorithms
for embedded software. I graduated from the University of Southampton with a
Master's in Electrical and Electronic Engineering in 2023. In light of the
recent layoffs at Dyson, I'm looking for a new role in a company where I can
contribute everything I've learned from my prior experiences as well as learn
and grow to be a highly skilled engineer (and hopefully not get laid off
again).

## Why Blackmagic

I am particularly excited about the opportunity at Blackmagic Design because I
am very much into tech, and Blackmagic is very much on the forefront of
innovation in the media production industry. The products you've developed,
such as advanced digital film cameras and cutting-edge video editing software,
have set new standards in the field. I am passionate about working on projects
that push the boundaries of technology, and Blackmagic's commitment to
providing high-quality solutions aligns perfectly with my values and career
goals.

As a Junior FPGA Design Engineer, I am eager to contribute to the development
of hardware solutions that empower creators and professionals worldwide. The
chance to work on the hardware side of your products, especially in the FPGA
domain, is thrilling because it offers a perfect blend of challenge and
opportunity for learning. I am motivated by the idea of being part of a team
that continuously innovates and brings groundbreaking products to market.
Moreover, Blackmagic Design's collaborative culture and focus on engineering
excellence make it an ideal place for me to grow and develop my skills further.

## What do you know about Blackmagic

Blackmagic Design is renowned for its high-quality and innovative products in
the professional video and cinema production industries. Founded in 2001, the
company has made significant contributions to the market with its extensive
range of products, including digital film cameras, broadcast converters, video
editing software, and more.

One of the standout innovations from Blackmagic is the Blackmagic URSA series
of cameras, which offer high-end cinematic quality at an accessible price
point, making them popular among independent filmmakers and professionals
alike. Additionally, the DaVinci Resolve software suite is a key product in the
post-production world, known for its powerful color correction and editing
capabilities. It’s widely used in the industry, not just for color grading but
also for editing, visual effects, and audio post-production.

Blackmagic Design has been a leader in democratizing high-quality video
production tools, making professional-grade equipment available to a broader
audience. The company's products are recognized for their reliability,
innovative features, and excellent value, which have set new standards in the
industry. This innovative approach and commitment to empowering creatives are
what make Blackmagic Design a standout player in the market.

## Tell us about a time when you had to overcome adversity

Talk about the 10 week deadline shortened

## What are your strengths/weaknesses

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
Another weakness I would say specifically for this role is that I am a bit
rusty with FPGA/Verilog stuff because I haven't used it at work, so I haven't
really touched it since uni but I'm sure that's something that can be easily
ironed out.

## Where do you see yourself in 5 years

## What is an FPGA on the inside

- Consists of LUTs, FFs, dual port RAMs, IO blocks, PLLs, Multipliers, Routing,
configurable logic block (CLB)

### What is Metastability

- Metastability means that a signal is in an unpredictable or unknown state.
This happens when data transitions extremely close to the active edge of the
clock, breaking setup and hold time constraints. The flop is unable to catch
the data entirely. ![[1280px-Metastability_D-Flipflops.svg.png]]

### How to prevent metastability?

- Primary reason is set-up and hold timing violations. You can synchronize the
asynchronous input signals with the system clock before applying them to the
synchronous system. 
- Another way is to have longer clock period to allow for resolution of
metastable states. 
- Can also add multiple synchronizing flip-flops or synchronizers to the
signals that travel from one clock domain to another, gives an entire clock
period to resolve metastability in first synchronizing flip-flop.

### Difference between combinational and sequential?

- Combinational is a circuit where the output is only a pure function of the
input. Sequential is where the output relies on not just the current values of
the input signals, but also the previous state

## Name a few types of latches

- JK Latch, SR Latch

## Name a few types of flip flops

- JK, D, T

## What is the difference between a flip flop and a latch?

- Flip flop uses a clock as an input but a latch does not. The clock input on
the ff is used to pass the D input on the ff to the Q output. A latch having no
clock will latch or hold the output steady.

- Don't use latch, can be difficult for FPGA tools to create properly, create
routing delays, can cause design to fail to meet timing

## What is the purpose of a PLL?

- Phase-locked loop is used to generated desired clock frequencies. They are
built into FPGAs and are able to take an input clock and derive a unique
out-of-phase clock from that input clock

## What is the difference between Inference and Instantiation?

- Inference is writing some generic HDL for a desired resource. The synthesis
tool will attempt to deduce the intended resource based on the written HDL. It
is more portable but not always possible

- Instantiation refers to using a predefined instantation template provided by
vendor documentation

## What is a Block RAM?

- A specific part of an FPGA that is usually a 16k or 32k bits storage element.
It can have dynamic width and depth. can be used for storing LUTs (not the
built in LUTs), Read-only data, FIFO for temporary data, crossing clock domains

## What is an always block?

- In verilog, an always block is used to describe sequential logic behaviour
within digital designs. It is primarily used to model the behaviour of
registers, flipflops, and other sequential elements

## What is the difference between asynchronous and synchronous logic?

- Synchronous means there is a clock involved, whereas asynchronous means there
is no clock. Most logic inside FPGA uses synchronous, e.g. ffs, brams, and
things like resets can be asynchronous. 
- Communication protocols can also be synchronous/asynchronous, e.g. UART is
async, SPI/I2C is sync

## Describe setup and hold time, what happens if they are violated?
- Setup is the amount of time required for the input of a ff to be stable
before the clock edge comes along. 

- Hold time is the amount of time required for the input of a ff to be stable
after the clock edge comes along

-  If either is violated, there can be a metastable condition inside the FPGA,
thus creating a timing error inside the place and route tool

## Why might you choose to use an FPGA in your design?

- FPGAs are high customizable, and some reason to use them might be that there
is a lot of peripherals, a lot of I/O, fast processing speed, a lot of math,
high data throughputs, interfaces to high bandwidth external memory, and
reprogrammability

## Difference between VHDL/Verilog/SystemVerilog

- VHDL and and Verilog are general-purpose digital design languages, SV
represents an enhanced version of Verilog
- VHDL is strongly typed, deterministic, and more verbose. emphasizes
unambiguous semantics and allows portability between tools
- Verilog is weakly typed and more concise with efficient notation, it is
deterministic. All data types are predefined in Verilog and each has a
bit-level representation. Syntax is C-like.
- SystemVerilog includes a set of extensions to Verilog to help engineers
design and verify larger and more complex designs. Combines Verilog and VHDL
features, as well as C and C++

## When to use assign?

- Assign is used for driving wire/net type declarations. Since wire change
values according to the value driving them, whenever the operands on the RHS
changes, the value is evaluated and assigned to LHS (thereby simulating a
wire). Continual assignment to wire outside an always statement.

## Blocking vs non-blocking assignment

There are three types of assignments in Verilog:
- **Continuous** assignments (assign x = y;). Can only be used when **not**
inside a procedure ("always block").
- Procedural **blocking** assignment: (x = y;). Can only be used inside a
procedure.
- Procedural **non-blocking** assignment: (x <= y;). Can only be used inside a
procedure.

Blocking assignment executes "in series" because a blocking assignment _blocks_
execution of the next statement until it completes. Therefore the results of
the next statement may depend on the first one being completed.

Non-blocking assignment executes in parallel because it describes assignments
that all occur at the same time. The result of a statement on the 2nd line will
not depend on the results of the statement on the 1st line. Instead, the 2nd
line will execute as if the 1st line had not happened yet.

## Static Timing Analysis:

- Used by place and route tools to ensure timing has been met.
- Based upon synchronous design techniques.
- Check the timing from register outputs or device inputs through any
combinatorial logic, and into the next register input or device output.
- E.g. between 2 flip flops,  some gates + setup + clock adds to 10ns delay,
max freq is 1/10ns = 100MHz. If design runs at 80MHz (12.5ns period), excess
amount (2.5ns) is the slack.
- Static timing analyzer performs this through the entire design to determine
the maximum frequency, and to flag any errors (negative slack).

## Explain LUTs

- An LUT stores a predefined list of logic outputs for any combination of
inputs: LUTs with four to six input bits are widely used.
- One of the 2 fundamental components in FPGA (register/flipflop is the other)
- Can implement any boolean algebra equation (not actually gates inside an
FPGA!)
- LUTs get programmed based on the boolean algebra shit you wanna implement

## Explain SerDes

- Stands for serializer-deserializer
- Datasheet has transceivers (max rate Gb/s) very fast frequencies
- USB, HDMI, Lightning, all serial (parallel is old stuff, LPT, PCI)
- Parallel: many pins, limited speeds, low bandwidth, simple
- Serial: Less pins, faster, high bandwidth, more power, complicated
- HDMI runs at 12GHz
- Serial has clock embedded in the data, receiver extracts clock and data
separately, clock is used to sample the data
- Clock encoding schemes: need to guarantee data transitions, e.g. long data of
all 0's needs some transitions (an encoding scheme such as manchester, HDL,
8B/10B)

##  Explain AXI?

- Read up about AXI https://www.youtube.com/watch?v=p5RIVEuxUds
- Stands for Advanced Xtensible interface, a protocol used in the Advanced
Microcontroller Bus architecture developed by ARM. It is widely used in FPGA
and ASIC designs to maange communication between different blocks of an SoC. 
- It is high performance, low latency
- Key features include separate address/control and data phases, support for
unaligned data transfers, and efficient data handling. Supports various burts
types, data widths, and latency scenarios.

## Difference between Verification and Validation

## Why FPGA for camera/image stuff?

- FPGAs are a lot faster, they can run a lot of instructions at the same time
- Because they are fast, can process high bandwidth stuff like video in real
time, thus making it ideal for stuff like HDMI (Video + Audio)

## Comms protocols (UART/SPI/I2C)

- UART: Universal Asynchronous Receiver/Transmitter. Has baud rate (bits per
second), Number of data bits (7,8), Parity Bit (On/Off), Stop Bits (0, 1, 2),
Flow Control (None, On, Hardware). 

## What do you know about cpu architectures?

- MIPS, PicoMIPS, RISC V
- ELABORATE MORE WHEN I HAVE TIME

## Difference between CPU, MCU, FPGA, when to use which?

- ELABORATE MORE WHEN I HAVE TIME

