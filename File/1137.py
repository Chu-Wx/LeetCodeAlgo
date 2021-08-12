def tribonacci(self, n: int) -> int:
  #og fibo
        L=[0,1,1]
        for i in range(3,n+1):
            L.append(L[i-1]+L[i-2]+L[i-3])
        return L[n]
  #dp
def tribonacci(self, n: int) -> int:
       dic = {0:0,1:1,2:1}
        
        def dfs(n):
            if n in dic:
                return dic[n]
            else:
                dic[n] = dfs(n-1)+dfs(n-2)+dfs(n-3)
                
            return dic[n]
        
        return dfs(n) 
