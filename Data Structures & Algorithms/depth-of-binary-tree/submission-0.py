import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxdepth = -math.inf
        if not root:
            return 0
        
        return max(maxdepth, 1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))