# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == 2:
            if root.right.val == 1:
                return True
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        elif root.val == 3:
            if root.right.val == 0:
                return False
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        return bool(root.val)
