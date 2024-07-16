# What is a static function with its usage

Functions with **static** keyword prefixed to the function declaraion / definition. Called in the source code of the file. 

# What is the header file and its usage in C 

File containing defintions and prototypes of the function begin used in the program are called a header file.

# What are the valid places to have a "break"

Only appear in loop statements

# What is the method to save data in a stack data structure type

Data is stored in a stack using **FILO**. Only top of the stack is accessible at a given instance.  

Storing mechanism is **PUSH** and **POP**

# What is variable initialisation and why is it important ?

If the variable is not given an initial value it can lead to unpredictable outputs when used in computations

# What modifier is used to store 32768

Ints can only store between -32768 to 32767 to store 32768 use long int or unsigned int 

# What are preprocessor directives
Preprocessor directives are placed at the beginning of every C program. Library files are specified, declaration of constants

# What is the order of precedence with regards to operators in C
In C, the order of precedence of operators determines the sequence in which operations are performed in expressions. Operators with higher precedence are evaluated before those with lower precedence. When operators have the same precedence, associativity determines the direction of evaluation (left-to-right or right-to-left).

Here is a summary of the operators in C, ordered from highest to lowest precedence:

1. **Primary operators**:
	- [ ] (array subscript)
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
1. **Logical OR**:
	- ||
1. **Conditional (ternary) operator**:
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
• **Right-to-left**: =, +=, -=, *=, /=, %=, <<=, >>=, &=, ^=, |=, ? :, unary operators (like !, ~, ++, --, - (unary minus), + (unary plus)), cast, sizeof, _Alignof
  
Understanding the precedence and associativity of operators is crucial for writing correct and predictable C programs, as it dictates the order in which parts of an expression are evaluated.

## Examples
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

# C a middle level language and how does it access the memory structures similar to assembly language routines

## Using Pointers

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

## Example
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

# What are the advantages and disadvantages of using a  Heap
| Advantages | Disadvantages|
|--|--|
|Memory in this structure can be allocated and deallocated in any order | Slower than a stack |
|Heaps allow for quick access to the minimum or maximum element | Slower than a stack |