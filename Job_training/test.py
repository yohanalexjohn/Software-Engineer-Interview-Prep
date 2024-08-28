from typing import DefaultDict, List


def solution(s: str) -> bool:
    # Map the closing brackets to the opening
    # use closing instead of opening to determine
    # when to pop
    bracket_map = {"}": "{", ")": "(", "]": "["}

    stack = []

    for bracket in s:
        if bracket in bracket_map:
            top_element = stack.pop() if stack else "#"

            # If the bracket is a closing bracket and
            # if the popped element does not match the
            # opening of the bracket it is not the top_element
            # that should have popped
            if bracket_map[bracket] != top_element:
                return False

        else:
            # Append the opening bracket to the top of the
            # stack
            stack.append(bracket)

    return not stack


print(solution("[]"))
print(solution("([{}])"))
print(solution("["))
print(solution("[(])"))
print(solution("{[]}"))
