# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import Counter
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.result = 0
        def dfs(curr, curr_sum=0, prevs=Counter([0])):
            if not curr:
                return
            # curr_sum - prevs = target
            # curr_sum - target = prevs
            
            new_sum = curr_sum+curr.val
            self.result += prevs[new_sum-targetSum]
            
            new_prevs = prevs+Counter([curr_sum+curr.val])
            
            dfs(curr.left, new_sum, new_prevs)
            dfs(curr.right, new_sum, new_prevs)
 
            return
        dfs(root)
        return self.result
