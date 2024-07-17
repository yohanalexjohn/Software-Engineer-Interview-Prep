# Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.

## Example 1

Input: x = 121 \
Output: true \

Explanation: 121 reads as 121 from left to right and from right to left.

## Example 2

Input: x = -121 \
Output: false \
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

## Example 3

Input: x = 10 \
Output: false \
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

```python
# Brute Force - 01 
def solution(data: int) -> bool:
    # If the number is negative, it's not a palindrome
    if data < 0:
        return False

    temp_data = data
    digits = []
        
    # First for loop to extract digits and store in a list
    temp_data = data
    for _ in range(data):
        if temp_data == 0:
            break
        digits.append(temp_data % 10)  # Get the last digit
        temp_data //= 10               # Remove the last digit
    
    size_of_digits = len(digits)

    # Second for Loop to check if palindrome 
    for i in range(size_of_digits):
        if digits[i] != digits[size_of_digits - 1]:
            return False
        size_of_digits -= 1

    return True

# Example usage
print(solution(121))  # Output: True
print(solution(-121)) # Output: False
print(solution(10))   # Output: False
    
solution(1234)

```

```python
# Brute Force - 02  
def solution(data: int) -> bool:
    # If the number is negative, it's not a palindrome
    if data < 0:
        return False

    original = data
    digits = []

    # First for loop to count the number of digits
    temp_data = data
    num_digits = 0
    for _ in range(data):
        if temp_data == 0:
            break
        temp_data //= 10
        num_digits += 1

    # Second for loop to extract digits and store in a list
    temp_data = data
    for _ in range(num_digits):
        digits.append(temp_data % 10)  # Get the last digit
        temp_data //= 10               # Remove the last digit

    # Reverse the number using the digits list
    reversed_num = 0
    for i in range(num_digits):
        reversed_num = reversed_num * 10 + digits[i]

    # Compare the original number with the reversed number
    return original == reversed_num

# Example usage
print(solution(121))  # Output: True
print(solution(-121)) # Output: False
print(solution(10))   # Output: False
```

```python
# Real solution 
def solution(data: int) -> bool:
    # If data is negative, it cannot be a palindrome
    if data < 0:
        return False

    # Convert the integer to a string
    str_data = str(data)
    len_data = len(str_data)
    i = 0 
    while i < len_data:
        if str_data[i] == str_data[len_data - 1]:
            len_data -= 1
            i += 1
        else:
            return False

    return True  

# Example usage
print(solution(121))  # Output: True
print(solution(-121)) # Output: False
print(solution(10))   # Output: False
```
