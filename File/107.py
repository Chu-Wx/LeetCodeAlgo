def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        else:
            que, res = [root],[]
            while que:
                level =[]
                for i in range(len(que)):
                    node = que.pop(0)
                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)
                    level.append(node.val)
                res.append(level)
                
            return res[::-1]
