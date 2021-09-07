def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def trim(node):
            if not node:
                return None
            node.left = trim(node.left)
            node.right = trim(node.right)
            if node.val == target and node.left == node.right == None:# at leafs and hit target val
                return None
            return node
                
                
        return trim(root)
