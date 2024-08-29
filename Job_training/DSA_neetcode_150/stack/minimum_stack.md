# Minimum Stack

Basically write your stack definitions

Design a stack class that supports the push, pop, top, and getMin operations.

- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element val onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

Each function should run in O(1) time.

## Example 1

```code
Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

Output: [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1
```

## Solution

```python
# Brute force
class MinStack:
    def __init__(self):
        self.stack_nums = []

    def __isEmpty__(self) -> bool:
        return not self.stack_nums

    def push(self, val: int) -> None:
        self.stack_nums.append(val)

    def pop(self) -> None:
        # To call private method which only takes in the
        # reference object don't have to pass in anything
        if self.__isEmpty__():
            return
        self.stack_nums.pop()

    def top(self) -> int:
        return self.stack_nums[-1] if not self.__isEmpty__() else None

    def getMin(self) -> int:
        return min(self.stack_nums)


minStack = MinStack()

minStack.push(1)
minStack.push(2)
minStack.push(0)

# Return 0
print(minStack.getMin())

minStack.pop()

# Return 2
print(minStack.top())

# Return 1
print(minStack.getMin())
```

```python
# Optimised

class MinStack:
    def __init__(self):
        # Two stacks one to calculate the current values
        # The other at each push to store the current 
        # Minimum of the stack
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # This operation is o(1) as only have to push 
        # to two separate stacks one value if had to be
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


minStack = MinStack()

minStack.push(1)
minStack.push(2)
minStack.push(0)

# Return 0
print(minStack.getMin())

minStack.pop()

# Return 2
print(minStack.top())

# Return 1
print(minStack.getMin())
```
