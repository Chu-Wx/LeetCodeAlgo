    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
        S = set(arr)
        ans = 0
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                x, y = arr[i], arr[j]
                length = 2
                while x+y in S:
                    x, y = y, x+y
                    length +=1
                    ans = max(length, ans)
        return ans
        
    '''Explain:
    we nned to use set() for the array to increase time complexity 
    loop though i and i next j and set it as x, and y initial length is 2 
    check if x+y is in set if yes then update x-> y , y-> x+y and length increase 1 beacasue we found 
    one more val in sub sque, get the max value of lenght by max() and return after loop'''
    
    
    #DP solution
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        dp = collections.defaultdict(int)
        s = set(A)
        for j in xrange(len(A)):
            for i in xrange(j):
                if A[j] - A[i] < A[i] and A[j] - A[i] in s:
                    dp[A[i], A[j]] = dp.get((A[j] - A[i], A[i]), 2) + 1
        return max(dp.values() or [0])
