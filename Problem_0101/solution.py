# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def rec_check(l, r):
            if not l or not r:
                return l is None and r is None
            return l.val == r.val \
                and rec_check(l.left, r.right) \
                and rec_check(l.right, r.left)
        return rec_check(root.left, root.right)
