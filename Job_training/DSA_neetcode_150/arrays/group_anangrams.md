# Group Anangrams

Given an array of strings strs, group all anagrams together into sublists. You
may return the output in any order.

An anagram is a string that contains the exact same characters as another
string, but the order of the characters can be different.

## Example 1

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

## Example 2

Input: strs = ["x"]

Output: /[/["x"]]

## Example 3

Input: strs = [""]

Output: /[/[""]]

```python
from typing import DefaultDict, List

def solution(strs: List[str]) -> List[List[str]]:
    # Use DefaultDict as it can handle first case 
    # Scenarios 
    ans = DefaultDict(list)
    for word in strs:
        # Algo sort the words first the sorted word
        # is the key to which the values will be the 
        # anagrams itself
        sorted_word = "".join(sorted(word))
        ans[sorted_word].append(word)

    # the list of the values as this has been sorted and 
    # calculated 
    return list(ans.values())


solution(["act", "pots", "tops", "cat", "stop", "hat"])
```

```cpp 
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        std::unordered_map<char, vector<string>>group;

        // Create unique keys
        for(int i(0) : strs.size())
        {
            // sort will sort the key and return void 
            // copy the key first
            string key = strs[i];
            std::sort(key.begin(), key.end());
            group[key].push_back(strs[i]);
        }

        std::vector<vector<string>> output;

        // extract the pairs
        for(const auto& pairs: group)
        {
            output.push_back(pairs.second);
        }

        return output;
    }
};
```
