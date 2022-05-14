# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def rec(node, l=None, r=None):
            if l is not None and node.val <= l:
                return False
            if r is not None and node.val >= r:
                return False
            if node.left and not rec(node.left, l=l, r=node.val):
                return False
            if node.right and not rec(node.right, l=node.val, r=r):
                return False
            return True
        return rec(root)
