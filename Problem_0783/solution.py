# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.nums = []
        def rec(node):
            if not node:
                return
            self.nums.append(node.val)
            rec(node.left)
            rec(node.right)
        rec(root)
        self.nums.sort()
        #print(self.nums)
        return min([j-i for i,j in zip(self.nums[:-1], self.nums[1:])])
