# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def rec(curr):
            result = 0
            curr_sum = curr.val
            curr_count = 1
            if curr.left:
                sub_result, sub_sum, sub_count = rec(curr.left)
                result += sub_result
                curr_sum += sub_sum
                curr_count += sub_count
            if curr.right:
                sub_result, sub_sum, sub_count = rec(curr.right)
                result += sub_result
                curr_sum += sub_sum
                curr_count += sub_count

            if curr.val == curr_sum // curr_count:
                result += 1
            #print(curr.val, curr_sum, curr_count)
            return result, curr_sum, curr_count
        
        result, _, _ = rec(root)
        return result
