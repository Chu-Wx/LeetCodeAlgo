def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            
            else:
                return dfs(root.left) + dfs(root.right)

        dfs(root1)# these 2lines make 2 times faster 
        dfs(root2)
        return dfs(root1)==dfs(root2)
