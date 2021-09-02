def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.Bal = True
        
        def dfs(node): # left and right represent the left arm and right arm of the current node 
            if not node: return 0
            lft, rgh = dfs(node.left), dfs(node.right)
            if abs(lft - rgh) > 1: 
                self.Bal = False
            return max(lft, rgh) + 1
            
        dfs(root)
        return self.Bal
