# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # left nothing, right nothing, return nothing
        # left start, right nothing, return left + curr
        # left dest, right nothing, return left + curr
        # left nothing, right start, return right + curr
        # left start, right start, invalid
        # left dest, right start, return right + curr + left_inv
       # left nothing, right dest
        # left start, right dest
        # left dest, right dest invalid
        
        def rec(root):
            start_result = ''
            end_result = ''
            if root.left:
                left_terminal, left_path = rec(root.left)
                if left_terminal == 'start':
                    start_result = left_path 
                    start_result += 'U'
                elif left_terminal == 'end':
                    end_result = left_path 
                    end_result += 'L'
                elif left_terminal == 'both':
                    return left_terminal, left_path
            if root.right:
                right_terminal, right_path = rec(root.right)
                if right_terminal == 'start':
                    start_result = right_path 
                    start_result += 'U'
                elif right_terminal == 'end':
                    end_result = right_path 
                    end_result += 'R'
                elif right_terminal == 'both':
                    return right_terminal, right_path
            
            if (start_result and end_result) or \
                (start_result and root.val == destValue) or \
                (root.val == startValue and end_result):
                return 'both', start_result + end_result[::-1]
            elif start_result or root.val == startValue:
                return 'start', start_result
            elif end_result or root.val == destValue:
                return 'end', end_result
            return 'none', ''

        _, path = rec(root)
        return path
