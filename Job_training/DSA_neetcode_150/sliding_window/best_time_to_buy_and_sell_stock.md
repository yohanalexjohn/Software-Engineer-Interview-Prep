# Best time to buy and sell stock

## Active recall

- Pattern: one-pass running minimum.
- Algorithm: keep lowest price seen so far and best profit so far.
- At each price, profit is `price - minPrice`; update best, then update min.
- Two-pointer framing: `right` always advances through possible sell days.
  `left` only jumps to `right` when `right` finds a new lower buy price.
- Time: O(n). Space: O(1).
- Common mistake: sell must happen after buy, so do not just subtract global min from global max if order is wrong.

Recall prompt:

- When does `left` move?
- Why does `right` never move backwards?

You are given an array prices where prices[i] is the price of a given stock on
the ith day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return 0.

## Example 1

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
6-1 = 5. Note that buying on day 2 and selling on day 1 is not allowed because
you must buy before you sell.

## Example 2

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

## Solution

```python
def solution(prices: list[int]) -> int:
    max_proft = 0
    # Create the largest number 
    # So that the first iteration is set properly
    # maybe just use max(prices + 1) ?
    buy_price = float("inf")

    for i in range(len(prices)):
        if prices[i] < buy_price:
            buy_price = prices[i]

        profit = prices[i] - buy_price

        if profit > max_proft:
            max_proft = profit

    return int(max_proft)


print(solution([7, 1, 5, 3, 6, 4]))
print(solution([7, 6, 4, 3, 2, 1]))
```

```cpp 
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int output = 0;

        for (int buy = 0; buy < prices.size(); ++buy)
        {
            for (int sell = buy + 1; sell < prices.size(); ++sell)
            {
                if (prices[sell] > prices[buy])
                {
                   int profit = prices[sell] - prices[buy];
                   output = std::max(output, profit);
                }
            }
        }

        return output;
    }
};
```

```cpp 
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.empty()) {
            return 0;
        }

        int minPrice = prices[0];
        int maxProfit = 0;

        for (int i = 0; i < prices.size(); ++i) {
            int profit = prices[i] - minPrice;

            maxProfit = std::max(maxProfit, profit);
            minPrice = std::min(minPrice, prices[i]);
        }

        return maxProfit;
    }
};
```
