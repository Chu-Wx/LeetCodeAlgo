#center exapnd 
def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in xrange(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]
      
    
    #Dp
def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 0:
            return ''
        
        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = True
        ans = s[0:1]
        for i in range(n):
            for j in range(i-1, -1, -1):
                if s[i] == s[j] and (i-j<2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i - j + 1 > len(ans):
                        ans = s[j:i+1]
        return ans
      
