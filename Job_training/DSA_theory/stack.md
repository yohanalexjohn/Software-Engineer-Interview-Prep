# Stack

## What is Stack

Linear Data structure that follows LIFO (Last in First Out)

Last Element inserted is the first to be popped out

## How to implement

Pointer to the top of the stack, aka the last element to be inserted
as we can access the element only on the top of the stack

## Types of stack data structure

1. Fixed Size Stack
2. Dynamic Size Stack

### Fixed Size Stack

Fixed size and cannot grow any further or shrink. If the stack is full any
element that is added causes an overflow error and if its under stack and an
element is removed an under stack error will occur

### Dynamic Size Stack

This stack can grow and reduce dynamically. If full can be added and grow and
vice versa. This type of stack is implemented using a linked list as it allows
for easy resizing.

## Basic Operation

- push()
- pop()
- top()
- isEmpty()
- isFull()

### Push Operation

Add an item to the stack

#### Algorithm for pushing

- Check if the stack is full
- if stack is full(top == size(stack) - 1), stack overflow no new element can
be added to the stack
- else if top = top + 1. Add the data to the top

### Pop Operation

Remove an element from the stack

#### Algorithm for the pop

- Check if stack is empty
- If top == -1 then stack underflow error and no element can be removed.
- Else top = top - 1. Return the stored top value to be read or deleted.

### Top Operation

Returns the top element of the stack

#### Algorithm for the top

- Check if the stack is empty.
- If empty (top == -1). Return None.
- Else return element stored at index = Top

### IsEmpty Operation

Returns a boolean of the stack empty status

#### Algorithm for the isEmpty

- Check for the value at the top of the stack
- If top == -1 then the stack is empty return true else false

### IsFull Operation

Returns a boolean of the stack full status

#### Algorithm for the isFull

- Check for the value at the top of the stack
- If the index value at top is at capacity (top == size(stack) - 1). The stack
is full and return true else false.

## Implementation

1. Using array

    - Push is implemented by incrementing the index and storing the element at
    the new index
    - Pop is implemented by returning the value stored at top index and then
    decrement the top index

2. Using Linked List

    - Push is implemented by creating a new node with the new data and the next
    pointer of the current top pointing to null changes to point to this new
    node.
    - Pop is implemented by first creating a temp node which is the root node.
    The root node next is the current node. The root node data is returned and
    the memory is freed which is the temp

### Using array

#### Advantages of array

1. Easy to implement
2. Memory is saved no pointers

#### Disadvantages of array

1. Not dynamic as the array is created with a fixed size at initialisation.
2. However can make dynamic if using lists in python or vectors in c++

#### Code in array

```c
#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <limits.h>
#include <stdlib.h>  // Include for dynamic memory allocation functions

#define STACK_CAPACITY 100  // Define a maximum capacity for the stack

// Structure of the stack data
typedef struct 
{
    int top;
    uint8_t size;
    int *array;
} Data;

// Initialize the stack with a given size
void createStack(Data* stack, uint8_t size) 
{
    stack->size = size;
    stack->top = -1;  // Empty stack

    // Allocate memory for the stack array
    stack->array = (int*)malloc(stack->size * sizeof(int));

    if (stack->array == NULL) {  // Check if memory allocation was successful
        printf("Memory allocation failed!\n");
        exit(EXIT_FAILURE);  // Exit if memory allocation fails
    }
}

// IsEmpty
bool isEmpty(Data* stack)
{
    return stack->top == -1;
}

// IsFull
bool isFull(Data* stack)
{
    return stack->top == stack->size - 1;
}

// Push data on stack
bool push(Data* stack, int data)
{
    if(isFull(stack))
    {
        return false;
    }

    stack->array[++stack->top] = data;
    printf("Pushed to the stack data: %d\n", data);

    return true;
}

// Pop data on stack
bool pop(Data* stack, int* data)
{
    if(isEmpty(stack))
    {
        return false;
    }

    // fixed size no free memory reset data on
    // current top by setting it to 0
    // set the new array top as the top value with 
    // data by decrementing data
    *data = stack->array[stack->top];
    stack->array[stack->top] = 0;
    stack->top--;

    return true;
}

// Driver program to test above functions
int main()
{
    Data stack; // Create a stack instance
    createStack(&stack, STACK_CAPACITY); // Initialize stack with defined capacity

    push(&stack, 10);
    push(&stack, 20);
    push(&stack, 30);

    int item;
    if (pop(&stack, &item)) {
        printf("%d popped from stack\n", item);
    } else {
        printf("Failed to pop from stack\n");
    }

    return 0;
}
```

### Using Linked List

#### Advantages of using Linked List

1. Dynamic group can grow and shrink accordingly

#### Disadvantages of using Linked List

1. Complexity increases
2. Extra memory due to pointers
3. Random access of data not possible

#### Code in Linked List

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>

// Create the data
typedef struct Data
{
    int data;
    struct Data* next;
}Data;

// Create a new node
Data* newNode(int data)
{
    Data* node = (Data*)malloc(sizeof(Data));

    if(!node)
    {
        printf("Memory Allocation failed");
        return NULL;
    }

    node->data = data;
    node->next = NULL;

    return node;
}

// IsEmpty. Dynamic so don't need to check if its
// full as we can just grow
bool isEmpty(Data* node)
{
    return (node == NULL);
}

// Push to the stack
bool push(Data** node, int data)
{
    Data* newTopNode = newNode(data);

    if(!newTopNode)
    {
        // Memory allocation failed
        return false;
    }

    // Link the old top node with the new node
    // Top is the first element
    newTopNode->next = *node;
    // Now make the top node the new node
    *node = newTopNode;

    return true;

}

// Pop to the stack
bool pop(Data** node, int* data)
{
    if(isEmpty(*node))
    {
        return false;
    }

    *data = (*node)->data;

    // Store the current root node
    Data* oldRoot =  *node;
    // Make the new root node the current root node next
    *node = (*node)->next;
    // Free the memory of the old root node
    free(oldRoot);

    return true;

}

// Driver program to test the above functions
int main() 
{
    Data* root = NULL;  // Initialize the stack root (top) as NULL

    // Test pushing to the stack
    push(&root, 10);
    push(&root, 20);
    push(&root, 30);

    // Test popping from the stack
    int poppedValue;
    if (pop(&root, &poppedValue)) {
        printf("%d popped from stack\n", poppedValue);
    } else {
        printf("Failed to pop from stack (stack might be empty)\n");
    }

    return 0;
}
```
