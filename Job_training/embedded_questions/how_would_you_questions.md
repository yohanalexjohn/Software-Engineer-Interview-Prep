# How would you questions

## Using the #define statement, how would you declare a manifest constant that returns the number of seconds in a year? Disregard leap years in your answer

# define SECONDS_IN_YEAR (60UL *60UL* 24UL * 365UL)

- UL = unsigned long
- The result of SECONDS_IN_YEAR is > 16 bit integer due to overflow
- tell compiler to use long and only positive values

## Write the ‘standard’ MIN macro. That is, a macro that takes two arguments and returns the smaller of the two arguments

# define MINI(A, B) ( (A) <= (B) ? (A) : (B) )

## I also use this question to start a discussion on the side effects of macros, e.g. what happens when you write code such as : least = MIN(*p++, b)

###  Side Effects from *p++

The expression *p++ involves two operations:
    1. Dereferencing p to get the value it points to (*p).
    2. Post-incrementing the pointer p (p++), which moves the pointer to the next element.

### Evaluation of MIN

The macro will evaluate the expression *p++ twice* if *p++ is less than b. This means that p will be incremented twice:

1. The comparison ((*p++) < (b)).
2. Value selection ((*p++) : (b)).

### Side Effects and Problems

#### Double Increment

If *p++ is indeed less than b, p will be incremented twice, which might not be the intended behavior. The pointer p will end up pointing to p + 2 instead of p + 1.

#### Unpredictable Behavior

Depending on the initial value of p and the elements it points to, this could lead to skipping elements in the array or accessing unintended memory locations, resulting in unpredictable behavior or bugs that are hard to trace.

#### Potential Undefined Behavior

Evaluating *p++ twice within the same statement can lead to undefined behavior according to the C standard, since the order of evaluation of sub expressions is not guaranteed.

### Proper Handling

To avoid such side effects, it's important to avoid writing expressions with side effects inside macros. Here’s how you can handle the MIN calculation more safely:

#### Separate the Operations

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

#  Using the variable a, write down definitions for the following

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
- int [*a](10); // A pointer to an array of 10 integers
- int (*a)(int); // A pointer to a function a that takes an integer argument and returns an integer
- int (*a[10])(int); // An array of 10 pointers to functions that take an integer argument and return an integer(a) An integer

## Embedded systems always require the user to manipulate bits in registers or variables. Given an integer variable a, write two code fragments. The first should set bit 3 of a. The second should clear bit 3 of a. In both cases, the remaining bits should be unmodified

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

## Embedded systems are often characterized by requiring the programmer to access a specific memory location. On a certain project it is required to set an integer variable at the absolute address 0x67a9 to the value 0xaa55. The compiler is a pure ANSI compiler. Write code to accomplish this task

```c
volatile uint16_t *address;

// Create a pointer to the sepcific memory address 
address = (volatile uint16_t *)0x67a9;

*address = 0xaa55; // Set the value at this address 

```

## Implement a Circular/Ring Buffer in C

```c
#include <stdio.h>
#include <stdbool.h>

#define BUFFER_SIZE 8  // Define the size of the circular buffer

// Global circular buffer structure
struct CircularBuffer {
    int buffer[BUFFER_SIZE];
    int head;
    int tail;
    int max;  // Maximum size of the buffer
    bool full;
} cb;  // Global instance of the circular buffer

// Initialize the circular buffer
void circular_buffer_init() {
    cb.head = 0;
    cb.tail = 0;
    cb.max = BUFFER_SIZE;
    cb.full = false;
}

// Add an element to the buffer
void circular_buffer_put(int data) {
    cb.buffer[cb.head] = data;
    if (cb.full) {
        cb.tail = (cb.tail + 1) % cb.max;
    }
    cb.head = (cb.head + 1) % cb.max;
    cb.full = (cb.head == cb.tail);
}

// Get an element from the buffer
int circular_buffer_get(int *data) {
    int r = -1;

    if (!circular_buffer_empty()) {
        *data = cb.buffer[cb.tail];
        cb.tail = (cb.tail + 1) % cb.max;
        cb.full = false;
        r = 0;
    }

    return r;
}

// Check if the buffer is empty
bool circular_buffer_empty() {
    return (!cb.full && (cb.head == cb.tail));
}

// Check if the buffer is full
bool circular_buffer_full() {
    return cb.full;
}

// Get the number of elements in the buffer
int circular_buffer_size() {
    if (cb.full) {
        return cb.max;
    }

    if (cb.head >= cb.tail) {
        return cb.head - cb.tail;
    }

    return cb.max + cb.head - cb.tail;
}
```

## Reverse Linked List 

```c
#include <stdio.h>
#include <stdlib.h>

// ---------- Singly linked list ----------

typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* reverseSingly(Node* head)
{
    Node* prev = NULL;
    Node* temp;

    while (head != NULL)
    {
        temp = head->next;
        head->next = prev;
        prev = head;
        head = temp;
    }

    return prev;
}

Node* pushSingly(Node* head, int data)
{
    Node* node = malloc(sizeof(Node));
    node->data = data;
    node->next = head;
    return node;
}

void printSingly(Node* head)
{
    while (head != NULL)
    {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

// ---------- Doubly linked list ----------

typedef struct DNode {
    int data;
    struct DNode* next;
    struct DNode* prev;
} DNode;

DNode* reverseDoubly(DNode* head)
{
    DNode* temp = NULL;

    while (head != NULL)
    {
        temp = head->prev;
        head->prev = head->next;
        head->next = temp;
        head = head->prev;
    }

    if (temp != NULL)
        head = temp->prev;

    return head;
}

DNode* pushDoubly(DNode* head, int data)
{
    DNode* node = malloc(sizeof(DNode));
    node->data = data;
    node->prev = NULL;
    node->next = head;
    if (head != NULL)
        head->prev = node;
    return node;
}

void printDoubly(DNode* head)
{
    while (head != NULL)
    {
        printf("%d <-> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

// ---------- main ----------

int main(void)
{
    // Singly linked list: build 1 -> 2 -> 3 -> 4 -> NULL
    Node* sHead = NULL;
    for (int i = 4; i >= 1; i--)
        sHead = pushSingly(sHead, i);

    printf("Singly before: ");
    printSingly(sHead);

    sHead = reverseSingly(sHead);

    printf("Singly after:  ");
    printSingly(sHead);

    // Doubly linked list: build 1 <-> 2 <-> 3 <-> 4 <-> NULL
    DNode* dHead = NULL;
    for (int i = 4; i >= 1; i--)
        dHead = pushDoubly(dHead, i);

    printf("\nDoubly before: ");
    printDoubly(dHead);

    dHead = reverseDoubly(dHead);

    printf("Doubly after:  ");
    printDoubly(dHead);

    return 0;
}

single pass so time complixxit is o(n)
```

## Imagine you have declared a variable as static before main and you have assigned it the value 42. When you print it in main, it prints 0. Where would you start to look?

First suspect: the .data copy didn't happen, or copied the wrong thing. If the startup code's .data copy loop has a bug (wrong source address, wrong size, or it's missing entirely 
for a custom/modified linker script), initialized statics silently stay at whatever RAM happened to contain — often 0 if .bss zeroing ran, or garbage otherwise. Since it printed 
exactly 0, that's actually a strong clue it's zero-initialized via .bss, not garbage.

Check the linker script — is this variable actually landing in .data (as expected for an initialized static) or has it been mis-placed into .bss? A misconfigured or hand-edited 
linker script is a classic cause.

Check symbol/section markers — _sdata, _edata, _sidata (or vendor equivalents) must correctly bound the .data section for the copy loop to work; if these markers are wrong, the copy 
either copies nothing or copies the wrong region.

Check for multiple definitions / linkage collision — if there are two variables with the same name in different translation units (one static, one accidentally not, or vice versa) the linker might resolve to the wrong one.

Check initialization order relative to when you're printing — if this print happens in another static/global constructor (C++) or an early init function that runs before the .data copy completes, you'd see the pre-init value.

As a last resort, inspect the disassembly/map file — confirm the address the variable actually lives at, and check the .data copy loop is really covering that address range.

Good framing to say out loud: "A static local prints 0 instead of its initializer almost always points to the .data-copy step in startup, since 0 is what you'd get from .bss zeroing overriding or replacing it — so I'd start at the linker script and startup code before suspecting the C logic itself."

## Design embedded firmware to keep it testable 

- Ask if the implementation would change in runtime if so stick to compile time polymorphism design whic will be template based else run time optimisation using Interface

I'd choose between runtime and compile-time polymorphism based on the requirements. I'd consider virtual interfaces where runtime substitution and testability are valuable, while
using templates or simpler static abstractions where performance, memory usage and deterministic execution are more important.

## Copy between fragmented source and destination segments

Maintain independent cursors because source and destination boundaries rarely
line up:

- Source cursor: `srcIndex` chooses the source segment; `srcOffset` chooses the
  next byte inside that segment.
- Destination cursor: `dstIndex` chooses the destination segment;
  `dstOffset` chooses the next byte inside it. Do not combine these four
  values: source and destination boundaries advance independently.
- Remaining bytes in current segments:
  `srcRemaining = src[srcIndex].len - srcOffset` and
  `dstRemaining = dst[dstIndex].len - dstOffset`.
- Copy `chunk = min(srcRemaining, dstRemaining)` bytes, then advance both
  offsets by `chunk`.
- When `srcOffset == src[srcIndex].len`, increment `srcIndex` and reset
  `srcOffset = 0`. Do the equivalent independently for destination.
- Stop successfully when the requested byte count is copied. Fail or report a
  short copy if either side runs out first.
- If `src` is an array/pointer to segment structs, use `src[i].len`. Use
  `src[i]->len` only when each array element is itself a pointer.
- Skip or advance past zero-length segments so the loop always makes progress.

Each byte is copied once and each segment boundary is crossed once: O(bytes +
source segments + destination segments) time and O(1) extra space.

Recall prompt:

- Can I update all four cursor values correctly when only one segment ends?
