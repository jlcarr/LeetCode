# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def rec(curr):
            if not curr.left and not curr.right:
                #print(curr.val, [1], 0)
                return [1], 0
            left_leaves, left_counts = [], 0
            if curr.left:
                left_leaves, left_counts = rec(curr.left)
            right_leaves, right_counts = [], 0
            if curr.right:
                right_leaves, right_counts = rec(curr.right)

            counts = left_counts + right_counts
            for dl, lcount in enumerate(left_leaves):
                for dr, rcount in enumerate(right_leaves):
                    if dr+dl+2 > distance:
                        break
                    counts += lcount * rcount
            leaves = [0] * min(distance, max(1+len(left_leaves), 1+len(right_leaves)))
            for dl, lcount in enumerate(left_leaves):
                if dl+1 < distance:
                    leaves[dl+1] += lcount
            for dr, rcount in enumerate(right_leaves):
                if dr+1 < distance:
                    leaves[dr+1] += rcount
            #print(curr.val, counts, leaves)
            return leaves, counts
        
        _, result = rec(root)
        return result

