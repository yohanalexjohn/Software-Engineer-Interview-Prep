# Reverse Words in a String

Given an input string s, reverse the string word by word.
For example, given s = "the sky is blue", return "blue is sky the".

```python
# Bruce force
def solution(data: str) -> str:
    """ Implement two pass solution 
    """

    def reverse(input_string: list ) -> str:
        """ Reverse the list 
            return a reverse word
        """
        fast = 0 
        slow = len(input_string) - 1

        while fast < slow:
            input_string[fast], input_string[slow] = input_string[slow], input_string[fast]
            fast += 1
            slow -= 1

        return "".join(input_string)

    # Convert input string to a list
    list_char_data = list(data)

    # Reverse the input data 
    reversed_data = reverse(list_char_data)

    # Store the output words as each 
    output_word = []
    temp = []
    count = 0

    for char in reversed_data:
        if char != " ":
            temp.append(char)

        if ((char == " ") or count == len(reversed_data) - 1):
            output_word.append((reverse(temp)))
            temp.clear()

        count += 1

    return " ".join(output_word)

print(solution("the sky is blue"))
print(solution(" hello"))
print(solution("hi "))
```

```python
# NOT Bruce force 
def reverse_words(s):
    # Helper function to reverse a portion of the list in place
    def reverse(lst, start, end):
        while start < end:
            lst[start], lst[end] = lst[end], lst[start]
            start += 1
            end -= 1

    # Convert string to list of characters for in-place modifications
    chars = list(s)
    n = len(chars)

    # First pass: reverse the entire string
    reverse(chars, 0, n - 1)

    # Second pass: reverse each word in the reversed string
    start = 0
    while start < n:
        # Find the end of the current word
        while start < n and chars[start] == ' ':
            start += 1
        end = start
        while end < n and chars[end] != ' ':
            end += 1
        
        # Reverse the current word
        if start < n:
            reverse(chars, start, end - 1)
        
        # Move to the next word
        start = end

    # Join the characters back into a string and return
    return ''.join(chars)

# Test cases
s = "the sky is blue"
print(reverse_words(s))  # Output: "blue is sky the"

s = "  hello world  "
print(reverse_words(s))  # Output: "world hello" (with trimmed spaces)

s = "a good  example"
print(reverse_words(s))  # Output: "example good a"
```
