def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        Q, ans = [root], []
        
        while Q: # for each q we creat new level 
            level = []
            for i in range(len(Q)): # len(Q) = cur lvl node counts
                
                node = Q.pop(0) # get fitst child and append all its children 
                for child in node.children:
                    Q.append(child)
                level.append(node.val)# then lvl append the current node val until empty
            ans.append(level)

        return ans
