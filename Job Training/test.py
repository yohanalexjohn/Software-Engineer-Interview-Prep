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
        print(profit, buy_price)

        if profit > max_proft:
            max_proft = profit

    return int(max_proft)


print(solution([7, 1, 5, 3, 6, 4]))
print(solution([7, 6, 4, 3, 2, 1]))
