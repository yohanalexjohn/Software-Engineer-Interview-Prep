# Number of elements to the right smaller than curr

## Active recall

- Pattern: count smaller elements to the right.
- Brute force algorithm: for each index, scan all elements to its right and count smaller values.
- Better algorithm: merge-sort counting or Fenwick tree with coordinate compression.
- Time: brute force O(n^2), optimized O(n log n). Space: O(n) for optimized approaches.
- Common mistake: tracking only the minimum to the right is not enough because the problem asks for a count.

Given an integer array nums, return an array answer such that:

```text 
answer[i]
is equal to the number of elements to the right of i that are smaller than nums[i].
Example:
Input:
nums = [5,2,6,1]

Output:
[2,1,1,0]
```


```cpp 
class Solution {
public:
    // Brute Force
    vector<int> countSmaller(vector<int>& nums) {

        vector<int> output;

        for(int i(0); i < nums.size(); i++)
        {
            int count(0);

            for(int j(i+1); j < nums.size(); j++)
            {
                if (nums[j] < nums[i])
                {
                    count++;
                }
            }
            output.push_back(count);
        }
        return output;
    }
};
```

```cpp 
class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();

        vector<pair<int, int>> indexed;
        indexed.reserve(n);

        for (int i = 0; i < n; ++i) {
            indexed.push_back({nums[i], i});
        }

        vector<int> counts(n, 0);
        vector<pair<int, int>> temp(n);

        mergeSort(indexed, temp, counts, 0, n - 1);

        return counts;
    }

private:
    void mergeSort(vector<pair<int, int>>& arr,
                   vector<pair<int, int>>& temp,
                   vector<int>& counts,
                   int left,
                   int right) {
        if (left >= right) {
            return;
        }

        int mid = left + (right - left) / 2;

        mergeSort(arr, temp, counts, left, mid);
        mergeSort(arr, temp, counts, mid + 1, right);

        merge(arr, temp, counts, left, mid, right);
    }

    void merge(vector<pair<int, int>>& arr,
               vector<pair<int, int>>& temp,
               vector<int>& counts,
               int left,
               int mid,
               int right) {
        int i = left;
        int j = mid + 1;
        int k = left;

        int smallerFromRight = 0;

        while (i <= mid && j <= right) {
            if (arr[j].first < arr[i].first) {
                temp[k++] = arr[j++];
                smallerFromRight++;
            }
            else {
                counts[arr[i].second] += smallerFromRight;
                temp[k++] = arr[i++];
            }
        }

        while (i <= mid) {
            counts[arr[i].second] += smallerFromRight;
            temp[k++] = arr[i++];
        }

        while (j <= right) {
            temp[k++] = arr[j++];
        }

        for (int x = left; x <= right; ++x) {
            arr[x] = temp[x];
        }
    }
};
```
