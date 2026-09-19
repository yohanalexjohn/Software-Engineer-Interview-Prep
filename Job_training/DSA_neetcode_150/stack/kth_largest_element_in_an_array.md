# Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element.

```text 
Example:
nums = [3,2,1,5,6,4]
k = 2

Output = 5
```

## Active recall

- Pattern: top K / kth largest.
- Use a min-heap of size `k`.
- Push each number; if heap size becomes greater than `k`, pop the smallest.
- At the end, heap top is the kth largest.
- Time: O(n log k). Space: O(k).

```cpp 
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {

        // keep only the k largest values we've seen
        std::priority_queue<
            int,
            std::vector<int>,
            std::greater<int>
        > minHeap;

        for (int num : nums) {
            minHeap.push(num);

            if (minHeap.size() > k) {
                // pop removes the smallest in minHeap
                minHeap.pop();
            }
        }

        return minHeap.top();
    }
};
```
