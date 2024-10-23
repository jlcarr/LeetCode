# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_sums = []
        def rec_level_sum(curr, depth=0):
            if not curr:
                return
            if len(level_sums) == depth:
                level_sums.append(0)
            level_sums[depth] += curr.val
            rec_level_sum(curr.left, depth=depth+1)
            rec_level_sum(curr.right, depth=depth+1)
        rec_level_sum(root)

        def fill_cousins(curr, depth=0, sib_sum=0):
            if not curr:
                return
            curr.val = level_sums[depth] - sib_sum
            sib_sum = 0
            if curr.left:
                sib_sum += curr.left.val
            if curr.right:
                sib_sum += curr.right.val
            fill_cousins(curr.left, depth=depth+1, sib_sum=sib_sum)
            fill_cousins(curr.right, depth=depth+1, sib_sum=sib_sum)
        fill_cousins(root, depth=0, sib_sum=root.val)
        return root
