# Toolchain Files

- Consists of programming tools like compiler, linker, assembler, debugger
- Used in embedded systems to compile code to particular architecture
- CMAKE to automate the build and linking

## linker scripts

- A linker script is a text file used by the linker to control the memory
regions and layout of the executable
- Tells what sections are placed where in the .text , .bss and how much should
be allocated

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

## .bss section

- Contains uninitialised global and static variables  
- No space in ROM
- Initial value set to 0 so no space needed

## Memory regions

### ROM

- .text
- .data

### RAM

- .bss
- .stack ( used for functional call management )
- .heap ( Dynamically allocated memory during program execution )
