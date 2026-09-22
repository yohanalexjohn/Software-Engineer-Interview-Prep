# Rob House

## Active recall

- Pattern: dynamic programming with choose/skip adjacent items.
- Algorithm: at each house, best is `max(skip current, rob current + best before previous)`.
- Keep two variables: `prev2` and `prev1`.
- Time: O(n). Space: O(1).
- Common mistake: adjacent houses cannot both be chosen, so greedy by largest value fails.

 dp[i] = max(
    dp[i - 1],        // skip current house
    dp[i - 2] + nums[i]   // rob current house
)

You’re given an array nums where nums[i] is the amount of money in house i.
You cannot rob two adjacent houses.
Return the maximum amount you can rob.

```text
Example:
nums = [1,2,3,1]

Output = 4

because:
rob house 0 -> 1
rob house 2 -> 3

total = 4
Another:
nums = [2,7,9,3,1]

Output = 12

```


```cpp
class Solution {
public:
    int rob(vector<int>& nums) {

        int twoBack {0};
        int previous{0};

        for(int money: nums)
        {
            int current =  std::max(previous, twoBack + money);

            twoBack = previous;
            previous = current;
        }

        return previous;
    }
};
```

