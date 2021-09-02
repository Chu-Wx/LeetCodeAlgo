def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not t: 
            return True
        
        if not s:
            return False
        # when find same node in big tree start compare
        if s.val == t.val and self.checkSubtree(s, t):
            return True
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
def checkSubtree(self, s, t):
        if not s and not t:
            return True
        
        if not s or not t:
            return False
        
        if s.val != t.val:
            return False
        
        return self.checkSubtree(s.left, t.left) and self.checkSubtree(s.right, t.right)
