def deleteAndEarn(self, nums):
        points = [0] * 10000
        for num in nums:
            points[num] += num   # num = [3,3,3,2,2,4] -> [0,0,4,9,4] value * occurances
        return self.rob(points) 
    def rob(self, nums):
        '''prev = curr = 0
        for value in nums:
            prev, curr = curr, max(prev + value, curr)
        return curr'''

        if not nums: return 0
        if len(nums) == 1: return nums[0]
    
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1] # return the last element
      
      
      '''same as houding robbing with one extra step : [3,3,3,2,2,4] -> [0,0,4,9,4] value * occurances
