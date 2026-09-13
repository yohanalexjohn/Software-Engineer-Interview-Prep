# Valid Anagram

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

