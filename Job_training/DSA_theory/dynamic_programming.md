# Dynamic Programming

## What is dynamic programming

Dynamic programming is a way of solving a problem by breaking it into smaller
overlapping subproblems and storing the answers.

The key idea:

```text
Solve small states once.
Reuse them to build bigger answers.
```

DP is not a data structure like an array, linked list, or stack. It is an
algorithmic technique. But it deserves its own DSA chapter because many
interview problems are recognised by the DP thinking pattern.

## When to think DP

Recognition clues:

- count the number of ways
- find minimum or maximum cost
- choose / skip decisions
- exact total or target amount
- grid paths with restricted movement
- repeated recursive choices
- greedy idea seems tempting but fails

Common wording:

```text
How many ways...
Minimum number of...
Maximum amount...
Can reuse choices...
Cannot choose adjacent...
Reach an exact target...
```

## The five-part DP framework

For every DP problem, ask these five questions:

1. State:
   - What does one subproblem mean?
   - Example: `dp[i]`, `dp[a]`, `dp[row][col]`.
2. Base case:
   - What answer do I already know before doing work?
3. Recurrence / transition:
   - How do smaller solved states create the next answer?
4. Calculation order:
   - Which states must be solved first?
5. Final answer:
   - Which state should be returned?

If the state is unclear, the code will feel random. Define the state in plain
English first.

## Top-down vs bottom-up

### Top-down recursion + memoization

Start from the final question and recursively ask smaller questions.

Store answers in a memo table so repeated calls are not recalculated.

Good when:

- recursive idea is easier to see
- not every state may be needed
- problem naturally branches into choices

Pattern:

```cpp
int solve(int state) {
    if (base_case) return answer;
    if (memo has state) return memo[state];

    memo[state] = combine(smaller states);
    return memo[state];
}
```

### Bottom-up iterative DP

Fill base cases first, then build larger states in an order where dependencies
are already ready.

Good when:

- all states are needed
- order is simple
- you want to avoid recursion stack

Pattern:

```cpp
dp[base] = known_answer;

for (state from small to large) {
    dp[state] = combine(previous states);
}

return dp[final_state];
```

## DP does not always mean a dp array

The stored state can be:

- full array: `vector<int> dp`
- 2D table: `vector<vector<int>> dp`
- hash map memo
- two rolling variables
- one rolling row for a grid

If each answer only needs the previous one or two states, use rolling state
instead of keeping the whole table.

Example:

```text
Climbing Stairs only needs previous two counts.
House Robber only needs skip-current and take-current history.
```

## Pattern: Climbing Stairs

Problem type:
count ways.

State:

```text
dp[i] = number of ways to reach step i
```

Base case:

```text
dp[0] = 1
dp[1] = 1
```

Transition:

```text
dp[i] = dp[i - 1] + dp[i - 2]
```

Why:

- last move could be from `i - 1`
- or last move could be from `i - 2`

Complexity:

```text
Time:  O(n)
Space: O(1) with rolling variables
```

## Pattern: House Robber

Problem type:
max total with adjacent choices blocked.

State:

```text
dp[i] = best amount from houses up to i
```

Core decision:

```text
skip current = previous
rob current  = twoBack + current money
```

Transition:

```text
current = max(previous, twoBack + money)
```

Important framing:

- `previous` means do not rob the current house.
- `twoBack + money` means rob the current house, so the adjacent previous house
  cannot be used.

Complexity:

```text
Time:  O(n)
Space: O(1)
```

Common mistake:

This is not Coin Change. Do not use `dp[current - coin] + 1`. House Robber is
take current vs skip current.

## Pattern: Coin Change

Problem type:
minimum number of reusable choices to reach an exact amount.

State:

```text
dp[a] = fewest coins needed to make amount a
```

Base case:

```text
dp[0] = 0
```

Transition:

```text
dp[a] = min(dp[a], dp[a - coin] + 1)
```

Meaning:

```text
dp[current - coin] + 1
= best way to make the remaining amount
  plus the coin I just chose
```

Bottom-up order:

```text
for current amount from 1 to amount:
    try every coin that fits
```

Example:

```text
coins = [1,3,4]
current = 6
```

`dp[6]` checks:

```text
coin 1 -> dp[5] + 1
coin 3 -> dp[3] + 1
coin 4 -> dp[2] + 1
```

Complexity:

```text
Time:  O(amount * number_of_coins)
Space: O(amount)
```

Common mistake:

Largest-first greedy can fail. For `[1,3,4]` and amount `6`, greedy gives
`4 + 1 + 1`, but optimal is `3 + 3`.

## Pattern: Unique Paths / Grid Paths

Problem type:
count paths through a grid.

State:

```text
dp[row][col] = number of ways to reach this cell
```

Base case:

- top row is `1` because there is only one way to keep moving right
- left column is `1` because there is only one way to keep moving down

Transition:

```text
dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
```

Order:

```text
fill from top-left to bottom-right
```

Why:

- top neighbour must already be solved
- left neighbour must already be solved

Complexity:

```text
Time:  O(rows * cols)
Space: O(rows * cols), or O(cols) with one rolling row
```

Common mistake:

Bottom-up grid DP does not need DFS. We are counting from already-solved
neighbouring states, not exploring every path one by one.

## Quick active recall

- What is the state?
- What is the base case?
- What is the recurrence?
- What order fills the states?
- What do I return?
- Can space be reduced?
- Is this top-down recursion + memoization or bottom-up iteration?

## Common DP mistakes

- Starting code before defining the state.
- Forgetting the base case.
- Filling the table in an order where needed states are not ready.
- Confusing different recurrences:
  - House Robber: `max(skip current, take current)`
  - Coin Change: `dp[current - coin] + 1`
  - Grid Paths: `top + left`
- Thinking DP always means a full `dp[]` array.
