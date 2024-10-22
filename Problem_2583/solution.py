# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sums = []
        def rec(curr, depth=0):
            if not curr:
                return
            if len(level_sums) < depth+1:
                level_sums.append(0)
            level_sums[depth] += curr.val
            rec(curr.left, depth=depth+1)
            rec(curr.right, depth=depth+1)
        rec(root)
        if len(level_sums) <= k-1:
            return -1
        level_sums.sort(reverse=True)
        return level_sums[k-1]
