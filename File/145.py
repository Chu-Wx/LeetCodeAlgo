def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        #main
        res=[]
        #postorder [left, right, root]
        def postorder(root):
            if root.left:
                postorder(root.left)
            if root.right:
                postorder(root.right)
            res.append(root.val)
        
        postorder(root)
        return res
