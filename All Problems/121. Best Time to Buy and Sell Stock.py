def max__profit(prices):
    buy_price = 0
    sell_price = 1
    max_profit = 0
    while sell_price < len(prices):
        current_profit = prices[sell_price] - prices[buy_price]

        if prices[buy_price] < prices[sell_price]:
            max_profit = max(max_profit, current_profit)
        else:
            buy_price = sell_price

        sell_price += 1
    return max_profit


def fastest_solution(prices):
    if len(prices) < 2:
        return 0

    lowest = highest = prices[0]
    difference = 0

    for i in prices[1:]:
        if i > highest:
            highest = i
            if highest - lowest > difference:
                difference = highest - lowest
        if i < lowest:
            lowest = i
            highest = -1

    return difference


if __name__ == '__main__':
    print(fastest_solution([7, 1, 5, 3, 6, 4]))
