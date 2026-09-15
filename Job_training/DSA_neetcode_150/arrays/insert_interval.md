# Insert Interval

You’re given a sorted list of non-overlapping intervals and one new interval. 
Insert the new interval into the correct position, merging if necessary.

```text
Example:
intervals = [[1,3],[6,9]]
newInterval = [2,5]

Output:
[[1,5],[6,9]]
Another:
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

Output:
[[1,2],[3,10],[12,16]]
```

```cpp 
class Solution {
public:
    vector<vector<int>> insert(
        vector<vector<int>>& intervals,
        vector<int>& newInterval
    ) {

        vector<vector<int>> output;

        int i {0};

        // Find position to insert 
        while (i < intervals.size() && 
               intervals[i][1] < newInterval[0]){
            output.push_back(intervals[i]);
            i++;
        }

        // Position found to insert
        // Check for overlap
        // Fix for overlap and exit
        while (i < intervals.size() &&
               intervals[i][0] <= newInterval[1]){

            newInterval[0] =
                std::min(newInterval[0], intervals[i][0]);

            newInterval[1] = 
                std::max(newInterval[1], intervals[i][1]);

            i++;
        }

        // Add the merged/new interval
        output.push_back(newInterval);

        // fill the rest of the list if any
        while( i < intervals.size())
        {
            output.push_back(intervals[i]);
            i++;
        }

        return output;
    }
};
```
