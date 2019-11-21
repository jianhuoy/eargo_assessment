TESTS = [
    [3,8,8,55,38,1,7,42,54,53],
    [3,3,2,5,32,23,23,2,1,34,32,2],
    [],
    [1]
    ]

# Input: a list of stock prices
# Output: a tuple of two days, the best buy and sell days to maximize gain
def find_buy_and_sell_days(prices):
    # low: current lowest stock price
    # low_day: the day on which we see the lowest stock price
    # max_gain: current maximum gain
    # buy_day, sell_day: current best buy and sell day combination 
    low = float('inf')
    low_day = None
    max_gain = -1
    buy_day = None
    sell_day = None

    for i in range(len(prices)):
        if low_day is None or prices[i] < low:
            low_day = i
            low = prices[i]
        
        if prices[i] - low > max_gain:
            max_gain = prices[i] - low
            buy_day = low_day
            sell_day = i

    return (buy_day + 1, sell_day + 1) if buy_day is not None else (-1, -1)

if __name__ == "__main__":
    for test in TESTS:
        buy, sell = find_buy_and_sell_days(test)
        print("Input: %s Result: Buy on %d, Sell on %d" % (test, buy, sell))