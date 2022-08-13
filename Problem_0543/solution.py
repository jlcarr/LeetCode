# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.sol = 0
        def rec(n):
            if not n:
                return 0
            l_depth = rec(n.left)
            r_depth = rec(n.right)
            self.sol = max(self.sol, l_depth+r_depth)
            return 1+max(l_depth, r_depth)
        rec(root)
        return self.sol
            
        
