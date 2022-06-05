# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:        
        self.global_max = root.val
        
        def singleMax(n):
            if n is None:
                return 0
            
            self.global_max = max(self.global_max, n.val)
            
            l_val = singleMax(n.left)
            self.global_max = max(self.global_max, l_val+n.val)
            r_val = singleMax(n.right)
            self.global_max = max(self.global_max, r_val+n.val)
            
            self.global_max = max(self.global_max, l_val+r_val+n.val)
            
            return max(l_val+n.val, r_val+n.val, n.val)
        
        
        singleMax(root)
        
        return self.global_max
