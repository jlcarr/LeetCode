# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.levelsums = []
        def rec(node, level):
            while len(self.levelsums) < level:
                self.levelsums.append(0)
            self.levelsums[level-1] += node.val
            if node.left:
                rec(node.left, level+1)
            if node.right:
                rec(node.right, level+1)

        rec(root, 1)
        result = 1
        maxsum = root.val
        for l,levelsum in enumerate(self.levelsums):
            if levelsum > maxsum:
                maxsum = levelsum
                result = l+1
        #print(self.levelsums)
        return result
