# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def tree_sum(curr):
            if not curr:
                return 0
            return tree_sum(curr.left) + curr.val + tree_sum(curr.right)
        
        self.tot = tree_sum(root)

        self.result = 0
        def rec(curr):
            if not curr:
                return 0
            left_sum = rec(curr.left)
            right_sum = rec(curr.right)
            self.result = max(self.result, left_sum*(self.tot-left_sum))
            self.result = max(self.result, right_sum*(self.tot-right_sum))
            return left_sum + right_sum + curr.val

        rec(root)

        return self.result % (10**9 + 7)
