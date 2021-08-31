def postorder(self, root: 'Node') -> List[int]:
        res = []
        if root == None: 
            return res
        
        self.recursion(root, res)
        return res

def recursion(self,root, res):
        #go through chidilren first 
        for child in root.children:
            self.recursion(child, res)
        #when at the end then append the root val
        res.append(root.val)
