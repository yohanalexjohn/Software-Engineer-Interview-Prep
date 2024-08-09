
# What are questions

## What is a static function with its usage

Functions with **static** keyword prefixed to the function declaraion / definition. Called in the source code of the file.

## What is the header file and its usage in C

File containing defintions and prototypes of the function begin used in the program are called a header file.

## What are the valid places to have a "break"

Only appear in loop statements

## What is the method to save data in a stack data structure type

Data is stored in a stack using **FILO**. Only top of the stack is accessible at a given instance.  

Storing mechanism is **PUSH** and **POP**

## What is variable initialisation and why is it important ?

If the variable is not given an initial value it can lead to unpredictable outputs when used in computations

## What modifier is used to store 32768

Ints can only store between -32768 to 32767 to store 32768 use long int or unsigned int

## What are preprocessor directives

Preprocessor directives are placed at the beginning of every C program. Library files are specified, declaration of constants

## What is the order of precedence with regards to operators in C

In C, the order of precedence of operators determines the sequence in which operations are performed in expressions. Operators with higher precedence are evaluated before those with lower precedence. When operators have the same precedence, associativity determines the direction of evaluation (left-to-right or right-to-left).

Here is a summary of the operators in C, ordered from highest to lowest precedence:

1. **Primary operators**:

   - \[ ] (array subscript)
   - ( ) (function call)
   - . (structure member)
   - -> (structure pointer)
   - ++ (postfix increment)
   - -- (postfix decrement)
   - ( ) (parentheses for grouping)

2. **Unary operators**:

   - \+ (unary plus)
   - \- (unary minus)
   - ! (logical NOT)
   - ~ (bitwise NOT)
   - ++ (prefix increment)
   - -- (prefix decrement)
   - \* (dereference)
   - & (address of)
   - sizeof (size in bytes)
   - _Alignof (alignment requirement)
   - typeof (type of a variable)

3. **Cast**:

   - (type)

4. **Multiplicative operators**:

   - \* (multiplication)
   - / (division)
   - % (modulus)

5. **Additive operators**:

   - \+ (addition)
   - \- (subtraction)

6. **Shift operators**:

   - \<< (left shift)
   - \>> (right shift)

7. **Relational operators**:

   - < (less than)
   - <= (less than or equal to)
   - \> (greater than)
   - \>= (greater than or equal to)

8. **Equality operators**:

   - == (equal to)
   - != (not equal to)

9. **Bitwise AND**:

   - &

10. **Bitwise XOR**:

    - ^

11. **Bitwise OR**:

    - |

12. **Logical AND**:

    - &&

13. **Logical OR**:

    - ||

14. **Conditional (ternary) operator**:

    - ? :

15. **Assignment operators**:

    - = (assignment)
    - += (add and assign)
    - -= (subtract and assign)
    - *= (multiply and assign)
    - /= (divide and assign)
    - %= (modulus and assign)
    - \<<= (left shift and assign)
    - \>>= (right shift and assign)
    - &= (bitwise AND and assign)
    - ^= (bitwise XOR and assign)
    - |= (bitwise OR and assign)

16. **Comma operator**:

    - ,

**Associativity**:

- Most binary operators (those that operate on two operands) are left-to-right associative.
- Assignment operators and the conditional operator are right-to-left associative.
  
Here’s a brief overview of the associativity rules:
  
• **Left-to-right**: *, /, %, +, -, <<, >>, <, <=, >, >=, \==, !=, &, ^, |, &&, ||, ,
• **Right-to-left**: =, +=, -=,*=, /=, %=, <<=, >>=, &=, ^=, |=, ? :, unary operators (like !, ~, ++, --, - (unary minus), + (unary plus)), cast, sizeof, _Alignof
  
Understanding the precedence and associativity of operators is crucial for writing correct and predictable C programs, as it dictates the order in which parts of an expression are evaluated.

### Examples

```c
#include <stdio.h>

int main() {
    int a = 1, b = 0, c = 1;
    
    if (a && b && c) {
        printf("All conditions are true.\n");
    } else {
        printf("At least one condition is false.\n");
    }

    return 0;
}
```

```c
#include <stdio.h>

int main() {
    int a, b, c;

    if (a = b = c = 1) {
        printf("Assignment successful and a is true.\n");
    } else {
        printf("Assignment failed or a is false.\n");
    }

    return 0;
}
```

## C a middle level language and how does it access the memory structures similar to assembly language routines

### Using Pointers

C provides a mechanism to work directly with memory addresses through pointers. Here’s a basic outline of how you can access memory-mapped I/O using pointers:

1. Declare a Pointer to the Desired Memory Location:

```c
volatile uint32_t *ptr = (volatile uint32_t *)0xADDRESS;
```

Replace 0xADDRESS with the actual memory address you want to access. The volatile keyword ensures that reads and writes through ptr are not optimized away by the compiler, which is crucial for memory-mapped I/O.

2. Read and write Operations:

- **Reading from the Memory Location:**

```c
uint32_t value = *ptr;
```

This writes new_value to the memory location pointed to by ptr.

### Example

Suppose you want to toggle an LED connected to a microcontroller via a memory-mapped register. Here’s how you might do it:

```c
#include <stdint.h>

// Define the base address of the GPIO port (hypothetical example)
#define GPIO_BASE_ADDRESS 0x40020000

// Register offset for GPIO data output register
#define GPIO_DATA_OFFSET 0x0

int main() {
    // Pointer to GPIO data output register
    volatile uint32_t *gpio_data = (volatile uint32_t *)(GPIO_BASE_ADDRESS + GPIO_DATA_OFFSET);

    // Enable or toggle an LED (hypothetical example)
    *gpio_data |= (1 << 10);  // Set bit 10 to turn on LED, 1 << 10 means shifting the binary number 1 ten positions to the left.
    // Or
    *gpio_data &= ~(1 << 10); // Clear bit 10 to turn off LED, ~(1 << 10) computes the bitwise NOT operation on 0000010000, resulting in 1111101111.

// For example, if gpio_data initially contains 0000010000000000, after *gpio_data &= ~(1 << 10);, it will be 0000000000000000, effectively turning off the LED connected to bit 10 of gpio_data.

    return 0;
}
```

**Considerations**

• **Type Safety:** Ensure that the type of pointer (uint32_t * in this example) matches the data width of the memory location you are accessing.

• **Volatility:** Use the volatile keyword to prevent the compiler from optimizing away accesses to memory-mapped I/O locations.

• **Memory Access:** Be cautious when accessing memory directly, as incorrect accesses can lead to system instability or crashes, especially on embedded systems.

By utilizing pointers and type casting in C, you can effectively access direct memory structures, enabling you to interact with hardware components or memory-mapped peripherals, which is essential for tasks like device drivers, embedded systems programming, and low-level system programming.

## What are the advantages and disadvantages of using a  Heap

| Advantages | Disadvantages|
|--|--|
|Memory in this structure can be allocated and deallocated in any order | Slower than a stack |
|Heaps allow for quick access to the minimum or maximum element | Slower than a stack |

## What are the uses of the keyword **static**

1. A variable declared within the body of a function and can maintain its value between function calls
2. A variable declared outside a function or within a module is not accessible to any other functions outside this module.
   Global only to that file
3. Functions declared static within the module are only accessible within that module and it is declared, defined and called within that module

## What does the work **const**

const : *read-only*

1. Used to define values that should not be changed after initialisation.

2. Function parameters: the function will not modify the parameter. This can be particularly useful for pointers or references to large data structures, improving performance by avoiding unnecessary copies.

```c
void processData(const int *data, int size) {
    // Cannot modify *data
    for (int i = 0; i < size; ++i) {
        printf("%d\n", data[i]);
    }
}
```

3. Compiler Optimisation probabilities as the data is not mutable

## what does the **volatile** keyword

1. A volatile variable is one that can change unexpectedly.
2. The compiler can make no assumptions about the value of the variable.
3. The optimizer must be careful to reload the variable every time it is used instead of holding a copy in a register.

Examples of volatile variables are:

1. Hardware registers in peripherals (e.g., status registers)
2. Non-stack variables referenced within an interrupt service routine.
3. Variables shared by multiple tasks in a multi-threaded application.

1. Can a parameter be both const and volatile? Explain your answer.
2. Can a pointer be volatile? Explain your answer.
3. What is wrong with the following function?:

```c
int square(volatile int *ptr)
{
return *ptr * *ptr;
}
```

The answers are as follows:

(a) Yes. An example is a read only status register. It is volatile because it can change unexpectedly. It is const because the program should not attempt to modify it.

(b) Yes. Although this is not very common. An example is when an interrupt service routine modifies a pointer to a buffer.

(c) This one is wicked. The intent of the code is to return the square of the value pointed to by *ptr. However, since*ptr points to a volatile parameter, the compiler will generate code that looks something like this:

```c
int square(volatile int *ptr)
{
 int a,b;
 a = *ptr;
 b = *ptr;
 return a * b;
}
```

Since it is possible for the value of *ptr to change unexpectedly, it is possible for a and b to be different. Consequently, this code could return a number that is not a square! The correct way to code this is:

```c
long square(volatile int *ptr)
{
 int a;
 a = *ptr;
 return a * a;
}
```

## if there are unsigned and signed int in a single conditional check between what happens

all ints (singed) are promoted to unsinged hence no negative values

## What are the problems with dynamic memory allocation in embedded systems?

### Memory Fragmentation

Description: Over time, dynamic memory allocation can lead to fragmentation, where free memory is split into small,
non-contiguous blocks.

Impact: Fragmentation can cause memory allocation requests to fail even when there is sufficient total free memory,
just not in a single contiguous block. This is particularly problematic in systems with limited memory resources.

### Unpredictable Allocation Times

Description: The time required to allocate or free memory dynamically can be unpredictable.

Impact: Embedded systems, especially those with real-time requirements, need predictable and deterministic behavior.
Unpredictable allocation times can lead to missed deadlines or erratic system behavior

### Memory Leaks

Description: Memory leaks occur when allocated memory is not properly deallocated, leading to a gradual increase in used memory.

Impact: Over time, memory leaks can exhaust available memory, leading to system crashes or malfunctions. Detecting and debugging
memory leaks can be particularly challenging in embedded systems.

### Increased Complexity

Description: Complexity dealing with dynamic memory allocation over static memory
Impact: This complexity can lead to bugs and make the system more difficult to develop, maintain, and test. The additional overhead
can also strain limited processing resources.

## What are the two types of semaphores

1. Counting Semaphores: Initial value greater than 1, fixed number of threads to access this resource simultaneously
2. Binary Semaphores: Value either 0 or 1 similar to mutex but different in behaviour

## what are the types of memory in embedded systems

- ROM: Non-volatile, read-only memory used for storing firmware and fixed code.

- Flash Memory: Non-volatile and electrically erasable, used for firmware and application storage.

- RAM: Volatile memory used for temporary data storage during operation. Includes SRAM and DRAM.

- NVRAM: Non-volatile and read-write memory used for frequent data updates that need to be retained across power cycles. Includes FRAM and MRAM.

- Cache Memory: High-speed, volatile memory used to speed up data access for the CPU.

- Registers: Fast, volatile memory located on the CPU, used for immediate data storage and processing.

## What are the different thread states in rtos

- Running: Actively being executed.
- Ready: Waiting to be executed.
- Blocked/Waiting: Awaiting an event or condition.
- Suspended: Temporarily paused.
- Terminated: Completed or terminated.
