# Longest substring without repeating characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"  
Output: 3  
Explanation: The answer is "abc", with the length of 3. Example 2:

Input: "bbbbb"  
Output: 1  
Explanation: The answer is "b", with the length of 1. Example 3:
Input: "pwwkew"

Output: 3
Explanation: The answer is "wke", with the length of 3.  
Note that the answer must be a substring, "pwke" is a subsequence
and not a substring.

## Algorithm

Sliding Window algorithm consists of two pointers slow and fast. Fast increments via the main loop. The slow only increments here when there is a match. 


```python
for window_length in range(length_of_string):
	# If character is in the unique list
	# Update the start index count
	if input[window_length] in seen:
		# seen["get_char_for_fast_pointer_index"]
		start_of_index = max(
		start_of_index, seen[input[window_length]] + 1)
	# Update the unique element found with the index it was found 
	# from the original input 
	seen[input[window_length]] = window_length
	# Unique element found is the buffer size difference 
	count = max(count, window_length - start_of_index + 1)

return count
```