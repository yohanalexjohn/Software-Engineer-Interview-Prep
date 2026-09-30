# Longest Repeating Character Replacement

## Active recall

- Keep character frequencies and `maxFreq`, the largest count of one character
  seen for the current/rightward window process.
- Replacements needed are `windowSize - maxFreq`.
- Expand right, update its frequency and `maxFreq`, then shrink while
  `windowSize - maxFreq > k`.
- Update the longest valid window after shrinking.
- Time O(n); space O(alphabet).

```cpp
int characterReplacement(const std::string& s, int k)
{
    std::array<int, 26> freq{};
    int left = 0;
    int maxFreq = 0;
    int best = 0;

    for (int right = 0; right < static_cast<int>(s.size()); ++right)
    {
        maxFreq = std::max(maxFreq, ++freq[s[right] - 'A']);

        while ((right - left + 1) - maxFreq > k)
        {
            --freq[s[left] - 'A'];
            ++left;
        }

        best = std::max(best, right - left + 1);
    }
    return best;
}
```

Connection: this is the same window skeleton as the zero-flip problem.
`zeroCount` directly counts required flips there; here
`windowSize - maxFreq` counts required replacements.
