# String to integer atoi function

Implement atoi to convert a string to an integer.

The atoi function first discards as many whitespace characters as necessary
until the first non-whitespace character is found. Then, starting from this
character, takes an optional initial plus or minus sign followed by as many
numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral
number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid
integral number, or if no such sequence exists because either str is empty or
it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the
correct value is out of the range of representable values, the maximum integer
value (2147483647) or the minimum integer value (–2147483648) is returned.

```python
# Brute force
class Solution:
    def myAtoi(self, data: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        numbers = "0123456789"
        number_in_string = ""
        if data == " ":
            return 0

        for i, char in enumerate(data):
            if char == "-" and i == 0:
                number_in_string += "-"

            # if char.isnumeric():
            elif char in numbers:
                number_in_string += char
            
            elif char.isalpha():
                if i == 0:
                    return 0
                return int(number_in_string)

            else:
                if char == " " and i == 0 and len(data) == 0:
                    return 0
                elif char == " ":
                    continue
                return int(number_in_string)

        # Step 5: Clamp the integer within the 32-bit signed integer range
        if int(number_in_string) < INT_MIN:
            return INT_MIN
        if int(number_in_string) > INT_MAX:
            return INT_MAX
        return int(number_in_string)
# Example usage
solution = Solution()

print(solution.myAtoi("1234"))
print(solution.myAtoi("-42"))
print(solution.myAtoi("0-1"))
print(solution.myAtoi("1337c0d3"))
print(solution.myAtoi("\
                      1337c0d3"))
print(solution.myAtoi("words and 987"))
```

```python
# ideal solution 
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        i = 0
        n = len(s)
        number_in_string = ""

        # Step 1: Ignore leading whitespaces
        while i < n and s[i].isspace():
            i += 1

        # Step 2: Check for optional '+' or '-'
        if i < n and (s[i] == '+' or s[i] == '-'):
            number_in_string += s[i]
            i += 1

        # Step 3: Read in next the characters until the next non-digit character or the end of the input
        while i < n and s[i].isdigit():
            number_in_string += s[i]
            i += 1

        # Step 4: Convert to integer if number_in_string is not empty or just a sign
        if number_in_string == "" or number_in_string == "+" or number_in_string == "-":
            return 0

        num = int(number_in_string)

        # Step 5: Clamp the integer within the 32-bit signed integer range
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num

```
