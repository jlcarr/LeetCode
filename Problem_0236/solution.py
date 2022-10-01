# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    done = False
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        if root is p:
            return p
        if root is q:
            return q
        left = self.lowestCommonAncestor(root.left, p, q)
        if self.done:
            return left
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            self.done = True
            return root
        if not left:
            return right
        return left
