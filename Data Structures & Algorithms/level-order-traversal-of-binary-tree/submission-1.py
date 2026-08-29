# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:      
        if root is None:
            return []
        res = [[root.val]]
        queue = []
        queue.append(root)
        while queue:
            tempres = []
            for i in range(len(queue)):
                curr = queue.pop(0)
                if curr.left:
                    tempres.append(curr.left.val)
                    queue.append(curr.left)
                if curr.right:
                    tempres.append(curr.right.val)
                    queue.append(curr.right)
            if tempres != []:
                res.append(tempres)
          
        return res

        