# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = 0
        if not root:
            return result
        if root.left:
            if not root.left.left and not root.left.right:
                result += root.left.val
            else:
                result += self.sumOfLeftLeaves(root.left)
        result += self.sumOfLeftLeaves(root.right)
        return result
