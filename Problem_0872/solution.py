# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaves(curr):
            if not curr:
                return []
            if not curr.left and not curr.right:
                return [curr.val]
            return leaves(curr.left) + leaves(curr.right)
        return leaves(root1) == leaves(root2)
