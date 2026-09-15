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
                    output.push_back(j - i);
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
            while(!waiting.empty() && (temperature[i] > temperatures[waiting.top()]))
            {
                int previous_temp_index = waiting.top();
                waiting.pop();

                // how many days to wait
                output[previous_temp_index] = i - previous_temp_index;
            }

            waiting.push_back(i);
        }

        return output;
}
```

