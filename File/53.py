def maxSubArray(self, nums: List[int]) -> int:
        # put total cur at 0 index (-2)
        #loop from index1
        total = cur = nums[0]
        for i in nums[1:]:
            #cur takes the sum and compare the index with pre sum get the max
            
            cur = max(cur+i,i)
            #total keep track of the overall max of all cur
            total = max(total,cur)
        return total
