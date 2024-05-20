# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = 0
        if root.left:
            result += self.distributeCoins(root.left)
            result += abs(root.left.val - 1)
            root.val += root.left.val - 1
        if root.right:
            result += self.distributeCoins(root.right)
            result += abs(root.right.val - 1)
            root.val += root.right.val - 1
        return result
