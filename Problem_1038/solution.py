# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def rec(curr, prefix):
            if not curr:
                return 0
            curr.val += rec(curr.right, prefix)
            subsum = curr.val + rec(curr.left, curr.val + prefix)
            curr.val += prefix
            return subsum
        rec(root, 0)
        return root
