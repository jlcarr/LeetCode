# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def rec(curr_node, curr_val):
            curr_val = 10 * curr_val + curr_node.val
            if not curr_node.left and not curr_node.right:
                return curr_val
            result = 0 
            if curr_node.left:
                result +=  rec(curr_node.left, curr_val)
            if curr_node.right:
                result +=  rec(curr_node.right, curr_val)
            return result
        return rec(root, 0)
