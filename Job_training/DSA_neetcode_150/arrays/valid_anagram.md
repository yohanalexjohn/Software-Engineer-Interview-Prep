# Valid Anagram

## Active recall

- Pattern: character frequency count.
- Algorithm: if lengths differ, return false. Count characters from first string and subtract for second.
- All counts must end at zero.
- Time: O(n). Space: O(1) for fixed lowercase alphabet, otherwise O(k).
- Common mistake: sorting works but is O(n log n); counting is cleaner for fixed alphabet.

```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {

        std::unordered_map<char, int>count;

        if(s.size() != t.size()) return false;

        for(int i(0); i < s.size(); i++)
        {
            count[s[i]]++;
            count[t[i]]--;
        }

        for(const auto& entery: count)
        {
           if(entery.second != 0)
           {
                return false;
           }
        }

        return true;
    }
};
```



```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        int count[26] = {};

        for (int i = 0; i < s.size(); ++i) {
            count[s[i] - 'a']++;
            count[t[i] - 'a']--;
        }

        for (int i = 0; i < 26; ++i) {
            if (count[i] != 0) {
                return false;
            }
        }

        return true;
    }
};
```
