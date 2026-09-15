# Merge Intervals

Given an array of intervals where:

```cpp
intervals[i] = {start, end}

merge all overlapping intervals and return the merged result.

Example:

Input:
[[1,3],[2,6],[8,10],[15,18]]
Output:
[[1,6],[8,10],[15,18]]
Because:
[1,3] and [2,6]
overlap and become:
[1,6]

Another:

Input:
[[1,4],[4,5]]

Output:
[[1,5]]
```

```cpp
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if(intervals.empty()) return {};

        // cant compare if not sorted
        std::sort(intervals.begin(), intervals.end());

        std::vector<vector<int>> output.push_back(intervals[0]);

        for(int i(1); i < intervals.size(), i++){
            // Compare last merged interval in the output.
            if(intervals[i][0] <= ouptput.back()[1]){
                // current interval 0 and the prev here output 1 
                // wiped out
                // sorted so output here is smaller and getting expanded
                output.back()[1] = 
                    std::max(output.back()[1], intervals[i][1]);
            }
            else{
                output.push_back(intervals[i]);
            }
        }

        return output;
    }
};
```

