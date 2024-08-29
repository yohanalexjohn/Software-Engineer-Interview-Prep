from typing import DefaultDict, List


class MinStack:
    def __init__(self):
        self.stack_nums = []

    def __isEmpty__(self) -> bool:
        return not self.stack_nums

    def push(self, val: int) -> None:
        self.stack_nums.append(val)

    def pop(self) -> None:
        # To call private method which only takes in the
        # refernce object dont have to pass in anythin
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
