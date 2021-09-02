def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # base case
        if not root:
            return True
        
        if root.right:
            if root.val != root.right.val: #Equavalent
                return False
            
        if root.left:
            if root.val != root.left.val: #Equavalent
                return False
        
        return self.isUnivalTree(root.right) and self.isUnivalTree(root.left)
