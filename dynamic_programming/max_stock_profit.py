# You are given access to yesterday's stock prices for a single stock. 
# The data is in the form of an array with the stock price in 30 minute intervals 
# from 9:30 a.m EST opening to 4:00 p.m EST closing time. With this data, 
# write a function that returns the maximum profit obtainable. 
# You will need to buy before you can sell.

# For example, suppose you have the following prices:

# prices = [3, 4, 7, 8, 6] 

# Note: This is a shortened array, just for the sake of example—a full set of prices 
# for the day would have 13 elements (one price for each 30 minute interval betwen 9:30 and 4:00),
# as seen in the test cases further down in this notebook.

# In order to get the maximum profit in this example, you would want to buy at a price of 3 and sell
# at a price of 8 to yield a maximum profit of 5. In other words, you are looking for 
# the greatest possible difference between two numbers in the array.


# ### The Idea
# The given array has the prices of a single stock at 13 different timestamps. 
# The idea is to pick two timestamps:
# "buy_at_min" and "sell_at_max" such that the buy is made before a sell. 
# We will use two pairs of indices while traversing the array: 
# Pair 1 - This pair keeps track of our maximum profit while iterating over the list. 
# It is done by storing a pair of indices - min_price_index , and max_price_index . 
# Pair 2 - This pair keeps track of the profit between the lowest price seen so far 
# and the current price while traversing the array. The lowest price seen so far is 
# maintained with current_min_price_index.

def max_returns(prices):
    """
    Calculate maxiumum possible return
    
    Args:
       prices(array): array of prices
    Returns:
       int: The maximum profit possible
    """
    min_price_index = 0
    max_price_index = 1
    current_min_price_index = 0
    for i in range(1, len(prices)):
        if prices[i] < prices[current_min_price_index]:
            current_min_price_index = i
        if prices[max_price_index] - prices[min_price_index] < prices[i] - prices[current_min_price_index]:
            max_price_index = i
            min_price_index = current_min_price_index
    max_profit = prices[max_price_index] - prices[min_price_index]
            
    
    return max_profit

# Test Cases
def test_function(test_case):
    prices = test_case[0]
    solution = test_case[1]
    output = max_returns(prices)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

def test():
    prices = [3, 4, 7, 8, 6]
    solution = 5
    test_case = [prices, solution]
    test_function(test_case)

    prices = [3, 4, 7, 8, 6, 2, 9]
    solution = 7
    test_case = [prices, solution]
    test_function(test_case)

    prices = [8, 6, 5, 4, 3, 2, 1]
    solution = 0
    test_case = [prices, solution]
    test_function(test_case)

if __name__ == "__main__":
    test()