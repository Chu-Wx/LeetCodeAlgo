def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool: #stack
        if root is None:
            return False
        stack = [(root, targetSum)]
        while stack:
            node, _sum = stack.pop()
            if node.left is node.right is None and node.val == _sum:
                return True
            if node.left:
                stack.append((node.left, _sum - node.val))
            if node.right:
                stack.append((node.right, _sum - node.val))
        return False
      
      #recur
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool      
        if not root:
            return False

        if not root.left and not root.right and root.val == targetSum:
            return True
        
        targetSum -= root.val

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
