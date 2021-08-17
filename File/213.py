def rob(self, nums: List[int]) -> int:
        return max(nums[0]+self.robbing(nums[2:-1]),self.robbing(nums[1:]))
    '''the differeent is here from house rob 1 we start 0 and rob the seond till -1 exclude lastone or we start from 1 and rob till end '''
    def robbing(self,num):
        if not num: return 0
        if len(num) == 1: return num[0]
        
        dp = [0] * len(num)
        dp[0] = num[0]
        dp[1] = max(num[0], num[1])
        for i in range(2, len(num)):
            dp[i] = max(num[i] + dp[i-2], dp[i-1])
        return dp[-1] 
        
        '''pre = cur = 0
        for i in range(len(num)):
            temp = pre
            pre = cur
            cur = max(num[i]+temp,pre)
        return cur
        '''
