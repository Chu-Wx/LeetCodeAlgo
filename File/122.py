def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                profit += (prices[i+1]-prices[i])         
        return profit
    '''Explain:
    we set our initial profit is 0
    then we loop through the prices O(N)
    when we find the next day price is higher than today
    we need to buy in and sell on next day
    other wise we dont need to do anything'''
