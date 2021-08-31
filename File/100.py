def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # if p left = q left true
        #first visit root then go to leaves 
        p_res=[]
        q_res=[]
        self.traverse(p,p_res)
        self.traverse(q,q_res)
        return p_res == q_res
        
def traverse(self,root,res):
        if not root: return []
        
        res.append(root.val)
        if root.left:
            self.traverse(root.left,res)
        else:
            res.append(0)
        if root.right:
            self.traverse(root.right,res)
        else:
            res.append(0)
            
         
       # faster 
def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not q and not p:
            return True
        elif not p or not q:
            return False
        elif p.val!=q.val:
            return False
        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
