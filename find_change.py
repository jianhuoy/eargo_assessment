COIN_VALUES = [25, 10, 5, 1]
TEST_CASES = [0, 1, 13, 88, 4999]

def find_changes(number):
    remaining = number
    
    res = []
    for i in range(len(COIN_VALUES)):
        res.append(remaining//COIN_VALUES[i])
        remaining = remaining % COIN_VALUES[i]

    return res

if __name__ == "__main__":
    
    for num in TEST_CASES:
        res = find_changes(num)
        total = sum([res[i]*COIN_VALUES[i] for i in range(len(res))])
        print("Input: %d, result: %s, successful: %s" % (num, res, total == num))
