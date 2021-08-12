def climbStairs(self, n: int) -> int:
        #DP fibonnaci dict with memori
        d = {1:1, 2:2}
        def dfs(n):
            if n < 3:
                return n
            if n not in d:
                d[n]=dfs(n-1)+dfs(n-2)
            return d[n]
        
        return dfs(n)
      
# og fibo solution
def climbStairs(self, n: int) -> int:
        L=[1,1]
        for i in range(2,n+1):
            L.append(L[i-1]+L[i-2])
        return L[n]
