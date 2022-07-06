# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = []
        if root.left:
            res.append(self.minDepth(root.left))
        if root.right:
            res.append(self.minDepth(root.right))
        if not res:
            return 1
        return 1 + min(res)
