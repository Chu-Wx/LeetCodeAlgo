def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        #main recursive 
        res=[]
        # inorder [left, root, right]
        def inorder(root,res):
            if root.left:
                inorder(root.left,res)
            res.append(root.val)
            if root.right:
                inorder(root.right,res)
            
            
        inorder(root,res)
        return res
