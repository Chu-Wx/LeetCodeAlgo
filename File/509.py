def fib(self, n: int) -> int:
        d=[0,1]
        for i in range(2,n+1):
            
            d.append(d[i-1]+d[i-2])
        return d[n]
      '''we initialize 0, 1 in the list and start dp on the third value and append them'''
      
#recursion 
def fib(self, n: int) -> int:
  if N == 0: return 0
	if N == 1: return 1
	return fib(N-1) + fib(N-2)
