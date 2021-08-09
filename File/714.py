def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash
    '''cash state is before you buy: comes from stay cash or you sell stock 
    hold state is after you buy : either stay hold or comes from cash -prices
     '''
