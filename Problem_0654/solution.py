# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def rec(l,r):
            #print(l,r)
            if l >= r:
                return None
            if l+1 == r:
                return TreeNode(nums[l])
            max_val, max_index = -1, 0
            for i in range(l,r):
                if max_val < nums[i]:
                    max_val = nums[i]
                    max_index = i
            left = rec(l, max_index)
            right = rec(max_index+1, r)
            return TreeNode(nums[max_index], left, right)
        
        return rec(0, len(nums))
