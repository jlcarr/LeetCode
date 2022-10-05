# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_left = []
        min_right = []
        def rec(curr, pos=0, level=0):
            if not curr:
                return
            if len(max_left) <= level:
                max_left.append(pos)
            max_left[level] = max(max_left[level], pos)
            if len(min_right) <= level:
                min_right.append(pos)
            min_right[level] = min(min_right[level], pos)
            rec(curr.left, 2*pos, level+1)
            rec(curr.right, 2*pos+1, level+1)
        rec(root)
        result = 0
        for i in range(min(len(max_left), len(min_right))):
            result = max(result, 1+max_left[i]-min_right[i])
        #print(max_left, min_right)
        return result
