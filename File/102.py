def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        else:
            que, res = [root], []# get a que for the node and res for the value 
            while que:
                level = []
                for i in range(len(que)): # que range how many nodes inside 
                    node = que.pop(0)
                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)# get node for child of current node
                    level.append(node.val) # get the node val of current 
                res.append(level)
        return res
