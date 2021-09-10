def maxNode(self, root):
        # write your code here
        self.max_num = -sys.maxsize
        self.result = None
        self.traverse(root)
        
        return self.result
    
def traverse(self, root):
        if root is None:
            return 
        if self.max_num < root.val:
            self.max_num = root.val
            self.result = root
        
        self.traverse(root.left)
        self.traverse(root.right)
