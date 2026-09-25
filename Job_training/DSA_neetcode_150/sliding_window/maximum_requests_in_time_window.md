# Maximum Requests in a Time Window

## Active recall

- Pattern: sliding window over sorted timestamps.
- Goal: find the largest number of requests whose timestamps fit inside one
  window.
- Valid window: `requests[right] - requests[left] <= window`.
- Algorithm: advance `right`; while the window is too wide, advance `left`;
  update `answer = max(answer, right - left + 1)`.
- Time: O(n). Space: O(1).
- Common mistake: this is an observation/counting problem. It is not the same
  as implementing a rate limiter that rejects requests after `maxRequests`.

Recall prompt:

- What condition makes the window invalid?
- Am I counting the maximum existing requests, or enforcing a live limit?

```cpp
int maxRequestsInWindow(const vector<int>& requests, int window) {
    int left = 0;
    int best = 0;

    for (int right = 0; right < requests.size(); ++right) {
        while (requests[right] - requests[left] > window) {
            ++left;
        }

        best = max(best, right - left + 1);
    }

    return best;
}
```
