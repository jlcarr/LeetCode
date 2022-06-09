# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.success = False
        if not root:
            return 0
        
        smaller = self.kthSmallest(root.left, k)
        if self.success:
            return smaller
        
        if smaller == k-1:
            self.success = True
            return root.val
        
        greater = self.kthSmallest(root.right, k-1-smaller)
        if self.success:
            return greater
        
        return smaller + 1 + greater
            
