# Top K Frequent Elements

## Active recall

- Pattern: frequency count + top K.
- Algorithm: count with `unordered_map`, then use bucket sort by frequency or a heap.
- Bucket sort uses `buckets[count]` to store values with that frequency, then
  walks from high frequency down until `k` values are collected.
- Time: O(n) with buckets, O(n log k) with heap. Space: O(n).
- Common mistake: heap should compare frequency, not the raw value.

Recall prompt:

- Why can bucket indexes go up to `nums.size()`?
- What do I store in `bucket[count]`: values or counts?

Given an integer array `nums` and an integer `k`, return _the_ `k` _most frequent elements_. You may return the answer in **any order**.

**Example 1:**

**Input:** nums = [1,1,1,2,2,3], k = 2
**Output:** [1,2]

**Example 2:**

**Input:** nums = [1], k = 1
**Output:** [1]

**Constraints:**

- `1 <= nums.length <= 105`
- `-104 <= nums[i] <= 104`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is **guaranteed** that the answer is **unique**.

**Follow up:** Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.

## Solution

```python
def solution(data: List[int], k: int) -> List[int]:
    new_element = []
    repeating_element_count = {}

    if len(data) == 1:
        new_element.append(data[0])
        return new_element

    for i in range(len(data)):
        repeating_element_count[data[i]] = (
            (repeating_element_count[data[i]] + 1)
            if data[i] in repeating_element_count.keys()
            else 1
        )

    repeating_element_count = dict(
        sorted(repeating_element_count.items(), key=lambda item: item[1], reverse=True)
    )

    new_element = list(repeating_element_count.keys())

    return (data[:k]) if not new_element else new_element[:k]


print(solution([1, 1, 1, 2, 2, 2, 3], 2))
print(solution([1], 1))
print(solution([3, 0, 1, 0], 1))
print(solution([1, 2], 2))
print(
    solution(
        [
            3,
            2,
            3,
            1,
            2,
            4,
            5,
            5,
            6,
            7,
            7,
            8,
            2,
            3,
            1,
            1,
            1,
            10,
            11,
            5,
            6,
            2,
            4,
            7,
            8,
            5,
            6,
        ],
        10,
    )
)
```

```cpp 
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> frequencies;

        // Find the Frequencies of each elements 
        for(int i(0); i < nums.size(); i++ )
        {
            frequencies[nums[i]]++;
        }

        // NO element can appear more than the size of the nums 
        // So need n + 1 buckets 
        // need n+ 1 as the index is is itself the frequency
        // so if we are to inedex via frequency we need to have 
        // n + 1 space. 
        vector<vector<int>> buckets(nums.size() + 1);

        // group frequencies as buckets
        for(const auto& entry: frequencies)
        {
            int value = entry.first;
            int frequency = entry.second;

            buckets[frequency].push_back(value); // bucket[count].push_back(value), not push
        }

        vector<int> result;

        for(int frequency = buckets.size() - 1;
            frequency >= 0 && result.size() < k;
            --frequency)
        {
            for(int value : buckets[frequency])
            {
                result.push_back(value);

                if(result.size() == k) // stop inside the nested loop, exactly at k
                {
                    return result;
                }
            }
        }

        return result;
    }
};
```
