# Longest substring containing at most two distinct characters.

## Active recall

- Pattern: sliding window with frequency map.
- Algorithm: expand right and count characters. While map has more than 2 active keys, shrink from left.
- Remove a key when its count reaches zero.
- Time: O(n). Space: O(1) because max distinct characters in the window is bounded.
- Common mistake: a set is not enough here because counts are needed when shrinking.

```text 
s = "eceba"
output = 3

"ece" contains only e and c

s = "ccaabbb"
output = 5

contains only a and b
```

```cpp
class Solution {
public:
    int lengthOfLongestSubstringTwoDistinct(string s) {
        int max_length{0};
        int left{0};

        std::unordered_map<char, int> count;

        for (int right{0}; right < s.size(); right++) {

            // Add current character into the window
            count[s[right]]++;

            // More than two distinct characters,
            // shrink the window from the left
            while (count.size() > 2) {
                count[s[left]]--;

                // Remove character only when there
                // are no copies left in the window
                if (count[s[left]] == 0) {
                    count.erase(s[left]);
                }

                left++;
            }

            max_length = std::max(
                max_length,
                right - left + 1
            );
        }

        return max_length;
    }
};
```
