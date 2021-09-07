def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def trim(node):
            if not node:
                return None
            elif node.val > high:
                return trim(node.left)
            elif node.val < low:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node
        return trim(root)
'''When node.val > high, we know that the trimmed binary tree must occur to the left of the node. 
Similarly, when node.val < low, the trimmed binary tree occurs to the right of the node. Otherwise, 
we will trim both sides of the tree.'''
