# Median of two sorted Arrays

## Active recall

- Pattern: binary search partition across two sorted arrays.
- Algorithm: binary search the smaller array so left partitions contain half the total elements.
- Correct partition when `leftA <= rightB` and `leftB <= rightA`.
- Odd total length returns max left. Even total length returns average of max left and min right.
- Time: O(log min(m, n)). Space: O(1).
- Common mistake: binary search the larger array; always search the smaller one.

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

## Example 1

nums1 = [1, 3] \
nums2 = [2]

The median is 2.0

## Example 2

nums1 = [1, 2] \
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

```python
# BST algorithm
def solution(array1: int, array2: int) -> int:

```
