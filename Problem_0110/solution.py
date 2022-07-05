# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return True,0
            l_v, l_h = dfs(node.left)
            if not l_v:
                return False,0
            r_v, r_h = dfs(node.right)
            if not r_v:
                return False,0
            #print(node.val, l_h,r_h)
            return abs(l_h-r_h) <= 1, max(l_h,r_h)+1
        
        return dfs(root)[0]
