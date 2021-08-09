def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        s1 = -prices[0]     # profit after buying
        s2 = 0              # profit after selling
        s0 = [0, 0]         # cooldown profit using a queue
        for p in prices:
            s1 = max(s1, s0[1] - p)
            s2 = max(s2, s1 + p)
            s0 = [s2, s0[0]]
        return s2
    
    '''when you enter the stock you can have 3 states
    1. s1 : after buying either stay s1 or come from cooldown which is s0[1]-p
    2. s2 : after selling either stay on s2 or comes from s1 + p 
    3. s0 : cooldown after you sell s2 or stay cool s0[0]'''
