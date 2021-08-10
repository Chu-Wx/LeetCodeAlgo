def partition(self, s: str) -> List[List[str]]:
        #DFS
        res = []
        self.dfs(s, [], res)
        return res

def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)

def isPal(self, s):
        return s == s[::-1]

'''Explain:
we can use dfs to backtrackning all the possible solutions
in dfs function: if s is empty then append the path to res and go abck to previous loop
if s has smth, then shrink and check if every loop is palindorme recusively'''

#DP 
