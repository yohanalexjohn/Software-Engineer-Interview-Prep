# Daily Temperatures

Given an array temperatures, return an array where answer[i] 
tells you how many days you have to wait until a warmer temperature. 
If there is no future warmer day, use 0.

```text 
Example:
Input:
[73,74,75,71,69,72,76,73]

Output:
[1,1,4,2,1,1,0,0]
```

## Active recall

- Pattern: monotonic stack / next greater value.
- Store indices, not temperatures.
- When current temperature is warmer than the index on top of the stack, pop it and fill the wait distance.
- Each index is pushed once and popped once, so the nested `while` is still O(n).
- Pre-size output with zeros for days that never get a warmer future day.

```cpp 
class Solution {
public:
    // Brute Force
    vector<int> dailyTemperatures(vector<int>& temperatures) {

        // Default to 0 only populate for value days
        std::vector<int> output(temperatures.size(), 0);

        for(int i(0); i < temperatures.size(); i++)
        {
            for(int j(i + 1); j < temperatures.size(); j++)
            {
               if(temperatures[j] > temperatures[i])
               {
                    output[i] = j - i;
                    break;
               }
            }
        }

        return output;
    }
};
```

```cpp
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        std::vector<int>output(temperatures.size(), 0);

        std::stack<int>waiting;

        for(int i(0); i < temperatures.size(); i++)
        {
            // Compare against current and previous
            while(!waiting.empty() && (temperatures[i] > temperatures[waiting.top()]))
            {
                int previous_temp_index = waiting.top();
                waiting.pop();

                // how many days to wait
                output[previous_temp_index] = i - previous_temp_index;
            }

            waiting.push(i);
        }

        return output;
    }
};
```

## October 1 mistake and invariant

- Today's mistake: comparing the current value with a raw stack index. Always dereference the candidate: `days[stack.top()]`.
- Waiting indices are increasing; their temperatures are non-increasing. Equal temperatures do not resolve a warmer-day query.
- Time O(n), space O(n). See [[next_greater_element]] for the same stack with a different output.
