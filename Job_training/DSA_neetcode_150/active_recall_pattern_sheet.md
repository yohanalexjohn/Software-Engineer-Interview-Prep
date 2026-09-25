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
Two Sum, Contains Duplicate, Contains Nearby Duplicate, Valid Anagram, Group Anagrams, Longest Consecutive Sequence.

- Recognition clue: Need fast lookup, matching pair, seen before, count frequencies, group by same key.
- Core idea: Use `unordered_map` / `unordered_set`. Store the information needed so each lookup is close to O(1). For anagrams, use sorted string or character-count key. For Longest Consecutive, put all numbers in a set and only start counting at `num` when `num - 1` is missing. For Contains Nearby Duplicate, store the most recent index for each value and check `i - lastIndex <= k`.
- Time / space: Usually O(n), sometimes O(n k log k) for sorting words. Space O(n).
- Common mistake I made: Forgetting whether the map should store value -> index, last index, count, or grouped list. Two Sum needs value -> index before inserting current. Contains Duplicate only needs a set. Longest Consecutive should not start counting from every number; only count sequence starts. Do not overcomplicate with nested loops when lookup is enough.

### Two pointers

Problems:
Valid Palindrome, 3Sum, Container With Most Water, Two Sum sorted, Remove Duplicates, Rotate Array reverse sections.

- Recognition clue: Array/string has order, sorted input, compare both ends, move inward, avoid extra space.
- Core idea: Use left/right pointers. Move the pointer that can still improve the answer. For Remove Duplicates, use read/write pointers: read scans every value, write marks where the next unique value should go. For rotate array, reverse whole array, reverse first `k`, reverse remaining `n-k`.
- Time / space: Usually O(n), O(1) extra space except output.
- Common mistake I made: Confusing iterator and value: `nums.begin() + k` is an iterator, `nums[k]` is the value. Remember `k %= nums.size()` and handle empty input.

### Sliding window

Problems:
Max Average Subarray, Longest Substring Without Repeating Characters, Longest Substring With At Most K Distinct.

- Recognition clue: Contiguous substring/subarray, grow and shrink a range, longest/shortest valid window.
- Fixed-size window: window length is given, for example size `k`. Add the new right value, remove the value leaving on the left, update best after the first full window.
- Variable-size window: window length is discovered. Move `right` to include new values. Move `left` only when the window breaks the rule. Track best answer as the window changes.
- Minimum Size Subarray Sum: positive integers. Expand `right`; while
  `sum >= target`, record `minLength`, subtract `nums[left]`, and move `left`.
  Start `minLength = nums.size() + 1`; return `0` if unchanged.
- Maximum requests in a time window: sorted timestamps. Keep
  `requests[right] - requests[left] <= window`; shrink while too wide; answer
  is `right - left + 1`. This counts an observed maximum, not a live
  `maxRequests` rate limiter.
- Set vs frequency map: For "no duplicates", an `unordered_set` is enough: erase from left until duplicate is gone. For "at most K distinct" or "counts matter", use an `unordered_map<char,int>` and shrink when the number of active keys breaks the rule.
- Time / space: O(n), space depends on map/set, usually O(k).
- Common mistake I made: Moving `left` too far or not far enough. Window problems are about a contiguous range, not choosing any elements. If negative numbers are allowed and the task asks for exact sum count, normal sliding window may fail; think prefix sum + hashmap.

### Running state / Kadane style

Problems:
Best Time to Buy and Sell Stock, Maximum Subarray, Maximum Product Subarray.

- Recognition clue: Best answer ending here, one pass, contiguous subarray, decide continue vs restart.
- Core idea: Keep enough state for the best answer ending at current index and a global result. For stock, `right` always advances and `left` only jumps when `right` finds a new lower price. For max product, track both min and max ending here because negatives can flip.
- Time / space: O(n), O(1).
- Common mistake I made: For Maximum Product Subarray, do not update `minProduct` then use the changed value for `maxProduct`. Save `oldMin` and `oldMax` first. Compare `current`, `oldMax * current`, and `oldMin * current` so the subarray can restart. Initialise from `nums[0]`, not `0`, because all values may be negative.

### Dynamic programming

Problems:
Climbing Stairs, House Robber, Coin Change, Unique Paths / Grid Paths.

- Recognition clue: A bigger answer is built from smaller repeated subproblems. Usually asks for count ways, min/max cost, best total, or choices under constraints.
- What DP means: Dynamic programming stores answers to subproblems so the same work is not recomputed. It does not always require a `dp[]` array; sometimes two variables, a hash map, or the call stack plus memo table is enough.
- Five-part framework:
  - State: what does one subproblem mean? Example: `dp[i]`, `dp[a]`, or `dp[row][col]`.
  - Base case: what answer is already known before the recurrence starts?
  - Recurrence / transition: how do smaller solved states create the next answer?
  - Calculation order: which states must be solved first?
  - Final answer: which state do I return?
- Top-down vs bottom-up:
  - Top-down: write recursive meaning first, then memoize repeated calls.
  - Bottom-up: fill base cases first, then iterate in an order where previous states are ready.
- Space optimisation: If each state only needs the last 1-2 states, use rolling variables instead of the full table.
- Common mistake I made: Trying to force every DP into the same shape. First define the state in plain English, then choose recursion, table, or rolling variables.

#### DP pattern: Climbing Stairs

Problems:
Climbing Stairs.

- Recognition clue: Count ways to reach step `n`, can move `1` or `2` at a time.
- State: `dp[i]` = number of ways to reach step `i`.
- Base case: `dp[0] = 1`, `dp[1] = 1`.
- Recurrence: `dp[i] = dp[i - 1] + dp[i - 2]`.
- Order: left to right from small steps to big steps.
- Final answer: `dp[n]`.
- Time / space: O(n) time. O(n) table or O(1) rolling space.
- Common mistake I made: This is not about greedy jumps. It counts all valid paths, so both previous states contribute.

```cpp
int climbStairs(int n) {
    int twoBack = 1; // ways to reach step 0
    int oneBack = 1; // ways to reach step 1

    for (int step = 2; step <= n; ++step) {
        int current = oneBack + twoBack;
        twoBack = oneBack;
        oneBack = current;
    }

    return oneBack;
}
```

Active recall:
- What does `dp[i]` mean?
- Why do I add `i - 1` and `i - 2`?
- Why can this become two variables?

#### DP pattern: House Robber

Problems:
[[dynamic_programming/rob_house|House Robber]].

- Recognition clue: Max total, choose or skip items, cannot choose adjacent houses.
- State: `dp[i]` = best money using houses up to index `i`.
- Base case: before any house, best is `0`. Rolling variables can start as `twoBack = 0`, `previous = 0`.
- Recurrence: `current = max(previous, twoBack + money)`.
- Take-vs-skip framing: `previous` means skip current house. `twoBack + money` means rob current house, so the previous adjacent house cannot be used.
- Order: scan left to right.
- Final answer: `previous` after processing all houses.
- Time / space: O(n) time, O(1) space.
- Common mistake I made: Do not use Coin Change logic here. House Robber is not `dp[current - coin] + 1`; it is take current vs skip current.

```cpp
int rob(vector<int>& nums) {
    int twoBack = 0;
    int previous = 0;

    for (int money : nums) {
        int current = max(previous, twoBack + money);
        twoBack = previous;
        previous = current;
    }

    return previous;
}
```

Active recall:
- What does skip current mean?
- Why does rob current use `twoBack`, not `previous`?
- Why does greedy largest-house fail?

#### DP pattern: Coin Change

Problems:
Coin Change.

- Recognition clue: Minimum number of reusable choices to reach an exact amount. Greedy largest-first may fail.
- State: `dp[a]` = fewest coins needed to make amount `a`.
- Base case: `dp[0] = 0`; all other amounts start as impossible / infinity.
- Recurrence: for every coin that fits, `dp[a] = min(dp[a], dp[a - coin] + 1)`.
- Meaning of `dp[current - coin] + 1`: solve the remaining amount first, then add the coin I just chose.
- Order: bottom-up loops through every current amount `1..amount`; for each current amount, try all coins that fit.
- Final answer: `dp[amount]`, or `-1` if still impossible.
- Time / space: O(amount * number_of_coins) time, O(amount) space.
- Greedy counterexample: `coins = [1,3,4]`, `amount = 6`. Greedy gives `4 + 1 + 1 = 3`; DP finds `3 + 3 = 2`.
- Common mistake I made: This is not `previous` / `twoBack`. Coin Change looks backward by each coin value: `current - coin`.

For `coins = [1,3,4]`, `dp[6]` checks:
- coin `1`: `dp[6 - 1] + 1 = dp[5] + 1`
- coin `3`: `dp[6 - 3] + 1 = dp[3] + 1`
- coin `4`: `dp[6 - 4] + 1 = dp[2] + 1`

```cpp
int coinChange(vector<int>& coins, int amount) {
    const int INF = amount + 1;
    vector<int> dp(amount + 1, INF);
    dp[0] = 0;

    for (int current = 1; current <= amount; ++current) {
        for (int coin : coins) {
            if (current - coin >= 0) {
                dp[current] = min(dp[current], dp[current - coin] + 1);
            }
        }
    }

    return dp[amount] == INF ? -1 : dp[amount];
}
```

Active recall:
- What does `dp[a]` store?
- Why is `dp[0] = 0`?
- For `dp[6]` with `[1,3,4]`, which previous states are checked?

#### DP pattern: Unique Paths / Grid Paths

Problems:
Unique Paths, Grid Paths.

- Recognition clue: Count paths through a grid when movement is only right/down or similar restricted directions.
- State: `dp[row][col]` = number of ways to reach that cell.
- Base case: top row is all `1` because there is only one way to keep moving right. Left column is all `1` because there is only one way to keep moving down.
- Recurrence: `dp[row][col] = dp[row - 1][col] + dp[row][col - 1]`.
- Order: fill top-left to bottom-right so top and left neighbors already exist.
- Final answer: bottom-right cell, `dp[rows - 1][cols - 1]`.
- Time / space: O(rows * cols) time. O(rows * cols) table, or O(cols) rolling row.
- Common mistake I made: Bottom-up grid DP does not need DFS. We are not exploring paths one by one; we are counting ways from already-solved neighboring states.

```cpp
int uniquePaths(int rows, int cols) {
    vector<vector<int>> dp(rows, vector<int>(cols, 1));

    for (int row = 1; row < rows; ++row) {
        for (int col = 1; col < cols; ++col) {
            dp[row][col] = dp[row - 1][col] + dp[row][col - 1];
        }
    }

    return dp[rows - 1][cols - 1];
}
```

Active recall:
- Why are the top row and left column `1`?
- Why fill top-left to bottom-right?
- Why is this not DFS in the bottom-up solution?

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
- Core idea: For sums, store previous prefix counts in a map. At index `i`, if current prefix is `sum`, then any previous prefix `sum - k` forms a subarray ending at `i` with sum `k`. For product except self, use left product pass and right product pass instead of division.
- Time / space: O(n), usually O(n) space. Product Except Self can be O(1) extra excluding output.
- Common mistake I made: Initialise prefix count with `{0: 1}` so a subarray starting at index `0` is counted. Product Except Self should not use division. Build output with prefix products first, then multiply by a running suffix product. Prefix/suffix was not right for Maximum Product Subarray because negatives and restart logic matter.

### Stack / monotonic stack

Problems:
Valid Parentheses, Longest Valid Parentheses, Min Stack, Daily Temperatures.

- Recognition clue: Need latest unresolved item, matching pairs, next greater/warmer value, undo in reverse order.
- Core idea: Use stack for LIFO. For Daily Temperatures, store indices waiting for a warmer future day. Pop while current value resolves the top. For Longest Valid Parentheses, store indices and start with sentinel `-1`; when a `)` empties the stack, push its index as the new invalid boundary.
- Time / space: O(n), O(n). Each index pushed once and popped once.
- Common mistake I made: For Daily Temperatures, stack stores indices, not temperatures. For Longest Valid Parentheses, length is `i - stack.top()` after popping a matched `(`; do not store only characters, because lengths need indices. A `while` inside a `for` can still be O(n).

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
Binary Search, Search Insert Position, Find Minimum in Rotated Sorted Array, Search in Rotated Sorted Array, Search Range.

- Recognition clue: Sorted or partly sorted input, target better than O(n), can eliminate half.
- Core idea: Use `left`, `right`, `mid`. Compare against sorted side or boundary to decide which half still contains the answer. Rotated sorted arrays still have structure.
- Time / space: O(log n), O(1).
- Pattern pairing:
  - Search Insert Position: find the first index where `nums[index] >= target`. Common inclusive version: `left = 0`, `right = nums.size() - 1`, `while (left <= right)`, discard `mid`, and return `left` when not found. Exclusive lower-bound version uses `right = nums.size()` and `left < right`.
  - Find Minimum in Rotated Sorted Array: no target. Compare `nums[mid]` with `nums[right]`. If `nums[mid] > nums[right]`, minimum is right side, so `left = mid + 1`. Else minimum can be `mid`, so `right = mid`.
  - Search in Rotated Sorted Array: target exists or not. First identify which half is sorted. If target is inside the sorted half, keep that half. Otherwise discard it.
  - Search Range: run two biased binary searches. First occurrence moves `right = mid - 1` after finding target. Last occurrence moves `left = mid + 1` after finding target.
- Common mistake I made: Boundary updates depend on whether `mid` can still be the answer. Use `[left, right]` with `left <= right` when discarding `mid`; use `right = mid` only in patterns like find-min where `mid` may be answer. Midpoint should be `left + (right - left) / 2`, not `left + (right + left) / 2`. Do not return `-1` early in rotated search before identifying the sorted half.

### Heap / priority queue

Problems:
Kth Largest Element, Top K Frequent Elements.

- Recognition clue: Need top K, kth largest/smallest, repeatedly remove best/worst.
- Core idea: Use `priority_queue` or bucket sort. For Top K Frequent, build a frequency map, put each value into `bucket[count]`, then traverse buckets from high frequency down. Min-heap of size K is useful for kth largest/top K.
- Time / space: Top K Frequent bucket sort is O(n), O(n). Heap versions are usually O(n log k) or O(n log n), space O(n) or O(k).
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
- Core idea: Single bit uses direct mask. Multi-bit field shifts right, then masks. Formula for `width` bits starting at bit `start`: `field = (value >> start) & ((1u << width) - 1)`. Status byte example: bit0 `POWER_ON`, bit1 `ERROR`, bits2-4 `MODE`, bit5 `CONNECTED`; `0b00110101` gives power true, error false, mode `5`, connected true.
- Time / space: O(1), O(1).
- Common mistake I made: Off-by-one bit positions. Remember whether bit 0 is the least significant bit.

### Embedded: endianness

Problems:
Parse bytes into 16-bit/32-bit values.

- Recognition clue: Bytes arrive in little-endian or big-endian order.
- Core idea: Place each byte into the correct significance position. For little-endian 16-bit: low byte first, high byte shifted by 8. For 32-bit big-endian `12 34 56 78`, result is `0x12345678`; little-endian byte order for that value is `78 56 34 12`. Cast to `uint32_t` before wide shifts.
- Time / space: O(1), O(1).
- Common mistake I made: Mixing byte order. Little-endian means `value = low | (high << 8)`.

### Embedded: circular buffer

Problems:
Fixed-size queue, producer/consumer, UART/log samples.

- Recognition clue: Need fixed-size queue behaviour with wraparound.
- Core idea: Use head/tail indices and wrap with modulo. Reserved-slot approach: `head` is next write, `tail` is next read, empty is `head == tail`, full is `(head + 1) % capacity == tail`, usable capacity is `N - 1`. Alternative: track `count`, so empty is `count == 0` and full is `count == capacity`.
- Time / space: Push/pop O(1), space O(n) for buffer.
- Common mistake I made: Confusing full and empty when `head == tail`. Keep one slot empty or track count.

### Embedded: byte parsing

Problems:
Frames, packets, commands, sensor data.

- Recognition clue: Need parse structured bytes safely.
- Core idea: Check length first, validate header/checksum/type, then extract fields. For `HEADER | LENGTH | PAYLOAD | CHECKSUM`, check minimum size, header `0xAA`, payload length `0..8`, exact packet size, checksum over payload, zero-length payload, extra bytes, and truncated bytes. Full-vector validation can be direct; streaming UART parsing benefits from persistent `HEADER -> LENGTH -> PAYLOAD -> CHECKSUM` state.
- Time / space: O(n) over packet length, O(1) extra usually.
- Common mistake I made: Parsing before checking length. Be explicit about signed/unsigned and byte order.

### Embedded: intermittent crash memory diagnostics

Problems:
Stack overflow, heap corruption, buffer overrun, occasional HardFault/reset on real hardware.

- Full note: [memory_corruption_diagnostics](../embedded_questions/memory_corruption_diagnostics.md)
- Recognition clue: Crash only happens sometimes, often after longer runtime, different task timing, larger input, or ISR/RTOS load.
- Core idea: Preserve evidence first, then prove what memory was overwritten.
- Recall checklist: stack fill pattern/high-water mark, stack canaries, RTOS high-water APIs, HardFault registers + PC/LR/SP, linker map stack region, heap integrity/tracing, heap guard patterns, double-free/use-after-free, AddressSanitizer off-target, buffer canaries, bounds checks, MPU guard regions.
- Watchdog: recovery mechanism, not the root-cause fix.
- Time / space: Debug technique, not algorithmic. Runtime overhead depends on checks, tracing, and guard regions.
- Common mistake I made: Saying "reset it with the watchdog" as if that fixes the bug. Watchdog recovers; it does not explain why memory was corrupted.

### Embedded: RTOS missed deadline diagnostics

Problems:
Periodic task occasionally misses deadline, but average CPU usage looks normal.

- Full note: [rtos](../embedded_questions/rtos.md)
- Recognition clue: Timing failure is rare/intermittent, so average CPU load is misleading. Think worst-case latency.
- Core idea: Timestamp expected wake time, actual start time, and completion time. Correlate misses with higher-priority task activity, ISR duration/frequency, long critical sections/interrupt masking, mutex wait time/owner, queue blocking/high-water marks, scheduler jitter, and worst-case execution time.
- Hardware proof: use RTOS trace/timestamp logging and GPIO toggles at wake/start/completion to inspect timing on a scope or logic analyser.
- Distinction: READY means able to run; BLOCKED means waiting for time/event/queue/mutex. In a pre-emptive RTOS, a lower-priority task cannot normally keep a higher-priority READY task from running.
- Remedies: shorten critical sections, bound ISR/task work, fix priorities, avoid long blocking calls, handle queue backpressure, and reduce workload if WCET approaches the period.
- Time / space: Debug technique, not algorithmic. Tracing/logging/GPIO overhead must be bounded so it does not create the timing bug.
- Common mistake I made: Saying "CPU usage is normal" rules out software timing issues. It does not; deadlines fail because of worst-case blocking, latency, or execution spikes.

### Embedded: 1 ms periodic task design

Problems:
Sample/control loop must run every 1 ms.

- Full note: [rtos](../embedded_questions/rtos.md)
- Recognition clue: Periodic deadline, deterministic timing, sensor/control loop, medical/embedded timing guarantee.
- Core idea: Use a hardware timer or RTOS periodic delay based on absolute time. Keep the 1 ms task short, bounded, and high enough priority. Move logging, formatting, I/O retries, and slow communication into lower-priority work.
- Timing detail: prefer `vTaskDelayUntil`/absolute wake timing over `vTaskDelay`, avoid blocking I/O, long mutexes, dynamic allocation, and heavy logging, and verify period/WCET/jitter with GPIO plus scope/logic analyser.
- Shared state: if ISR or another task updates data used by the loop, protect it with atomic access, brief critical sections, or a queue/message. `volatile` alone is not synchronization.
- Time / space: Design answer, not algorithmic. Main complexity is worst-case execution time and jitter.
- Common mistake I made: Designing a permanent busy polling loop. The task should block until its next release and then do bounded work.


### Embedded: RTOS task architecture and primitives

Problems:
Periodic sensing, processing pipeline, UART packets, watchdog, ISR handoff.

- Full note: [rtos](../embedded_questions/rtos.md)
- Recognition clue: Multiple tasks with different deadlines, queues filling, ISR bytes, watchdog supervision, or several system-state flags.
- Core idea: Keep deadline-critical acquisition short and periodic (`vTaskDelayUntil` style), process from queues, let UART/comms own TX/RX parsing in task context, and use a supervisor task to refresh the watchdog only after all critical tasks report progress.
- Primitive choice: queue = payload/descriptor transfer; mutex = shared ownership; binary semaphore = event signal/no ownership; counting semaphore = N events/resources; notification = lightweight one-to-one wake; event group = multiple boolean bits with ANY/ALL wait; stream buffer = UART byte stream; message buffer = variable-length complete records.
- Backpressure: bigger queues absorb bursts, not sustained producer > consumer mismatch. If all buffers are busy, the producer should block/drop by explicit policy; do not overwrite in-use data.
- Buffer handles: pass pointer/handle + length + timestamp between tasks, not large image bytes. Use fixed buffer pool + free-buffer queue; after queue send, producer must not reuse the buffer until returned.
- SPI ownership: separate chip selects do not arbitrate the shared controller. Prefer a dedicated SPI-owner task with request queue, DMA if useful, and requester notification; otherwise mutex the whole transaction.
- Queue vs notification prompt: queue carries payload such as `SensorSample`; notification wakes one known task when data is already in a buffer.
- Common mistake I made: Adding a mutex around an RTOS queue, or kicking the watchdog from one healthy task while another critical task is dead.

### Embedded: UART / SPI / I2C debugging

Problems:
Peripheral does not respond, corrupted bytes, intermittent communication failure.

- Full note: [microcontroller_basics](../embedded_questions/microcontroller_basics.md)
- Recognition clue: Device ID read fails, bus stuck, wrong bytes, timeout, only fails at speed.
- Core idea: Check power, ground, pins/alternate functions, clocks, pull-ups/chip-select, baud/rate/mode, addressing, and logic-analyser waveform before blaming application logic.
- UART: confirm baud, parity, stop bits, TX/RX crossover, ground, framing errors, and buffer overrun.
- SPI: confirm CPOL/CPHA, chip select timing, bit order, clock speed, MISO/MOSI wiring, and whether the device needs dummy reads.
- I2C: confirm pull-ups, address width/shift, ACK/NACK, bus speed, stuck SDA/SCL, and whether another device holds the bus.
- Common mistake I made: Debugging only in code. For bus problems, prove the physical waveform and protocol settings.

### Embedded: startup reset-to-main

Problems:
Explain what happens from reset until `main()`, or debug static/global init.

- Full note: [microcontroller_basics](../embedded_questions/microcontroller_basics.md)
- Recognition clue: Reset vector, vector table, stack pointer, `.data`, `.bss`, constructors, `main`.
- Core idea: CPU loads initial stack pointer and reset handler from the vector table. Startup code sets low-level state, copies `.data` from flash to RAM, zeroes `.bss`, runs C/C++ runtime init and static constructors, then calls `main`.
- Common mistake I made: If an initialized static prints as `0`, suspect `.data` copy/startup/linker script before blaming normal C logic.

### Embedded: testing without hardware

Problems:
How to test firmware logic before boards are available.

- Recognition clue: Hardware unavailable, CI needed, driver not ready, medical/embedded reliability question.
- Core idea: Separate pure logic from hardware access. Test state machines, parsers, algorithms, safety checks, and protocol framing on host with mocks/fakes for drivers. Use simulators/emulators where useful, then integration/HIL tests for real timing and electrical behavior.
- Common mistake I made: Saying "can't test without hardware." You cannot prove everything, but you can test most decision logic and edge cases early.

### Embedded: ISR / main-loop shared state

Problems:
Interrupt updates a flag/counter/buffer that main loop or task reads.

- Recognition clue: ISR and main/task touch the same variable, intermittent missed events, corrupted counter, flag sometimes not seen.
- Core idea: Keep ISR short. Use `volatile` only so memory-mapped/ISR-updated objects are re-read, but use atomic operations, interrupt masking, critical sections, or queues for atomicity and ordering. For multi-byte values on small MCUs, a read/write may not be atomic.
- Counter detail: a 32-bit aligned access may be naturally atomic on some MCUs, but `volatile` does not guarantee atomicity. Overflow/wraparound is separate from concurrency.
- Common mistake I made: Treating `volatile` as enough for thread safety. It prevents some compiler caching; it does not make compound operations atomic.

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
  - `std::move` is a cast to an rvalue/xvalue. It does not move by itself and may still copy if no suitable move operation exists.
  - `noexcept` move constructors help containers such as `std::vector` prefer moving during reallocation while preserving exception guarantees.
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
  - `std::atomic`: gives thread-safe atomic operations and memory-order guarantees. Use for shared data between threads. It does not necessarily lock memory; implementation depends on type/platform.
- Time / space: O(1), O(1).
- Common mistake I made: Reading declarations from the wrong side. Read around the `*`: `const int*` protects the value, `int* const` protects the pointer. Do not say `volatile` makes code thread-safe.

### C++ locks and condition variables

Problems:
`lock_guard`, `unique_lock`, `scoped_lock`, `condition_variable`, waking a worker thread.

- Recognition clue: Shared condition changes, one thread should sleep until work/data is ready, avoid polling.
- Core idea: `lock_guard` is simple scoped locking. `unique_lock` is movable and can unlock/relock, so it is used with `condition_variable::wait`. `scoped_lock` can acquire multiple mutexes together using a deadlock-avoiding algorithm.
- Condition variable pattern:
  - protect shared state with a mutex.
  - waiting thread calls `cv.wait(lock, predicate)`.
  - notifier changes the shared state while holding the mutex, then calls `notify_one()` or `notify_all()`.
- Predicate reason: wakeups can be spurious, and a notification only means "check the condition again." The predicate keeps waiting until the real condition is true.
- Time / space: Synchronisation primitive, not algorithmic. Benefit is avoiding CPU-wasting polling.
- Common mistake I made: Saying the thread should "check occasionally." With a condition variable it sleeps until notified, then re-checks the predicate safely.

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
