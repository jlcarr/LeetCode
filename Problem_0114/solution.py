# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node:
                return None,None
            left_start,left_end = dfs(node.left)
            right_start,right_end = dfs(node.right)
            node.left = None
            node.right = None
            end = None
            if left_start and right_start:
                node.right = left_start
                left_end.right = right_start
                return node, right_end
            elif left_start and not right_start:
                node.right = left_start
                return node, left_end
            elif not left_start and right_start:
                node.right = right_start
                return node, right_end
            else:
                return node, node
        dfs(root)
