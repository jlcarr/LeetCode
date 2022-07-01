# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if n == 0:
            return None
        v = nums[n//2]
        l = nums[:n//2]
        r = nums[n//2+1:]
        return TreeNode(val=v, left=self.sortedArrayToBST(l), right=self.sortedArrayToBST(r))
