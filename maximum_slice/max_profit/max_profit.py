def calculate_max_profit(A):
    min_buy_price = None
    max_profit = 0

    for value in A:
        min_buy_price = value if min_buy_price is None else min(min_buy_price, value)
        profit = value - min_buy_price
        max_profit = profit if profit > max_profit else max_profit
    return max_profit
