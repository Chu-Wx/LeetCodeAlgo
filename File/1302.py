def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        res= []
        self.bfs(root, res)
        return sum(res[-1]) # the last element in res is the deepest level
        
def bfs(self, root, res):
        if not root:
            return None
        
        que =[root]
        while que:
            #start loop
            #empty level
            level = []
            for i in range(len(que)):
                node = que.pop(0)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                #after append the node in the que 
                # append the value into 
                level.append(node.val)
            #after level is created
            res.append(level)
            
