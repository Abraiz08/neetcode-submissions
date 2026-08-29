# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            # here just consider what will ahppen at the absolute bottom after returning
            # the node will be calculating using the height between it and itws children, which is what we want, which is why we should do it before then doing the return value
            # at each point in the recursion, you are working with the subproblems of the node
            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.res