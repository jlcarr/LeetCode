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
        def dfs(curr):
            if not curr:
                return Counter()
            subs = dfs(curr.left) + dfs(curr.right)
            subs = Counter({k+curr.val:count for k,count in subs.items()})
            subs[curr.val] += 1
            self.result += subs[targetSum]
            return subs
        dfs(root)
        return self.result
