# Valid Number
Question:
Validate if a given string is numeric.

```python
def solution(data: str) -> bool:
    num = "0123456789"

    back = len(data) - 1
    front = 0
    spec_char_count = 0

    if len(data) == 0:
        return False 
    
    # Get rid of any trailing or starting whitespace
    if data[front] == " ":
        front +=1

    if data[back] == " ":
        back -=1

    while front < back:
        if spec_char_count > 1:
            return False

        if data[front].isalpha() or data[back].isalpha():
            return False
        
        if data[front] == " " or data[back] == " ":
            return False
        
        if data[front].isdigit() and data[back].isdigit():
            front += 1
            back -= 1 
            continue

        if data[front] == "." or data[back] == ".":
            if data[front] == "." and data[back] == ".":
                return False
            spec_char_count += 1
            front += 1
            back -= 1 

    return True

print(solution("123"))
print(solution(" 123"))
print(solution("123 "))
print(solution("1.23 "))
print(solution("1.2.3 "))
print(solution("1. 2.3 "))


    
```