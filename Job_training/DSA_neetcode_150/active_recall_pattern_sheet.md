# Amazon OA Active Recall Pattern Sheet

Use this as a quick recall sheet before doing new questions.

The aim is not to memorise full solutions. The aim is to recognise:

```text
This problem looks like X, so I should consider Y.
```

For each problem, recall these 4 things:

- Recognition clue
- Core idea
- Time / space
- Common mistake I made

## Daily review method before Amazon OA

### Daily 10-15 minute active recall warm-up

Do this before new problems.

1. Pattern recall, 5 minutes:
   - Read only the problem clue.
   - Say the likely pattern out loud.
   - Say why it is that pattern.
2. Syntax recall, 3 minutes:
   - Quick C++ checks: `unordered_map`, `priority_queue`, stack, binary-search midpoint, bit masks.
3. Algorithm recall, 5 minutes:
   - Pick 1-2 older problems.
   - Explain the mechanism in words only.
   - No coding unless the explanation shows a gap.
4. Then start new problems.

If I cannot explain the idea without looking, mark it for review.

### Sept 16 full recall session

Use 20-30 minutes before HackerRank practice:

- Mix old problems, not just yesterday's.
- Cover the full pattern sheet quickly.
- Say recognition clue, core idea, time, space, and common mistake.
- Mark weak patterns for one clean re-code.

### 30 minute coding recall

Pick 3 problems:

- 1 easy pattern I should solve cleanly.
- 1 medium pattern I often confuse.
- 1 embedded/C++ style question.

For each:

```text
2 minutes: explain brute force
2 minutes: explain better pattern
15-20 minutes: code
3 minutes: check edge cases and complexity
```

Do not learn a brand new hard pattern the day before the OA. Review mistakes,
syntax, edge cases, and recognition.

### Sept 17 morning of OA

Only do light warm-up:

- 5-10 minutes only.
- Two Sum.
- Binary Search.
- One stack or sliding-window question.
- One bit/byte extraction question.

Stop before getting tired.

## Pattern tracker

### Hashing / seen values

Problems:
Two Sum, Contains Duplicate, Valid Anagram, Group Anagrams, Longest Consecutive Sequence.

- Recognition clue: Need fast lookup, matching pair, seen before, count frequencies, group by same key.
- Core idea: Use `unordered_map` / `unordered_set`. Store the information needed so each lookup is close to O(1). For anagrams, use sorted string or character-count key.
- Time / space: Usually O(n), sometimes O(n k log k) for sorting words. Space O(n).
- Common mistake I made: Forgetting whether the map should store value -> index, count, or grouped list. Two Sum needs value -> index before inserting current. Contains Duplicate only needs a set. Do not overcomplicate with nested loops when lookup is enough.

### Two pointers

Problems:
Valid Palindrome, 3Sum, Container With Most Water, Two Sum sorted, Remove Duplicates, Rotate Array reverse sections.

- Recognition clue: Array/string has order, sorted input, compare both ends, move inward, avoid extra space.
- Core idea: Use left/right pointers. Move the pointer that can still improve the answer. For Remove Duplicates, use read/write pointers: read scans every value, write marks where the next unique value should go. For rotate array, reverse whole array, reverse first `k`, reverse remaining `n-k`.
- Time / space: Usually O(n), O(1) extra space except output.
- Common mistake I made: Confusing iterator and value: `nums.begin() + k` is an iterator, `nums[k]` is the value. Remember `k %= nums.size()` and handle empty input.

### Sliding window

Problems:
Longest Substring Without Repeating Characters.

- Recognition clue: Contiguous substring/subarray, grow and shrink a range, longest/shortest valid window.
- Core idea: Move `right` to include new values. Move `left` only when the window breaks the rule. Track best answer as the window changes.
- Set vs frequency map: For "no duplicates", an `unordered_set` is enough: erase from left until duplicate is gone. For "at most K distinct" or "counts matter", use an `unordered_map<char,int>` and shrink when the number of active keys breaks the rule.
- Time / space: O(n), space depends on map/set, usually O(k).
- Common mistake I made: Moving `left` too far or not far enough. Window problems are about a contiguous range, not choosing any elements.

### Running state / Kadane style

Problems:
Best Time to Buy and Sell Stock, Maximum Subarray, Maximum Product Subarray.

- Recognition clue: Best answer ending here, one pass, contiguous subarray, decide continue vs restart.
- Core idea: Keep enough state for the best answer ending at current index and a global result. For max product, track both min and max ending here because negatives can flip.
- Time / space: O(n), O(1).
- Common mistake I made: For max product, do not update `minProduct` then use the changed value for `maxProduct`. Save `oldMin` and `oldMax` first. Also compare against `current` so the subarray can restart.

### Dynamic programming / exact total

Problems:
Coin Change.

- Recognition clue: Minimum/maximum number of choices to reach an exact total, choices can be reused, and greedy may fail -> dynamic programming.
- Core idea: Let `dp[a]` be the fewest coins needed to make amount `a`. Base case: `dp[0] = 0`. For each amount and each coin, if `a - coin >= 0`, update `dp[a] = min(dp[a], dp[a - coin] + 1)`.
- Time / space: O(amount * number_of_coins) time, O(amount) space.
- Greedy counterexample: `coins = [1,3,4]`, `amount = 6`. Greedy takes `4 + 1 + 1 = 3` coins, but optimal is `3 + 3 = 2` coins.
- Common mistake I made: Sorting and repeatedly taking the largest coin is not generally correct unless the coin system has special structure.

### Intervals

Problems:
Merge Intervals, Insert Interval.

- Recognition clue: Ranges with start/end, overlapping intervals, or sorted non-overlapping intervals plus one new interval.
- Core idea: Merge Intervals sorts first, then compares each interval with `output.back()`. Insert Interval is already sorted, so use three phases: copy intervals before `newInterval`, merge overlaps into `newInterval`, push merged `newInterval`, then append intervals after.
- Time / space: Merge Intervals O(n log n) from sorting, O(n) output. Insert Interval O(n) time, O(n) output space.
- Common mistake I made: In Insert Interval, after merging into `newInterval`, remember to `output.push_back(newInterval)` before appending the remaining intervals.

### Prefix sum

Problems:
Subarray Sum Equals K, Product Except Self.

- Recognition clue: Need sum/product over ranges or "everything except current" without nested loops.
- Core idea: For sums, store previous prefix counts in a map. For product except self, use left product pass and right product pass instead of division.
- Time / space: O(n), usually O(n) space. Product Except Self can be O(1) extra excluding output.
- Common mistake I made: Product Except Self should not use division. Build output with prefix products first, then multiply by a running suffix product. Prefix/suffix was not right for Maximum Product Subarray because negatives and restart logic matter.

### Stack / monotonic stack

Problems:
Valid Parentheses, Min Stack, Daily Temperatures.

- Recognition clue: Need latest unresolved item, matching pairs, next greater/warmer value, undo in reverse order.
- Core idea: Use stack for LIFO. For Daily Temperatures, store indices waiting for a warmer future day. Pop while current value resolves the top.
- Time / space: O(n), O(n). Each index pushed once and popped once.
- Common mistake I made: For Daily Temperatures, stack stores indices, not temperatures. Pre-size output with zeros for days with no warmer future day. A `while` inside a `for` can still be O(n).

### Linked list

Problems:
Reverse Linked List, Linked List Cycle, Merge Two Sorted Lists.

- Recognition clue: Nodes and pointers, no random access, detect cycle, relink nodes.
- Core idea: Use pointer manipulation. Reverse with `prev`, `curr`, `next`. Cycle detection uses slow/fast pointers. Merge by walking two sorted lists.
- Time / space: Usually O(n), O(1) extra.
- Common mistake I made: Losing the rest of the list by changing `curr->next` before saving `next`. For cycle detection, move fast by two and slow by one.

### Grid / flood fill

Problems:
Number of Islands.

- Recognition clue: 2D grid + connected regions/components. Usually means DFS/BFS flood fill.
- Core idea: Outer row/column scan finds an unvisited `'1'`, so increment island count. Then flood fill from that cell through all 4-directionally connected land and mark each visited cell, for example change `'1'` to `'0'`, so the same island is not counted again.
- Time / space: O(rows * cols) time. DFS recursion stack can be O(rows * cols) worst case. BFS queue can also be O(rows * cols) worst case.
- Common mistake I made: The outer row/column scan is not BFS. It only finds possible starting points. The flood-fill traversal itself is the DFS or BFS.

### Binary search

Problems:
Binary Search, Find Minimum in Rotated Sorted Array, Search in Rotated Sorted Array, Search Range.

- Recognition clue: Sorted or partly sorted input, target better than O(n), can eliminate half.
- Core idea: Use `left`, `right`, `mid`. Compare against sorted side or boundary to decide which half still contains the answer. Rotated sorted arrays still have structure.
- Time / space: O(log n), O(1).
- Pattern pairing:
  - Find Minimum in Rotated Sorted Array: no target. Compare `nums[mid]` with `nums[right]`. If `nums[mid] > nums[right]`, minimum is right side, so `left = mid + 1`. Else minimum can be `mid`, so `right = mid`.
  - Search in Rotated Sorted Array: target exists or not. First identify which half is sorted. If target is inside the sorted half, keep that half. Otherwise discard it.
  - Search Range: run two biased binary searches. First occurrence moves `right = mid - 1` after finding target. Last occurrence moves `left = mid + 1` after finding target.
- Common mistake I made: Boundary updates depend on whether `mid` can still be the answer. Use `[left, right]` with `left <= right` when discarding `mid`; use `right = mid` only in patterns like find-min where `mid` may be answer. Midpoint should be `left + (right - left) / 2`, not `left + (right + left) / 2`. Do not return `-1` early in rotated search before identifying the sorted half.

### Heap / priority queue

Problems:
Kth Largest Element, Top K Frequent Elements.

- Recognition clue: Need top K, kth largest/smallest, repeatedly remove best/worst.
- Core idea: Use `priority_queue`. For top K, count first, then keep a heap of candidates. Min-heap of size K is useful for kth largest/top K.
- Time / space: Usually O(n log k) or O(n log n), space O(n) or O(k).
- Common mistake I made: For Kth Largest, keep a min-heap of size `k`: push each number, and if size exceeds `k`, pop the smallest. The heap top is the kth largest. Decide if popping removes useful or unwanted candidates.

### Advanced ordering / counting

Problems:
Count Smaller After Self.

- Recognition clue: Need how many smaller values appear to the right, not just whether one exists.
- Core idea: Brute force is nested loops. Better solutions need ordering plus counts, like merge-sort counting or Fenwick tree.
- Time / space: Brute force O(n^2), O(1) extra excluding output. Merge sort O(n log n), O(n).
- Common mistake I made: Storing only the minimum is not enough because it loses count information. This is lower priority than core OA patterns.

### Embedded: bit extraction

Problems:
Extract fields from register/byte, masks and shifts.

- Recognition clue: Need specific bits from a byte/register.
- Core idea: Shift right, then mask. Formula for `width` bits starting at bit `start`: `field = (value >> start) & ((1u << width) - 1)`. Keep constants readable.
- Time / space: O(1), O(1).
- Common mistake I made: Off-by-one bit positions. Remember whether bit 0 is the least significant bit.

### Embedded: endianness

Problems:
Parse bytes into 16-bit/32-bit values.

- Recognition clue: Bytes arrive in little-endian or big-endian order.
- Core idea: For little-endian 16-bit: low byte first, high byte shifted by 8. Cast before shifting if needed.
- Time / space: O(1), O(1).
- Common mistake I made: Mixing byte order. Little-endian means `value = low | (high << 8)`.

### Embedded: circular buffer

Problems:
Fixed-size queue, producer/consumer, UART/log samples.

- Recognition clue: Need fixed-size queue behaviour with wraparound.
- Core idea: Use head/tail indices and wrap with modulo. Decide full/empty rule clearly: either keep one slot empty, so full is `(head + 1) % capacity == tail`, or track `count`, so empty is `count == 0` and full is `count == capacity`.
- Time / space: Push/pop O(1), space O(n) for buffer.
- Common mistake I made: Confusing full and empty when `head == tail`. Keep one slot empty or track count.

### Embedded: byte parsing

Problems:
Frames, packets, commands, sensor data.

- Recognition clue: Need parse structured bytes safely.
- Core idea: Check length first, validate header/checksum/type, then extract fields. Avoid reading past buffer.
- Time / space: O(n) over packet length, O(1) extra usually.
- Common mistake I made: Parsing before checking length. Be explicit about signed/unsigned and byte order.

### C++ ownership

Problems:
`unique_ptr`, `shared_ptr`, `weak_ptr`, raw owning pointers, copy/move constructors, move semantics, RAII.

- Recognition clue: Class owns a raw resource (`new`, file handle, socket, mutex handle) -> think ownership semantics, Rule of Five / Rule of Zero.
- Core idea: RAII ties resource lifetime to object lifetime. Constructor/acquire, destructor/release. This gives deterministic cleanup even on early return or exceptions.
- Smart pointer ownership:
  - `unique_ptr`: exactly one owner, move-only, default choice for exclusive ownership.
  - `shared_ptr`: reference-counted shared ownership, resource freed when last owner is destroyed.
  - `weak_ptr`: non-owning observer of a `shared_ptr`; use it to break circular references such as parent owns child and child points back to parent.
- Copy vs move constructor:
  - Copy constructor creates a separate object from an lvalue. For real ownership it must deep-copy or be deleted.
  - Move constructor takes resources from an rvalue. It transfers handles/pointers and leaves the source valid but unspecified/empty.
- If a class owns `uint8_t* data`, the compiler-generated copy constructor does a shallow copy of the pointer.
- That means `Buffer b = a;` makes two `Buffer` objects point at the same heap allocation.
- No second 128-byte heap allocation is made by the copy.
- The local `Buffer` objects live on the stack only for their members: pointer + size.
- Danger: both destructors call `delete[]` on the same pointer -> double-delete / undefined behaviour.
- Safe move-only pattern:
  - delete copy constructor and copy assignment.
  - implement move constructor and move assignment.
  - move transfers pointer and size.
  - null out the source pointer after moving.
  - move assignment deletes the destination's existing resource before taking the new one.
  - include a self-move guard.
  - mark move operations `noexcept`.
- Time / space: O(1), O(1).
- Common mistake I made: Thinking `std::move` itself moves data. It only allows move constructor/assignment to run.

```cpp
class Buffer {
private:
    uint8_t* data;
    size_t size;

public:
    explicit Buffer(size_t size)
        : data(new uint8_t[size]), size(size) {}

    ~Buffer() {
        delete[] data;
    }

    Buffer(const Buffer&) = delete;
    Buffer& operator=(const Buffer&) = delete;

    Buffer(Buffer&& other) noexcept
        : data(other.data), size(other.size) {
        other.data = nullptr;
        other.size = 0;
    }

    Buffer& operator=(Buffer&& other) noexcept {
        if (this != &other) {
            delete[] data;
            data = other.data;
            size = other.size;
            other.data = nullptr;
            other.size = 0;
        }
        return *this;
    }
};
```

### C++ parameter passing and lookup

Problems:
Passing strings/vectors, map lookup, read-only inputs.

- Recognition clue: Function receives a large object or needs to check a key in `unordered_map`.
- Core idea:
  - `const T&`: no copy, read-only view of caller's object. Use for large inputs when the function only reads.
  - `T value`: makes a local copy for lvalues, but can move from rvalues. Use when the function needs its own modifiable copy or will store it.
  - Vector copy copies all elements, O(n). Vector move transfers the internal buffer pointer/size/capacity, usually O(1); source remains valid but unspecified.
  - `map.count(key)`: returns 0 or 1 for `unordered_map`, good for existence.
  - `map.find(key)`: returns iterator, good when I need the value without doing a second lookup.
- Time / space: `const T&` O(1). Copy O(n). Move usually O(1). Hash lookup average O(1).
- Common mistake I made: Using `count()` and then `operator[]`, which may do another lookup and can insert a default value. Use `find()` when I need to read the mapped value.

### C++ pointers, references, and concurrency keywords

Problems:
Pointer constness, references vs pointers, `volatile` vs `std::atomic`.

- Recognition clue: Interview asks what can be changed: the pointed-to value, the pointer variable, or both.
- Core idea:
  - `const int* p`: pointer to const int. Can change `p`; cannot change `*p`.
  - `int* const p`: const pointer to int. Cannot change `p`; can change `*p`.
  - `const int* const p`: const pointer to const int. Cannot change `p` or `*p`.
  - Reference: alias to an existing object, must be initialized, cannot be reseated, usually use when null is not valid.
  - Pointer: stores an address, can be null, can be reseated, use when optional/reassignable.
  - `volatile`: tells compiler the value may change outside normal program flow, useful for memory-mapped registers, but not thread synchronization.
  - `std::atomic`: gives thread-safe atomic operations and memory-order guarantees. Use for shared data between threads.
- Time / space: O(1), O(1).
- Common mistake I made: Reading declarations from the wrong side. Read around the `*`: `const int*` protects the value, `int* const` protects the pointer. Do not say `volatile` makes code thread-safe.

## Personal mistakes to check before submitting

- Did I initialise `result` correctly, usually from `nums[0]`?
- Did I handle empty input when the problem allows it?
- Did I use semicolons in `for` loops, not commas?
- Did I use `push_back`, not `push`, for `vector`?
- Did I return the answer with a semicolon?
- Did I include the right headers mentally: `vector`, `stack`, `unordered_map`,
  `algorithm`, `queue`?
- Did I explain brute force first, then the better pattern?
- Did I say both time and space complexity?

## Quick problem links

- [[arrays/two_sum]]
- [[arrays/valid_anagram]]
- [[arrays/group_anangrams]]
- [[arrays/product_of_array_excuding_self]]
- [[arrays/max_product_sub_array]]
- [[arrays/remove_duplicates]]
- [[arrays/rotate_array]]
- [[arrays/merge_intervals]]
- [[arrays/insert_interval]]
- [[arrays/number_of_islands]]
- [[arrays/find_minimum_in_rotated_sorted_array]]
- [[arrays/top_k_frequent_elements]]
- [[sliding_window/best_time_to_buy_and_sell_stock]]
- [[sliding_window/longest_substring_without_repeating_characters]]
- [[sliding_window/sub_array_sum_equals_k]]
- [[stack/valid_parentheses]]
- [[stack/kth_largest_element_in_an_array]]
- [[stack/minimum_stack]]
- [[stack/daily_temperatures]]
- [[two_pointer/valid_palindrome]]
- [[two_pointer/three_sum]]
- [[two_pointer/max_water_container]]
- [[linked lists/reverse_linked_list]]
- [[linked lists/has_cycle]]
- [[linked lists/merge_two_sorted_lists]]
- [[binary_search/binary_search]]
- [[binary_search/find_minimum_in_rotated_sorted_array]]
- [[binary_search/search_in_rotated_sorted_array]]
- [[binary_search/searchRange]]
- [circular_buffer](../embedded_questions/coding_questions_asked_interview/circular_buffer.md)
- [parse_16_bit_little_endian](bit_manipulation/parse_16_bit_little_endian.md)
