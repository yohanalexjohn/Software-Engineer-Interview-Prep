# Rotate Array

## Active recall

- Pattern: array rotation in-place.
- Algorithm: reduce `k %= n`, reverse whole array, reverse first `k`, reverse remaining `n-k`.
- Time: O(n). Space: O(1).
- Common mistake: not handling `k > n` or empty input.

Given an integer array nums, rotate the array to the right by k steps.

```text
nums = [1,2,3,4,5,6,7]
k = 3

Output:
[5,6,7,1,2,3,4]
```

```cpp 
class Solution { public:
    void rotate(vector<int>& nums, int k) {
        
        if (nums.empty()) return;

        int rotate_steps = k % nums.size();

        std::reverse(nums.begin(), nums.end());
        std::reverse(nums.begin(), nums.begin()+ rotate_steps);
        std::reverse(nums.begin() + rotate_steps, nums.end());
    }
};

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        if (nums.empty()) {
            return;
        }

        int n = nums.size();
        k %= n;

        reverseRange(nums, 0, n - 1);
        reverseRange(nums, 0, k - 1);
        reverseRange(nums, k, n - 1);
    }

private:
    void reverseRange(vector<int>& nums, int left, int right) {
        while (left < right) {
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;

            left++;
            right--;
        }
    }
};

std::swap(nums[left], nums[right]); // could use this to ignore temp
```
