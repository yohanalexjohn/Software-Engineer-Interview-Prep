# Longest Palindromic Substring

## Active recall

- Pattern: expand around center.
- Algorithm: every palindrome has a center. Try each index as odd center and each gap as even center.
- Expand while left/right characters match, then update best range.
- Time: O(n^2). Space: O(1).
- Common mistake: even-length palindromes need a center between two characters.

@TODO

Given a string S, find the longest palindromic substring in S. You may assume
that the maximum length of S is 1000, and there exists one unique longest
palindromic substring.

```python
def solution(data:str) -> str:
```
