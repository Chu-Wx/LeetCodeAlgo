def maxProfit(self, prices: List[int]) -> int:
        maxProfit , minPrice = 0 , float('inf')
        
        for curPrice in prices:
            minPrice = min(minPrice, curPrice)
            curProfit = curPrice - minPrice
            maxProfit = max(maxProfit, curProfit)
        return maxProfit
        '''Explain:
        we set the max profit and minimum price as 0 and infinite as first
        loop through the prices O(N)
        when we find a smaller price we set it as minprice and keep it to the next iteration
        we get the iteration profit by simply find current price - minimum price 
        then we keep the max profit by compare current profit and the max profit
        return the max after loop'''
