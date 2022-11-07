# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        sub_depth_map = dict()
        other_depth_map = dict()

        def sub_depths_dfs(curr):
            if not curr:
                return -1
            result = 0
            result = max(result, 1+sub_depths_dfs(curr.left))
            result = max(result, 1+sub_depths_dfs(curr.right))
            sub_depth_map[curr.val] = result
            return result
        sub_depths_dfs(root)
        #print(sub_depth_map)
        
        def other_depths_dfs(curr, other_depth=-1, depth=0):
            #print(curr.val, other_depth, depth)
            other_depth = max(other_depth, depth-1)
            other_depth_map[curr.val] = other_depth
            if curr.left and curr.right:
                max_other = max(other_depth, depth+1+sub_depth_map[curr.right.val])
                other_depths_dfs(curr.left, other_depth=max_other, depth=depth+1)
                max_other = max(other_depth, depth+1+sub_depth_map[curr.left.val])
                other_depths_dfs(curr.right, other_depth=max_other, depth=depth+1)
            elif curr.right:
                other_depths_dfs(curr.right, other_depth=other_depth, depth=depth+1) 
            elif curr.left:
                other_depths_dfs(curr.left, other_depth=other_depth, depth=depth+1) 
        other_depths_dfs(root)
        #print(other_depth_map)
            
        result = []
        for q in queries:
            result.append(other_depth_map[q])
        return result
            
