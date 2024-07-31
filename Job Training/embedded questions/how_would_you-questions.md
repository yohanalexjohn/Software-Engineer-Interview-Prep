# How would you questions

## Using the #define statement, how would you declare a manifest constant that returns the number of seconds in a year? Disregard leap years in your answer.

#define SECONDS_IN_YEAR (60UL * 60UL * 24UL * 365UL)

- UL = unsigned long 
- The result of SECONDS_IN_YEAR is > 16 bit integer due to overflow
- tell compiler to use long and only positive values

## Write the ‘standard’ MIN macro. That is, a macro that takes two arguments and returns the smaller of the two arguments.

#define MINI(A, B) ( (A) <= (B) ? (A) : (B) )

## I also use this question to start a discussion on the side effects of macros, e.g. what happens when you write code such as : least = MIN(*p++, b)

### Side Effects from *p++:

The expression *p++ involves two operations:
    1. Dereferencing p to get the value it points to (*p).
    2. Post-incrementing the pointer p (p++), which moves the pointer to the next element.

### Evaluation of MIN:

The macro will evaluate the expression *p++ twice* if *p++ is less than b. This means that p will be incremented twice:
1. The comparison ((*p++) < (b)).
2. Value selection ((*p++) : (b)).

### Side Effects and Problems

#### Double Increment:

If *p++ is indeed less than b, p will be incremented twice, which might not be the intended behavior. The pointer p will end up pointing to p + 2 instead of p + 1.

#### Unpredictable Behavior:

Depending on the initial value of p and the elements it points to, this could lead to skipping elements in the array or accessing unintended memory locations, resulting in unpredictable behavior or bugs that are hard to trace.

#### Potential Undefined Behavior:

Evaluating *p++ twice within the same statement can lead to undefined behavior according to the C standard, since the order of evaluation of subexpressions is not guaranteed.

### Proper Handling

To avoid such side effects, it's important to avoid writing expressions with side effects inside macros. Here’s how you can handle the MIN calculation more safely:

#### Separate the Operations:

Break down the expression to separate the side effects from the macro:
```c
int temp = *p++;
least = MIN(temp, b);
// Avoiding Macros for Such Operations:
// Consider using inline functions if you need to perform operations that could have side effects:

static inline int min(int a, int b) {
    return a < b ? a : b;
}

least = min(*p++, b);
```
### Conclusion
Macros can be powerful, but they come with risks, especially when dealing with expressions that have side effects such as pointer increments. Careful handling and understanding of the expanded macro code are essential to avoid unintended behavior and ensure the correctness of your program. Using inline functions is a safer alternative for complex operations.

# Using the variable a, write down definitions for the following:

Using the variable a, write down definitions for the following:

- An integer

- A pointer to an integer

- A pointer to a pointer to an integer

- An array of ten integers

- An array of ten pointers to integers

- A pointer to an array of ten integers

- A pointer to a function that takes an integer as an argument and returns an integer

- An array of ten pointers to functions that take an integer argument and return an integer.

The answers are:

- int a; // An integer
- int *a; // A pointer to an integer
- int **a; // A pointer to a pointer to an integer
- int a[10]; // An array of 10 integers
- int *a[10]; // An array of 10 pointers to integers
- int (*a)[10]; // A pointer to an array of 10 integers
- int (*a)(int); // A pointer to a function a that takes an integer argument and returns an integer
- int (*a[10])(int); // An array of 10 pointers to functions that take an integer argument and return an integer(a) An integer


## Embedded systems always require the user to manipulate bits in registers or variables. Given an integer variable a, write two code fragments. The first should set bit 3 of a. The second should clear bit 3 of a. In both cases, the remaining bits should be unmodified.

```c
#define BIT3 (0x01 << 3)

static int a;

void set_bit3(void){
    a |= BIT3;  
}

void clear_bit3(void){
    a &= ~BIT3;
}
```

## Embedded systems are often characterized by requiring the programmer to access a specific memory location. On a certain project it is required to set an integer variable at the absolute address 0x67a9 to the value 0xaa55. The compiler is a pure ANSI compiler. Write code to accomplish this task.

```c
volatile uint16_t *address;

// Create a pointer to the sepcific memory address 
address = (volatile uint16_t *)0x67a9;

*address = 0xaa55; // Set the value at this address 

```




