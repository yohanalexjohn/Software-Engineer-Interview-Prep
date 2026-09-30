# Largest Rectangle in Histogram

## Active recall

This is the same monotonic-stack family as Daily Temperatures:

- Daily Temperatures keeps decreasing unresolved temperatures; a warmer value
  pops them and uses index distance.
- Histogram keeps increasing bar indices; a shorter value pops taller bars and
  uses the distance between smaller boundaries as width.

For a popped height at index `bar`:

- current index `i` is the first smaller bar on the right;
- after popping, `st.top()` is the left boundary (smaller or equal with the strict `>` pop condition below);
- width is `i - st.top() - 1`, or `i` when the stack is empty;
- area is `heights[bar] * width`.

Process a sentinel height `0` after the input to flush all remaining bars.
Each index is pushed and popped once: O(n) time, O(n) space.

```cpp
int largestRectangleArea(const std::vector<int>& heights)
{
    std::stack<int> st;
    int best = 0;

    for (int i = 0; i <= static_cast<int>(heights.size()); ++i)
    {
        const int current =
            (i == static_cast<int>(heights.size())) ? 0 : heights[i];

        while (!st.empty() && heights[st.top()] > current)
        {
            const int height = heights[st.top()];
            st.pop();
            const int width = st.empty() ? i : i - st.top() - 1; // exclude both boundary bars
            best = std::max(best, height * width);
        }
        st.push(i);
    }
    return best;
}
```

## Do not confuse with Container With Most Water

Container height is limited by two chosen endpoints, which supports a
two-pointer argument. A histogram rectangle must fit under every bar in its
span, so its height is the minimum across the span. Endpoint-only max/min logic
misses interior limiting bars.

Equal-height detail: the `>` comparison keeps a nondecreasing stack of heights. An equal left boundary can limit this particular popped bar, but the earlier equal bar later recovers the full plateau width. A shorter current bar means a popped taller bar cannot extend farther right. The usual strict-smaller-left explanation assumes equal heights are consolidated; keep the tie rule consistent with the code.
