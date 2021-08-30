def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root :
            return []
        
        #recur
        res=[]
        # preorder [root, left, right]
        def preorder(root):
            res.append(root.val)
            if root.left:
                preorder(root.left)
            if root.right:
                preorder(root.right)
            
        preorder(root)
        return res
