# Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,  
"A man, a plan, a canal: Panama" is a palindrome. "race a car" is not a palindrome.

Example Questions Candidate Might Ask:

Q: What about an empty string? Is it a valid palindrome?  
A: For the purpose of this problem, we define empty string as valid palindrome.

```python
# Brute Force 
def solution(data: str) -> bool:
    clean_string = [] 

    for char in data.lower():
        if char.isalpha(): 
            clean_string.append("".join(char))
    
    # 2 pointer technique 
    start = 0
    end = len(clean_string) - 1

    print(clean_string)

    if end == 1:
        return True
    
    while start < end:
        if clean_string[start] == clean_string[end]:
            start += 1
            end -= 1
        else:
            return False

    return True

# Example usage
print(solution("A man, a plan, a canal: Panama")) # Output: True
print(solution("race a car")) # Output: False
print(solution("r")) # Output: False

```

```python
# 2 pointer but different 
def solution(data: str) -> bool:
    # Initialize two pointers
    left, right = 0, len(data) - 1
    
    while left < right:
        # Move the left pointer to the next alphanumeric character
        while left < right and not data[left].isalnum():
            left += 1
        # Move the right pointer to the previous alphanumeric character
        while left < right and not data[right].isalnum():
            right -= 1
        
        # Compare characters at the pointers, ignoring case
        if data[left].lower() != data[right].lower():
            return False
        
        # Move both pointers towards the center
        left += 1
        right -= 1
    
    return True

# Example usage
print(solution("A man, a plan, a canal: Panama")) # Output: True
print(solution("race a car")) # Output: False
print(solution("r")) # Output: False

```