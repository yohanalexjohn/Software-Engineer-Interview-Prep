# Differences 
## Structure vs Unions

| Structure    | Unions      |
| --- | --- |
| Contains each of the named members  | Contains one of the named variables at any given time|
| Size is large enough to hold all members| Size is large enough to hold the largest member |
| Structure elements are of the same size| Unions elements can be of different sizes |

## malloc() and calloc()

| Malloc()                                         | calloc()                                                        |
| ------------------------------------------------ | --------------------------------------------------------------- |
| takes one argument malloc(a)                     | Takes two arguments calloc(b,c)                                 |
| Where a is the number of bytes                   | Where b is the no of objects and c is the size of those objects |
| Memory allocated contains garbage values         | It initialises the contains of block of memory to zero          |
| It allocates contiguous(shared) memory locations | Memory allocated is not contiguous                              |

## Pass by reference vs pass by value 

| Pass by reference | Pass by value |
| --- | --- |
| Pass a pointer to the value  | Pass a copy of the variable |
| Direct manipulation of the variable | Cannot Change the value of the original variable  |

## Arrays vs Pointers  

| Arrays                                                 | Pointers                                                                                             |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| Size is allocated space automatically                  | Explicitly assigned to point to an allocated space                                                   |
| It cannot be resized                                   | It can be sized using realloc()                                                                      |
| It cannot be reassigned                                | It can be reassigned                                                                                 |
| sizeof() returns number of bytes occupied by the array | Number of bytes used to store the pointer variable which depending the architecture can be different |

## Arrays vs Linked list  

| Arrays                                                                                 | Linked List                                                                                                         |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Repeated pattern of variables in contiguous storage                                    | Set of structures scattered through memory held together by pointers in each element that point to the next element |
| Move from one element to the next through a fixed constant integer in a repeatable way | Use the **next** pointer in each structure which says what the next element is                                      |

## Enums vs Macros  

| Enums                                             | Macros                                                                                                                                   |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| They are a list of named integer-valued constants | Abbreviations for lengthy and frequently used statements                                                                                 |
| Enums declare a type, hence can be type checked   | Types are not defined can be anything as the entire code is substituted by a single line. Only used as it is faster for control transfer |

## Enums vs Pre-processor defines  

| Enums | Defines |
| --- | --- |
| Have a default behaviour and type | value has to be explicitly defined  |
| local effect to the enum block | Global effect to the file
| Sizes are fixed for the enumeration variables | No size as its a text subsitution

## Array name and a pointer variable

| Array Name | Pointer variable |
| --- | --- |
| Fixed address and is not a variable  | pointer variable is a variable  |
| Array name cannot be initialised | Must be initialised  |
| Name begins with a constant | ++ and -- operators cannot be applied to it  |

## Array  of pointers and a pointer to an array 

| Array of pointers | Pointer to an array |
| --- | --- |
| int *array_name[size] | int ( *array_name)[size] |
| Size represents the row size | Size represents the column size |
| Space may be dynamic | space is dependent on the architecture |

## Constant Pointer  and a pointer to a constant  

| const char *p | char const *p | char* const p | const char * const p |
| --- | --- | --- | --- |
| p is a pointer to a const char | p is a pointer to a const char | p is a const pointer to a char | p is a const pointer to a const character |
| Cannot modify the character that p points to | Cannot modify the character that p points to  | Can modify the character that p points to | Cannot modify what P points to nor change what the character is |
| P can change what it points to  | P can change what it points to | Cannot change the pointer to point to itself or another character | Cannot modify what P points to nor change what the character is |

#### Examples
``` c
const char *p = "Hello";
*p = 'h'; // Error: cannot modify the value pointed to by p
p = "World"; // OK: can change the pointer to point to another character
```

``` c
char ch = 'A';
char * const p = &ch;
*p = 'B'; // OK: can modify the value pointed to by p
p = &anotherChar; // Error: cannot change the pointer itself
```

```c
const char ch = 'A';
const char * const p = &ch;
*p = 'B'; // Error: cannot modify the value pointed to by p
p = &anotherChar; // Error: cannot change the pointer itself
```

### Are the expressions *ptr ++ and ++ *ptr same?

| *ptr ++ | ++ *ptr |
| --- | --- |
| post - increment operatrion. The value of the ptr is used first and then incremented by 1 | The value of the ptr is used and added(pre -increment) by 1
| the value of the pointer changes by 1 or now points to the next pointer in the array  | The pointer remains unchanged

#### Example 
``` c
#include <stdio.h>

int main() {
    int arr[] = {10, 20, 30};
    int *ptr = arr;

    int a = *ptr++;  // a = 10, ptr now points to arr[1] (20)
    ptr = arr;       // Resetting ptr to the start of the array
    int b = ++*ptr;  // b = 11, arr[0] is now 11, ptr still points to arr[0]

    printf("a = %d, b = %d\n", a, b);  // Output: a = 10, b = 11

    return 0;
}
```

## compilers vs interpreters
| compilers | interpreters|
| --- | --- |
| Take the whole program as a whole and convert to object code before execution| Execute code line by line|
| All syntax errors can be caught before code execution | Errors are only caught during execution |


## Mutexes vs Semaphores

| Mutexes | Semaphores |
| --- | --- |
| Mutual exclusion | Signal and resource counting |
| The locking thread must unlock |  Any thread can signal and wait   |
| Binary can either be in a lock or unlocked state | Each time a thread is passed a count is decremented |
| Blocking state as if locked cant move till unlocked  | Blocks if counter is zero  |
| Can be recursive | Typically not recursive |
| Protect critical sections | Synhchronise access to resources or limit concurrent access |
| faster and lightweight simple lock and unlock  | Flexible as can handle multiple instances |


## MPU vs MCU

| MPU | MCU |
| -- | -- |
| Micro Processor Unit typically has a very powerful cpu | Contains a system on chip with hardware pheripheals like ram, rom, flash, watchdog timer, clock, adc  |
| Higher power consumption  | lower power consumption |
| more expensive | cheaper |
| can run more complex tasks | can run simpler task on products  |

## RTOS vs General OS

| RTOS | General OS |
| -- | -- |
| Provides deterministic and predictable timing for task execution. | Timing may be less predictable; not designed for strict real-time constraints. |
| Priority-based and deterministic scheduling algorithms. | Often uses non-deterministic, time-sharing scheduling. |
| Designed to handle interrupts with minimal latency and jitter. | May have higher latency in handling interrupts due to complex task scheduling. |
| Optimized for minimal resource usage and guaranteed timing. | Optimized for overall resource efficiency and user experience. |
| Used in embedded systems, industrial control, automotive, medical devices. | Used in desktop computers, servers, and general-purpose applications. |
| Often lacks a graphical user interface (GUI); primarily command-line or simple interfaces. | Typically provides a comprehensive GUI for user interaction. |
| Generally simpler to reduce overhead and ensure predictability. | More complex to support a wide range of applications and hardware.|




