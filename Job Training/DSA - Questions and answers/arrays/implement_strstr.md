# Implement strstr

Returns the index of the first occurrence of needle in haystack, or –1
if needle is not part of haystack.

```python
# Brute force 2 pointer 
def solution(haystack: str, needle) -> bool:
    slow = 0
    fast = 0
    # print("Length of the haystack : ", len(haystack))
    # print("Length of the needle : ", len(needle))

    sub_string = [] 

    while fast < len(haystack):
        if slow < len(needle):
            if ((haystack[fast] == needle[slow]) ):
                slow += 1
                sub_string.append(haystack[fast])
                # print(sub_string)
            else:
                if((len(sub_string) != 0) and (haystack[fast - 1] == needle[slow - 1])):
                    # print(sub_string)
                    slow -= 1
                    fast -= 1
                    sub_string.pop(0) 
        fast += 1

    match_string = "".join(sub_string)
    print("match string returned ", match_string)

    if match_string == needle:
        return True

    return False

# Example usage
print(solution("hello", "ll"))  # Output: True
print(solution("hello", "llhshs"))  # Output: False 
print(solution("hello", "lo"))  # Output: True 
print(solution("hello", "he"))  # Output: True 

```
```python
def strstr(haystack, needle):
    # Edge case: if needle is an empty string, return 0
    if needle == "":
        return 0

    # Get lengths of both haystack and needle
    len_haystack = len(haystack)
    len_needle = len(needle)

    # Iterate through haystack
    for i in range(len_haystack - len_needle + 1):
        # Use two pointers to check for substring match
        j = 0
        while j < len_needle and haystack[i + j] == needle[j]:
            j += 1
        # If we've matched the whole needle
        if j == len_needle:
            return i

    # If needle is not found, return -1
    return -1

# Test cases
haystack = "Hello, world!"
needle = "world"
print(strstr(haystack, needle))  # Output: 7

needle = "Python"
print(strstr(haystack, needle))  # Output: -1

needle = "o"
print(strstr(haystack, needle))  # Output: 4

needle = ""
print(strstr(haystack, needle))  # Output: 0 (empty needle is considered to be found at the start)

```

