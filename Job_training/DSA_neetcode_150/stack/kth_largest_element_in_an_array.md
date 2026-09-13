# Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element.

```text 
Example:
nums = [3,2,1,5,6,4]
k = 2

Output = 5
```

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

