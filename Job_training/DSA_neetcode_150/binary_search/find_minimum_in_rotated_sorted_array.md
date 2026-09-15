# Find Minimum in Rotated Sorted Array

You’re given a sorted array that has been rotated an unknown number of times.

```c++
Example:
[3,4,5,1,2]
The minimum is:
1

Another example:
[4,5,6,7,0,1,2]

Output:
0
```

since its sorted a binary search will make it faster to extract less time than o(n)

```cpp 
class Solution {
public:
    int findMin(vector<int>& nums) {

        int minimum = nums[0];
    
        while (left < right)
        {
            int middle = left + (right - left) / 2;

            if (nums[mid] > nums[right])
            {
                left = middle + 1;
            }
            else{
                right = mid; // not mid - 1 as mid might be the minimum
            }
        }

        return nums[left];
    }
};
```
